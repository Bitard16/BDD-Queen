from pyeda.boolalg import *
from pyeda.inter import *


import graphviz as gv
from graphviz import Source
from graphviz.dot import *



import matplotlib 
print ("N queens problem solver with bdd visualisation on python")
print ("Put data of razmer doski" )
# Сделать королев с безграничными досками и визуализировать BDD
#rd = int(input())
X = exprvars('x', 8, 8)
R = And(*[OneHot(*[X[r,c] for c in range(8)]) for r in range(8)])
C = And(*[OneHot(*[X[r,c] for r in range(8)]) for c in range(8)])
starts = [(i, 0) for i in range(8-2, 0, -1)] + [(0, i) for i in range(8-1)]
lrdiags = []
for r,c in starts:
    lrdiags.append([])
    ri,ci = r,c
    while ri < 8 and ci < 8:
        lrdiags[-1].append((ri,ci))
        ri += 1
        ci += 1
DLR = And(*[OneHot0(*[X[r,c] for r, c in diag]) for diag in lrdiags])
starts = [(i, 8-1) for i in range(8-2, -1, -1)] + [(0, i) for i in range(8-2, 0, -1)]
rldiags = []
for r, c in starts:
    rldiags.append([])
    ri, ci = r, c
    while ri < 8 and ci >= 0:
        rldiags[-1].append((ri, ci))
        ri += 1
        ci -= 1
DRL = And(*[OneHot0(*[X[r,c] for r, c in diag]) for diag in rldiags])
# BDD Visualisation

S = R & C & DLR & DRL 
#R,C,DLR,DRL = map(bddvar,'RCDLRDRL')
#gv = Source(S.to_dot())
#gv.render('render_pdf_name',view=True)
print (S.to_dot())



def display(point):
     chars = list()
     for r in range(8):
         for c in range(8):
             if point[X[r,c]]:
                 chars.append("Q")
             else:
                 chars.append(".")
         if r != 7:
             chars.append("\n")
     print("".join(chars))
print(display(S.satisfy_one()))
for i, soln in enumerate(S.satisfy_all()):
    print("Solution", i+1, end="\n\n")
    display(soln)
    print("")
print(S.satisfy_count())
print(len(list(S.satisfy_all())))

    
    


