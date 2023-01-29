from RobotArm import RobotArm
r = RobotArm('exercise 3')
for i in range(1, 5):
    r.grab()
    r.moveRight()
    r.drop()
    r.moveLeft()