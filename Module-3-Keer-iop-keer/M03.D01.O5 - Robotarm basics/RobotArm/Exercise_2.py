from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:
robotArm.grab();

for _ in range(7):
    robotArm.moveRight()

robotArm.drop()

for _ in range(3):
    robotArm.moveLeft()

robotArm.grab()

for _ in range(3):
    robotArm.moveRight()

robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()