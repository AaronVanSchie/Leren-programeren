from RobotArm import RobotArm
r = RobotArm('exercise 6')
r.moveRight()
for i in range(3):
    r.grab()
    r.moveLeft()
    r.drop()
    r.moveRight()
    r.grab()
    r.moveRight()
    r.drop()
    r.moveLeft()