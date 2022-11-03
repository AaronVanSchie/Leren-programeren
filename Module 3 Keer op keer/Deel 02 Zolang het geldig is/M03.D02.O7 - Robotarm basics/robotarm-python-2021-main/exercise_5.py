from RobotArm import RobotArm
r = RobotArm('exercise 5')
for i in range(7):
    r.moveRight()
r.grab()
r.moveRight()
r.drop()
for i in range (7):
    r.moveLeft()
    r.moveLeft()
    r.grab()
    r.moveRight()
    r.drop()