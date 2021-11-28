#!/usr/bin/env python3
import time
#range settings between 6am - 5pm 
start = 6
end = 17

# #test parameter
#hour = 17
# ###
def day_check(start, end):
    hour = int(time.strftime("%H"))
    if hour >= start and hour <= end:
        print("day time")
        return True
    else:
        print("night time")
        return False

day_check(start,  end)

#  >= Greater than or equal to x >= y	
#  <= Less than or equal to    x <= y
