#!/usr/bin/env python3
from threading import Thread
import tinytuya
#import time

#import os
import json
with open('snapshot.json') as json_file:
    jdata = json.load(json_file)

counter = 0
def lights(name, *num):
#    1 = on/ off toggle
#    2 = just off
#    3 = Full Brightness & on/ off toggle
#    4 = Brightness and temp according to counter
#    5 = Brightness only according to counter
#    6 = Colour Tempature only according to counter
    global br_counter, col_counter
    for item in jdata["devices"]:
        if item["name"] == name:
            break
    d = tinytuya.BulbDevice(item["id"], item["ip"], item["key"])
    d.set_version(float(item["ver"]))
    d.set_socketPersistent(True)
    data = d.status()
    for n in num:
        if n == 2:
            d.turn_off()
        if n == 1:
            if(data['dps']['20'] == True):
                #print("its on Turning off")
                d.turn_off()
            elif(data['dps']['20'] == False):
                #print("its off Turing on")
                d.turn_on()
            d.set_brightness_percentage(brightness=50)
            d.set_colourtemp_percentage(50)
        if n == 3:
            if(data['dps']['20'] == True):
                #print("its on Turning off")
                d.turn_off()
            elif(data['dps']['20'] == False):
                #print("its off Turing on")
                d.turn_on()
            d.set_brightness_percentage(brightness=100)
            d.set_colourtemp_percentage(100)
        if n == 4:
            #print(counter)
            d.set_brightness_percentage(br_counter)
            d.set_colourtemp_percentage(br_counter)
        if n == 5:
            d.set_brightness_percentage(br_counter)            
        if n == 6:
            d.set_colourtemp_percentage(col_counter) 
#-------------------------------------------------------------------------------
def bed_lights(name, *num):
    global counter
    for item in jdata["devices"]:
        if item["name"] == name:
            break
    d = tinytuya.BulbDevice(item["id"], item["ip"], item["key"])
    d.set_version(float(item["ver"]))
    d.set_socketPersistent(True)
    data = d.status()
    for n in num:
        if n == 1:
            if(data['dps']['1'] == True):
                ##print("its on Turning off")
                d.turn_off()
            elif(data['dps']['1'] == False):
                ##print("its off Turing on")
                d.turn_on()
        if n == 2:
            d.turn_off()
        if n == 4:
#            print(counter)
            d.set_brightness_percentage(counter)
            d.set_colourtemp_percentage(counter)
            if counter == 100:
                counter = 0
#lights("Leo's Light", 3)      
#lights("Leo's Light", 4)      

#lights("Light_1", 4)   
#-------------------------------------------------------------------------------
def bed():
    #Thread(target = bed_lights, args=('Bedroom Light', 1)).start() #My Bed Room
    bed_lights('Bedroom Light', 1)
    
def leo():
    #Thread(target = lights, args=("Leo's Light", 1)).start() #Leos room
    lights("Leo's Light", 1)
    
def living():
    Thread(target = lights, args=('Light_1', 1)).start()
    Thread(target = lights, args=('Light_2', 1)).start() #Living Room
    Thread(target = lights, args=('Light_3', 1)).start()
#---------------------------------------brightness zone--------------------    
def leo_br():
    global counter
    #Thread(target = lights, args=("Leo's Light", 4)).start() #Leos room brightness
    lights("Leo's Light", 4)
    counter += 10
    
def living_br():
    #global counter
    Thread(target = lights, args=('Light_1', 3)).start()
    Thread(target = lights, args=('Light_2', 3)).start() #Living Room brightness
    Thread(target = lights, args=('Light_3', 3)).start()
    #counter += 10
    #print(counter)
    
def living_br2():
    global counter
    lights("Light_1", 4) 
    lights("Light_2", 4) 
    lights("Light_3", 4) 
    counter += 10
    #print(counter)

def bed_br():
    bed_lights('Bedroom Light', 4)
    

#---------------------------------------------------------------------------------------all off ctrl---------------------
def all_pof():
    Thread(target = bed_lights, args=('Bedroom Light', 2)).start()
    Thread(target = lights, args=("Leo's Light", 2)).start()
    Thread(target = lights, args=('Light_1', 2)).start()
    Thread(target = lights, args=('Light_2', 2)).start()
    Thread(target = lights, args=('Light_3', 2)).start()
#---------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    living()
