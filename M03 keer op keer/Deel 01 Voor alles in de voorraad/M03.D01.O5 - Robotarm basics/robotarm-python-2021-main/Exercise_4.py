from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:

robotArm.grab()
for i in range(5):
    for i in range(2):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(2):
        robotArm.moveLeft()

for i in range(2):
    robotArm.moveRight

for i in range(5):
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()