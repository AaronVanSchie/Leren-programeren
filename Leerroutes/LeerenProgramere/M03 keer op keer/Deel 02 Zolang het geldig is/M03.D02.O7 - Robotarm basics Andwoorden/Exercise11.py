from RobotArm import RobotArm
r = RobotArm('exercise 11')
r.speed = 3
for i in range(8):
    r.grab()
    if r.scan() == "white":
        for i in range(1):
            r.moveRight()
        r.drop()
    if r.scan() != "white":
        r.drop()
        r.moveRight()