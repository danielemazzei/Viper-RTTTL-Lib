################################################################################
# RTTTL Library Basics
#
# Created by ZERYNTH Team 2015 CC
# Authors: D. Mazzei, G. Baldi,  
###############################################################################


import rtttl
import streams

s=streams.serial()

# define a RTTTL melody to be played by passing it the RTTTL string.
# find more songs at http://ez4mobile.com/nokiatone/rtttf.htm and many other websites
song = rtttl.tune("StWars:d=4,o=5,b=160:8f,8f,8f,2a#.,2f.6,8d#6,8d6,8c6,2a#.6,f.6,8d#6,8d6,8c6,2a#.6,f.6,8d#6,8d6,8d#6,2c6,p,8f,8f,8f,2a#.,2f.6,8d#6,8d6,8c6,2a#.6,f.6,8d#6,8d6,8c6,2a#.6,f.6,8d#6,8d6,8d#6,2c6")

while True:
    print("Waiting for input")
    print("Use p for PLAY")
    # Read the serial port waiting for the Play start command 
    line=str(s.readline())  
    if line[0]=="p":
        print("Start Melody")
        print("-"*30)
        print("MAY THE FORCE BE WITH YOU!")
        print("-"*30)
        
        # play the melody actuating the PWM of pin D8 (Try it with the TOI Shield)
        song.play(D8.PWM)

        
        