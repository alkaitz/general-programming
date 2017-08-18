'''
Created on Aug 1, 2017

@author: alkaitz
'''

import math

'''
    There is a 2D tunnel with width w and a set of radars (x, y, radius) placed inside of it.
    Check if it is possible to cross from one side to the other without raising any alarm
'''

def distance(position1, position2):
    origX, origY = position1
    destX, destY = position2
    return math.sqrt(abs(origX - destX)**2 + abs(origY - destY)**2)

def triggersRadar(position, radar):
    radarPosition, radiusSensor = radar
    return  distance(position, radarPosition) <= radiusSensor

def doRadarsCollide(radar1, radar2):
    radarPosition1, radiusSensor1 = radar1
    radarPosition2, radiusSensor2 = radar2
    return distance(radarPosition1, radarPosition2) < radiusSensor1 + radiusSensor2

def doesRadarTouchBorder(radar, width):
    radarPosition, radiusSensor = radar
    radarX, _ = radarPosition
    borderPosition = (radarX, width)
    return distance(radarPosition, borderPosition) < radiusSensor

def createContiguousGroups(radars):
    def doGroupsCollide(group1, group2):
        return any(True for r1 in group1 for r2 in group2 if doRadarsCollide(r1, r2))

    groups = map(lambda x: {x}, radars)
    result = []
    while groups:
        group = groups.pop()
        for other in groups:
            if doGroupsCollide(group, other):
                groups.remove(other)
                group = group.union(other)
        result.append(group)
    return result

def canCrossTunnel(width, radars):
    groups = createContiguousGroups(radars)
    for group in groups:
        # Verify if the group crosses both borders
        crossesUpper, crossesDown = False, False
        for radar in group:
            if doesRadarTouchBorder(radar, 0):
                crossesDown = True
            if doesRadarTouchBorder(radar, width):
                crossesUpper = True
        if crossesUpper and crossesDown:
            return False
    return True

if __name__ == '__main__':
    def testRadar():
        assert(not triggersRadar((0,0), ((1,1),1)))
        assert(triggersRadar((0,0), ((2,0),2)))

    def testGroups():
        collidingGroup = [
                        ((0,0), 2),
                        ((0,2), 1)
                        ]
        apartGroup = [
                    ((0,0), 1),
                    ((0,3), 1)
                    ]
        mixedGroup = [
                    ((0,0), 3),
                    ((2,2), 1),
                    ((10,0), 2)
                    ]
        assert(len(createContiguousGroups(collidingGroup)) == 1)
        assert(len(createContiguousGroups(apartGroup)) == 2)
        assert(len(createContiguousGroups(mixedGroup)) == 2)

    def testTunnel():
        assert(canCrossTunnel(10, [((1,1), 5)]))
        assert(not canCrossTunnel(2, [((1,1), 5)]))
        assert(canCrossTunnel(100, [((1,1), 5), ((3,5), 20), ((50,50), 5)]))

    testRadar()
    testGroups()
    testTunnel()
    print "Successful"