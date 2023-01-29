from RobotArm import RobotArm
r = RobotArm('exercise 8')
r.speed = 4
r.moveRight()
for i in range(7):
    r.grab()
    for i in range(8):
        r.moveRight()
    r.drop()
    for i in range(8):
        r.moveLeft()