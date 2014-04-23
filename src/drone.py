#Drone implementation in python

import mcpi.minecraft as minecraft
import mcpi.block as block

class Drone:
  
  def __init__(self):
    # Connect to the Minecraft server
    self._world = minecraft.Minecraft.create()
    self._checkPoints = {}
    self._direction = 1 #default
    self._movements = [{}, {}, {}, {}]
    #east
    self._movements[0]['right'] = self._moveRight
    self._movements[0]['left'] = self._moveLeft
    self._movements[0]['fwd'] = self._moveFwd
    self._movements[0]['back'] = self._moveBack
    #south
    self._movements[1]['right'] = self._movements[0]['back']
    self._movements[1]['left'] = self._movements[0]['fwd']
    self._movements[1]['fwd'] = self._movements[0]['right']
    self._movements[1]['back'] = self._movements[0]['left']
    #west
    self._movements[2]['right'] = self._movements[0]['left']
    self._movements[2]['left'] = self._movements[0]['right']
    self._movements[2]['fwd'] = self._movements[0]['back']
    self._movements[2]['back'] = self._movements[0]['fwd']
    #north
    self._movements[3]['right'] = self._movements[0]['fwd']
    self._movements[3]['left'] = self._movements[0]['back']
    self._movements[3]['fwd'] = self._movements[0]['left']
    self._movements[3]['back'] = self._movements[0]['right']

  def chkpt(self, name):
    self._checkPoints[name] = self._world.player.getPos()

  def right(self, amount):
    self._movements[self._direction]['right'](amount)
    return self

  def left(self, amount):
    self._movements[self._direction]['left'](amount)
    return self

  def fwd(self, amount):
    self._movements[self._direction]['fwd'](amount)
    return self

  def back(self, amount):
    self._movements[self._direction]['back'](amount)
    return self

  def _moveRight(self, amount):
    [x, y, z] = self._world.player.getPos()
    print([x, y, z])
    z = z + amount
    print([x, y, z])
    self._world.player.setPos(x, y, z)

  def _moveLeft(self, amount):
    [x, y, z] = self._world.player.getPos()
    print([x, y, z])
    z = z - amount
    print([x, y, z])
    self._world.player.setPos(x, y, z)

  def _moveFwd(self, amount):
    [x, y, z] = self._world.player.getPos()
    print([x, y, z])
    x = x + amount
    print([x, y, z])
    self._world.player.setPos(x, y, z)

  def _moveBack(self, amount):
    [x, y, z] = self._world.player.getPos()
    print([x, y, z])
    x = x - amount
    print([x, y, z])
    self._world.player.setPos(x, y, z)

  def pillar(self):
    # Get the player's current position and store the coordinates
    [x,y,z] = self._world.player.getPos()
    # Set some variables to customize your pillar
    height = 3
    material = block.BRICK_BLOCK
    # Build the pillar. It will be "height" blocks high and located one step away from the player.
    for level in range(0, height):
      self._world.setBlock( x+1, y+level, z+1, material )
      level = level + 1;

