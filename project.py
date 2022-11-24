import time
import psutil
from plyer import notification

print("Started....")

cBatteryPercent = 0
pBatteryPercent = 0

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
        time.sleep(1)

