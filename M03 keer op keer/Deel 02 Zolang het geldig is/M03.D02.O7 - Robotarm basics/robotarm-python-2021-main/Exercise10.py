from RobotArm import RobotArm
r = RobotArm('exercise 10')
r.speed = 4
aantalrechts = 9
aantalLinks = 8
for i in range(5):
    r.grab()
    for i in range(aantalrechts):
        r.moveRight()
    r.drop()
    for i in range(aantalLinks):
        r.moveLeft()
    aantalrechts -= 2
    aantalLinks -= 2