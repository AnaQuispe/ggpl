from pyplasm import *
from larlib import *
from numpy import *
import csv


def INTERNAL_DOORS(filename,hDoor):
    with open(filename, "rb") as file:
        reader = csv.reader(file, delimiter=",")
        externalWalls = []

        for row in reader:
            x1 = float(row[0])
            x2 = float(row[1])
            y1 = float(row[2])
            y2 = float(row[3])
            externalWalls.append(OFFSET([0.15, 0.15])(POLYLINE([[x1, y1], [x2, y2]])))
        doors = PROD([STRUCT(externalWalls), Q(hDoor)])

    return doors

def WINDOWS(filename, hWindow):

    with open(filename, "rb") as file:
        reader = csv.reader(file, delimiter=",")
        externalWalls = []

        for row in reader:
            x1 = float(row[0])
            x2 = float(row[1])
            y1 = float(row[2])
            y2 = float(row[3])
            externalWalls.append(OFFSET([0.15, 0.15])(POLYLINE([[x1, y1], [x2, y2]])))
        window = PROD([STRUCT(externalWalls), Q(hWindow)])

    return window

def WALLS(filename, hWall):
    with open(filename, "rb") as file:
        reader = csv.reader(file, delimiter=",")
        externalWalls = []

        for row in reader:
            x1 = float(row[0])
            x2 = float(row[1])
            y1 = float(row[2])
            y2 = float(row[3])
            externalWalls.append(OFFSET([0.15, 0.15])(POLYLINE([[x1, y1], [x2, y2]])))
        walls = PROD([STRUCT(externalWalls), Q(hWall)])

    return walls

def groundFloor():

    walls = WALLS("walls.lines", 1.1)
    door = STRUCT([CUBOID([0.6, 0.21, 0.7]), T([1, 3])([0.3, 0.7])(R([2, 3])(-PI / 2)(MY_CYLINDER([0.3, 0.21])(16)))])
    doors_hole = STRUCT([T([1, 2])([3.4, -0.06])(door), T([1, 2])([3.4, 7.2])(door),
                         T([1, 2])([0.15, 3.4])(R([1, 2])(PI / 2)(door)),
                         T([1, 2])([7.41, 3.4])(R([1, 2])(PI / 2)(door))])

    inDoor = STRUCT([R([1, 2])(PI/4)(T([1,2])([3.1,-0.175])(CUBOID([4.2, 0.35, 0.75]))), T(1)(7.3)(R([1, 2])(3 * PI / 4)
                    (T([1, 2])([3.1,-0.175])(CUBOID([4.2,0.35,0.75])))),T([1,2])([3.4, 1.85])(OFFSET([0.0, 4.0])(door)),
                     T([1, 2])([1.7, 4.05])(R([1, 2])(-PI / 2)(OFFSET([0.0, 4.0])(S(1)([0.75 / 0.6])(door))))])

    center = DIFFERENCE([T([1, 2])([3.7, 3.675])(DIFFERENCE([MY_CYLINDER([1.71, 1.1])(32),MY_CYLINDER([1.21, 1.1])(32)]))])

    holes = STRUCT([INTERNAL_DOORS("internalDoors.lines", 0.7), T(3)(0.6)(WINDOWS("windows2.lines", 0.3)), doors_hole,
                    inDoor])
    floor = STRUCT([TEXTURE("marmo_rosso2.png")(T(3)(0.001)(MKPOL([[[0,0],[0,7.35],[7.35,0],[7.35,7.35]],[[1, 2, 3, 4]],
                    [[1]]]))), COLOR([1, 0.92, 0.84])(T(3)(-0.011)(CUBOID([7.35, 7.35, 0.01])))])
    finalGroundFloor = COLOR([1, 0.92, 0.84])(DIFFERENCE([STRUCT([walls, center]), holes]))

    detail1 = MKPOL([[[0,0],[0,7.35],[7.35,0],[7.35,7.35]],[[1, 2, 3, 4]],[[1]]])

    return STRUCT([finalGroundFloor, floor])


def firstFloor():

    walls = WALLS("walls.lines", 2.2)
    finalWalls = STRUCT([walls, T([1,2])([3.37,2])(CUBOID([0.66,0.3,2.1])), T([1,2])([3.37,5.05])(CUBOID([0.66,0.3,2.1])),
                        T([1,2])([2.05,3.27])(CUBOID([0.3,0.86,2.1])), T([1,2])([5.05,3.27])(CUBOID([0.3,0.86,2.1]))])
    centralDoor = STRUCT([CUBOID([0.6, 0.21, 1.5]), T([1, 3])([0.3, 1.5])(R([2, 3])(-PI / 2)(MY_CYLINDER([0.3, 0.21])(16)))])
    externalDoor = CUBOID([0.6, 0.21, 1.4])
    externalDoorHole = STRUCT([T([1, 2])([3.4, -0.06])(externalDoor), T([1, 2])([3.4, 7.2])(externalDoor),
                         T([1, 2])([0.15, 3.4])(R([1, 2])(PI / 2)(externalDoor)),
                         T([1, 2])([7.41, 3.4])(R([1, 2])(PI / 2)(externalDoor))])

    internalDoor = STRUCT([R([1, 2])(PI / 4)(T([1, 2])([3.1, -0.175])(CUBOID([4.2, 0.35, 0.75]))),
                           T(1)(7.3)(R([1, 2])(3 * PI / 4)(T([1, 2])([3.1, -0.175])(CUBOID([4.2, 0.35, 0.75])))),
                           T([1, 2])([3.4, 1.85])(OFFSET([0.0, 4.0])(centralDoor)),
                     T([1, 2])([1.7, 4.05])(R([1, 2])(-PI / 2)(OFFSET([0.0, 4.0])(S(1)([0.75 / 0.6])(centralDoor))))])

    internalWindow = STRUCT([R([1, 2])(PI / 4)(T([1, 2])([3.1, -0.175])(CUBOID([4.2, 0.35, 0.3]))),
                           T(1)(7.3)(R([1, 2])(3 * PI / 4)(T([1, 2])([3.1, -0.175])(CUBOID([4.2, 0.35, 0.33]))))])

    center1 = T([1, 2])([3.7,3.675])(DIFFERENCE([MY_CYLINDER([1.45,2.1])(32),MY_CYLINDER([1.35,2.1])(32)]))
    center2 = T([1, 2,3])([3.7, 3.675, 2.1])(DIFFERENCE([MY_CYLINDER([1.71, 0.1])(32), MY_CYLINDER([1.35, 0.1])(32)]))
    holes = STRUCT([INTERNAL_DOORS("internalDoors.lines", 1.4), T(3)(0.3)(WINDOWS("windows.lines", 0.9)), externalDoorHole,
                    internalDoor, T(3)(1.3)(internalWindow)])

    floor = STRUCT([TEXTURE("marmo_rosso2.png")(T(3)(0.001)(MKPOL([[[0,0],[0,7.35],[7.35,0],[7.35,7.35]],[[1, 2, 3, 4]],
                    [[1]]]))), COLOR([1, 0.92, 0.84])(T(3)(-0.011)(CUBOID([7.35,7.35,0.01])))])


    finalFirstFloor = COLOR([1, 0.92, 0.84])(DIFFERENCE([STRUCT([finalWalls, center1]), holes]))

    return STRUCT([finalFirstFloor, floor, COLOR([1, 0.92, 0.84])(center2)])

def secondFloor():
    walls = WALLS("walls.lines", 1.1)

    externalDoor = CUBOID([0.6, 0.21, 0.9])
    externalDoorHole = STRUCT([T([1, 2])([3.4, -0.06])(externalDoor), T([1, 2])([3.4, 7.2])(externalDoor),
                               T([1, 2])([0.15, 3.4])(R([1, 2])(PI / 2)(externalDoor)),
                               T([1, 2])([7.41, 3.4])(R([1, 2])(PI / 2)(externalDoor))])

    inDoor = STRUCT([R([1, 2])(PI / 4)(T([1, 2])([3.1, -0.175])(CUBOID([4.2,0.35,0.75]))), T(1)(7.3)(R([1, 2])(3 * PI/4)
                    (T([1, 2])([3.1, -0.175])(CUBOID([4.2, 0.35,0.75]))))])

    center = DIFFERENCE([T([1, 2])([3.7,3.675])(DIFFERENCE([MY_CYLINDER([1.71,1.1])(32), MY_CYLINDER([1.61, 1.1])(32)]))])

    holes = STRUCT([INTERNAL_DOORS("internalDoors2.lines", 0.9), T(3)(0.6)(WINDOWS("windows2.lines", 0.3)),
                    inDoor, externalDoorHole])
    floorBase = COLOR([1, 0.92, 0.84])((DIFFERENCE(
        [T(3)(-0.016)(CUBOID([7.35, 7.35, 0.015])), T([1, 2, 3])([2, 2, -0.016])(CUBOID([3.35, 3.35, 0.015]))])))

    finalGroundFloor = COLOR([1, 0.92, 0.84])(DIFFERENCE([STRUCT([walls, center]), holes]))

    return STRUCT([finalGroundFloor, floorBase])

def villa():
    ground = groundFloor()
    first = firstFloor()
    second = secondFloor()
    return STRUCT([ground, T(3)(1.1)(first), T(3)(3.3)(second), T([1, 2, 3])([3.7,3.675,3.3])(balcony())])


def balcony():
    colA = MY_CYLINDER([0.015, 0.36])(16)
    colB = T([1, 2])([1.35, -0.06])(CUBOID([0.037, 0.06, 0.36]))
    fb = R([1, 2])(PI / 20)(
        STRUCT([T([1, 2])([1.37, 0.037])(colA), T([1, 2])([1.365, 0.111])(colA), T([1, 2])([1.37, -0.037])(colA),
                T([1, 2])([1.365, -0.111])(colA), R([1, 2])(PI / 20)(colB), R([1, 2])(-PI / 20)(T(2)(0.04)(colB))]))
    fragBalcony = STRUCT([fb, R([1, 2])(PI / 10)(fb), R([1, 2])(2 * PI / 10)(fb), R([1, 2])(3 * PI / 10)(fb),
                          R([1, 2])(4 * PI / 10)(fb)])
    balcon = STRUCT(
        [fragBalcony, R([1, 2])(PI / 2)(fragBalcony), R([1, 2])(PI)(fragBalcony), R([1, 2])(-PI / 2)(fragBalcony),
         T(3)(0.36)(DIFFERENCE([MY_CYLINDER([1.41, 0.04])(32), MY_CYLINDER([1.33, 0.04])(32)]))])
    return COLOR([1, 0.92, 0.84])(balcon)

#VIEW(firstFloor())
#VIEW(villa())
#VIEW(secondFloor())

#VIEW(floor)

#VIEW(balcony())
