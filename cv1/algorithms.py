from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from math import sqrt, acos, pi

class Algorithms:
    def __init__(self):
        pass

    def getPointAndEdgePosition(self, q, p1: QPointF, p2: QPointF):
        # compute vectors
        u_x = q.x() - p1.x()
        u_y = q.y() - p1.y()
        v_x = p2.x() - p1.x()
        v_y = p2.y() - p1.y()

        # compute determinant
        d = (u_x * v_y) - (v_x * u_y)

        # determine point and edge position
        # point in left halfplane
        if d > 0:
            return 1

        # point in right halfplace
        elif d < 0:
            return 0

        # colinear point
        return -1

    def getAngle(self, q, p1: QPointF, p2: QPointF):
        # compute vectors
        u_x = p1.x() - q.x()
        u_y = p1.y() - q.y()
        v_x = p2.x() - q.x()
        v_y = p2.y() - q.y()

        # compute the scalar product of vectors
        uv = u_x * v_x + u_y * v_y

        # compute the norms of vectors
        norm_u = sqrt(u_x**2 + u_y**2)
        norm_v = sqrt(v_x ** 2 + v_y ** 2)

        # point is the same as a vertex
        if norm_u == 0 or norm_v == 0:
            return 0

        # round down to 1 if greater
        if uv / (norm_u * norm_v) > 1:
            return abs(acos(1))

        # round up to -1 if smaller
        elif uv / (norm_u * norm_v) < -1:
            return abs(acos(-1))

        # return angle
        return abs(acos(uv / (norm_u * norm_v)))

    def windingNumber(self, q, pol):
        # initialize sum of omega angle and tolerance
        omega_sum = 0
        epsilon = 1.0e-10

        # loop through polygon
        for i in range(len(pol)-1):
            # check if the coordinates of the point and the vertex are same
            if pol[i].x() == q.x() and pol[i].y() == q.y():
                # point lies on the vertex
                return -1

            # get position of point and edge
            pos = self.getPointAndEdgePosition(q, pol[i], pol[i+1])

            # get angle between point and vertices of the edge
            omega = self.getAngle(q, pol[i], pol[i+1])

            # point in left halfplane
            if pos == 1:
                omega_sum += omega

            # point in right halfplane
            if pos == 0:
                omega_sum -= omega

            # colinear point - it lies between the nodes
            elif (pol[i].x() - q.x()) * (pol[i+1].x() - q.x()) <= 0 and (pol[i].y() - q.y()) * (pol[i+1].y() - q.y()) <= 0:
                # point lies on the edge
                return -1

        # point is inside
        if abs(abs(omega_sum) - 2*pi) < epsilon:
            return 1

        # point is outside
        return 0

    def rayCrossing(self, q, pol):
        # initialize number of left and right intersections and number of vertices
        kl = 0
        kr = 0
        n = len(pol)

        # process all vertices
        for i in range(n):
            # reducing of coordinates
            xi = pol[i].x() - q.x()  # i-tý bod
            yi = pol[i].y() - q.y()
            xi1 = pol[(i + 1) % n].x() - q.x()
            yi1 = pol[(i + 1) % n].y() - q.y()

            # point is vertex
            if xi == 0 and yi == 0:
                return -1

            # computing of intersection
            if (yi1 - yi) == 0:
                continue
            else:
                xm = (xi1 * yi - xi * yi1) / (yi1 - yi)

            # looking for a suitable segment
            # right ray
            if (yi > 0) != (yi1 > 0) and xm > 0:
                kr += 1

            # left ray
            elif (yi < 0) != (yi1 < 0) and xm < 0:
                kl += 1

            # point is on boundary of polygon
        if (kr % 2) != (kl % 2):
            print("tut")
            return -1

            # point is inside polygon
        if (kr % 2) == 1:
            return 1
            # point is outside
        return 0
