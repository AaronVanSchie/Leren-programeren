from RobotArm import RobotArm
r = RobotArm('exercise 7')
r.speed = 4
for i in range(5):
    r.moveRight()
    for i in range(6):
        r.grab()
        r.moveLeft()
        r.drop()
        r.moveRight()
    r.moveRight()