from pyplasm import *
from larlib import *

# script 2.2.1

def segment(): return CUBOID([1]);
def square(): return CUBOID([1, 1]);
def cube(): return CUBOID([1, 1, 1]);

VIEW(segment())
VIEW(square())
VIEW(cube())

# script 2.2.3

def verts(): return ([[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0], [0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]]);

def pol_1D():

    cells = [[1, 4], [2, 4], [4, 8]]
    pols = [[1, 2, 3]]
    mkframe = MKPOL([verts(), cells, pols])
    return mkframe;

def pol_2D():

    mkframe = MKPOL([verts(), [[1, 2, 3, 4], [2, 4, 8]], [[1], [2]]])
    return mkframe;

def pol_3D():

    mkframe = MKPOL([verts(), [[1, 2, 3, 5], [2, 3, 4, 8]], [[1, 2]]])
    return mkframe;

def mixed_D():

    mkframe = MKPOL([verts(), [[1, 2, 3, 5], [2, 3, 4], [4, 8]], [[1, 2, 3]]])
    return mkframe;

VIEW(pol_1D())
VIEW(pol_2D())
VIEW(pol_3D())
VIEW(mixed_D())

# script prova cilindri

a = COLOR([1.0, 0, 0])(MY_CYLINDER([1, 1])(4))
b = COLOR([1.0, 0.3, 0.3])(T(1)(2.5)(MY_CYLINDER([1, 2])(8)))
c = COLOR([1.0, 0.6, 0.6])(T(1)(5.5)(MY_CYLINDER([1.5, 3])(16)))
d = COLOR([1.0, 0.8, 0.8])(T(1)(9.5)(MY_CYLINDER([1.5, 4])(24)))

VIEW(STRUCT([a, b, c, d]))

# script 1.5.3

def Leg():
    return CUBOID([0.1, 0.1, 0.7]);

def Plane():
    return CUBOID([1, 1, 0.2]);

def Table():
    return STRUCT([Leg(), T(1)(0.9)(Leg()), T(2)(0.9)(Leg()), T([1, 2])([0.9, 0.9])(Leg()), T(3)(0.7)(Plane())]);

VIEW(COLOR([0.6, 0.4, 0.2])(Leg()))
VIEW(COLOR([0.6, 0.4, 0.2])(Plane()))
VIEW(COLOR([0.6, 0.4, 0.2])(Table()))


# script 1.5.4 (1-skeleton)

def out():
    return STRUCT([SKEL_1(CUBOID([1, 1, 1])), SKEL_1(SIMPLEX(3))])

VIEW(out())

# example 1.5.5

piano_x = QUOTE([10, -10, 10])
piano_xy = PROD([piano_x,piano_x])
piano_xyz = PROD([piano_xy, QUOTE([3])])

VIEW(piano_x)
VIEW(piano_xy)
VIEW(piano_xyz)

# script 1.5.9 (boolean example)

def a():
    return T([1, 2])([-0.5, -0.5])(CUBOID([1, 1, 1]));

def b():
    return R([1, 2])(PI/4)(a());

VIEW(STRUCT([COLOR([0.9, 0.0, 0.9])(UNION([a(), b()])), COLOR([1.0, 0.2, 1.0])(T(1)(1.5)(INTERSECTION([a(), b()]))),
           COLOR([1, 0.4, 1])(T(1)(3)(XOR([a(), b()]))), COLOR([1, 0.6, 1])(T(1)(4.5)(DIFFERENCE([a(), b()])))]))

# script1.5.10 (table model (2))

def legs():
    return PROD([PROD([QUOTE([0.1, -0.8, 0.1]), QUOTE([0.1, -0.8, 0.1])]), QUOTE([0.7])]);

def plane():
    return PROD([PROD([QUOTE([1]), QUOTE([1])]), QUOTE([0.2])]);

def table():
    return TOP([legs(), plane()]);


def chair():
    m = S([1, 2, 3])([0.4, 0.4, 0.5])(table())
    return COLOR([0.8, 0.4, 0.0])(T([1, 2])([0.3, 0.3])(m));

#VIEW(chair())

def assembly():
    a = RIGHT([table(), chair()])
    b = LEFT([table(), chair()])
    c = UP([table(), chair()])
    d = DOWN([table(), chair()])
    return STRUCT([a, b, c, d])

VIEW(COLOR([0.6, 0.4, 0.2])(assembly()))

# script 1.6.3

def cube(): return CUBOID([1, 1, 1]);
def cube1(): return COLOR(CYAN)(cube());
def cube2(): return COLOR(MAGENTA)(cube());
def cube3(): return COLOR(YELLOW)(cube());
def basis(): return STRUCT([EMBED(1), CUBOID([3, 3])]);
def assembly(): return TOP([TOP([cube1(), cube2()]), cube3()]);
def out(): return TOP([basis(), assembly()]);


VIEW(out())
VIEW(SKEL_1(out()))
VIEW(TOP([basis(), SKEL_1(assembly())]))
VIEW(TOP([basis(), COLOR(RED)(SWEEP([0.2, 0.2, 0.2])(SKEL_1(assembly())))]))
VIEW(TOP([basis(), COLOR(RED)(OFFSET([0.1, 0.1, 0.1])(SKEL_1(assembly())))]))
VIEW(TOP([basis(), STRUCT([COLOR(RED)(OFFSET([0.1, 0.1, 0.1])(SKEL_1(assembly()))), assembly()])]))
