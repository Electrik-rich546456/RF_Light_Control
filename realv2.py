#!/usr/bin/env python3

import time
from rpi_rf import RFDevice
from datetime import datetime
from button_device import ButtonDevice
import signal
import sys
import my_roomctrl
import time_ex

rfdevice = RFDevice(gpio=27)
rfdevice.enable_rx()

#Time range settings between 6am - 10pm 
start = 6
end = 22
###########


# cleanup on exit
def signal_handler(sig, frame):
    rfdevice.cleanup()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

class MultipleLightButton(ButtonDevice):
    def __init__(self, id, *lights, debug=True):
        self.debug = debug
        debounce = 250.0
        long_time = 2000.0
        ButtonDevice.__init__(self, id, debounce, long_time)
        self.button_name = buttons[id]
#        self.lights = {}
#        self.statuses = {}
        self.pressing = False
#        self.fade_up = True
    def log(self, action, message):
        if self.debug:
            dt = datetime.now().strftime('%r %d/%m/%Y')
            print(f"{dt}\t{self.button_name}\t{action}\t{message}")
    def short_press(self):
        #self.button_name = buttons[id]
        #print( buttons[id])
        if (buttons[id]) == ("Hallway" or "Entrance"):
            #print(self.button_name, "short press")
            if time_ex.day_check(start,  end):
                #my_roomctrl.living()
                my_roomctrl.living_br()
            else:
                my_roomctrl.living()
#        print(type(self.button_name))
#        <class 'str'>        
    def long_rolling(self):
        if not self.pressing:
            self.pressing = True
        #print(self.button_name, "long rolling")
    def long_press(self):
        #print(self.button_name, "long press")
        #self.log('LONG', "Toggle pressing to False")
        self.pressing = False
#        self.fade_up = not self.fade_up
        
buttons = {
    3764961: "Leo's Buttons",
    835186: "Entrance",
    818562: "Hallway"
#    3764962: "Leo FadeUp",
#    3764964: "Leo FadeDown"
}

b = {}
for id in buttons:
    b[buttons[id]] = id

rooms = [
    #MultipleLightButton(b["Leo's Buttons"], "Leo's Light"),
    MultipleLightButton(b["Entrance"]),
    MultipleLightButton(b["Hallway"])
]

while True:
    for room in rooms:
        room.process(rfdevice)
    time.sleep(0.01)
