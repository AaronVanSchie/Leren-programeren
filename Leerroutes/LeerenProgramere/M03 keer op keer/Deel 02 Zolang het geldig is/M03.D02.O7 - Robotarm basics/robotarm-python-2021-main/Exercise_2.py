from RobotArm import RobotArm
r = RobotArm('exercise 2')
r.grab()
for i in range(7):
    r.moveRight()
r.drop()
for i in range(3):
    r.moveLeft()
r.grab()
for i in range(3):
    r.moveRight()
r.drop()