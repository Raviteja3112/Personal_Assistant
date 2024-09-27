import Speak as s
import psutil
import time
from plyer import notification


def battery():
    battery=psutil.sensors_battery()
    battery_percent=str(battery.percent)
    plugged=battery.power_plugged
    s.speak(f"sir, Battery percentage is {battery_percent}")
    title_message="Battery Notification"
    notification.notify(title=title_message,message=str(battery_percent) + "%Percetage Remaining",timeout=4)
    if plugged and battery_percent>="92%":
        s.speak("Sir battery is almost full you can remove plug")
    elif plugged:
        s.speak("Sir your system is charging")
        s.speak(f"{100-battery.percent} % more to charge to full")
    else:
        if battery_percent>="70%" :
            s.speak("I am ok my powers are stable")
        elif battery_percent>="20%":
            s.speak("My powers are getting low")
        else:
            s.speak("Its killing my energy, charge me its going to shutdown")
           

            
def cpu_usage():
    cpu=psutil.cpu_percent(interval=1)
    s.speak(f"cpu percentage is {cpu}")
    process_id=psutil.pids()
    s.speak(f"sir currently {len(process_id)} processes are running in your system")

    cpu_statistics=psutil.cpu_stats()
    s.speak(f"{cpu_statistics.ctx_switches} number of context switches since boot" )

"""
    if(cpu>5):
        s.speak("CPU limit has reached")
        s.speak("I am stopping some programs which are stopped in CPU")

        for each in process_id:
            each_process_data=psutil.Process(each)
            if(each_process_data.status()=='stopped'):
                print(each_process_data.name())
                try:
                    if each in process_id:
                        each_process_data.kill() 
                        s.speak(each_process_data.name()+ " has terminated from CPU")
                except Exception as e:
                    s.speak(e)
                    s.speak(f"{each_process_data.name()}  is not terminatted")
            
            cpu=psutil.cpu_percent(interval=1)
            s.speak(f"cpu percentage is {cpu}")
            if(cpu<=5):
                s.speak("cpu back to normal usage")
                break
        

    else:
        s.speak(f"CPU usage is {cpu}")
"""

if __name__=="__main__":
    cpu_usage()
    battery()
