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

    internalDoor = STRUCT([R([1, 2])(PI / 4)(T([1, 2])([3.1, -0.15])(CUBOID([4.2, 0.3, 0.75]))),
                           T(1)(7.4)(R([1, 2])(3 * PI / 4)(T([1, 2])([3.1, -0.15])(CUBOID([4.2, 0.3, 0.75])))),
                           T([1, 2])([3.4, 1.85])(OFFSET([0.0, 4.0])(centralDoor)),
                     T([1, 2])([1.7, 4.05])(R([1, 2])(-PI / 2)(OFFSET([0.0, 4.0])(S(1)([0.75 / 0.6])(centralDoor))))])

    internalWindow = STRUCT([R([1, 2])(PI / 4)(T([1, 2])([3.1, -0.15])(CUBOID([4.2, 0.3, 0.3]))),
                           T(1)(7.4)(R([1, 2])(3 * PI / 4)(T([1, 2])([3.1, -0.15])(CUBOID([4.2, 0.3, 0.33]))))])

    center1 = T([1, 2])([3.7,3.675])(DIFFERENCE([MY_CYLINDER([1.45,2.16])(32),MY_CYLINDER([1.35,2.16])(32)]))
    center2 = T([1, 2,3])([3.7, 3.675, 2.16])(DIFFERENCE([MY_CYLINDER([1.71, 0.04])(32), MY_CYLINDER([1.18, 0.04])(32)]))
    holes = STRUCT([INTERNAL_DOORS("internalDoors.lines", 1.4), T(3)(0.3)(WINDOWS("windows.lines", 0.9)), externalDoorHole,
                    internalDoor, T(3)(1.25)(internalWindow)])

    floor = STRUCT([TEXTURE("marmo_rosso2.png")(T(3)(0.001)(MKPOL([[[0,0],[0,7.35],[7.35,0],[7.35,7.35]],[[1, 2, 3, 4]],
                    [[1]]]))), COLOR([1, 0.92, 0.84])(T(3)(-0.011)(CUBOID([7.35,7.35,0.01])))])


    finalFirstFloor = COLOR([1, 0.92, 0.84])(DIFFERENCE([STRUCT([finalWalls, center1]), holes]))

    return STRUCT([finalFirstFloor, floor, COLOR([1, 0.92, 0.84])(center2), T([1, 2,3])([3.7, 3.675, 1.9])
                    (detailDome([1.35,1.22, 1.3,0.13,0.07])([1.22,1.18, 0.03]))])

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




def detailDome(params1):
    re1, ri1, ri21, h11, h21 = params1
    def detailDome1(params2):

        re2, ri2, h12 = params2

        det1 = T([1, 3])([ri1, 0.02])(CUBOID([0.08, 0.08, h11-0.02]))
        cop = []
        for i in range(1, 6):
            frag = R([1, 2])(PI / 10 * (i - 1))(det1)
            cop.append(frag)
        fragCop = STRUCT(cop)
        finalCop = STRUCT([fragCop, R([1, 2])(PI / 2)(fragCop), R([1, 2])(PI)(fragCop), R([1, 2])(-PI / 2)(fragCop)])
        cyl1 = STRUCT([DIFFERENCE([MY_CYLINDER([re1,h11])(16), MY_CYLINDER([ri21,h11])(32)]),
                       T(3)(h11)(DIFFERENCE([MY_CYLINDER([re1, h21])(16), MY_CYLINDER([ri1+0.01, h21])(32)]))])
        finalDet1 = STRUCT([finalCop, cyl1])

        det2 = T(1)(ri2)(CUBOID([0.045, 0.08, 0.03]))
        cop2 = []
        for i in range(1, 6):
            frag = R([1, 2])(PI / 10 * (i - 1))(det2)
            cop2.append(frag)
        fragCop2 = STRUCT(cop2)
        finalCop2 = STRUCT([fragCop2, R([1, 2])(PI / 2)(fragCop2), R([1, 2])(PI)(fragCop2), R([1, 2])(-PI / 2)(fragCop2)])
        cyl2 = T(3)(0.03)(DIFFERENCE([MY_CYLINDER([re1, h12])(16), MY_CYLINDER([ri2+0.01, h12])(32)]))
        finalDet2 = STRUCT([finalCop2, cyl2])

        return COLOR([1, 0.92, 0.84])(STRUCT([finalDet1, T(3)(h11+h21)(finalDet2)]))

    return detailDome1

def balcony():
    colA = MY_CYLINDER([0.015, 0.36])(16)
    colB = T([1, 2])([1.23, -0.036])(CUBOID([0.037, 0.036, 0.36]))
    fb = R([1, 2])(PI / 20)(
        STRUCT([T([1, 2])([1.25, 0.035])(colA), T([1, 2])([1.245, 0.105])(colA), T([1, 2])([1.25, -0.035])(colA),
                T([1, 2])([1.245, -0.105])(colA), R([1, 2])(PI / 20)(colB), R([1, 2])(-PI / 20)(T(2)(0.036)(colB))]))
    fragBalcony = STRUCT([fb, R([1, 2])(PI / 10)(fb), R([1, 2])(2 * PI / 10)(fb), R([1, 2])(3 * PI / 10)(fb),
                          R([1, 2])(4 * PI / 10)(fb)])
    balcon = STRUCT(
        [fragBalcony, R([1, 2])(PI / 2)(fragBalcony), R([1, 2])(PI)(fragBalcony), R([1, 2])(-PI / 2)(fragBalcony),
         T(3)(0.36)(DIFFERENCE([MY_CYLINDER([1.3, 0.04])(32), MY_CYLINDER([1.21, 0.04])(32)]))])
    return COLOR([1, 0.92, 0.84])(balcon)

def externalStair():

    stairs = []
    for i in range(1, 20):
        step = T([1, 3])([2.05 - (0.1079 * i), 0.055 * (i - 1)])(CUBOID([0.1079, 3.4, 0.055]))
        stairs.append(step)

    return STRUCT(stairs)



def lateralStructure():

    # GROUND FLOOR OF THE LATERAL STRUCTURE OF THE VILLA

    w1 = CUBOID([3.65, 0.25,0.95])
    det = DIFFERENCE([STRUCT([T(2)(-0.06)(CUBOID([3.71,0.37,0.3])),T(2)(-0.03)(CUBOID([3.68,0.31,0.5]))]), w1])
    wall1 = STRUCT([w1, T(2)(3.65)(w1), T([1,2])([1.3,0.25])(CUBOID([0.15,3.4,0.95])), det, T(2)(3.65)(det)])
    roof = MKPOL([[[0,-0.06],[3.71,-0.06],[3.71,0.31],[1.6,0.31],[1.6,3.59],[3.71,3.59],[3.71,3.96],[0,3.96],[0,0.31],[0,3.59]],
                  [[1,2,3,9],[10,5,6,7,8],[9,4,5,10]],[[1]]])
    d1 = STRUCT([T(2)(-0.1)(CUBOID([0.8,0.5,0.65])), DIFFERENCE([T([1,2,3])([0.4,0.31,-0.095])(R([2,3])(PI/2)(MY_CYLINDER([0.85,0.31])(32))),
                                                      T([1,3])([-0.7,-1.3])(CUBOID([2,0.31,1.95]))])])
    hw = T([1,3])([1.6,0.575])(CUBOID([0.4,0.25,0.3]))
    holeDoor = STRUCT([T([1,2])([0.25,-0.06])(d1), T([1,2])([0.25,3.65])(d1), T([1,2])([1.3,1.65])(CUBOID([0.15,0.6,0.8])),
                       hw, T(2)(3.65)(hw)])
    finalRoof = T(3)(0.95)(PROD([roof, Q(0.15)]))
    finalGroundFloor = STRUCT([DIFFERENCE([STRUCT([wall1, finalRoof]), holeDoor]), T([1,2])([1.6,0.25])(externalStair())])

    # FIRST FLOOR OF THE LATERAL STRUCTURE OF THE VILLA

    w2 = T(3)(1.1)(CUBOID([1.27, 0.25, 1.9]))

    holeWall = STRUCT([CUBOID([0.8, 0.25, 1.25]), T([1, 3])([0.4, 1.25])(R([2, 3])(-PI / 2)(MY_CYLINDER([0.4, 0.25])(16)))])
    wall2 = DIFFERENCE([STRUCT([w2,T(2)(3.65)(w2)]), T([1,3])([0.25,1.1])(holeWall),
                        T([1,2,3])([0.25,3.65,1.1])(holeWall)])
    detw = OFFSET([0, 0.035, 0])(MKPOL([[[0.45, -0.035, 3], [0.85, -0.035, 3], [0.7, -0.035, 2.74], [0.6, -0.035, 2.74]],
                                        [[1, 2, 3, 4]], [[1]]]))
    dw = T([1,2,3])([-0.03,-0.03, 2.2])(CUBOID([0.31,0.31,0.15]))
    detw1 = STRUCT([dw, T(2)(3.65)(dw),T(1)(1.03)(dw),T([1,2])([1.03,3.65])(dw)])
    det2 = T([1, 3])([0.25, 1.1])(CUBOID([0.8, 0.1, 0.35]))
    det3 = T([2,3])([-0.03, 1.1])(CUBOID([1.27,0.03,0.15]))
    finalDetail = STRUCT([det2, T(2)(3.8)(det2), det3, T(2)(3.93)(det3), detw,T(2)(3.935)(detw), detw1])

    col1 = MY_CYLINDER([0.1,1.75])(16)
    col2 = MY_CYLINDER([0.14, 0.07])(16)
    detcolp = R([1,3])(-PI/2)(MY_CYLINDER([0.05,0.25])(16))
    detcolumn = STRUCT([T([1,2,3])([1.32,0,2.954])(detcolp),T([1,2,3])([1.32,0.2,2.954])(detcolp)])
    columns = []
    for i in range (1,7):
        base = T([1,2,3])([1.3,0.72*(i-1),1.1])(CUBOID([0.3,0.3,0.15]))
        col = T([1,2,3])([1.45,0.15+0.72*(i-1),1.25])(col1)
        det01 = T([1,2,3])([1.45,0.15+0.72*(i-1),1.25])(col2)
        det02 = T(2)(0.05+0.72*(i-1))(detcolumn)
        column = STRUCT([base,col,det01, T(3)(1.68)(det01), det02])
        columns.append(column)

    holeRoof = OFFSET([0,3.4])(T([1,2,3])([0.65,0.25,-0.558])(R([2,3])(-PI/2)(MY_CYLINDER([0.85,0.06])(32))))
    roof = DIFFERENCE([STRUCT([T(2)(-0.03)(CUBOID([1.63,3.96,0.15])), T([2,3])([-0.06,0.15])(CUBOID([1.66,4.02,0.15]))]), holeRoof])
    finalFirstFloor = STRUCT([wall2, finalDetail, STRUCT(columns), T(3)(3)(roof)])

    # SECOND FLOOR OF THE LATERAL STRUCTURE OF THE VILLA

    d4 = STRUCT([T(2)(-0.035)(CUBOID([1.635,3.97,0.17])), T([2,3])([-0.065,0.17])(CUBOID([1.665,4.03,0.05]))])
    detail4 = DIFFERENCE([d4, CUBOID([1.6,3.9,0.3])])
    hole3 = R([1,3])(-PI/2)(MY_CYLINDER([0.1,0.15])(16))
    holeWall3 = STRUCT([T([1,2,3])([1.45,1.22,0.45])(hole3), T([1,2,3])([1.45,2.68,0.45])(hole3)])
    wall3 = OFFSET([0.15,0,0])(MKPOL([[[1.45,0,0.22],[1.45,3.9,0.22],[1.45,1.95,0.95]],[[1,2,3]],[[1]]]))

    r1 = OFFSET([1.665,0,0])(MKPOL([[[0, -0.094, 0.22],[0,-0.065, 0.17],[0, 1.95, 0.95],[0, 1.95, 1]],[[1, 2, 3, 4]], [[1]]]))
    roof1 = STRUCT([r1, T([1, 2])([1.665, 3.9])(R([1, 2])(PI)(r1))])
    r2 = OFFSET([1.7,0,0])(MKPOL([[[0, -0.14, 0.3],[0,-0.094, 0.22],[0, 1.95, 1],[0, 1.95, 1.08]],[[1, 2, 3, 4]], [[1]]]))
    roof2 = STRUCT([r2, T([1, 2])([1.7, 3.9])(R([1, 2])(PI)(r2))])
    r3 = TEXTURE("tegole4.png")(OFFSET([1.72,0,0])(MKPOL([[[0, -0.2015, 0.28],[0,-0.19, 0.26],[0, 1.95, 1.08],[0, 1.95, 1.1]],
                                                          [[1, 2, 3, 4]], [[1]]])))
    roof3 = STRUCT([r3, T([1, 2])([1.72, 3.9])(R([1, 2])(PI)(r3))])
    detRoof1 = []
    detr = CUBOID([0.061,0.03,0.061])
    for j in range(1,14):
        detr1 = T([1,2,3])([0.061*(j*2-1),-0.065,0.109])(detr)
        detRoof1.append(detr1)
    detRoof2 = []
    det2 = CUBOID([0.03,0.061,0.061])
    for k in range(1,33):
        detr2 = T([1, 2, 3])([1.635, 0.061 * (k * 2 - 1), 0.109])(det2)
        detRoof2.append(detr2)
    detRoof3 =[]
    for m in range(1,17):
        detr3 = T([1,2,3])([1.6, 0.061*(m*2-1),0.0235*(m*2-1)])(det2)
        detRoof3.append(detr3)
    roof4 = T(3)(0.16)(STRUCT(detRoof3))

    dtroof = STRUCT([T([1,2,3])([1.35,0.05,0.33])(CUBOID([0.2,0.2,0.15])), TEXTURE("tegole4.png")(T([1,2,3])([1.32,0.02,0.48])
                                                                                                  (CUBOID([0.26,0.26,0.05])))])
    finalDetRoof = STRUCT([STRUCT(detRoof1), T(2)(3.995)(STRUCT(detRoof1)), T(2)(-0.0305)(STRUCT(detRoof2)),
                           T([1,2])([3.23,3.9])(R([1,2])(PI)(roof4)), roof4,dtroof,T(2)(3.6)(dtroof), T([2,3])([1.8,0.66])(dtroof)])
    finalWall3 = STRUCT([detail4,DIFFERENCE([wall3, holeWall3]), roof1, roof2, roof3,finalDetRoof])


    return COLOR([1, 0.92, 0.84])(STRUCT([finalGroundFloor, finalFirstFloor, T(3)(3.3)(finalWall3)]))

# this function return a half of sphere
def HALFSPHERE(radius):

    def HALFSPHERE0(subds):
        N, M = subds
        domain = Hpc(Grid([N * [PI / N], M * [2 * PI / M]]))
        domain = MAT([[1, 0, 0, 0], [-PI / 2, 1, 0, 0], [-PI, 0, 1, 0], [0, 0, 0, 1]])(domain)
        fx = lambda p: radius * math.cos(p[0]) * math.sin(p[1])
        fy = lambda p: radius * math.cos(p[0]) * math.cos(p[1])
        fz = lambda p: radius * ABS(math.sin(p[0]))
        ret = GMAP([fx, fy, fz])(domain)
        return ret
    return HALFSPHERE0


def roof():

    base = OFFSET([0,3.9,0])(T(3)(-0.12)(MKPOL([[[-0.03,-0.03,0],[-0.18,-0.18,0.12],[7.53,-0.18,0.12],[7.38,-0.03,0]],[[1,2,3,4]],[[1]]])))
    finalBase = STRUCT([base, T([1,2])([7.35,7.35])(R([1,2])(PI)(base))])
    r1 = OFFSET([0,0,0.04])(MKPOL([[[-0.2,-0.2,0],[3.675,3.675,1.65],[7.55,-0.2,0]],[[1,2,3]],[[1]]]))
    roof = TEXTURE("tegole3.png")(DIFFERENCE([r1,T([1,2])([3.7,3.675])(MY_CYLINDER([1.71, 1.8])(32))]))

    bigRoof = STRUCT([roof,T(1)(7.35)(R([1,2])(PI/2)(roof)),T([1,2])([7.35,7.35])(R([1,2])(PI)(roof)),T(2)(7.35)(R([1,2])(-PI/2)(roof))])
    centerWalls = DIFFERENCE([STRUCT([T([1,2])([3.7,3.675])(MY_CYLINDER([1.71, 1.2])(32)), finalBase]),
                              T([1,2,3])([3.7,3.675,-0.12])(MY_CYLINDER([1.61, 1.9])(32))])

    finalRoof = COLOR([1, 0.92, 0.84])(STRUCT([bigRoof, centerWalls]))
    dome = T([1, 2, 3])([3.7, 3.675, 0.62])(HALFSPHERE(1.6)([32, 32]))

    frag1 = fragDome([1.77,1.61,0.15,1])
    frag2 = fragDome([1.61,1.52,0.15,3])
    frag3 = fragDome([1.48, 1.45,0.1,2])
    frag4 = fragDome([1.34,1.32, 0.13,2])
    frag5 = fragDome([1.21,1.19, 0.11,1])
    frag6 = fragDome([1.05,1.02, 0.11,1])
    frag7 = fragDome([0.905, 0.87,0.08,3])
    frag8 = fragDome([0.72,0.7,0.05,3])
    frag9 = fragDome([0.56, 0.5,0.02,3])

    det2 = MKPOL([[[0.32, 0.137, 0], [0.32, -0.137, 0], [0.1, -0.0475, 0.16], [0.1, 0.0475, 0.16]], [[4, 3, 2, 1]], [[1]]])
    detDome1 = STRUCT([det2, R([1, 2])(PI / 4)(det2), R([1, 2])(PI / 2)(det2), R([1, 2])(PI / 4 * 3)(det2), R([1, 2])(PI)(det2),
                      R([1, 2])(-PI / 4)(det2),R([1, 2])(-PI / 2)(det2), R([1, 2])(-PI / 4 * 3)(det2)])
    det3 = MKPOL([[[0.15, 0.062, 0], [0.15, -0.062, 0], [0, 0, 0.08]], [[3, 2, 1]], [[1]]])
    detDome2 = STRUCT([det3, R([1, 2])(PI / 4)(det3), R([1, 2])(PI / 2)(det3), R([1, 2])(PI / 4 * 3)(det3), R([1, 2])(PI)(det3),
                        R([1, 2])(-PI / 4)(det3), R([1, 2])(-PI / 2)(det3), R([1, 2])(-PI / 4 * 3)(det3)])
    onDome = COLOR([1, 0.92, 0.84])(STRUCT([T(3)(1.099)(MY_CYLINDER([0.35, 0.03])(32)), T(3)(1.129)(MY_CYLINDER([0.37, 0.02])(32)), T(3)(1.149)(detDome1),
                     T(3)(1.309)(MY_CYLINDER([0.1, 0.01])(16)), T(3)(1.319)(detDome2)]))

    finalDome = STRUCT([frag1,T(3)(0.15)(frag2), T(3)(0.3)(frag3), T(3)(0.41)(frag4), T(3)(0.56)(frag5), T(3)(0.67)(frag6),
                        T(3)(0.805)(frag7), T(3)(0.909)(frag8), T(3)(1)(frag9), onDome])

    det4 = STRUCT([detailDome([1.63, 1.46, 1.56, 0.13, 0.07])([1.46, 1.42, 0.03]),
                   R([1, 2])(PI / 20)(detailDome([1.63, 1.46, 1.56, 0.13, 0.07])([1.46, 1.42, 0.03]))])

    det5 = R([1,2])(PI/15)(detailDome([1.52,1.37, 1.47,0.13,0.07])([1.37,1.33, 0.03]))
    finalDet =  STRUCT([det4, T(3)(0.25)(det5)])

    return STRUCT([finalRoof, T([1,2,3])([3.7,3.675,1.2])(finalDome), dome, T([1, 2])([3.7,3.675])(finalDet)])


def fragDome(parameters):
    re,ri,h,t = parameters

    base = COLOR([1, 0.92, 0.84])(DIFFERENCE([MY_CYLINDER([re,h])(32),MY_CYLINDER([ri,h])(16)]))
    angle = (3.14*(re+0.02))/20
    if(t==1):
        c = R([1, 2])(PI / 40)(TEXTURE("tegole1.png")(T(1)(re + 0.02)(R([1, 3])(PI / 12 * 4)(T([1, 2])([-0.005, -(angle / 2)])(CUBOID([0.005, angle, 0.25]))))))
    if(t ==2):
        c = R([1, 2])(PI / 40)(TEXTURE("tegole1.png")(T(1)(re+0.02)(R([1, 3])(PI / 14* 4)(T([1, 2])([-0.005, -(angle/2)])(CUBOID([0.005, angle, 0.25]))))))
    if(t==3):
        c = R([1, 2])(PI / 40)(TEXTURE("tegole1.png")(T(1)(re+0.02)(R([1, 3])(PI / 10 * 4)(T([1, 2])([-0.005, -(angle/2)])(CUBOID([0.005, angle, 0.25]))))))
    cop = []
    for i in range(1, 11):
        frag = R([1, 2])(PI / 20 * (i - 1))(c)
        cop.append(frag)
    fragCop = STRUCT(cop)
    finalCop = STRUCT([fragCop, R([1, 2])(PI / 2)(fragCop), R([1, 2])(PI)(fragCop), R([1, 2])(-PI / 2)(fragCop)])

    return STRUCT([base, T(3)(h)(finalCop)])


def villa():
    ground = groundFloor()
    first = firstFloor()
    second = secondFloor()
    r = roof()
    centralStruct = T([1,2])([3.65,3.65])(STRUCT([ground, T(3)(1.1)(first), T(3)(3.3)(second), T([1, 2, 3])([3.7,3.675,3.3])(balcony()),
                                                  T(3)(4.4)(r)]))
    lateral = lateralStructure()

    latStruct = STRUCT([T([1,2])([11,5.5])(lateral), T([1,2])([9.15,11])(R([1,2])(PI/2)(lateral)),
                        T([1,2])([3.65,9.15])(R([1,2])(PI)(lateral)), T([1,2])([5.5,3.65])(R([1,2])(-PI/2)(lateral))])
    return STRUCT([centralStruct, latStruct])


def detailWindowDoor(param):
    if param == "window":
        det1 = T(3)(0.25)(CUBOID([0.58,0.05,0.05]))
        det2 = T([1,2,3])([0.03,0.01,0.2])(CUBOID([0.52,0.04,0.05]))
        det3 = OFFSET([0,0.03,0])(MKPOL([[[0.03,0.02,0.2],[0.04,0.02,0.15],[0.54,0.02,0.15],[0.55,0.02,0.2]],[[1,2,3,4]],[[1]]]))
        holeWindow = T([1, 3])([0.09, 0.3])(CUBOID([0.4, 0.2, 0.9]))
        det4 = DIFFERENCE([T([1,2,3])([0.03,0.01,0.3])(CUBOID([0.52,0.04,1.02])), holeWindow])
        finalDet1 = STRUCT([T([2,3])([-0.02,1.12])(det2), T([2,3])([-0.04,1.17])(det2), det1, det2, det3, det4])

        c1 = DIFFERENCE([T([2,3])([0.06,0.21])(R([1,3])(-PI/2)(MY_CYLINDER([0.06,0.05])(16))),T(2)(0.09)(CUBOID([0.05,0.1,0.27]))])
        c2 = T([2, 3])([0.07, 0.03])(R([1, 3])(-PI / 2)(MY_CYLINDER([0.03, 0.05])(16)))
        c3 = OFFSET([0.05,0,0])(MKPOL([[[0,0.09,0.03],[0,0.005,0.19],[0,0.045,0.19]],[[1,2,3]],[[1]]]))

        finalDet2 = STRUCT([c1,c2,c3])

        d1 = OFFSET([0,0.12,0])(MKPOL([[[0,0,0],[0.345,0,0.2],[0.69,0,0],[0.05,0,0],[0.343,0,0.17],[0.66,0,0],[0.06,0,0.03],
                                        [0.63,0,0.03]],[[1,2,5,4],[2,3,6,5]],[[1]]]))
        d2 = OFFSET([0,0.09,0])(MKPOL([[[0,0,0],[0.06,0,0.03],[0.63,0,0.03],[0.69,0,0]],[[1,2,3,4]],[[1]]]))

        finalDet3 = STRUCT([d1, T(2)(0.03)(d2)])
        finalWindow = T(2)(-0.12)(STRUCT([T(2)(0.07)(finalDet1), T([1,2,3])([-0.02,0.03,1.15])(finalDet2), T([1,2,3])([0.55,0.03,1.15])(finalDet2),
                           T([1,3])([-0.055,1.42])(finalDet3)]))
        return finalWindow
    elif param == "door":

        det1 = STRUCT([T([1,2])([0.195,0.075])(CUBOID([0.72,0.08,1.52])), T([1,2])([0.135,0.115])(CUBOID([0.84,0.04,1.64]))])
        finalDet1 = DIFFERENCE([det1,T(1)(0.255)(CUBOID([0.6,0.5,1.4]))])

        d1 = OFFSET([0.1,0,0])(MKPOL([[[0,0.135,0.03],[0,0.015,0.255],[0,0.08,0.255]],[[1,2,3]],[[1]]]))
        d2 =DIFFERENCE([T([2,3])([0.09,0.3])(R([1,3])(-PI/2)(MY_CYLINDER([0.09,0.1])(16))), T(2)(0.135)(CUBOID([0.2,0.7,0.4]))])
        d3 = T([2, 3])([0.105, 0.03])(R([1, 3])(-PI / 2)(MY_CYLINDER([0.03, 0.1])(16)))
        finalDet2 = STRUCT([d1,d2,d3])

        c1 = T(2)(0.035)(OFFSET([0,0.12,0])(MKPOL([[[0,0,1.64],[0.555,0,1.87],[1.11,0,1.64],[1.035,0,1.64],[0.075,0,1.64],
                                         [0.555,0,1.83]],[[1,2,6,5],[2,6,4,3]],[[1]]])))
        c2 = T(2)(0.065)(OFFSET([0,0.09,0])(MKPOL([[[0,0,1.64],[0.1,0,1.68],[1.01,0,1.68],[1.11,0,1.64]],[[1,2,3,4]],[[1]]])))
        c3 = T(2)(0.115)(OFFSET([0,0.04,0])(MKPOL([[[1.035,0,1.64],[0.075,0,1.64],[0.555,0,1.83]],[[1,2,3]],[[1]]])))
        detUp1 = []
        detr = CUBOID([0.049, 0.035, 0.04])
        for j in range(1, 10):
            detr1 = T([1, 3])([0.049 * (j * 2 - 1), 1.6])(detr)
            detUp1.append(detr1)

        detUp2 = []
        detr2 = CUBOID([0.046, 0.035, 0.04])
        for m in range(1, 6):
            detr3 = T([1, 3])([0.049 * (m * 2 - 1), 1.625 +0.0195 * (m * 2 - 1)])(detr2)
            detUp2.append(detr3)

        finalDet3 = STRUCT([c1,c2, c3, T([1,2])([0.086,0.08])(STRUCT(detUp1)), T([1,2])([0.089,0.08])(STRUCT(detUp2)),
                            T([1, 2])([1.02, 0.115])(R([1,2])(PI)(STRUCT(detUp2)))])

        finalDoor = T(2)(-0.155)(STRUCT([finalDet1, T([1,2,3])([0.035,0.02,1.25])(finalDet2),
                                         T([1,2,3])([0.975,0.02,1.25])(finalDet2), finalDet3]))
        return finalDoor

def movingStructureBuilder(X, Y, Z, B):
        """
        :param X: a list of distances on the X axis
        :param Y: a list of distances on the Y axis
        :param Z: a list of distances on the Z axis
        :param B: a three-dimensional matrix of occupancy
        :return: a 2nd order function
        """
        struct = []
        x = 0
        for l in range(0, len(B)):  # for each x
            y = 0
            for w in range(0, len(B[l])):  # for each y
                z = 0
                for h in range(0, len(B[l][w])):  # for each z
                    if (w > 0) and (w < len(B[l]) - 1):
                        if ((B[l][w][h] is True) and (B[l][w - 1][h] is False) and (B[l][w + 1][h] is False)):
                            struct.append(TEXTURE("grass3.png")(T([1, 2, 3])([x, y, z])(CUBOID([X[l], Y[w], Z[h]]))))
                        elif (B[l][w][h]):
                            struct.append(TEXTURE("wood2.png")(T([1, 2, 3])([x, y, z])(CUBOID([X[l], Y[w], Z[h]]))))
                    elif (B[l][w][h]):
                        struct.append(TEXTURE("wood2.png")(T([1, 2, 3])([x, y, z])(CUBOID([X[l], Y[w], Z[h]]))))

                    z += Z[h]
                y += Y[w]
            x += X[l]
        pol = STRUCT(struct)

        return pol
def window():

        wx = [0.04,0.14,0.04,0.14,0.04]
        wy = [0.04,0.02,0.04]
        wz = [0.04,0.6,0.04,0.18,0.04]
        wb = [[[True,True,True,True,True],[True,True,True,True,True],[True,True,True,True,True]],
              [[True,False,True,False,True],[True,True,True,False,True],[True,False,True,False,True]],
              [[True,True,True,False,True],[True,True,True,False,True],[True,True,True,False,True]],
              [[True, False, True, False, True], [True, True, False, True, True], [True, False, True, False, True]],
              [[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]]
             ]
        glass = TEXTURE("grass3.png")(OFFSET([0,0.024,0])(MKPOL([[[0.04,0.038,0.68],[0.04,0.038,0.86],[0.36,0.038,0.86],
                                                                  [0.36,0.038,0.68]],[[1,2,3,4]],[[1]]])))
        return STRUCT([movingStructureBuilder(wx, wy, wz, wb),glass])


#VIEW(groundFloor())
#VIEW(firstFloor())
#VIEW(villa())
#VIEW(secondFloor())
#VIEW(floor)
#VIEW(balcony())
#VIEW(lateralStructure())
#VIEW(externalStair())
#VIEW(fragDome([1.77,1.61,0.15, 2]))
#VIEW(roof())
#VIEW(detailWindowDoor("window"))
VIEW(window())
