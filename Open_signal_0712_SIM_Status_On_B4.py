import uiautomator2 as u2
import time
import os
from datetime import datetime

def writeFile(fileName,RSRP):
    fs = open(fileName, "a")   #"w" create a new or overwrite an exist file
    fs.write(str(datetime.now().strftime("%y-%m-%d-%H-%M"))+",RSRP:,"+ str(RSRP) + "\n")
    # fs.write(str(datetime.now().strftime("%y-%m-%d-%H-%M"))+",RSRP:,"+str(RSRP)+",DB"+"\n")
    fs.close()

def main():
    d = u2.connect_usb()
    
    while d(resourceId="android:id/alertTitle", text=u"SIM status").exists():
        if True:
            # d.screen_off()
            # for i in range(2):

            Dutsignal = (d(resourceId="com.android.settings:id/signal_strength_label", text=u"Signal strength").sibling(resourceId="com.android.settings:id/signal_strength_value").get_text())
            # print(Dutsignal)
            RSRP = Dutsignal[:4]   #strip DB wording
            # RSRP=Dutsignal.strip("dBm 46 asu")   #strip DB wording
            print("-----RSRP:"+ RSRP)
            d(resourceId="android:id/alertTitle").click()   #to reset display sleep timer
            time.sleep(60)                                  #to set timer to read RSRP 
            writeFile("signal.txt",RSRP)

            if int(RSRP) < -90:            #if signal is worse than -45, log in Bad_signal.txt
                writeFile("Bad_signal.txt",RSRP) 
        else:
            break                   

if __name__ == '__main__':
    main()
