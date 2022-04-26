import pydirectinput
import time
#import cv2


# before starting travel to Palace Approach Ledge-Road

#Keybindings must be WASD for movement. E active. Q rotate camera left. C camera down. B camera lock. M Attack. L Strong Attack

def busy_wait(dt):   
    current_time = time.time()
    while (time.time() < current_time+dt):
        pass


def start():
    ### Gives 10 seconds to tab into the elden ring game window
    print('Tab into Elden Ring')
    for i in range(0,10):
        print(".",end='')
        busy_wait(1)
    print('go')
    play()
    
    
    
def play():
    tracker=0
    

    for i in range(0,1000000000):
        loop=0
        tracker=tracker+1
        busy_wait(2)
        pydirectinput.press('g')
        busy_wait(.4)
        pydirectinput.press('f')
        busy_wait(.4)
        pydirectinput.press('e')
        busy_wait(.4)
        pydirectinput.press('e')            
    

        for i in range(0,10):
            # waits for loading to be completed. Default is 10 seconds
            #Because this is a timing based bot some experimentation may be needed for optimal results
            loop+=1
            print(loop,end='\n')
            busy_wait(1)
        
          
    
        if tracker%50==0:
            # if counter is divisible by 50 refill arrows by resting at fire.
            pydirectinput.keyDown('w')
            busy_wait(.35)
            pydirectinput.keyUp('w')
            pydirectinput.press('e')
            busy_wait(4)
            pydirectinput.press('q')
        pydirectinput.keyDown('q')
        busy_wait(.4750)
        pydirectinput.keyUp('q')
        pydirectinput.keyDown('w')
        busy_wait(1.20)
        pydirectinput.keyUp('w')
        pydirectinput.keyDown('c')
        busy_wait(.2000)
        pydirectinput.keyUp('c')
        # Next line determines how long to wait before firing. Due to animation differences some bows need different timing.
        busy_wait(4)
        pydirectinput.press('b')
        
        if tracker%2==0:
            pydirectinput.press('l')
            busy_wait(.45)
            pydirectinput.press('l')
        else: 
            pydirectinput.press('m')
            busy_wait(.45)
            pydirectinput.press('m')                
        busy_wait(9)
        
start()