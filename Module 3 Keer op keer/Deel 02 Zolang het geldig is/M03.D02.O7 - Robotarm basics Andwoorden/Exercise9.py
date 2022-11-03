from RobotArm import RobotArm
r = RobotArm('exercise 9')
x = 1
for i in range(4):
    for i in range(x):
        r.grab()
        for i in range(4):
            r.moveRight()
        r.drop()
        for i in range(4):
            r.moveLeft()
    r.moveRight()
    x += 1