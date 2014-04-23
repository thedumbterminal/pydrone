import drone
import mcpi.block as block

d = drone.Drone()

d.chkpt('castle')

#moat
d.back(9).left(9).cylinder(block.WOOL, 20, 1)

d.pillar()
