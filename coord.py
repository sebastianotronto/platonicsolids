#!/usr/bin/python

from math import sqrt, sin, cos

phi = (1.0+sqrt(5.0))/2.0

def projcoord(P, alpha, beta):
	x, y, z = P
	xnew =  x*cos(alpha) + y*sin(alpha)
	ynew =  x*sin(alpha)*sin(beta) - y*cos(alpha)*sin(beta) + z*cos(beta)
	return xnew, ynew

def printtikz(shape, alpha, beta):
	for i in range(len(shape)):
		x, y = projcoord(shape[i], alpha, beta)
		print("\coordinate (P" + str(i) + ") at (" + str(x) + ", " + str(y) + ");")

tetrahedron = [(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)]

octahedron =  [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

cube =	[(1,1,1), (1,1,-1), (1,-1,1), (1,-1,-1), (-1,1,1), (-1,1,-1), (-1,-1,1), (-1,-1,-1)]

dodecahedron = cube + [(0,1/phi,phi), (0,1/phi,-phi), (0,-1/phi,phi), (0,-1/phi,-phi),
		       (1/phi,phi,0), (1/phi,-phi,0), (-1/phi,phi,0), (-1/phi,-phi,0),
		       (phi,0,1/phi), (-phi,0,1/phi), (phi,0,-1/phi), (-phi,0,-1/phi)]

icosahedron = [(0,1,phi), (0,1,-phi), (0,-1,phi), (0,-1,-phi),
	       (1,phi,0), (1,-phi,0), (-1,phi,0), (-1,-phi,0),
	       (phi,0,1), (-phi,0,1), (phi,0,-1), (-phi,0,-1)]

printtikz(icosahedron, 0.2, 0.2)
