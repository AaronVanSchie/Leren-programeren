from RobotArm import RobotArm
r = RobotArm('exercise 4')
r.grab()
for i in range(5):
    for i in range(2):
        r.moveRight()
    r.drop()
    for i in range(2):
        r.moveLeft()
for i in range(2):
    r.moveRight
for i in range(5):
    r.moveLeft()
    r.drop()
    r.moveRight()