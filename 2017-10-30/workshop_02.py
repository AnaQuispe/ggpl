from pyplasm import *

def ggpl_stairBookcase( dx, dy, dz):

    """ This function returns a wooden stair bookcase with measures taken from the dx, dy and dz parameters.
            :param dx: distance along the x axis.
            :param dy: distance along the y axis.
            :param dz: distance along the z axis.
            :return: an object HPC
            """

    externalStructure = STRUCT([T([1, 2, 3])([0, 0.7, 0.02])(CUBOID([0.02, 0.33, 2.66])),
                                                 T([2, 3])([1.03, 0.02])(CUBOID([3.10, 0.02, 2.68])),
                                                 T(1)(3.08)(CUBOID([0.02, 1.03, 2.7])),
                                                 T([2, 3])([0.7, 2.68])(CUBOID([3.08, 0.35, 0.02])),
                                                 T(2)(0.7)(CUBOID([3.08, 0.35, 0.02]))])

    verticalTable = CUBOID([0.02, 0.33, 2.66])
    verticalBlocks = []
    for i in range(1, 14): verticalBlocks.append(T([1, 2, 3])([0.2 * i + 0.02 * i, 0.7, 0.02])(verticalTable))

    horizontalTable = CUBOID([0.2, 0.33, 0.02])
    horizontalBlocks = []
    books = []
    for i in range(1, 15):
        if i % 2 == 1:
            for k in range(1, 6):
                horizontalBlocks.append(T([1, 2, 3])([0.2*(i-1) + 0.02*i, 0.7, 0.47*k + 0.02*k])(horizontalTable))
                books.append(T([1, 2, 3])([0.2 * (i - 1) + 0.02 * i, 0.75, 0.47 * k + 0.02 * (k + 1)])(
                    TEXTURE("books2.png")(CUBOID([0.2, 0.10, 0.2]))))
        else:
            horizontalBlocks.append(T([1, 2, 3])([0.2*(i-1) + 0.02*i, 0.7, 0.23])(horizontalTable))
            for k in range(1, 5):
                horizontalBlocks.append(T([1, 2, 3])([0.2*(i-1) + 0.02*i, 0.7, 0.47*k + 0.23 + 0.02*k])(horizontalTable))
                books.append(T([1, 2, 3])([0.2 * (i - 1) + 0.02 * i, 0.75, 0.47*k + 0.02*(k+1) + 0.23])(
                                TEXTURE("books3.png")(CUBOID([0.2, 0.10, 0.2]))))
    # scale bookcase
    baseStair = T(1)(0.66)(CUBOID([2.42, 0.7, 0.02]))
    stairBlock = CUBOID([0.22, 0.7, 0.02])
    stair = []
    underStairBlocks = []

    for i in range(4, 15):
        if i % 2 == 0:
            underStairBlocks.append(T([1, 3])([0.2*(i-1) + 0.02*(i-1), 0.02])(CUBOID([0.02, 0.7, 0.21 + 0.235*(i-4) + 0.02*((i/2)-2)])))
            stair.append(T([1, 3])([0.2 * (i - 1) + 0.02 * (i-1),  0.21 + 0.235*(i-4) + 0.02*((i/2)-1)])(stairBlock))
            horizontalBlocks.append(T([1, 3])([0.2 * (i - 1) + 0.02 * i, 0.23])(CUBOID([0.2, 0.7, 0.02])))
            for k in range(2, (i/2)-1):
                horizontalBlocks.append(T([1, 3])([0.2 * (i - 1) + 0.02 * i, 0.47 * (k -1)+ 0.02 *(k-1)+ 0.23])(CUBOID([0.2, 0.7, 0.02])))
                books.append(T([1, 2, 3])([0.2 * (i - 1) + 0.02 * i, 0.05, 0.47 * (k -1)+ 0.02 *(k)+ 0.23])(TEXTURE("books3.png")(CUBOID([0.2, 0.10, 0.2]))))
        else:
            underStairBlocks.append(T([1, 3])([0.2 * (i - 1) + 0.02 * (i - 1), 0.02])
                                    (CUBOID([0.02, 0.7, 0.47*((i/2)-1) + 0.02*((i/2)-2)])))
            stair.append(T([1, 3])([0.2 * (i - 1) + 0.02 * (i - 1), 0.47*((i/2)-1) + 0.02*((i/2)-1)])(stairBlock))
            for k in range(2, (i/2)):
                horizontalBlocks.append(T([1, 3])([0.2 * (i - 1) + 0.02 * i, 0.47 * (k -1) + 0.02 * (k-1)])(CUBOID([0.2, 0.7, 0.02])))
                books.append(T([1, 2, 3])([0.2 * (i - 1) + 0.02 * i, 0.05, 0.47 * (k - 1) + 0.02 * (k)])(
                    TEXTURE("books4.png")(CUBOID([0.2, 0.10, 0.2]))))
    firstBlockStructure = STRUCT([externalStructure, STRUCT(verticalBlocks), STRUCT(horizontalBlocks)])
    StairStructure = STRUCT([baseStair, STRUCT(underStairBlocks), STRUCT(stair)])
    bookcase = TEXTURE("wood2.png")(STRUCT([firstBlockStructure, StairStructure]))
    #bookcaseWithBooks = STRUCT([bookcase, STRUCT(books)])

    return S([1, 2, 3])([dx, dy, dz])(bookcase)

# execution with the real measures (in meters) of the bookcase model
dx, dy, dz = 3.10, 1.05, 2.7
#VIEW(ggpl_stairBookcase(dx, dy, dz))

# execution with different parameters
dx, dy, dz = 6, 3, 4
#VIEW(ggpl_stairBookcase(dx, dy, dz))


