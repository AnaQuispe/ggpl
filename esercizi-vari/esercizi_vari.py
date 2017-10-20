from larlib import *

# primo esercizio

#VIEW(CUBE(1))

#secondo esercizio

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



# terzo esercizio

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

# quarto esercizio

V = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]]
FV = [[0, 1, 3], [1, 2, 4], [2, 4, 5], [3, 4, 6], [4, 6, 7], [5, 7, 8]]
model = larExtrude1((V, FV), 4*[1, 2, -3])
VIEW(EXPLODE(1, 1, 1.2)(MKPOLS(model)))

#quinto esercizio

model = larExtrude1(VOID, 10*[1])
VIEW(EXPLODE(1.5, 1.5, 1.5)(MKPOLS(model)))
model = larExtrude1(model, 10*[1])
VIEW(EXPLODE(1.5, 1.5, 1.5)(MKPOLS(model)))
model = larExtrude1(model, 10*[1])
VIEW(EXPLODE(1.5, 1.5, 1.5)(MKPOLS(model)))

# sesto esercizio

model = larExtrude1(VOID, 10*[1, -1])
VIEW(EXPLODE(1.5, 1.5, 1.5)(MKPOLS(model)))
model = larExtrude1(model, 10*[1])
VIEW(EXPLODE(1.5, 1.5, 1.5)(MKPOLS(model)))

