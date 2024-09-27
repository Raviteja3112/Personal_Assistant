from geopy.geocoders import Nominatim
from geopy import distance
import Speak as s
geocoder=Nominatim(user_agent="capstone project")
location1="mangalagiri"
location2="phagwara"
coordinates1=geocoder.geocode(location1)
coordinates2=geocoder.geocode(location2)
lat1,long1=(coordinates1.latitude),(coordinates1.longitude)
lat2,long2=(coordinates2.latitude),(coordinates2.longitude)
place1=(lat1,long1)
place2=(lat2,long2)
dis=distance.distance(place1,place2)
dis=str(dis)
dis=float
s.speak("the distance between "+str(location1)+" and "+str(location2)+" is{:.2f}".format(dis))      