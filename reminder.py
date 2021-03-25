from plyer import notification
import time

if __name__ == '__main__':
    while(True):
        notification.notify(
            title = "Please take a water break!!",
            message = "The U.S. National Academies of Sciences, Engineering, and Medicine says to drink 15.5 cups of water a day!!",
            app_icon = (r"C:\Users\RV\Desktop\WATER NOTIFICATION\back.ico"),
            timeout = 10
        )
        time.sleep(1800)
