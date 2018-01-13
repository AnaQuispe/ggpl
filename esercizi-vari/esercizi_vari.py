from larlib import *

# esercizio 1
#VIEW(CUBE(1))

# esercizio 2
#VIEW1 = VIEW(T([1, 2])([0.3, 0.3])(STRUCT([finalWallC, mediumTowers, bigTower])))


def larSimplexFacets(simplices):

    out = []
    d = len(simplices[0])
    for simplex in simplices:
        out += AA(sorted)([simplex[0:k] + simplex[k+1:d] for k in range(d)])
    out = set(AA(tuple)(out))
    return sorted(out)

simplices = [[1, 2, 4], [2, 4, 5], [2, 3, 5]]
larSimplexFacets(simplices)                     #OUT: [(1, 2), (1, 4), (2, 3), (2, 4), (2, 5), (3, 5), (4, 5)]

V = [[0, 0], [0, 1], [2, 0], [4, 0], [1.5, 3], [3.5, 2.5]]
FV = simplices
model = V, FV

#VIEW(STRUCT(MKPOLS(model)))
#VIEW(SKEL_1(STRUCT(MKPOLS(model))))

EV = larSimplexFacets(FV)
#VIEW(STRUCT(MKPOLS((V, EV))))



# esercizio 3

def larExtrude1(model, pattern):
    """ Simplicial model extrusion in accord with a 1D pattern """

    V, FV = model
    d, m = len(FV[0]), len(pattern)
    coords = list(cumsum([0] + (AA(ABS)(pattern))))
    offset, outcells, rangelimit = len(V), [], d*m
    for cell in FV:
        tube = [v + k*offset for k in range(m+1) for v in cell]
        cellTube = [tube[k:k+d+1] for k in range(rangelimit)]
        outcells += [reshape(cellTube, newshape=(m, d, d+1)).tolist()]
    outcells = AA(CAT)(TRANS(outcells))
    cellGroups = [group for k, group in enumerate(outcells) if pattern[k] > 0]
    outVertices = [v + [z] for z in coords for v in V]
    outModel = outVertices, CAT(cellGroups)
    return outModel

model = [[0, 0], [1, 0], [0, 1]], [[0, 1, 2]]
pattern = [1]

larExtrude1(model, pattern)

#VIEW(STRUCT(MKPOLS((larExtrude1(model, pattern)))))
#VIEW(EXPLODE(1.2, 1.2, 1.2)(MKPOLS((larExtrude1(model, pattern)))))

pattern = [1]*10
#VIEW(STRUCT(MKPOLS((larExtrude1(model, pattern)))))

# esercizio 4

V = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]]
FV = [[0, 1, 3], [1, 2, 4], [2, 4, 5], [3, 4, 6], [4, 6, 7], [5, 7, 8]]
model = larExtrude1((V, FV), 4*[1, 2, -3])
#VIEW(EXPLODE(1, 1, 1.2)(MKPOLS(model)))

# esercizio 5

model = larExtrude1(VOID, 10*[1])
#VIEW(EXPLODE(1.5, 1.5, 1.5)(MKPOLS(model)))
model = larExtrude1(model, 10*[1])
#VIEW(EXPLODE(1.5, 1.5, 1.5)(MKPOLS(model)))
model = larExtrude1(model, 10*[1])
#VIEW(EXPLODE(1.5, 1.5, 1.5)(MKPOLS(model)))

# esercizio 6

model = larExtrude1(VOID, 10*[1, -1])
#VIEW(EXPLODE(1.5, 1.5, 1.5)(MKPOLS(model)))
model = larExtrude1(model, 10*[1])
#VIEW(EXPLODE(1.5, 1.5, 1.5)(MKPOLS(model)))

# code for wotkshop_03

# cuppola structure A

pezzoCuppola = STRUCT(MKPOLS([[[0, 1.5, 0], [1, 1.5, 0], [1.24, 0.3, 0], [0.3, 0, 0], [1, 1.5, 2], [2, 1.5, 2],
                          [2.18, 0.6, 2], [1.24, 0.3, 2], [2, 1.5, 3.2], [3, 1.5, 3.2], [3.12, 0.9, 3.2], [2.18, 0.6, 3.2],
                          [3, 1.5, 4], [4, 1.5, 4], [4.06, 1.2, 4], [3.12, 0.9, 4], [4, 1.5, 4.6], [5, 1.5, 4.6],
                          [4.06, 1.2, 4.6], [5, 1.5, 5]],
                          [[0, 1, 2, 3], [7, 6, 5, 4], [0, 4, 5, 1], [1, 5, 6, 2],[6, 7, 3, 2], [3, 7, 4, 0],
                           [7, 11, 8, 4], [4, 8, 9, 5], [6, 5, 9, 10],[10, 11, 7, 6], [4, 5, 6, 7], [11, 10, 9, 8],
                           [11, 15, 12, 8], [12, 13, 9, 8], [13, 14, 10, 9],[14, 15, 11, 10], [8, 9, 10, 11],
                           [15, 14, 13, 12],[15, 18, 16, 12], [17, 13, 12, 16], [14, 17, 18, 15],[18, 17, 16],
                           [13, 17, 14], [12, 13, 14, 15],[16, 18, 19], [19, 17, 16], [19, 18, 17], [16, 17, 18]], [[1]]]))
a = T(2)(5)(pezzoCuppola)
b = T([1, 2])([0.745, -1.43])(R([1, 2])(PI/10.2)(pezzoCuppola))


