'''
Created on Aug 1, 2017

@author: alkaitz
'''
import math

'''
    There is a tunnel with width w and a set of radars (x, y, radius) places in the tunnel. Check if it is possible to cross from 
    one side to the other without raising any alarm
'''

def triggersRadar(position, radar):
    posX, posY = position
    radarX, radarY, radius = radar
    return (math.sqrt(abs(posX - radarX)**2 + abs(posY - radarY)**2) <= radius)

def checkTunnel(width, radars):
    pass

if __name__ == '__main__':
    assert(not triggersRadar((0,0), (1,1,1)))
    assert(triggersRadar((0,0), (2,0,2)))