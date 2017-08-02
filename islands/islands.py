'''
Created on Aug 1, 2017

@author: alkaitz
'''

'''
    There is an infinite 2D ocean which you can edit by placing or removing soil cells.
    Every time you include or remove a soil cell we want to know the number of existing
    islands in the ocean. An island is a North/South/East/West connected amount of soil cells.
'''

# Ocean is a set of islands
ocean = []
existingSoils = set()

# Island is a set of soil cells and a set of cells that should be considered to expand

class Island:
    soils = set()
    expandables = set()

    def containsSoil(self, position):
        return position in self.soils

    def canExpandTo(self, position):
        return position in self.expandables

    def __repr__(self):
        return str(self.soils) + ", " + str(self.expandables)

    def __str__(self):
        return str(self.soils) + ", " + str(self.expandables)

def getExpandableCells(position):
    result = set()
    posX, posY = position
    if not (posX + 1, posY) in existingSoils: result.add((posX + 1, posY))
    if not (posX - 1, posY) in existingSoils: result.add((posX - 1, posY))
    if not (posX, posY + 1) in existingSoils: result.add((posX, posY + 1))
    if not (posX, posY - 1) in existingSoils: result.add((posX, posY - 1))
    return result

def createIsland(position):
    island = Island()
    island.soils = {position}
    island.expandables = getExpandableCells(position)
    return island

def createSoil(position):
    targetIslands = []
    for island in ocean:
        if island.canExpandTo(position) or island.containsSoil(position):
            targetIslands.append(island)

    if not targetIslands:
        ocean.append(createIsland(position))
        existingSoils.add(position)
    elif len(targetIslands) == 1:
        island = targetIslands[0]
        island.soils.add(position)
        island.expandables.remove(position)
        newExpandables = getExpandableCells(position)
        island.expandables = island.expandables.union(newExpandables)
        existingSoils.add(position)
    else:
        print "Case not covered"
        raise "Error"

    return len(ocean)

def removeSoil(position):
    #TODO Fill content
    return len(ocean)

def printInfo():
    print "Islands: ", islands, " Ocean: ", ocean, " Soils: ", existingSoils

if __name__ == '__main__':
    islands = createSoil((0,0))
    printInfo()
    islands = createSoil((5,5))
    printInfo()
    islands = createSoil((0,1))
    printInfo()