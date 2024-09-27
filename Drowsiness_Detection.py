from imutils import face_utils
from scipy.spatial import distance
import dlib
import cv2
import vlc
import os
import random
import Speak as s

def eye_aspect_ratio(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])
	C = distance.euclidean(eye[0], eye[3])
	ear = (A + B) / (2.0 * C)
	return ear

thresh = 0.25
frame_check = 20

detect = dlib.get_frontal_face_detector()
#it predicts all face the landmarks in face 
predict = dlib.shape_predictor(".\shape_predictor_68_face_landmarks.dat")

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]


def drowsiness_activator():
        #movieplay()
        cap=cv2.VideoCapture(0)
        movie_dir='C:\\Users\\N Ravi Teja\\Videos\\Movies\\English\\'
        movies=os.listdir(movie_dir)
        flag=True
        while(flag):
                num=random.randint(0,len(movies)-1)
                if(movies[num].endswith('.mp4')):
                        MoviePlay=(os.path.join(movie_dir,movies[num]))
                        flag=False
        media = vlc.MediaPlayer(MoviePlay)
        media.play()
        while True:
            _,frame=cap.read()
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces= detect(gray)
            if len(faces)>0:
                media.set_pause(0)
            else:
                media.set_pause(1)
                cv2.putText(frame,"No face Detected", (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                s.speak("No face Detected")
            for face in faces:
                x1=face.left()
                y1=face.top()
                x2=face.right()
                y2=face.bottom()
                cv2.rectangle(frame,(x1,y1),(x2,y2),(255,255,0),3)
                
                shape= predict(gray,face)
                shape=face_utils.shape_to_np(shape)

                leftEye=shape[lStart:lEnd]
                rightEye=shape[rStart:rEnd]
                leftEAR=eye_aspect_ratio(leftEye)
                rightEAR=eye_aspect_ratio(rightEye)
                ear=(leftEAR+rightEAR)/2.0
                if ear<thresh:
                    flag+=1
                    if flag>=frame_check:     
                                                         # frame, message, co-ord,font for message, size of font,colot,thickness font)                               
                        cv2.putText(frame,"You are closing eyes", (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                        media.set_pause(1)
                        cv2.putText(frame,f"EAR: {ear} ", (25, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                else:
                    flag=0
                    media.set_pause(0)
                     
            cv2.imshow('cam',frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

        media.stop()
        cap.release()
        cv2.destroyAllWindows()
            
if __name__=='__main__':
    drowsiness_activator()