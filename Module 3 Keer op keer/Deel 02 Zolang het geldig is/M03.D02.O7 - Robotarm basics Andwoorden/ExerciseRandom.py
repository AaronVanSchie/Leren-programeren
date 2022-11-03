from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
x = 1
robotArm.grab()
robotArm.scan()
while robotArm.scan() == "white" or robotArm.scan() == "green" or robotArm.scan() == "red" or robotArm.scan() == "blue" or robotArm.scan() == "yellow":
    for i in range(x):
        robotArm.moveRight()
    robotArm.drop()
    x += 1
    for i in range(x - 1):
        robotArm.moveLeft()
    robotArm.grab()
    robotArm.scan()
    if robotArm.scan() == "":
        exit()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()