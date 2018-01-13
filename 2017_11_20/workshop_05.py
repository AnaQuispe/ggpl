from pyplasm import *
from larlib import *
from numpy import *
import csv

def first_floor(filename):

    with open(filename, "rb") as file:
        reader = csv.reader(file, delimiter=",")
        externalWalls = []

        for row in reader:
            x1 = float(row[0])
            x2 = float(row[1])
            y1 = float(row[2])
            y2 = float(row[3])
            externalWalls.append(OFFSET([0.15, 0.15])(POLYLINE([[x1, y1], [x2, y2]])))
        walls = PROD([STRUCT(externalWalls), Q(1.1)])
        det = STRUCT([T([1, 2])([-0.06, -0.06])(CUBOID([7.47, 7.47, 0.3])),
                      T([1, 2])([-0.03, -0.03])(CUBOID([7.41, 7.41, 0.5]))])
        final_wall = STRUCT([DIFFERENCE([det, CUBOID([7.35, 7.35, 0.5])]), walls])

        door = STRUCT([CUBOID([0.6, 0.21, 0.7]), T([1, 3])([0.3,0.7])(R([2, 3])(-PI / 2)(MY_CYLINDER([0.3, 0.21])(16)))])
        doors_hole = STRUCT([T([1, 2])([3.4, -0.06])(door), T([1, 2])([3.4, 7.2])(door),
                        T([1, 2])([0.15, 3.4])(R([1, 2])(PI / 2)(door)),
                        T([1, 2])([7.41, 3.4])(R([1, 2])(PI / 2)(door))])

        w_lat = STRUCT([T([1, 3])([0.6, 0.6])(CUBOID([0.4, 0.15, 0.3])), T([1, 3])([6.4, 0.6])(CUBOID([0.4, 0.15, 0.3]))])
        windows_hole= STRUCT([w_lat,T(2)(7.2)(w_lat),T(1)(0.15)(R([1,2])(PI/2)(w_lat)),T(1)(7.35)(R([1, 2])(PI / 2)(w_lat))])

        inDoor = STRUCT([R([1, 2])(PI / 4)(T([1, 2])([3.1, -0.175])(CUBOID([4.2, 0.35, 0.75]))),T(1)(7.3)(R([1, 2])
                (3 * PI / 4)(T([1, 2])([3.1, -0.175])(CUBOID([4.2, 0.35, 0.75])))),T([1, 2])([3.4, 1.85])(OFFSET([0.0,4.0])
                    (door)), T([1, 2])([1.7, 4.05])(R([1,2])(-PI/2)(OFFSET([0.0,4.0])(S(1)([0.75/0.6])(door))))])
        centerHoles = COLOR([1,0.92,0.84])(DIFFERENCE([T([1, 2])([3.7, 3.675])(DIFFERENCE([MY_CYLINDER([1.71, 1.1])(32),
                                                                      MY_CYLINDER([1.61, 1.1])(32)])), inDoor]))
        floor = TEXTURE("marmo_rosso2.png")(T(3)(-0.01)(CUBOID([7.35,7.35,0.01])))
        final = COLOR([1,0.92,0.84])(DIFFERENCE([final_wall, STRUCT([doors_hole, windows_hole])]))
        return STRUCT([final, centerHoles,floor])

VIEW(first_floor("piano_terra.lines"))