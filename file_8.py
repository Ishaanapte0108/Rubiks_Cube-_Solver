import keyboard
import time
from datetime import datetime
solution = []
s1 = []
s2 = []
s3 = []


class cube():
    a = ['W', 'O', 'G']
    b = ['W', 'O']
    # a['FRONT','TOP','LEFT']  b['FRONT','TOP']  c['FRONT','TOP','RIGHT']
    c = ['W', 'O', 'B']
    d = ['W', 'G']
    e = ['W']
    f = ['W', 'B']  # d['FRONT','LEFT']  e['FRONT']  f['FRONT','RIGHT']
    g = ['W', 'G', 'R']
    h = ['W', 'R']
    # g['FRONT','LEFT','DOWN']  h['FRONT','DOWN']  i['FRONT','DOWN','RIGHT']
    i = ['W', 'R', 'B']
    # -------------
    j = ['O', 'G']
    k = ['O']
    l = ['O', 'B']  # j['TOP','LEFT']  k['TOP']  l['TOP','RIGHT']
    m = ['G']
    n = ['B']  # m['LEFT']  |  |  n['RIGHT']
    o = ['G', 'R']
    p = ['R']
    q = ['R', 'B']  # o['LEFT','DOWN']  p['DOWN']  q['DOWN','RIGHT']
    # --------------
    r = ['O', 'G', 'Y']
    s = ['O', 'Y']
    # r['TOP','LEFT','BACK']  s['TOP','BACK']  t['TOP','RIGHT','BACK']
    t = ['O', 'B', 'Y']
    u = ['G', 'Y']
    v = ['Y']
    w = ['B', 'Y']  # u['LEFT','BACK']  v['BACK']  w['RIGHT','BACK']
    x = ['G', 'R', 'Y']
    y = ['R', 'Y']
    # x['LEFT','DOWN','BACK']  y['DOWN','BACK']  z['DOWN','RIGHT','BACK']
    z = ['R', 'B', 'Y']

    # centers = [e, k, m, n, p, v]
    # edges = [self.b, d, f, h, j, l, o, q, s, u, w, y]
    # l1 = [b, d, f, h]
    # l2 = [j, o, q, l]
    # l3 = [s, u, y, w]
    # corners = [a, c, g, i, r, t, x, z]
    def center(self):
        centers = [self.e, self.k, self.m, self.p, self.n, self.v]
        return centers

    def edge(self):
        # edges = [b,d,f,h,j,l,o,q,s,u,w]
        edges = [self.b, self.d, self.f, self.h, self.j, self.l,
                 self.o, self.q, self.s, self.u, self.w, self.y]

        # w contains blue
        return edges

    def corner(self):
        corners = [self.a, self.c, self.g, self.i,
                   self.r, self.t, self.x, self.z]
        return corners

    def layers(self):
        l1 = [self.b, self.d, self.f, self.h]
        l2 = [self.j, self.o, self.q, self.l]
        l3 = [self.s, self.u, self.y, self.w]
        return l1, l2, l3

    def F(self):
        # a,b,c,d,e,f,g,h,i
        tempcorner = self.a.copy()
        tempedge = self.b.copy()

        self.a, self.b, self.g, self.d, self.i, self.h, self.f, self.c = self.g, self.d, self.i, self.h, self.c, self.f, tempedge, tempcorner
        # i,c
        self.i[1], self.i[2] = self.i[2], self.i[1]
        self.c[1], self.c[2] = self.c[2], self.c[1]

        solution.append('F')

    def R(self):
        # c,f,i,l,n,q,t,w,z
        tempcorner = self.c.copy()
        tempedge = self.l.copy()
        self.c, self.l, self.i, self.f, self.z, self.q, self.t, self.w = self.i, self.f, self.z, self.q, self.t, self.w, tempcorner, tempedge
        # c,i,z,t,w,q
        self.c[0], self.c[1] = self.c[1], self.c[0]
        self.i[1], self.i[2] = self.i[2], self.i[1]
        self.z[0], self.z[2] = self.z[2], self.z[0]
        self.t[1], self.t[2] = self.t[2], self.t[1]
        self.w[0], self.w[1] = self.w[1], self.w[0]
        self.q[0], self.q[1] = self.q[1], self.q[0]

        solution.append('R')

    def L(self):
        # a,d,g,j,m,o,r,u,x
        tempcorner = self.a.copy()
        tempedge = self.d.copy()
        self.a, self.d, self.r, self.j, self.x, self.u, self.g, self.o = self.r, self.j, self.x, self.u, self.g, self.o, tempcorner, tempedge
        # a,r,x,o,g,j
        self.a[1], self.a[2] = self.a[2], self.a[1]
        self.r[0], self.r[1], self.r[2] = self.r[2], self.r[0], self.r[1]
        self.x[0], self.x[1] = self.x[1], self.x[0]
        self.o[0], self.o[1] = self.o[1], self.o[0]
        self.g[0], self.g[1], self.g[2] = self.g[1], self.g[2], self.g[0]
        self.j[0], self.j[1] = self.j[1], self.j[0]
        solution.append('L')

    def D(self):
        # g,h,i,o,p,q,x,y,z
        tempcorner = self.g.copy()
        tempedge = self.h.copy()
        self.g, self.h, self.x, self.o, self.z, self.y, self.i, self.q = self.x, self.o, self.z, self.y, self.i, self.q, tempcorner, tempedge
        # g,x,o,z,i,q
        self.g[1], self.g[2] = self.g[2], self.g[1]
        self.x[0], self.x[1], self.x[2] = self.x[2], self.x[0], self.x[1]
        self.o[0], self.o[1] = self.o[1], self.o[0]
        self.z[0], self.z[1] = self.z[1], self.z[0]
        self.i[0], self.i[1], self.i[2] = self.i[1], self.i[2], self.i[0]
        self.q[0], self.q[1] = self.q[1], self.q[0]
        solution.append('D')

    def U(self):
        # a,b,c,j,k,l,r,s,t
        tempcorner = self.a.copy()
        tempedge = self.b.copy()
        self.a, self.b, self.c, self.l, self.t, self.s, self.r, self.j = self.c, self.l, self.t, self.s, self.r, self.j, tempcorner, tempedge
        # a,b,c,t,r
        self.a[0], self.a[2] = self.a[2], self.a[0]
        self.b[0], self.b[1] = self.b[1], self.b[0]
        self.c[0], self.c[1] = self.c[1], self.c[0]
        self.t[1], self.t[2] = self.t[2], self.t[1]
        self.r[0], self.r[1] = self.r[1], self.r[0]
        self.j[0], self.j[1] = self.j[1], self.j[0]
        solution.append('U')

    def B(self):
        # r,s,t,u,v,w,x,y,z
        tempcorner = self.r.copy()
        tempedge = self.s.copy()
        self.r, self.s, self.t, self.w, self.z, self.y, self.x, self.u = self.t, self.w, self.z, self.y, self.x, self.u, tempcorner, tempedge
        # r,t
        self.r[0], self.r[1] = self.r[1], self.r[0]
        self.t[0], self.t[1] = self.t[1], self.t[0]
        solution.append('B')

    def Bd(self):
        # r,s,t,u,v,w,x,y,z
        tempcorner = self.r.copy()
        tempedge = self.s.copy()
        self.r, self.s, self.x, self.u, self.z, self.y, self.t, self.w = self.x, self.u, self.z, self.y, self.t, self.w, tempcorner, tempedge
        # t,z
        self.t[0], self.t[1] = self.t[1], self.t[0]
        self.z[0], self.z[1] = self.z[1], self.z[0]
        solution.append('Bd')

    def Fd(self):
        tempcorner = self.a.copy()
        tempedge = self.d.copy()
        # a,b,c,f,g,h,i=c,f,i,h,tempcorner,tempedge,g
        self.a = self.c
        self.c = self.i
        self.d = self.b
        self.b = self.f
        self.f = self.h
        self.i = self.g
        self.g = tempcorner
        self.h = tempedge
        # swapping
        temp = self.a[1]
        self.a[1] = self.a[2]
        self.a[2] = temp

        temp = self.c[1]
        self.c[1] = self.c[2]
        self.c[2] = temp
        solution.append('Fd')

    def Rd(self):
        tempcorner = self.c.copy()
        tempedge = self.l.copy()
        self.c, self.l, self.t, self.w, self.z, self.q, self.f, self.i = self.t, self.w, self.z, self.q, self.i, self.f, tempedge, tempcorner
        # swapping
        self.c[1], self.c[2] = self.c[2], self.c[1]
        self.l[0], self.l[1] = self.l[1], self.l[0]
        # 0,2 of t  0 1 of i 1 2 of z
        self.t[0], self.t[2] = self.t[2], self.t[0]
        self.i[0], self.i[1] = self.i[1], self.i[0]
        self.z[1], self.z[2] = self.z[2], self.z[1]
        self.w[0], self.w[1] = self.w[1], self.w[0]
        solution.append('Rd')

    def Ld(self):
        # a,d,g,j,m,o,r,u,x
        tempcorner = self.a.copy()
        tempedge = self.d.copy()
        self.a, self.d, self.g, self.o, self.x, self.u, self.r, self.j = self.g, self.o, self.x, self.u, self.r, self.j, tempcorner, tempedge
        # swapping a 01
        #
        self.a[0], self.a[1], self.a[2] = self.a[2], self.a[0], self.a[1]
        self.r[1], self.r[2] = self.r[2], self.r[1]
        self.u[0], self.u[1] = self.u[1], self.u[0]
        self.d[0], self.d[1] = self.d[1], self.d[0]
        self.x[0], self.x[1], self.x[2] = self.x[1], self.x[2], self.x[0]
        self.g[0], self.g[1] = self.g[1], self.g[0]
        solution.append('Ld')

    def Dd(self):
        tempcorner = self.i.copy()
        tempedge = self.h.copy()
        self.i, self.h, self.z, self.q, self.y, self.x, self.o, self.g = self.z, self.q, self.x, self.y, self.o, self.g, tempedge, tempcorner
        # swapping
        self.x[1], self.x[2] = self.x[2], self.x[1]
        self.y[0], self.y[1] = self.y[1], self.y[0]
        self.z[0], self.z[1], self.z[2] = self.z[1], self.z[2], self.z[0]
        self.g[0], self.g[1], self.g[2] = self.g[2], self.g[0], self.g[1]
        self.h[0], self.h[1] = self.h[1], self.h[0]
        self.i[0], self.i[1] = self.i[1], self.i[0]
        solution.append('Dd')

    def Ud(self):
        tempcorner = self.r.copy()
        tempedge = self.s.copy()
        self.r, self.s, self.t, self.l, self.c, self.b, self.j, self.a = self.t, self.l, self.c, self.b, self.a, self.j, tempedge, tempcorner
        # swapping
        self.r[1], self.r[2] = self.r[2], self.r[1]
        self.t[0], self.t[1] = self.t[1], self.t[0]
        self.l[0], self.l[1] = self.l[1], self.l[0]
        self.a[0], self.a[1] = self.a[1], self.a[0]
        self.b[0], self.b[1] = self.b[1], self.b[0]
        self.c[0], self.c[2] = self.c[2], self.c[0]
        solution.append('Ud')

    def acceptCube(self, cu):
        import opencv_6 as o
        sc = o.allsides
        # sc = [['Y', 'O', 'W', 'B', 'W', 'Y', 'W', 'R', 'Y'],
        #       ['B', 'W', 'R', 'W', 'O', 'G', 'R', 'W', 'G'],
        #       ['R', 'G', 'G', 'W', 'G', 'Y', 'W', 'B', 'B'],
        #       ['O', 'G', 'G', 'O', 'R', 'Y', 'R', 'R', 'Y'],
        #       ['O', 'O', 'Y', 'R', 'B', 'G', 'O', 'O', 'B'],
        #       ['B', 'B', 'W', 'Y', 'Y', 'R', 'O', 'B', 'G']]

        # layer1
        self.a[0], self.a[1], self.a[2] = sc[0][0], sc[1][6], sc[2][2]
        self.b[0], self.b[1] = sc[0][1], sc[1][7]
        self.c[0], self.c[1], self.c[2] = sc[0][2], sc[1][8], sc[4][0]
        self.d[0], self.d[1] = sc[0][3], sc[2][5]
        self.e[0] = sc[0][4]  # white center
        self.f[0], self.f[1] = sc[0][5], sc[4][3]
        self.g[0], self.g[1], self.g[2] = sc[0][6], sc[2][8], sc[3][0]
        self.h[0], self.h[1] = sc[0][7], sc[3][1]
        self.i[0], self.i[1], self.i[2] = sc[0][8], sc[3][2], sc[4][6]
        # layer2
        self.j[0], self.j[1] = sc[1][3], sc[2][1]
        self.k[0] = sc[1][4]  # orange center
        self.l[0], self.l[1] = sc[1][5], sc[4][1]
        self.m[0] = sc[2][4]  # green center
        self.n[0] = sc[4][4]  # blue center
        self.o[0], self.o[1] = sc[2][7], sc[3][3]
        self.p[0] = sc[3][4]  # red center
        self.q[0], self.q[1] = sc[3][5], sc[4][7]
        # layer 3
        self.r[0], self.r[1], self.r[2] = sc[1][0], sc[2][0], sc[5][2]
        self.s[0], self.s[1] = sc[1][1], sc[5][1]
        self.t[0], self.t[1], self.t[2] = sc[1][2], sc[4][2], sc[5][0]
        self.u[0], self.u[1] = sc[2][3], sc[5][5]
        self.v[0] = sc[5][4]  # yellow center
        self.w[0], self.w[1] = sc[4][5], sc[5][3]
        self.x[0], self.x[1], self.x[2] = sc[2][6], sc[3][6], sc[5][8]
        self.y[0], self.y[1] = sc[3][7], sc[5][7]
        self.z[0], self.z[1], self.z[2] = sc[3][8], sc[4][8], sc[5][6]


def scramble_cube(cu):
    cu.U()
    cu.R()
    # cu.B()
    # cu.Rd()
    # cu.Bd()
    # cu.Ud()
    # cu.B()

    # cu.B()
    # cu.R()
    # cu.L()
    # cu.Bd()
    # cu.Rd()
    # cu.D()
    # cu.B()
    # cu.Bd()
    # cu.Dd()

    # cu.R()
    # cu.Ud()
    # cu.Ld()
    # cu.D()
    # cu.L()
    # cu.L()
    # cu.B()
    # cu.F()
    # cu.L()
    # cu.R()
    # cu.Ud()
    # cu.Bd()
    # cu.Fd()
    # cu.U()
    # cu.Dd()
    # cu.Rd()

    solution.clear()


def disp(cu):
    print("", cu.a, cu.b, cu.c, '\n', cu.d, cu.e, cu.f, '\n', cu.g, cu.h, cu.i, '\n--------------------------\n', cu.j, cu.k, cu.l, '\n', cu.m,
          '\t', cu.n, '\n', cu.o, cu.p, cu.q, '\n--------------------------\n', cu.r, cu.s, cu.t, '\n', cu.u, cu.v, cu.w, '\n', cu.x, cu.y, cu.z)


# ['O','G','B','R']


def findWhiteEdges(cu):
    count = 0
    whiteEdgePlacement = ['0', '1', '2', '3']
    # print(cu.edge())
    for ii in cu.edge():
        if 'W' in ii:
            if 'O' in ii:
                whiteEdgePlacement[0] = count
            elif 'G' in ii:
                whiteEdgePlacement[1] = count
            elif 'B' in ii:
                whiteEdgePlacement[2] = count
            else:
                whiteEdgePlacement[3] = count
        count += 1
    return whiteEdgePlacement


def findWhiteCorners(cu):
    count = 0
    whiteCornerPlacement = ['0', '1', '2', '3']
    for ii in cu.corner():
        if 'W' in ii:
            if 'G' in ii and 'O' in ii:
                whiteCornerPlacement[0] = count
            if 'O' in ii and 'B' in ii:
                whiteCornerPlacement[1] = count
            if 'G' in ii and 'R' in ii:
                whiteCornerPlacement[2] = count
            if 'R' in ii and 'B' in ii:
                whiteCornerPlacement[3] = count
        count += 1

    return whiteCornerPlacement


# def findYellowEdges(cu):
#     count = 0
#     yellowEdgePlacement = ['0', '1', '2', '3']
#     for ii in cu.edge():
#         if 'Y' in ii:
#             if 'O' in ii:
#                 yellowEdgePlacement[0] = count
#             elif 'G' in ii:
#                 yellowEdgePlacement[1] = count
#             elif 'B' in ii:
#                 yellowEdgePlacement[2] = count
#             else:
#                 yellowEdgePlacement[3] = count
#         count += 1
#     return yellowEdgePlacement

def findSecondLayerEdges(cu):
    edges = cu.edge()
    count = 0
    a = ['0', '1', '2', '3']
    for ii in edges:
        if ('G' in ii and 'O' in ii):
            #print('found O-G piece', count)
            a[0] = count
            count += 1
            continue

        if ('O' in ii and 'B' in ii):
            #print('found o-b piece ', count)
            a[1] = count
            count += 1
            continue

        if ('G' in ii and 'R' in ii):
            #print('found g-r piece ', count)
            a[2] = count
            count += 1
            continue

        if ('R' in ii and 'B' in ii):
            #print('found g-r piece ', count)
            a[3] = count
            count += 1
            continue

        count = count+1

    return a


def yellow_cross_C1(cu):
    edges = cu.edge()

    if (edges[8][0] == 'Y' and edges[9][0] == 'Y' and edges[10][0] == 'Y' and edges[11][0] == 'Y'):
        #print('executed yellow cross 1')
        cu.U()
        cu.R()
        cu.B()
        cu.Rd()
        cu.Bd()
        cu.Ud()


def yellow_cross_c2(cu):
    edges = cu.edge()

    if (edges[8][1] == 'Y' and edges[10][1] == 'Y'):
        #print('executed yellow cross 2 1')
        cu.B()
        cu.B()

        cu.U()
        cu.R()
        cu.B()
        cu.Rd()
        cu.Bd()
        cu.Ud()
    elif (edges[8][1] == 'Y' and edges[9][1] == 'Y'):
        #print('executed yellow cross 2 2')
        cu.B()

        cu.U()
        cu.R()
        cu.B()
        cu.Rd()
        cu.Bd()
        cu.Ud()
    elif (edges[11][1] == 'Y' and edges[10][1] == 'Y'):
        #print('executed yellow cross 2 3')
        cu.Bd()

        cu.U()
        cu.R()
        cu.B()
        cu.Rd()
        cu.Bd()
        cu.Ud()
    elif (edges[11][1] == 'Y' and edges[9][1] == 'Y'):
        #print('executed yellow cross 2 4')
        cu.U()
        cu.R()
        cu.B()
        cu.Rd()
        cu.Bd()
        cu.Ud()


def yellow_cross_c3(cu):
    edges = cu.edge()
    if ((edges[8][1] == 'Y' and edges[11][1] == 'Y') and (edges[9][1] != 'Y' and edges[10][1] != 'Y')):
        #print('executed yellow cross 3 1')
        cu.B()
        cu.U()
        cu.R()
        cu.B()
        cu.Rd()
        cu.Bd()
        cu.Ud()
    if ((edges[9][1] == 'Y' and edges[10][1] == 'Y') and (edges[8][1] != 'Y' and edges[11][1] != 'Y')):

        #print('executed yellow cross 3 2')
        cu.U()
        cu.R()
        cu.B()
        cu.Rd()
        cu.Bd()
        cu.Ud()


def white_orange(cu, v):
    edges = cu.edge()
# working on orange-white piece
    # print(v)

    if v[0] == 10:
        # rotations:
        #print("Executing O-W at 10")
        cu.B()
        cu.U()
        cu.U()
    elif v[0] == 8:
        #print("Executing O-W at 8")
        # rotations:
        cu.U()
        cu.U()
    elif v[0] == 9:
        #print("Executing O-W at 9")
        # rotations:
        cu.Bd()
        cu.U()
        cu.U()
    elif v[0] == 11:
        #print("Executing O-W at 11")
        # rotations:
        cu.B()
        cu.B()
        cu.U()
        cu.U()
    elif v[0] == 4:
        #print("Executing O-W at 4")
        # rotations:
        cu.Ud()
    elif v[0] == 5:
        #print("Executing O-W at 5")
        # rotations:
        cu.U()
    elif v[0] == 6:
        #print("Executing O-W at 6")
        # rotations:
        cu.Ld()
        cu.F()
    elif v[0] == 7:
        #print("Executing O-W at 7")
        # rotations:
        cu.R()
        cu.Fd()

    elif v[0] == 1:
        #print("Executing O-W at 1")
        # rotations:
        cu.F()
    elif v[0] == 3:
        #print("Executing O-W at 3")
        # rotations:
        cu.F()
        cu.F()
    elif v[0] == 2:
        #print("Executing O-W at 2")
        # rotations:
        cu.Fd()


def white_orange_orientation(cu):
    edges = cu.edge()
    if edges[0][0] == 'O':
        #print("executed O-W orientation")
        cu.F()
        cu.R()
        cu.U()


def white_green(cu, v):
    edges = cu.edge()
    # print(v)
# working on orange-green piece
    if v[1] == 2:
        # rotations:
        #print("Executing G-W at 2")
        cu.Rd()
        cu.Dd()
        cu.Dd()
        cu.Ld()
    elif v[1] == 3:
        # rotations:
        #print("Executing G-W at 3")
        cu.Dd()
        cu.Ld()
    elif v[1] == 4:
        #print("Executing G-W at 4")
        # rotations:
        cu.L()
    elif v[1] == 5:
        #print("Executing G-W at 5")
        # rotations:
        cu.R()
        cu.B()
        cu.B()
        cu.L()
        cu.L()
    elif v[1] == 6:
        #print("Executing G-W at 6")
        # rotations:
        cu.Ld()
    elif v[1] == 7:
        #print("Executing G-W at 7")
        # rotations:
        cu.Dd()
        cu.Dd()
        cu.Ld()
    elif v[1] == 8:
        #print("Executing G-W at 8")
        # rotations:
        cu.B()
        cu.L()
        cu.L()
    elif v[1] == 9:
        #print("Executing G-W at 9")
        # rotations:
        cu.L()
        cu.L()
    elif v[1] == 10:
        #print("Executing G-W at 10")
        # rotations:
        cu.B()
        cu.B()
        cu.L()
        cu.L()
    elif v[1] == 11:
        #print("Executing G-W at 11")
        # rotations:
        cu.D()
        cu.Ld()


def white_green_orientation(cu):
    edges = cu.edge()
    if edges[1][0] == 'G':
        #print("executed w-g orientation")
        cu.Fd()
        cu.Dd()
        cu.F()
        cu.Ld()
       # print("b edge : ", edges[0])


def white_blue(cu, v):
    edges = cu.edge()
    # print(v)
# working on orange-green piece
    if v[2] == 3:
        # rotations:
        #print("Executing B-W at 3")
        cu.D()
        cu.R()
    elif v[2] == 4:
        # rotations:
        #print("Executing B-W at 4")
        cu.Ld()
        cu.Bd()
        cu.Bd()
        cu.L()
        cu.R()
        cu.R()
    elif v[2] == 5:
        #print("Executing B-W at 5")
        # rotations:
        cu.Rd()
    elif v[2] == 6:
        # rotations:
        #print("Executing B-W at 6")
        cu.D()
        cu.D()
        cu.R()
    elif v[2] == 7:
        # rotations:
        #print("Executing B-W at 7")
        cu.R()
    elif v[2] == 8:
        # rotations:
        #print("Executing B-W at 8")
        cu.Bd()
        cu.R()
        cu.R()
    elif v[2] == 9:
        # rotations:
        #print("Executing B-W at 9")
        cu.Bd()
        cu.Bd()
        cu.R()
        cu.R()
    elif v[2] == 10:
        #print("Executing B-W at 10")
        # rotations:
        cu.R()
        cu.R()
    elif v[2] == 11:
        # rotations:
        #print("Executing B-W at 11")
        cu.Dd()
        cu.R()


def white_blue_orientation(cu):
    edges = cu.edge()
    if edges[2][0] == 'B':
        #print("executed orientation for W-B")
        cu.Fd()
        cu.Ud()
        cu.F()
        cu.Rd()
       # print("b edge : ", edges[0])


def white_red(cu, v):
    edges = cu.edge()
    #print("Before red=", v)

    if v[3] == 4:
        # rotations:
        #print("Executing R-W at 4")
        cu.L()
        cu.L()
        cu.D()
        cu.Ld()
        cu.Ld()
    elif v[3] == 5:
        # rotations:
        #print("Executing R-W at 5")
        cu.Rd()
        cu.Rd()
        cu.Dd()
        cu.R()
        cu.R()
    elif v[3] == 6:
        # rotations:
        #print("Executing R-W at 6")
        cu.D()
    elif v[3] == 7:
        # rotations:
        #print("Executing R-W at 7")
        cu.Dd()
    elif v[3] == 8:
        # rotations:
        #print("Executing R-W at 8")
        cu.Bd()
        cu.Bd()
        cu.Dd()
        cu.Dd()
    elif v[3] == 9:
        # rotations:
        #print("Executing R-W at 9")
        cu.B()
        cu.Dd()
        cu.Dd()
    elif v[3] == 10:
        # rotations:
        #print("Executing R-W at 10")
        cu.Bd()
        cu.Dd()
        cu.Dd()
    elif v[3] == 11:
        #print("Executing R-W at 11")
        cu.Dd()
        cu.Dd()


def white_red_orientation(cu):
    edges = cu.edge()
    if edges[3][0] == 'R':
        #print("executed orientation for R")
        cu.D()
        cu.D()
        cu.B()
        cu.R()
        cu.Dd()
        cu.Rd()


def orange_green_corner(cu, v):
    corners = cu.corner()
    if v[0] == 1:
        #print("Executing O-G-Corner at 1")
        cu.R()
        cu.B()
        cu.B()
        cu.Rd()
        cu.U()
        cu.Bd()
        cu.Ud()

    elif v[0] == 2:
        #print("Executing O-G-Corner at 2")
        cu.Dd()
        cu.Bd()
        cu.D()
        cu.B()
        cu.U()
        cu.Bd()
        cu.Ud()

    elif v[0] == 3:
        #print("Executing O-G-Corner at 3")
        cu.D()
        cu.B()
        cu.Dd()
        cu.B()
        cu.B()
        cu.U()
        cu.Bd()
        cu.Ud()

    elif v[0] == 4:
        #print("Executing O-G-Corner at 4")
        cu.B()
        cu.U()
        cu.Bd()
        cu.Ud()

    elif v[0] == 5:
        #print("Executing O-G-Corner at 5")
        cu.B()
        cu.B()
        cu.U()
        cu.Bd()
        cu.Ud()

    elif v[0] == 6:
        #print("Executing O-G-Corner at 6")
        cu.U()
        cu.Bd()
        cu.Ud()

    elif v[0] == 7:
        cu.Bd()
        cu.U()
        cu.Bd()
        cu.Ud()


def orange_green_CO(cu):
    corners = cu.corner()
    if corners[0][0] == 'O':
        cu.U()
        cu.Bd()
        cu.Ud()
        cu.B()
        cu.U()
        cu.Bd()
        cu.Ud()
    if corners[0][0] == 'G':
        cu.Ld()
        cu.B()
        cu.L()
        cu.Bd()
        cu.Ld()
        cu.B()
        cu.L()


def orange_blue_corner(cu, v):
    corners = cu.corner()

    if v[1] == 2:
        #print("Executing O-B-Corner at 2")
        cu.Dd()
        cu.Bd()
        cu.D()
        cu.R()
        cu.Bd()
        cu.Rd()

    elif v[1] == 3:
        #print("Executing O-B-Corner at3")
        cu.D()
        cu.B()
        cu.Dd()
        cu.B()
        cu.R()
        cu.Bd()
        cu.Rd()

    elif v[1] == 4:
       # print("Executing O-B-Corner at 4")
        cu.R()
        cu.Bd()
        cu.Rd()

    elif v[1] == 5:
        #print("Executing O-B-Corner at 5")
        cu.B()
        cu.R()
        cu.Bd()
        cu.Rd()

    elif v[1] == 6:
        #print("Executing O-B-Corner at 6")
        cu.R()
        cu.Bd()
        cu.Bd()
        cu.Rd()

    elif v[1] == 7:
        cu.B()
        cu.B()
        cu.R()
        cu.Bd()
        cu.Rd()


def orange_blue_CO(cu):
    corners = cu.corner()

    if corners[1][0] == 'O':
        #print("Executing O at front of O-B_corner")
        cu.R()
        cu.B()
        cu.Rd()
        cu.Bd()
        cu.R()
        cu.B()
        cu.Rd()
    if corners[1][0] == 'B':
        #print("Executing B at front of O-B_corner Piece")
        cu.R()
        cu.Bd()
        cu.Rd()
        cu.B()
        cu.R()
        cu.Bd()
        cu.Rd()


def green_red_corner(cu, v):
    corners = cu.corner()
    # print(v)

    if v[2] == 3:
        #print("Executing G-R-Corner at 3")
        cu.D()
        cu.B()
        cu.Dd()
        cu.B()
        cu.Dd()
        cu.B()
        cu.D()

    elif v[2] == 4:
        #print("Executing G-R-Corner at 4")
        cu.Dd()
        cu.B()
        cu.D()

    elif v[2] == 5:
       # print("Executing G-R-Corner at 5")
        cu.B()
        cu.Dd()
        cu.B()
        cu.D()

    elif v[2] == 6:
        #print("Executing G-R-Corner at 6")
        cu.Bd()
        cu.Dd()
        cu.B()
        cu.D()

    elif v[2] == 7:
        #print("Executing G-R-Corner at 7")
        cu.Bd()
        cu.Bd()
        cu.Dd()
        cu.B()
        cu.D()


def green_red_CO(cu):
    corners = cu.corner()

    if corners[2][0] == 'G':
        #print("Executing orientation of G-R_corner Piece G at front")
        cu.Dd()
        cu.Bd()
        cu.D()
        cu.Bd()
        cu.Bd()
        cu.L()
        cu.Bd()
        cu.Ld()

    if corners[2][0] == 'R':
        #print("Executing orientation of G-R_corner Piece R at front")
        cu.Dd()
        cu.Bd()
        cu.D()
        cu.B()
        cu.L()
        cu.Bd()
        cu.Ld()
        cu.B()
        cu.Dd()
        cu.B()
        cu.D()


def red_blue_corner(cu, v):
    corners = cu.corner()
    # print(v)

    if v[3] == 4:
        #print("Executing B-R-Corner at 4")
        cu.Bd()
        cu.D()
        cu.Bd()
        cu.Dd()

    elif v[3] == 5:
        #print("Executing B-R-Corner at 5")
        cu.D()
        cu.Bd()
        cu.Dd()

    elif v[3] == 6:
        #print("Executing B-R-Corner at 6")
        cu.Bd()
        cu.Bd()
        cu.D()
        cu.Bd()
        cu.Dd()

    elif v[3] == 7:
        #print("Executing B-R-Corner at 7")
        cu.B()
        cu.D()
        cu.Bd()
        cu.Dd()


def red_blue_CO(cu):
    corners = cu.corner()

    if corners[3][0] == 'R':
        #print("Executing orientation of B-R_corner Piece R at front")
        cu.D()
        cu.B()
        cu.Dd()
        cu.Bd()
        cu.D()
        cu.B()
        cu.B()
        cu.Dd()
        cu.Bd()
        cu.D()
        cu.B()
        cu.Dd()

    if corners[3][0] == 'B':
        #print("Executing orientation of B-R_corner Piece B at front")
        cu.D()
        cu.B()
        cu.Dd()
        cu.Bd()
        cu.D()
        cu.B()
        cu.Dd()

# l2


def secondLayerO_G(cu, v):
    edges = cu.edge()

    if v[0] == 4:
        pass

    elif v[0] == 5:
        cu.B()
        cu.R()
        cu.Bd()
        cu.Rd()
        cu.Bd()
        cu.Ud()
        cu.B()
        cu.U()

        cu.B()
        cu.B()

        cu.Bd()
        cu.Ld()
        cu.B()
        cu.L()
        cu.B()
        cu.U()
        cu.Bd()
        cu.Ud()

    elif v[0] == 6:
        cu.B()
        cu.L()
        cu.Bd()
        cu.Ld()
        cu.Bd()
        cu.Dd()
        cu.B()
        cu.D()

        cu.Bd()
        cu.Ld()
        cu.B()
        cu.L()
        cu.B()
        cu.U()
        cu.Bd()
        cu.Ud()

    elif v[0] == 7:
        cu.Bd()
        cu.Rd()
        cu.B()
        cu.R()
        cu.B()
        cu.D()
        cu.Bd()
        cu.Dd()

        cu.Bd()
        cu.Ld()
        cu.B()
        cu.L()
        cu.B()
        cu.U()
        cu.Bd()
        cu.Ud()

    elif v[0] == 8:

        cu.Bd()
        cu.Ld()
        cu.B()
        cu.L()
        cu.B()
        cu.U()
        cu.Bd()
        cu.Ud()

    elif v[0] == 9:
        cu.Bd()

        cu.Bd()
        cu.Ld()
        cu.B()
        cu.L()
        cu.B()
        cu.U()
        cu.Bd()
        cu.Ud()

    elif v[0] == 10:
        cu.B()

        cu.Bd()
        cu.Ld()
        cu.B()
        cu.L()
        cu.B()
        cu.U()
        cu.Bd()
        cu.Ud()

    elif v[0] == 11:
        cu.B()
        cu.B()

        cu.Bd()
        cu.Ld()
        cu.B()
        cu.L()
        cu.B()
        cu.U()
        cu.Bd()
        cu.Ud()


def secondLayerO_G_orientation(cu):
    edges = cu.edge()

    if edges[4][0] == 'G':
        cu.Bd()
        cu.Ld()
        cu.B()
        cu.L()
        cu.B()
        cu.U()
        cu.Bd()
        cu.Ud()

        cu.B()
        cu.B()

        cu.Bd()
        cu.Ld()
        cu.B()
        cu.L()
        cu.B()
        cu.U()
        cu.Bd()
        cu.Ud()


def secondLayerO_B(cu, v):
    edges = cu.edge()

    if v[1] == 5:
        pass

    elif v[1] == 6:
        cu.B()
        cu.L()
        cu.Bd()
        cu.Ld()
        cu.Bd()
        cu.Dd()
        cu.B()
        cu.D()

        cu.Bd()

        cu.Bd()
        cu.Ud()
        cu.B()
        cu.U()
        cu.B()
        cu.R()
        cu.Bd()
        cu.Rd()

    elif v[1] == 7:
        cu.Bd()
        cu.Rd()
        cu.B()
        cu.R()
        cu.B()
        cu.D()
        cu.Bd()
        cu.Dd()

        cu.Bd()

        cu.Bd()
        cu.Ud()
        cu.B()
        cu.U()
        cu.B()
        cu.R()
        cu.Bd()
        cu.Rd()

    elif v[1] == 8:
        cu.Bd()

        cu.Bd()
        cu.Ud()
        cu.B()
        cu.U()
        cu.B()
        cu.R()
        cu.Bd()
        cu.Rd()

    elif v[1] == 9:
        cu.Bd()
        cu.Bd()

        cu.Bd()
        cu.Ud()
        cu.B()
        cu.U()
        cu.B()
        cu.R()
        cu.Bd()
        cu.Rd()

    elif v[1] == 10:

        cu.Bd()
        cu.Ud()
        cu.B()
        cu.U()
        cu.B()
        cu.R()
        cu.Bd()
        cu.Rd()

    elif v[1] == 11:

        cu.B()

        cu.Bd()
        cu.Ud()
        cu.B()
        cu.U()
        cu.B()
        cu.R()
        cu.Bd()
        cu.Rd()


def secondLayerO_B_orientation(cu):
    edges = cu.edge()

    if edges[5][0] == 'B':
        cu.Bd()
        cu.Ud()
        cu.B()
        cu.U()
        cu.B()
        cu.R()
        cu.Bd()
        cu.Rd()

        cu.Bd()
        cu.Bd()

        cu.Bd()
        cu.Ud()
        cu.B()
        cu.U()
        cu.B()
        cu.R()
        cu.Bd()
        cu.Rd()


def secondLayerG_R(cu, v):
    edges = cu.edge()

    if v[2] == 6:
        pass

    elif v[2] == 7:
        cu.Bd()
        cu.Rd()
        cu.B()
        cu.R()
        cu.B()
        cu.D()
        cu.Bd()
        cu.Dd()

        cu.B()

        cu.Bd()
        cu.Dd()
        cu.B()
        cu.D()
        cu.B()
        cu.L()
        cu.Bd()
        cu.Ld()

    elif v[2] == 8:
        cu.B()

        cu.Bd()
        cu.Dd()
        cu.B()
        cu.D()
        cu.B()
        cu.L()
        cu.Bd()
        cu.Ld()

    elif v[2] == 9:
        cu.Bd()
        cu.Dd()
        cu.B()
        cu.D()
        cu.B()
        cu.L()
        cu.Bd()
        cu.Ld()

    elif v[2] == 10:

        cu.B()
        cu.B()

        cu.Bd()
        cu.Dd()
        cu.B()
        cu.D()
        cu.B()
        cu.L()
        cu.Bd()
        cu.Ld()

    elif v[2] == 11:
        cu.Bd()

        cu.Bd()
        cu.Dd()
        cu.B()
        cu.D()
        cu.B()
        cu.L()
        cu.Bd()
        cu.Ld()


def secondLayerG_R_orientation(cu):
    edges = cu.edge()

    if edges[6][0] == 'R':
        cu.Bd()
        cu.Dd()
        cu.B()
        cu.D()
        cu.B()
        cu.L()
        cu.Bd()
        cu.Ld()

        cu.B()
        cu.B()

        cu.Bd()
        cu.Dd()
        cu.B()
        cu.D()
        cu.B()
        cu.L()
        cu.Bd()
        cu.Ld()


def secondLayerR_B(cu, v):
    edges = cu.edge()

    if v[3] == 7:
        pass

    elif v[3] == 8:
        cu.Bd()

        cu.B()
        cu.D()
        cu.Bd()
        cu.Dd()
        cu.Bd()
        cu.Rd()
        cu.B()
        cu.R()

    elif v[3] == 9:
        cu.Bd()
        cu.Bd()

        cu.B()
        cu.D()
        cu.Bd()
        cu.Dd()
        cu.Bd()
        cu.Rd()
        cu.B()
        cu.R()

    elif v[3] == 10:
        cu.B()
        cu.D()
        cu.Bd()
        cu.Dd()
        cu.Bd()
        cu.Rd()
        cu.B()
        cu.R()

    elif v[3] == 11:
        cu.B()

        cu.B()
        cu.D()
        cu.Bd()
        cu.Dd()
        cu.Bd()
        cu.Rd()
        cu.B()
        cu.R()


def secondLayerR_B_orientation(cu):
    edges = cu.edge()

    if edges[7][0] == 'B':
        cu.B()
        cu.D()
        cu.Bd()
        cu.Dd()
        cu.Bd()
        cu.Rd()
        cu.B()
        cu.R()

        cu.Bd()
        cu.Bd()

        cu.B()
        cu.D()
        cu.Bd()
        cu.Dd()
        cu.Bd()
        cu.Rd()
        cu.B()
        cu.R()

# l2


def checkSecondLayer(cu):
    check = 0

    if cu.j == ['O', 'G']:
        check += 1
    if cu.k == ['O']:
        check += 1
    if cu.l == ['O', 'B']:
        check += 1
    if cu.m == ['G']:
        check += 1
    if cu.n == ['B']:
        check += 1
    if cu.o == ['G', 'R']:
        check += 1
    if cu.p == ['R']:
        check += 1
    if cu.q == ['R', 'B']:
        check += 1

    return check


def checkMatchingYellowEdgesWithcenter(cu):
    edges = cu.edge()
    # print(edges)
    if (edges[8][0] == 'O' and edges[9][0] == 'G' and edges[11][0] == 'R' and edges[10][0] == 'B'):
        return 1

    return 0


def checkReadyMadeYellowCross(cu):
    edges = cu.edge()
    # check ready made yello cross
    if (edges[8][1] == 'Y' and edges[9][1] == 'Y' and edges[10][1] == 'Y' and edges[11][1] == 'Y'):
        #print('yellow cross present')
        return 1

    return 0


def yellowEdges_c1(cu):
    edges = cu.edge()
    # opposite edges matching
    #print(edges[9][0], ' ', edges[8][0], ' ', edges[10][0], ' ', edges[11][0])

    if ((edges[8][0] == 'B' and edges[11][0] == 'G') or (edges[8][0] == 'G' and edges[11][0] == 'B')):
        # print('exe1')
        cu.R()
        cu.B()
        cu.Rd()
        cu.B()
        cu.R()
        cu.B()
        cu.B()
        cu.Rd()

    elif ((edges[9][0] == 'B' and edges[10][0] == 'G') or (edges[9][0] == 'G' and edges[11][0] == 'B')):
        # print('exe2')
        cu.Bd()

        cu.R()
        cu.B()
        cu.Rd()
        cu.B()
        cu.R()
        cu.B()
        cu.B()
        cu.Rd()

    elif ((edges[8][0] == 'O' and edges[11][0] == 'R') or (edges[8][0] == 'R' and edges[11][0] == 'O')):
        # print('exe3')
        cu.R()
        cu.B()
        cu.Rd()
        cu.B()
        cu.R()
        cu.B()
        cu.B()
        cu.Rd()
    elif ((edges[9][0] == 'O' and edges[10][0] == 'R') or (edges[9][0] == 'R' and edges[10][0] == 'O')):

        print(edges[9][0], ' ', edges[11][0])
        #print('in exe4')
        cu.Bd()

        cu.R()
        cu.B()
        cu.Rd()
        cu.B()
        cu.R()
        cu.B()
        cu.B()
        cu.Rd()


def yellow_edges_c2(cu):
    edges = cu.edge()

    if (edges[8][0] == 'O' and edges[10][0] == 'B'):
        #print('executing o-b edge')
        cu.Bd()

        cu.R()
        cu.B()
        cu.Rd()
        cu.B()
        cu.R()
        cu.B()
        cu.B()
        cu.Rd()
        return 0

    elif (edges[11][0] == 'R' and edges[10][0] == 'B'):
        #print('executing r-b edge')
        cu.R()
        cu.B()
        cu.Rd()
        cu.B()
        cu.R()
        cu.B()
        cu.B()
        cu.Rd()
        return 0

    elif (edges[11][0] == 'R' and edges[9][0] == 'G'):
        #print('executing r-g edge')
        cu.B()

        cu.R()
        cu.B()
        cu.Rd()
        cu.B()
        cu.R()
        cu.B()
        cu.B()
        cu.Rd()
        return 0

    elif (edges[8][0] == 'O' and edges[9][0] == 'G'):
       #print('executing o-g edge')
        cu.Bd()
        cu.Bd()

        cu.R()
        cu.B()
        cu.Rd()
        cu.B()
        cu.R()
        cu.B()
        cu.B()
        cu.Rd()
        return 0
    cu.B()
    return 1


def yellow_edges_c3(cu):
    edges = cu.edge()
    #print('inside yellow_edges_c3')
    if (edges[8][0] == 'O' and edges[10][0] == 'B' and edges[11][0] == 'R' and edges[9][0] == 'G'):
        #print('executed yellow_edges_c3')
        return 0
    else:

        cu.B()
        return 1


def alignYellowCorners_c1(cu):
    # no matching corners
    corners = cu.corner()
   # print(corners[4], ' ', corners[5], ' ', corners[6], ' ', corners[7])

    check = 0
    if 'G' in corners[4]:
        check += 1
    if 'O' in corners[4]:
        check += 1
    if check == 2:
        return 4

    check = 0
    if 'B' in corners[5]:
        check += 1
    if 'O' in corners[5]:
        check += 1
    if check == 2:
        return 5

    check = 0
    if 'R' in corners[6]:
        check += 1
    if 'G' in corners[6]:
        check += 1
    if check == 2:
        return 6

    check = 0
    if 'B' in corners[7]:
        check += 1
    if 'R' in corners[7]:
        check += 1
    if check == 2:
        return 7

    #print('aligning atleast one edge')
    cu.B()
    cu.R()
    cu.Bd()
    cu.Ld()
    cu.B()
    cu.Rd()
    cu.Bd()
    cu.L()
    return 1


def checkMatchingYellowCorners(cu):

    corners = cu.corner()
    num = 0
    list = [0, 0, 0, 0]
    # o-g edge
    check = 0
    if 'G' in corners[4]:
        check += 1
    if 'O' in corners[4]:
        check += 1
    if check == 2:
        num += 1
        list[0] = 4

    # o-b edge
    check = 0
    if 'B' in corners[5]:
        check += 1
    if 'O' in corners[5]:
        check += 1
    if check == 2:
        num += 1
        list[1] = 5

    # g-r edge
    check = 0
    if 'R' in corners[6]:
        check += 1
    if 'G' in corners[6]:
        check += 1
    if check == 2:
        num += 1
        list[2] = 6

    # r-b edge
    check = 0
    if 'B' in corners[7]:
        check += 1
    if 'R' in corners[7]:
        check += 1
    if check == 2:
        num += 1
        list[3] = 7

    list.append(num)
    return list


def alignYellowCorners_c2(cu, pos):
    if pos == 4:
        cu.Bd()

        cu.B()
        cu.R()
        cu.Bd()
        cu.Ld()
        cu.B()
        cu.Rd()
        cu.Bd()
        cu.L()

        cu.B()

    elif pos == 5:
        cu.B()
        cu.R()
        cu.Bd()
        cu.Ld()
        cu.B()
        cu.Rd()
        cu.Bd()
        cu.L()

    elif pos == 6:
        #print('6th case being executed')
        cu.Bd()
        cu.Bd()

        cu.B()
        cu.R()
        cu.Bd()
        cu.Ld()
        cu.B()
        cu.Rd()
        cu.Bd()
        cu.L()

        cu.B()
        cu.B()

    elif pos == 7:
        cu.B()

        cu.B()
        cu.R()
        cu.Bd()
        cu.Ld()
        cu.B()
        cu.Rd()
        cu.Bd()
        cu.L()

        cu.Bd()


# def corner5O(cu):

#     corners = cu.corner()
#     if (corners[5][0], corners[5][1], corners[5][2] == 'O', 'B', 'Y'):
#         return 1

#     cu.Rd()
#     cu.Fd()
#     cu.R()
#     cu.F()
#     cu.Rd()
#     cu.Fd()
#     cu.R()
#     cu.F()
#     return 0


# def corner7O(cu):
#     corners = cu.corner()
#     if (corners[7][0], corners[7][1], corners[7][2] == 'R', 'B', 'Y'):
#         return 1

#     cu.B()

#     cu.Rd()
#     cu.Fd()
#     cu.R()
#     cu.F()
#     cu.Rd()
#     cu.Fd()
#     cu.R()
#     cu.F()
#     return 0


# def corner6O(cu):
#     corners = cu.corners()
#     if (corners[6][0], corners[6][1], corners[6][2] == 'G', 'R', 'Y'):
#         return 1
def YellowCornersPerfectlyOriented(cu):
    check = 0
    list = [0, 0, 0, 0, 0]
    corners = cu.corner()
    #print(corners[5][0], corners[5][1], corners[5][2])
    if (corners[5][0] == 'O' and corners[5][1] == 'B' and corners[5][2] == 'Y'):
        check += 1
        list[1] = 5
    if (corners[6][0] == 'G' and corners[6][1] == 'R' and corners[6][2] == 'Y'):
        check += 1
        list[2] = 6
    if (corners[7][0] == 'R' and corners[7][1] == 'B' and corners[7][2] == 'Y'):
        check += 1
        list[3] = 7
    if (corners[4][0] == 'O' and corners[4][1] == 'G' and corners[4][2] == 'Y'):
        check += 1
        list[0] = 4

    list[4] = check
    return list


def corner5Orientation(cu):
    corners = cu.corner()
    #print("corner 5 = ", corners[5])
    if (corners[5][0] == 'O' and corners[5][1] == 'B' and corners[5][2] == 'Y'):
        #print('executed twice before leaving')
        cu.B()
        return 1

    cu.Rd()
    cu.Fd()
    cu.R()
    cu.F()
    return 0


def corner6Orientation(cu):
    corners = cu.corner()
    if (corners[5][0] == 'B' and corners[5][1] == 'R' and corners[5][2] == 'Y'):
        #print('executed twice thrice leaving')
        cu.B()
        return 1

    cu.Rd()
    cu.Fd()
    cu.R()
    cu.F()
    return 0


def corner7Orientation(cu):
    corners = cu.corner()
    if (corners[5][0] == 'R' and corners[5][1] == 'G' and corners[5][2] == 'Y'):
        #print('executed 4 times')
        cu.B()
        return 1

    cu.Rd()
    cu.Fd()
    cu.R()
    cu.F()
    return 0


def corner4Orientation(cu):
    corners = cu.corner()
    if (corners[5][0] == 'G' and corners[5][1] == 'O' and corners[5][2] == 'Y'):
        cu.B()
        return 1

    cu.Rd()
    cu.Fd()
    cu.R()
    cu.F()
    return 0


def checkFirstLayer(cu):
    check = 0
    if cu.a == ['W', 'O', 'G']:
        check += 1
    if cu.b == ['W', 'O']:
        check += 1
    if cu.c == ['W', 'O', 'B']:
        check += 1
    if cu.d == ['W', 'G']:
        check += 1
    if cu.e == ['W']:
        check += 1
    if cu.f == ['W', 'B']:
        check += 1
    if cu.g == ['W', 'G', 'R']:
        check += 1
    if cu.h == ['W', 'R']:
        check += 1
    if cu.i == ['W', 'R', 'B']:
        check += 1

    return check


def cubeSolvedChecker(cu):
    check = 0
    if cu.a == ['W', 'O', 'G']:
        check += 1
    if cu.b == ['W', 'O']:
        check += 1
    if cu.c == ['W', 'O', 'B']:
        check += 1
    if cu.d == ['W', 'G']:
        check += 1
    if cu.e == ['W']:
        check += 1
    if cu.f == ['W', 'B']:
        check += 1
    if cu.g == ['W', 'G', 'R']:
        check += 1
    if cu.h == ['W', 'R']:
        check += 1
    if cu.i == ['W', 'R', 'B']:
        check += 1
    if cu.j == ['O', 'G']:
        check += 1
    if cu.k == ['O']:
        check += 1
    if cu.l == ['O', 'B']:
        check += 1
    if cu.m == ['G']:
        check += 1
    if cu.n == ['B']:
        check += 1
    if cu.o == ['G', 'R']:
        check += 1
    if cu.p == ['R']:
        check += 1
    if cu.q == ['R', 'B']:
        check += 1
    if cu.r == ['O', 'G', 'Y']:
        check += 1
    if cu.s == ['O', 'Y']:
        check += 1
    if cu.t == ['O', 'B', 'Y']:
        check += 1
    if cu.u == ['G', 'Y']:
        check += 1
    if cu.v == ['Y']:
        check += 1
    if cu.w == ['B', 'Y']:
        check += 1
    if cu.x == ['G', 'R', 'Y']:
        check += 1
    if cu.y == ['R', 'Y']:
        check += 1
    if cu.z == ['R', 'B', 'Y']:
        check += 1

    return check


cu = cube()
# scramble_cube(cu)
cu.acceptCube(cu)
strt = datetime.now()
disp(cu)

# # for o-w
edgeList = findWhiteEdges(cu)
white_orange(cu, edgeList)
white_orange_orientation(cu)

# for w-g
edgeList = findWhiteEdges(cu)
white_green(cu, edgeList)
white_green_orientation(cu)

# for w-b
edgeList = findWhiteEdges(cu)
white_blue(cu, edgeList)
white_blue_orientation(cu)

# for w-r
edgeList = findWhiteEdges(cu)
white_red(cu, edgeList)
white_red_orientation(cu)

# for o-g corner piece
cornerList = findWhiteCorners(cu)
orange_green_corner(cu, cornerList)
orange_green_CO(cu)

# for 0-b corner piece
cornerList = findWhiteCorners(cu)
orange_blue_corner(cu, cornerList)
orange_blue_CO(cu)

# for g-r corner piece
cornerList = findWhiteCorners(cu)
green_red_corner(cu, cornerList)
green_red_CO(cu)

# for r-b piece
cornerList = findWhiteCorners(cu)
red_blue_corner(cu, cornerList)
red_blue_CO(cu)
# disp(cu)

cFL = checkFirstLayer(cu)
if cFL == 9:
    print('\nFIRST layer successfully solved')
    #solution.append('FIRST LAYER DONE')
    s1 = solution.copy()
    solution.clear()

else:
    print('First layer not solved\nWrong pieces = ', 9-cFL)


# second layer

# fidning the second layer edges
fSLE = findSecondLayerEdges(cu)
# print(fSLE)
secondLayerO_G(cu, fSLE)
secondLayerO_G_orientation(cu)

fSLE = findSecondLayerEdges(cu)
secondLayerO_B(cu, fSLE)
secondLayerO_B_orientation(cu)

fSLE = findSecondLayerEdges(cu)
secondLayerG_R(cu, fSLE)
secondLayerG_R_orientation(cu)

fSLE = findSecondLayerEdges(cu)
secondLayerR_B(cu, fSLE)
secondLayerR_B_orientation(cu)

cSl = checkSecondLayer(cu)
if cSl == 8:
    print('\nSECOND Layer successfully solved')
    #solution.append('SECOND LAYER DONE')
    s2 = solution.copy()
    solution.clear()
else:
    print('second layer remains unsolved\nwrong pieces = ', 8-cSl)
# yellow cross


cRMYC = checkReadyMadeYellowCross(cu)

#print('cRMYC = ', cRMYC)
if cRMYC != 1:
    yellow_cross_C1(cu)
    yellow_cross_c2(cu)
    yellow_cross_c3(cu)


# yellow edges

rotate = 0
cMYEWC = 0

while(rotate < 4):
    #print('enterd into edge checking')
    cMYEWC = checkMatchingYellowEdgesWithcenter(cu)
    if cMYEWC == 1:
        break
    cu.B()
    rotate += 1


if cMYEWC != 1:

    yellowEdges_c1(cu)
    cc = 1
    while(cc == 1):
        #print('while loop 1')
        cc = yellow_edges_c2(cu)

    ccd = 1
    while(ccd == 1):
        ccd = yellow_edges_c3(cu)
        #print("while loop 2")


# yellow corners alignment
mm = checkMatchingYellowCorners(cu)
# print(mm)

if mm[4] != 4:
    #print("Entered mm if loop")
    pos = alignYellowCorners_c1(cu)
    #print('1st pos = ', pos)
    # print('displaying cube after pos\n')
    # disp(cu)

    while(pos == 1):
       # print("while loop 3")
        pos = alignYellowCorners_c1(cu)
        #print("new pos = ", pos)

    zz = [0, 0, 0, 0, 0]
    while (zz[4] != 4):
        alignYellowCorners_c2(cu, pos)
        zz = checkMatchingYellowCorners(cu)  # check this throughly
        # print(zz)


#print('displaying cube after aligning corners\n')
# disp(cu)

# yellow corners orientation
cPO = YellowCornersPerfectlyOriented(cu)
#print('cPO=', cPO)

if cPO[4] != 4:
    jj = 0
    while(jj == 0):
        jj = corner5Orientation(cu)
        #print("while loop 5")

    kk = 0
    while(kk == 0):
        kk = corner6Orientation(cu)
        #print("while loop 6")

    tt = 0
    while(tt == 0):
        tt = corner7Orientation(cu)
        #print("while loop 7")

    yy = 0
    while(yy == 0):
        yy = corner4Orientation(cu)
        #print("while loop 8")

cSC = cubeSolvedChecker(cu)
if cSC == 26:
    end = datetime.now()
    print('\nTHIRD layer successfully solved\n\nCube solved in ', end-strt, 'second')
    #solution.append('THIRD LAYER DONE')
    # disp(cu)
    s3 = solution.copy()
    solution.clear()

if cSC == 26:
    while True:
        s = input(
            '\nShow solution : Y\nShow Detailed Solution : D\nQuit : Q \nEnter Choice : ')
        if s == 'y' or s == 'Y':
            # time.sleep(1)
            # for i in solution:
            #     print(i)
            #     time.sleep(1)
            # print(solution)
            print('\n---------------------------------------------------------------FIRST LAYER------------------------------------------------------------\n\n', s1)
            print('\n---------------------------------------------------------------SECOND LAYER------------------------------------------------------------\n\n', s2)
            print('\n---------------------------------------------------------------THIRD LAYER-------------------------------------------------------------\n\n', s3, '\n')
        elif s == 'd' or s == 'D':

            count_s1 = len(s1)
            i = 0

            print("\nPlease follow the following ", count_s1,
                  " instruction displayed carefully to solve the first layer of the rubiks cube: \n")
            while(i < count_s1):
                print("step ", i+1, ": ", end=" ")
                if s1[i] == 'F':
                    print(' FRONT Face ClockWise\n')
                elif s1[i] == 'Fd':
                    print('FRONT Counter-ClockWise\n')
                elif s1[i] == 'R':
                    print('RIGHT ClockWise\n')
                elif s1[i] == 'Rd':
                    print('RIGHT Counter-ClockWise\n')
                elif s1[i] == 'L':
                    print('LEFT ClockWise\n')
                elif s1[i] == 'Ld':
                    print('LEFT Counter-ClockWise\n')
                elif s1[i] == 'U':
                    print('UPPER ClockWise\n')
                elif s1[i] == 'Ud':
                    print('UPPER Counter-ClockWise\n')
                elif s1[i] == 'B':
                    print('BACK ClockWise\n')
                elif s1[i] == 'Bd':
                    print('BACK Counter-ClockWise\n')
                elif s1[i] == 'D':
                    print('DOWN ClockWise\n')
                elif s1[i] == 'Dd':
                    print('DOWN Counter-ClockWise\n')

                while True:
                    time.sleep(0.5)
                    a = keyboard.read_key()
                    if str(a) == "enter":
                        break
                i += 1

        elif s == 'q' or 'Q':
            break
