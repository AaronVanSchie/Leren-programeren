from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
robotArm.speed = 4

for i in range(100):
    robotArm.grab()
    if robotArm.scan() == 'red':
        for i in range(9):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(9):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
robotArm.wait()