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
    det1 = T([1,2])([-0.03,-0.03])(CUBOID([7.41, 0.03,0.5]))
    det2 = T([1,2])([-0.06,-0.06])(CUBOID([7.47, 0.03,0.3]))
    det3 = T([1, 2, 3])([-0.06, -0.06, 0.95])(CUBOID([7.47, 0.06, 0.15]))
    detailWall1 = STRUCT([det1, T(2)(7.38)(det1), T(1)(-0.03)(R([1,2])(PI/2)(det1)), T(1)(7.35)(R([1,2])(PI/2)(det1))])
    detailWall2 = STRUCT([det2, T(2)(7.44)(det2), T(1)(-0.09)(R([1,2])(PI/2)(det2)), T(1)(7.35)(R([1,2])(PI/2)(det2))])
    detailWall3 = STRUCT([det3, T(2)(7.41)(det3), T(1)(-0.06)(R([1, 2])(PI / 2)(det3)), T(1)(7.35)(R([1, 2])(PI / 2)(det3))])

    finalWall = STRUCT([walls,detailWall1, detailWall2, detailWall3])
    door = STRUCT([CUBOID([0.6, 0.21, 0.7]), T([1, 3])([0.3, 0.7])(R([2, 3])(-PI / 2)(MY_CYLINDER([0.3, 0.21])(16)))])
    doors_hole = STRUCT([T([1, 2])([3.4, -0.06])(door), T([1, 2])([3.4, 7.2])(door),
                         T([1, 2])([0.15, 3.4])(R([1, 2])(PI / 2)(door)),
                         T([1, 2])([7.41, 3.4])(R([1, 2])(PI / 2)(door))])

    inDoor = STRUCT([R([1, 2])(PI/4)(T([1,2])([3.1,-0.175])(CUBOID([4.2, 0.35, 0.75]))), T(1)(7.3)(R([1, 2])(3 * PI / 4)
                    (T([1, 2])([3.1,-0.175])(CUBOID([4.2,0.35,0.75])))),T([1,2])([3.4, 1.85])(OFFSET([0.0, 4.0])(door)),
                     T([1, 2])([1.7, 4.05])(R([1, 2])(-PI / 2)(OFFSET([0.0, 4.0])(S(1)([0.75 / 0.6])(door))))])

    center = DIFFERENCE([T([1, 2])([3.7, 3.675])(DIFFERENCE([MY_CYLINDER([1.71, 1.1])(32),MY_CYLINDER([1.21, 1.1])(32)]))])

    holes = STRUCT([INTERNAL_DOORS("internalDoors.lines", 0.7), T(3)(0.575)(WINDOWS("windows2.lines", 0.3)), doors_hole,
                    inDoor])
    floor = STRUCT([TEXTURE("marmo_rosso2.png")(T(3)(0.001)(MKPOL([[[0,0],[0,7.35],[7.35,0],[7.35,7.35]],[[1, 2, 3, 4]],
                    [[1]]]))), COLOR([1, 0.92, 0.84])(T(3)(-0.011)(CUBOID([7.35, 7.35, 0.01])))])
    finalGroundFloor = COLOR([1, 0.92, 0.84])(DIFFERENCE([STRUCT([finalWall, center]), holes]))


    return STRUCT([finalGroundFloor, floor])


def firstFloor():

    walls = WALLS("walls.lines", 2.2)
    det1 = T([1, 2])([-0.03, -0.03])(CUBOID([7.41, 0.03, 0.15]))
    det2 = T([1, 2])([-0.06, -0.06])(CUBOID([7.47, 0.06, 0.15]))
    detailWall1 = STRUCT([det1, T(2)(7.38)(det1), T(1)(-0.03)(R([1, 2])(PI / 2)(det1)), T(1)(7.35)(R([1, 2])(PI / 2)(det1))])
    detailWall2 = STRUCT([det2, T(2)(7.41)(det2), T(1)(-0.06)(R([1, 2])(PI / 2)(det2)), T(1)(7.35)(R([1, 2])(PI / 2)(det2))])
    finalWalls = STRUCT([walls, T([1,2])([3.37,2])(CUBOID([0.66,0.3,2.1])), T([1,2])([3.37,5.05])(CUBOID([0.66,0.3,2.1])),
                        T([1,2])([2.05,3.27])(CUBOID([0.3,0.86,2.1])), T([1,2])([5.05,3.27])(CUBOID([0.3,0.86,2.1])),
                         detailWall1, T(3)(1.9)(detailWall1), T(3)(2.05)(detailWall2)])
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

    det1 = T([1, 2])([-0.045, -0.045])(CUBOID([7.44, 0.045, 0.25]))
    det2 = T([1, 2,3])([-0.07, -0.07,0.25])(CUBOID([7.49, 0.07, 0.05]))
    detailWall1 = STRUCT([det1, T(2)(7.395)(det1), T(1)(-0.045)(R([1, 2])(PI / 2)(det1)), T(1)(7.35)(R([1, 2])(PI / 2)(det1))])
    detailWall2 = STRUCT([det2, T(2)(7.42)(det2), T(1)(-0.07)(R([1, 2])(PI / 2)(det2)), T(1)(7.35)(R([1, 2])(PI / 2)(det2))])
    finalWall = STRUCT([walls, detailWall1,detailWall2])
    externalDoor = CUBOID([0.6, 0.22, 0.9])
    externalDoorHole = STRUCT([T([1, 2])([3.4, -0.07])(externalDoor), T([1, 2])([3.4, 7.2])(externalDoor),
                               T([1, 2])([0.15, 3.4])(R([1, 2])(PI / 2)(externalDoor)),
                               T([1, 2])([7.42, 3.4])(R([1, 2])(PI / 2)(externalDoor))])

    inDoor = STRUCT([R([1, 2])(PI / 4)(T([1, 2])([3.1, -0.175])(CUBOID([4.2,0.35,0.75]))), T(1)(7.3)(R([1, 2])(3 * PI/4)
                    (T([1, 2])([3.1, -0.175])(CUBOID([4.2, 0.35,0.75]))))])

    center = DIFFERENCE([T([1, 2])([3.7,3.675])(DIFFERENCE([MY_CYLINDER([1.71,1.1])(32), MY_CYLINDER([1.61, 1.1])(32)]))])

    holes = STRUCT([INTERNAL_DOORS("internalDoors2.lines", 0.9), T(3)(0.6)(WINDOWS("windows2.lines", 0.3)),
                    inDoor, externalDoorHole])
    floorBase = COLOR(BROWN)((DIFFERENCE(
        [T(3)(-0.014)(CUBOID([7.35, 7.35, 0.015])), T([1, 2, 3])([2, 2, -0.014])(CUBOID([3.35, 3.35, 0.015]))])))

    finalGroundFloor = COLOR([1, 0.92, 0.84])(DIFFERENCE([STRUCT([finalWall, center]), holes]))

    return STRUCT([finalGroundFloor, floorBase])



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

def externalStair():

    stairs = []
    for i in range(1, 20):
        step = T([1, 3])([2.05 - (0.1079 * i), 0.055 * (i - 1)])(CUBOID([0.1079, 3.4, 0.055]))
        stairs.append(step)

    return STRUCT(stairs)



def lateralStructure():

    # ground floor of the lateral structure of the villa

    w1 = CUBOID([3.65, 0.25,0.95])
    det = DIFFERENCE([STRUCT([T(2)(-0.06)(CUBOID([3.71,0.37,0.3])),T(2)(-0.03)(CUBOID([3.68,0.31,0.5]))]), w1])
    wall1 = STRUCT([w1, T(2)(3.65)(w1), T([1,2])([1.3,0.25])(CUBOID([0.15,3.4,0.95])), det, T(2)(3.65)(det)])
    roof = MKPOL([[[0,-0.06],[3.71,-0.06],[3.71,0.31],[1.6,0.31],[1.6,3.59],[3.71,3.59],[3.71,3.96],[0,3.96],[0,0.31],[0,3.59]],
                  [[1,2,3,9],[10,5,6,7,8],[9,4,5,10]],[[1]]])
    d1 = STRUCT([T(2)(-0.1)(CUBOID([0.8,0.5,0.65])), DIFFERENCE([T([1,2,3])([0.4,0.31,-0.095])(R([2,3])(PI/2)(MY_CYLINDER([0.85,0.31])(32))),
                                                      T([1,3])([-0.7,-1.3])(CUBOID([2,0.31,1.95]))])])
    holeDoor = STRUCT([T([1,2])([0.25,-0.06])(d1), T([1,2])([0.25,3.65])(d1), T([1,2])([1.3,1.65])(CUBOID([0.15,0.6,0.8]))])
    finalRoof = T(3)(0.95)(PROD([roof, Q(0.15)]))
    finalGroundFloor = STRUCT([DIFFERENCE([STRUCT([wall1, finalRoof]), holeDoor]), T([1,2])([1.6,0.25])(externalStair())])

    # first floor of the lateral structure of the villa

    w2 = T(3)(1.1)(CUBOID([1.27, 0.25, 1.9]))
    holeWall = STRUCT([CUBOID([0.8, 0.25, 1.25]), T([1, 3])([0.4, 1.25])(R([2, 3])(-PI / 2)(MY_CYLINDER([0.4, 0.25])(16)))])
    wall2 = DIFFERENCE([STRUCT([w2,T(2)(3.65)(w2)]), T([1,3])([0.25,1.1])(holeWall), T([1,2,3])([0.25,3.65,1.1])(holeWall)])

    det2 = T([1, 3])([0.25, 1.1])(CUBOID([0.8, 0.1, 0.35]))
    det3 = T([2,3])([-0.03, 1.1])(CUBOID([1.27,0.03,0.15]))
    finalDetail = STRUCT([det2, T(2)(3.8)(det2), det3, T(2)(3.93)(det3)])

    columns = []
    for i in range (1,7):
        base = T([1,2,3])([1.3,0.72*(i-1),1.1])(CUBOID([0.3,0.3,0.15]))
        col = T([1,2,3])([1.45,0.15+0.72*(i-1),1.25])(MY_CYLINDER([0.1,1.75])(16))
        column = STRUCT([base,col])
        columns.append(column)

    return COLOR([1, 0.92, 0.84])(STRUCT([finalGroundFloor, wall2, finalDetail, STRUCT(columns)]))

def villa():
    ground = groundFloor()
    first = firstFloor()
    second = secondFloor()

    centralStruct = T([1,2])([3.65,3.65])(STRUCT([ground, T(3)(1.1)(first), T(3)(3.3)(second), T([1, 2, 3])([3.7,3.675,3.3])(balcony())]))
    lateral = lateralStructure()
    latStruct = STRUCT([T([1,2])([11,5.5])(lateral), T([1,2])([9.15,11])(R([1,2])(PI/2)(lateral)),
                        T([1,2])([3.65,9.15])(R([1,2])(PI)(lateral)), T([1,2])([5.5,3.65])(R([1,2])(-PI/2)(lateral))])
    return STRUCT([centralStruct, latStruct])

#VIEW(groundFloor())
#VIEW(firstFloor())
VIEW(villa())
#VIEW(secondFloor())

#VIEW(floor)

#VIEW(balcony())

#VIEW(lateralStructure())
#VIEW(externalStair())
