from pyplasm import *
from larlib import *

def simpleTower(re, ri, ht, nw):
    """ This function returns a simple tower
            :param re: external radius of the tower
            :param ri: internal radius of the tower
            :param ht: high of the tower
            :param nw: numer of wall of th tower
            :return: an object HPC  """

    def towerDetail(hd1, hd2, dd1, dd2):
        """ This function returns  details of a simple tower
                :param hd1: height of the first detail
                :param hd2: height of the second detail
                :param dd1: distance from the tower of the first detail
                :param dd2: distance from the tower of the second detail
                """
        tower = TEXTURE("marmo.png")(DIFFERENCE([MY_CYLINDER([re, ht])(nw), MY_CYLINDER([ri, ht])(16)]))
        detail1 = TEXTURE("marmo.png")(STRUCT([T(3)(hd1)(DIFFERENCE([MY_CYLINDER([re + dd2, hd2])(16), MY_CYLINDER([ri, hd2])(16)])),
                          DIFFERENCE([MY_CYLINDER([re + dd1, hd1])(16), MY_CYLINDER([ri, hd1])(16)])]))

        detail2 = TEXTURE("marmo.png")(DIFFERENCE([MY_CYLINDER([re + dd1, hd1])(16), MY_CYLINDER([re, hd1])(16)]))
        column = T([1, 2])([double((-re * 3) / 2), -0.15])(CUBOID([re * 3, 0.3, ht - dd1]))
        columns = STRUCT([column, R([1, 2])(PI / 6)(column), R([1, 2])(PI / 3)(column), R([1, 2])(-PI / 6)(column),
                          R([1, 2])(-PI / 3)(column)])
        detail3 = TEXTURE("marmo.png")(T(3)(hd1)(INTERSECTION(
            [DIFFERENCE([MY_CYLINDER([re + dd1, ht - hd1])(16), MY_CYLINDER([re, ht - hd1])(16)]), columns])))

        return STRUCT([tower, T(3)(ht)(detail1), detail2, detail3])
    return towerDetail

def mediumTowerA(re, ri, ht):
    """ This function returns a medium tower with six walls and windows
                :param re: external radius of the tower
                :param ri: internal radius of the tower
                :param ht: high of the tower
                :return: an object HPC  """
    def towerDetail(hd1, hd2, dd1, dd2):
        """ This function returns  details of a simple tower
                        :param hd1: height of the first detail
                        :param hd2: height of the second detail
                        :param dd1: distance from the tower of the first detail
                        :param dd2: distance from the tower of the second detail
                        """
        tower = DIFFERENCE([MY_CYLINDER([re, ht])(16), MY_CYLINDER([ri, ht])(16)])
        detail1 = STRUCT([T(3)(hd1)(DIFFERENCE([MY_CYLINDER([re + dd2, hd2])(16), MY_CYLINDER([ri, hd2])(16)])),
                          DIFFERENCE([MY_CYLINDER([re + dd1, hd1])(16), MY_CYLINDER([ri, hd1])(16)])])

        detail2 = DIFFERENCE([MY_CYLINDER([re + dd1, hd1])(16), MY_CYLINDER([re, hd1])(16)])
        column = T([1, 2])([double((-re * 3) / 2), -0.15])(CUBOID([re * 3, 0.3, ht - dd1]))
        columns = STRUCT([column, R([1, 2])(PI / 3)(column), R([1, 2])(PI / 3)(column), R([1, 2])(-PI / 3)(column),
                          R([1, 2])(2*PI/3)(column), R([1, 2])(-2*PI/3)(column), R([1, 2])(PI)(column)])
        detail3 = T(3)(hd1)(INTERSECTION([DIFFERENCE([MY_CYLINDER([re + double(dd1/2), ht - hd1])(16),
                                                      MY_CYLINDER([re, ht - hd1])(16)]), columns]))
        detail4 = STRUCT([T(3)(0.08)(CONE([0.25, 0.35])(4)), MY_CYLINDER([0.28, 0.08])(16)])
        window = MY_CYLINDER([0.225, 4])(16)
        windows = STRUCT([R([1, 2])(PI/6)(T([1, 3])([2, 0.65])(R([1, 3])(PI/2)(window))),
                          R([1, 2])(-PI / 6)(T([1, 3])([2, 0.65])(R([1, 3])(PI / 2)(window))),
                          R([1, 2])(PI / 2)(T([1, 3])([2, 0.65])(R([1, 3])(PI / 2)(window)))])
        finalTower = STRUCT([tower, T(3)(ht)(detail1), detail2, detail3, T(3)(2.999)(detail4)])
        return TEXTURE("marmo.png")(DIFFERENCE([finalTower, windows]))
    return towerDetail

def mediumTowerB(re, ri, ht):
    """ This function returns a medium tower with eigth walls and windows
                    :param re: external radius of the tower
                    :param ri: internal radius of the tower
                    :param ht: high of the tower
                    :return: an object HPC  """
    def towerDetail(hd1, hd2, dd1, dd2):
        """ This function returns  details of a simple tower
                                :param hd1: height of the first detail
                                :param hd2: height of the second detail
                                :param dd1: distance from the tower of the first detail
                                :param dd2: distance from the tower of the second detail
                                """
        tower = DIFFERENCE([MY_CYLINDER([re, ht])(8), MY_CYLINDER([ri, ht])(16)])
        detail1 = STRUCT([T(3)(hd1)(DIFFERENCE([MY_CYLINDER([re + dd2, hd2])(16), MY_CYLINDER([ri, hd2])(16)])),
                          DIFFERENCE([MY_CYLINDER([re + dd1, hd1])(16), MY_CYLINDER([ri, hd1])(16)])])

        detail2 = DIFFERENCE([MY_CYLINDER([re + dd1, hd1])(16), MY_CYLINDER([re, hd1])(8)])
        column = T([1, 2])([double((-re * 3) / 2), -0.15])(CUBOID([re * 3, 0.3, ht - dd1]))
        columns = STRUCT([column, R([1, 2])(PI/4)(column), R([1, 2])(-PI/4)(column), R([1, 2])(PI/2)(column)])
        detail3 = T(3)(hd1)(INTERSECTION([DIFFERENCE([MY_CYLINDER([re + double(dd1/2), ht - hd1])(16),
                                                      MY_CYLINDER([re, ht - hd1])(16)]), columns]))
        detail4 = STRUCT([T(3)(0.1)(CONE([0.35, 0.5])(4)), MY_CYLINDER([0.38, 0.1])(16)])
        window = MY_CYLINDER([0.225, 4])(16)
        windows = T(3)(double(ht/2))(STRUCT([R([1, 2])(PI/8)(T(1)(2)(R([1, 3])(PI/2)(window))),
                          R([1, 2])(-PI/8)(T(1)(2)(R([1, 3])(PI/2)(window))),
                          R([1, 2])(3*PI/8)(T(1)(2)(R([1, 3])(PI / 2)(window))),
                          R([1, 2])(-3*PI/8)(T(1)(2)(R([1, 3])(PI / 2)(window)))]))

        finalTower = STRUCT([tower, T(3)(ht)(detail1), detail2, detail3, T(3)(3.599)(detail4)])
        return TEXTURE("marmo.png")(DIFFERENCE([finalTower, windows]))
    return towerDetail

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
# This function returns a quarter of sphere
def QUARTERSPHERE (radius):

	def QUARTERSPHERE0 (subds):
		N , M = subds
		domain = Hpc(Grid([N*[PI/(2*N)],M*[PI/M]]))
		domain = MAT([[1,0,0,0],[-PI/2,1,0,0],[-PI,0,1,0],[0,0,0,1]])(domain)
		fx  = lambda p: radius * math.cos(p[0]) * math.sin  (p[1])
		fy  = lambda p: radius * math.cos(p[0]) * math.cos (p[1])
		fz  = lambda p: radius * ABS(sin(p[0]))
		ret=  GMAP([fx, fy, fz])(domain)
		return ret
	return QUARTERSPHERE0


def bigTower(re, ri, ht):
    """ This function returns the big tower of the final structure
                            :param re: external radius of the tower
                            :param ri: internal radius of the tower
                            :param ht: high of the tower
                            :return: an object HPC  """
    def bigT(hd1, hd2, dd1, dd2):
        """ This function returns  details of a simple tower
                                        :param hd1: height of the first detail
                                        :param hd2: height of the second detail
                                        :param dd1: distance from the tower of the first detail
                                        :param dd2: distance from the tower of the second detail
                                        """
        tower = DIFFERENCE([MY_CYLINDER([re, ht])(16), MY_CYLINDER([ri, ht])(16)])
        detail1 = STRUCT([T(3)(hd1)(DIFFERENCE([MY_CYLINDER([re + dd2, hd2])(16), MY_CYLINDER([ri, hd2])(16)])),
                          DIFFERENCE([MY_CYLINDER([re + dd1, hd1])(16), MY_CYLINDER([ri, hd1])(16)])])

        detail2 = STRUCT([T(3)(hd2)(DIFFERENCE([MY_CYLINDER([re + dd1, hd1])(16), MY_CYLINDER([re, hd1])(16)])),
                          DIFFERENCE([MY_CYLINDER([re + dd2, hd2])(16), MY_CYLINDER([ri, hd2])(16)])])
        column = T([1, 2])([double((-re * 3) / 2), -0.2])(CUBOID([re * 3, 0.4, ht - dd1]))
        columns = STRUCT([R([1, 2])(PI/6)(column), R([1, 2])(-PI/6)(column), R([1, 2])(PI/3)(column), R([1, 2])(-PI/3)(column)])
        detail3 = T(3)(hd1)(INTERSECTION([DIFFERENCE([MY_CYLINDER([re + double(dd1/2)+0.05, ht - hd1])(16),
                                                      MY_CYLINDER([re, ht - hd1])(16)]), columns]))
        holeDet = STRUCT([T([1, 3])([0.15, 0.1])(CUBOID([0.1, 0.6, 0.4])), T([1, 3])([0.35, 0.1])(CUBOID([0.1, 0.6, 0.4])),
                          T([2, 3])([0.15, 0.1])(CUBOID([0.6, 0.1, 0.4])), T([2, 3])([0.35, 0.1])(CUBOID([0.6, 0.1, 0.4]))])
        det = DIFFERENCE([CUBOID([0.6, 0.6, 0.6]), holeDet])
        detail4 = STRUCT([MY_CYLINDER([0.65, 0.15])(16), T([1, 2, 3])([-0.4, -0.4, 0.15])(CUBOID([0.8, 0.8, 0.2])),
                          T([1, 2, 3])([-0.3, -0.3, 0.35])(det), T([1, 2, 3])([-0.4, -0.4, 0.95])
                          (CUBOID([0.8, 0.8, 0.1])), T(3)(1.05)(CONE([0.27, 0.8])(16))])
        window1 = MY_CYLINDER([0.56, 8])(16)
        window2 = MY_CYLINDER([0.3, 8])(16)
        windows = T(3)(double(ht/2) + hd1+hd2)(STRUCT([T(1)(4)(R([1, 3])(PI/2)(window1)),
                          R([1, 2])(PI/4)(T(1)(4)(R([1, 3])(PI/2)(window2))),
                          R([1, 2])(-PI/4)(T(1)(4)(R([1, 3])(PI/2)(window2))),
                          R([1, 2])(PI/2)(T(1)(4)(R([1, 3])(PI/2)(window1)))]))

        finalTower = STRUCT([tower, T(3)(ht)(detail1), detail2, detail3, T(3)(6.799)(detail4)])
        return TEXTURE("marmo.png")(DIFFERENCE([finalTower, windows]))
    return bigT


def bigWall():
    """This function returns an object HPC. The big wall of the final structure"""
    wall = TEXTURE("marmo.png")(CUBOID([12.4, 0.2, 6.8]))
    det1 = TEXTURE("marmo.png")(STRUCT([T([1, 2, 3])([-0.25, -0.25, 4.45])(CUBOID([12.9, 0.25, 0.3])), T([1, 2])([-0.15, -0.15])
                    (CUBOID([12.7, 0.15, 0.5]))]))
    col = TEXTURE("marmo.png")(STRUCT([T([1, 2])([-0.2, -0.2])(CUBOID([0.5, 0.2, 6.3])), T([1, 2])([1.9, -0.2])(CUBOID([0.5, 0.2, 6.3])),
                  T([1, 2])([4, -0.2])(CUBOID([0.5, 0.2, 6.3])), T([1, 2])([7.9, -0.2])(CUBOID([0.5, 0.2, 6.3])),
                  T([1, 2])([10, -0.2])(CUBOID([0.5, 0.2, 6.3])), T([1, 2])([12.1, -0.2])(CUBOID([0.5, 0.2, 6.3]))]))

    intWall = TEXTURE("marmo.png")(OFFSET([0.05, 0.05, 0.05])(STRUCT(MKPOLS([[[3.3, 2.9, 0], [3.7, 3.3, 0], [4, 3, 0], [5.85, 3, 0], [5.85, 2.4, 0], [6.5, 2.4, 0],
                [6.5, 3, 0], [8.5, 3, 0],[8.65, 3.2, 0], [9.008, 2.85, 0], [3.3, 2.9, 6.5], [3.7, 3.3, 6.5], [4, 3, 6.5], [5.85, 3, 2],
                [5.85, 2.4, 2], [6.5, 2.4, 2], [6.5, 3, 2], [8.5, 3, 6.5], [8.65, 3.2, 6.5], [9.008, 2.85, 6.5], [5.85, 3, 6.5],
                 [6.5, 3, 6.5]], [[0, 10, 11, 1], [1, 11, 12, 2], [2, 12, 20, 3], [3, 13, 14, 4], [5, 15, 16, 6],
                [6, 21, 17, 7], [7, 17, 18, 8], [8, 18, 19, 9], [13, 20, 21, 16], [14, 15, 16, 13]], [[1]]]))))
    holeDoor = STRUCT([R([1, 2])(PI / 4)(T([1, 2])([2, -0.25])(CUBOID([13, 0.5, 6.5]))), T(2)(12.3)(R([1, 2])(-PI / 4)
                            (T([1, 2])([2, -0.25])(CUBOID([13, 0.5,6.5]))))])
    mediumTower = TEXTURE("marmo.png")(DIFFERENCE([MY_CYLINDER([1.8, 6.8])(16), MY_CYLINDER([1.6, 6.8])(16)]))

    mediumTowers = DIFFERENCE([STRUCT([T([1, 2])([2, 2])(mediumTower), T([1, 2])([2, 10.4])(mediumTower), T([1, 2])([10.4, 2])
                    (mediumTower), T([1, 2])([10.4, 10.4])(mediumTower)]), holeDoor])

    intWalls = STRUCT([intWall, T(1)(12.35)(R([1, 2])(PI/2)(intWall)), T([1, 2])([12.4, 12.35])(R([1, 2])(PI)(intWall)),
                       T([1, 2])([0.03,12.4])(R([1, 2])(-PI/2)(intWall))])

    det2 = STRUCT([T([1, 2, 3])([0.425, -0.1, 0.5])(MY_CYLINDER([0.225, 2.875])(16)), T([1, 2, 3])([1.175, -0.1, 0.5])
                    (MY_CYLINDER([0.225, 2.875])(16))])

    det3 = STRUCT([DIFFERENCE([T([1, 2, 3])([0.425, 0.1, 2.875])(R([2, 3])(PI / 2)(MY_CYLINDER([0.225, 0.1])(16))),
           CUBOID([1.6, 0.1, 2.875])]), DIFFERENCE([T([1, 2, 3])([0.8, 0.05, 3.1])(R([2, 3])(PI / 2)(MY_CYLINDER([0.6, 0.1])(16))),
           T(2)(-0.05)(CUBOID([1.6, 0.1, 3.1]))]), DIFFERENCE([T([1, 2, 3])([1.175, 0.1, 2.875])(R([2, 3])(PI / 2)
           (MY_CYLINDER([0.225, 0.1])(16))), CUBOID([1.6, 0.1, 2.875])])])

    finalDet2 = STRUCT([T(1)(0.3)(det2), T(1)(2.4)(det2), T(1)(8.4)(det2), T(1)(10.5)(det2)])
    finalDet3 = T([2, 3])([-0.1, 0.5])(STRUCT([DIFFERENCE([CUBOID([1.6, 0.1, 3.95]), det3]), T([1, 3])([0.3, 4.5])
                                                (CUBOID([1, 0.1, 1]))]))
    detailsWall = TEXTURE("marmo.png")(STRUCT([T(1)(0.3)(finalDet3), T(1)(2.4)(finalDet3), T(1)(8.4)(finalDet3), T(1)(10.5)(finalDet3)]))
    window = MY_CYLINDER([0.225, 13])(16)
    windows = T([2, 3])([12.8, 5.5])(R([2, 3])(PI / 2)(STRUCT([T(1)(1.1)(window), T(1)(3.2)(window), T(1)(9.2)(window),
                                                               T(1)(11.3)(window)])))

    holeWall = STRUCT([T([1, 2])([3.9, -2.3])(CUBOID([4.6, 4.6, 4.74])), T([1, 2, 3])([4.8, -1.4, 4.74])
                            (CUBOID([2.8, 2.8, 0.35])), T([1, 2, 3])([6.2, -0.7, 5.09])(MY_CYLINDER([1.23, 3])(16))])

    lateral = INTERSECTION([wall, holeWall])
    lateralHoleWall = STRUCT([lateral, T(2)(-0.2)(lateral), T(2)(-0.4)(lateral)])

    finalWall = TEXTURE("marmo.png")(DIFFERENCE([STRUCT([wall, det1, col, detailsWall]), STRUCT([finalDet2, windows, lateralHoleWall])]))
    bigWall = STRUCT(
        [finalWall, T(1)(12.4)(R([1, 2])(PI / 2)(finalWall)), T([1, 2])([12.4, 12.4])(R([1, 2])(PI)(finalWall)),
         T(2)(12.4)(R([1, 2])(3 * PI / 2)(finalWall)), intWalls, mediumTowers])

    return bigWall

def structure_5towers():
    """This function returns an structure with five domes"""
    holeDome = STRUCT([T([1, 2, 3])([4.6, 2.3, 3])(R([1, 3])(PI / 2)(MY_CYLINDER([0.9, 5])(16))),
                       T([1, 2, 3])([2.3, 4.6, 3])(R([2, 3])(PI / 2)(MY_CYLINDER([0.9, 5])(16)))])

    holeTowers = STRUCT([T(1)(1.2)(CUBOID([2.2, 0.2, 3])), T([1, 2])([1.2, 4.4])(CUBOID([2.2, 0.2, 3])),
                         T(2)(1.2)(CUBOID([0.2, 2.2, 3])), T([1, 2])([4.4, 1.2])(CUBOID([0.2, 2.2, 3]))])
    holeWall = STRUCT([holeDome, holeTowers])
    wall = TEXTURE("marmo.png")(DIFFERENCE([CUBOID([4.6, 0.2, 4.3]), holeWall]))
    walls = STRUCT([wall, T(1)(0.2)(R([1, 2])(PI / 2)(wall)), T(2)(4.4)(wall), T(1)(4.6)(R([1, 2])(PI / 2)(wall))])
    finalWall = STRUCT([T([1, 2])([1.3, 1.3])(walls)])

    doors = T(1)(3.3)(CUBOID([0.6, 7.2, 2]))
    stower1 = TEXTURE("marmo.png")(DIFFERENCE([DIFFERENCE([T([1, 2])([3.6, 1.3])(simpleTower(1.1, 0.9, 2.5, 200)(0.3, 0.2, 0.07, 0.2)),
                                T([1, 2])([1.5, 1.5])(CUBOID([4.2, 4.2, 3]))]), doors]))
    stower2 = TEXTURE("marmo.png")(DIFFERENCE([T([1, 2])([1.3, 3.6])(simpleTower(1.1, 0.9, 2.5, 200)(0.3, 0.2, 0.07, 0.2)),
                    T([1, 2])([1.5, 1.5])(CUBOID([4.2, 4.2, 3]))]))
    finalTowers = STRUCT([stower1, stower2, T([1, 2])([7.2, 7.2])(R([1, 2])(PI)(stower1)),
                        T([1, 2])([7.2, 7.2])(R([1, 2])(-PI)(stower2))])

    roof = T([1, 2, 3])([1.05, 1.05, 4.3])(STRUCT([T(3)(0.15)(DIFFERENCE([CUBOID([5.1, 5.1, 0.3]), T([1, 2])([1.15, 1.15])
            (CUBOID([2.8, 2.8, 0.3]))])), T([1, 2])([0.15, 0.15])(DIFFERENCE([CUBOID([4.8, 4.8, 0.15]), T([1, 2])
            ([0.4, 0.4])(CUBOID([4, 4, 0.15]))])), T([1, 2, 3])([1.05, 1.05, 0.45])(DIFFERENCE([CUBOID([3, 3, 0.35]),
            T([1, 2])([0.1, 0.1])(CUBOID([2.8, 2.8, 0.25]))]))]))

    finalRoof = TEXTURE("marmo.png")(DIFFERENCE([roof, T([1, 2, 3])([3.6, 3.6, 4.75])(R([1, 2])(PI / 2)(MY_CYLINDER([1.15, 2.05])(16)))]))
    mediumTower = T([1, 2, 3])([3.6, 3.6, 5.1])(mediumTowerA(1.3, 1.1, 1.2)(0.2, 0.3, 0.15, 0.3))
    floorTower = MY_CYLINDER([1.3, 0.4])(16)
    floorA = TEXTURE("marmo.png")(T([1, 2])([1.2, 1.2])(STRUCT([T(1)(2.4)(floorTower), T(2)(2.4)(floorTower), T([1,2])([2.4, 4.8])(floorTower),
                     T([1,2])([4.8,2.4])(floorTower), CUBOID([4.8, 4.8, 0.4])])))
    dome = QUARTERSPHERE(1.1)([32, 32])
    domes = STRUCT([T([1, 2, 3])([3.6, 1.3, 3])(R([1, 2])(PI/2)(dome)), T([1, 2, 3])([1.3, 3.6, 3])(dome),
                    T([1, 2, 3])([3.6, 5.9, 3])(R([1, 2])(-PI/2)(dome)), T([1, 2,3])([5.9, 3.6, 3])(R([1, 2])(PI)(dome)),
                    T([1, 2, 3])([3.6, 3.6, 6.8])(HALFSPHERE(1.3)([32, 32]))])

    structure = STRUCT([T(3)(0.4)(STRUCT([finalTowers, finalWall, finalRoof, mediumTower])), floorA])
    return STRUCT([structure, TEXTURE("tegole2.png")(T(3)(0.4)(domes))])

def ggpl_leonardoChurch(dx, dy, dz):
    """ This function returns  details of a simple tower
                    :param dx: distance along the x axis
                    :param dy: distance along the y axis
                    :param dz: distance along the z axis
                    :return: an object HPC"""
    wall = bigWall()
    roof = TEXTURE("marmo.png")(T([1, 2, 3])([-0.3, -0.3, 6.3])(STRUCT([T(3)(0.2)(CUBOID([13, 13, 0.3])),
                                                   T([1, 2])([0.15, 0.15])(DIFFERENCE([CUBOID([12.7, 12.7, 0.2]),
                                                                                       T([1, 2])([0.15, 0.15])(CUBOID(
                                                                                           [12.4, 12.4, 0.2]))]))])))

    holeRoof = STRUCT([T([1, 2, 3])([2, 2, 6.5])(MY_CYLINDER([1.4, 0.4])(16)), T([1, 2, 3])([2, 10.4, 6.5])
                        (MY_CYLINDER([1.4, 0.4])(16)), T([1, 2, 3])([10.4, 2, 6.5])(MY_CYLINDER([1.4, 0.4])(16)),
                        T([1, 2, 3])([10.4, 10.4, 6.5])(MY_CYLINDER([1.4, 0.4])(16)), T([1, 2, 3])([6.2, 6.2, 6.5])
                       (MY_CYLINDER([3, 0.4])(16))])

    holeWall = STRUCT([T([1, 2])([3.9, -2.3])(CUBOID([4.6, 4.6, 4.74])), T([1, 2, 3])([4.8, -1.4, 4.74])
                        (CUBOID([2.8, 2.8, 0.35])), T([1, 2, 3])([6.2, -0.7, 5.09])(MY_CYLINDER([1.23, 3])(16))])

    lateral = INTERSECTION([wall, holeWall])
    lateralHoleWall = STRUCT([lateral, T(2)(-0.2)(lateral), T(2)(-0.4)(lateral)])

    finalLateralHole = STRUCT([lateralHoleWall, T(1)(-0.2)(R([1, 2])(PI / 2)(lateralHoleWall)),
                               T(2)(12.6)(lateralHoleWall), T(1)(12.4)(R([1, 2])(PI / 2)(lateralHoleWall))])
    finalRoof = TEXTURE("marmo.png")(DIFFERENCE([roof, STRUCT([holeRoof, finalLateralHole])]))

    mediumTower = STRUCT([T(3)(6.8)(mediumTowerB(1.6, 1.4, 1.5)(0.25, 0.25, 0.1, 0.25)), TEXTURE("tegole2.png")
                            (T(3)(8.8)(HALFSPHERE(1.6)([16, 16])))])

    mediumTowers = STRUCT([T([1, 2])([2, 2])(mediumTower), T([1, 2])([2, 10.4])(mediumTower), T([1, 2])([10.4, 2])
                            (mediumTower), T([1, 2])([10.4, 10.4])(mediumTower)])

    bigTw = STRUCT([T([1, 2, 3])([6.2, 6.2, 6.8])(bigTower(3, 2.8, 3)(0.5, 0.5, 0.2, 0.35)), T([1,2, 3])
                        ([6.2, 6.2, 10.8])(TEXTURE("tegole2.png")(HALFSPHERE(2.8)([16, 16])))])
    structure_5tower = structure_5towers()
    lateralStructures  = STRUCT([T([1, 2])([2.6, -4.5])(structure_5tower), T([1, 2])([2.7, 2.6])(R([1, 2])(PI/2)(structure_5tower)),
                                 T([1, 2])([16.9, 2.6])(R([1, 2])(PI/2)(structure_5tower)), T([1, 2])([2.6, 9.7])(structure_5tower)])

    floor = TEXTURE("marmo.png")(T([1, 2])([-0.25, -0.25])(CUBOID([12.9, 12.9, 0.4])))
    base = TEXTURE("marmo.png")(STRUCT([T([1,2])([-3.2, -3.2])(CUBOID([18.8, 18.8, 0.5])), T([1,2])([1.6, -5.5])(CUBOID([9.8, 23.4, 0.5])),
                   T([1,2])([-5.5, 1.6])(CUBOID([23.4, 9.8, 0.5]))]))
    finalStructure = STRUCT([wall, mediumTowers, bigTw, finalRoof])
    church = T([1, 2])([5.5, 5.5])(STRUCT([T(3)(0.9)(finalStructure), T(3)(0.5)(floor), base, T(3)(0.5)(lateralStructures)]))
    return S([1, 2, 3])([double(dx/23.4), double(dy/23.4), double(dz/16.35)])(church)


VIEW(STRUCT([simpleTower(1.1, 0.9, 2.5, 200)(0.3, 0.2, 0.07, 0.2), TEXTURE("tegole2.png")(T(3)(3)(HALFSPHERE(1.1)([16, 16])))]))
VIEW(STRUCT([mediumTowerA(1.3, 1.1, 1.2)(0.2, 0.3, 0.15, 0.3), TEXTURE("tegole2.png")(T(3)(1.7)(HALFSPHERE(1.3)([16, 16])))]))
VIEW(STRUCT([mediumTowerB(1.6, 1.4, 1.5)(0.25, 0.25, 0.1, 0.25), TEXTURE("tegole2.png")(T(3)(2)(HALFSPHERE(1.6)([16, 16])))]))
VIEW(STRUCT([bigTower(3, 2.8, 3)(0.5, 0.5, 0.2, 0.35), TEXTURE("tegole2.png")(T(3)(4)(HALFSPHERE(2.8)([16, 16])))]))
VIEW(structure_5towers())
dx, dy, dz = 23.4, 23.4, 16.35

VIEW(ggpl_leonardoChurch(dx, dy, dz))

dx, dy, dz = 11.7, 11.7, 8.175
VIEW(ggpl_leonardoChurch(dx, dy, dz))

