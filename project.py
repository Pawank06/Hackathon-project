
import time
import psutil
from plyer import notification

print("Started....")

cBatteryPercent = 0
pBatteryPercent = 0

#This is code the for battery remainde when connected to charging

if psutil.sensors_battery().power_plugged: #If charging is active
    pBatteryPercent = 0
    while True:
        cBattery = psutil.sensors_battery()
        CurrentBatteryPercent = cBattery.percent
        cBatteryPercent = CurrentBatteryPercent
        if cBatteryPercent >= pBatteryPercent:
            title = "Battery Percent Reminder" #display the notification title
            message = f'Your current battery percent is {CurrentBatteryPercent}'
            notification.notify(title = title, message = message)
            pBatteryPercent = cBatteryPercent + 1

        time.sleep(5)
        
#This code is for without charging

while(True):
    battery = psutil.sensors_battery()
    percent = battery.percent
     
    notification.notify(
        title="Battery Percentage",
        message=str(percent)+"% Battery remaining",
        timeout=10
    )
     
    # after every 60 mins it will show the
    # battery percentage
    time.sleep(5)
     
    continue

