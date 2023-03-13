from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from math import *

#Inicializace 'Ray crossing' algoritmu

class Ray_crossing:
    def __init__(self):
        pass

    def setLocalCoordinates(self, p: QPoint, q: QPoint):

        #Výpočet souřadníc bodu
        x = p.x() - q.x()
        y = p.y() - q.y()

        #Nové souřadnice bodu
        p_shifted = QPoint(x, y)

        return p_shifted

    #Analýza křížení linií v horní polorovině
    def getCrossingStatusU(self, p1: QPoint, p2: QPoint):
        if (p1.y() > 0) != (p2.y() > 0):
            return True
        return False

    #Analýza křížení linií ve spodní polorovině
    def getCrossingStatusL(self, p1: QPoint, p2: QPoint):
        if (p1.y() < 0) != (p2.y() < 0):
            return True
        return False

#Počet křížení mezi Q-ray a hranami polygonu
    def getPositionPointAndPolygon(self, q: QPoint, pol: QPolygon):
        k_r = 0
        k_l = 0
        n = len(pol)

        #Změna souřadníc bodů na lokální souřadnice
        for i in range(n):
            p1 = self.setLocalCoordinates(pol[(i + 1) % n], q)  # p[i]
            p2 = self.setLocalCoordinates(pol[i], q)  # p[i-1]

            #Pokud je bod na vrcholu
            epsilon = 1.0e-10
            if abs(0 - p1.x()) < epsilon and abs(0 - p1.y()) < epsilon:
                return 1

            #Křížení v pravé polorovině
            if self.getCrossingStatusU(p1, p2):
                x_m = (p1.x() * p2.y() - p2.x() * p1.y()) / (p1.y() - p2.y())

                #Součet křížení
                if x_m > 0:
                    k_r += 1

            #Křížení v levé polorovině
            if self.getCrossingStatusL(p1, p2):
                x_m = (p1.x() * p2.y() - p2.x() * p1.y()) / (p1.y() - p2.y())

                #Součet křížení
                if x_m < 0:
                    k_l += 1


        #Pokud je bod na hraně polygonu
        if k_l % 2 != k_r % 2:
            return 1

        #Pokud je bod uvnitř polygonu
        elif k_r % 2 == 1:
            return 1

        #Pokud je bod mimo polygon
        else:
            return 0



#Inicializace 'Winding number' algoritmu

class Winding_number:
    def __init__(self):
        pass

    def getPointAndLinePosition(self, a: QPoint, p1: QPoint, p2: QPoint):
        #Analýza bodu a přímky
        eps = 1.0e-10

        #Souřadnice
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y()
        vx = a.x() - p1.x()
        vy = a.y() - p1.y()

        #Determinant
        t = ux * vy - vx * uy

        #Pokud se bod nachází v levé polorovině
        if t > eps:
            return 1

        #Pokud se bod nachází v pravé polorovině
        if t < -eps:
            return 0

        #Kolineární bod
        return -1


#Počítání úhlů mezi přímkami
    def get2LinesAngle(self, p1: QPoint, p2: QPoint, p3: QPoint, p4: QPoint):
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y()
        vx = p4.x() - p3.x()
        vy = p4.y() - p3.y()

        #Skalární součin vektorů
        uv = ux * vx + uy * vy

        #Normy vektorů
        nu = (ux ** 2 + uy ** 2) ** 0.5
        nv = (vx ** 2 + vy ** 2) ** 0.5

        #Pokud se bod nachází na vrcholu (norma jednoho z vektorů je rovna 0)
        if nu * nv == 0:
            return 0

        #Odtranění zaokrouhlení
        try:
            return abs(acos(uv / (nu * nv)))
        except:
            return 0


#Analýza pozice bodu vůči polygonu
    def getPositionPointAndPolygon(self, q: QPoint, pol: QPolygon) -> int:

        n = len(pol)
        omega_sum = 0

        #Smyčka v uzlech
        for i in range(n):

            #Pozice  q, pi, pi+1
            pos = self.getPointAndLinePosition(q, pol[i], pol[(i + 1) % n])

            #Úhel q, pi, pi+1
            omega = self.get2LinesAngle(q, pol[i], q, pol[(i + 1) % n])


            #Winding number
            if pos == 1:

                #Pro bod v levé polorovině
                omega_sum += omega

            elif pos == 0:
                #Pro bod v pravé polorovině
                omega_sum -= omega

            else:
                #Bod je kolineární
                x_check = (q.x() - pol[i].x()) * (q.x() - pol[(i + 1) % n].x())
                y_check = (q.y() - pol[i].y()) * (q.y() - pol[(i + 1) % n].y())

                if x_check <= 0 and y_check <= 0:
                    return 1


        #Počáteční bod uvnitř polygonu
        epsilon = 1.0e-10

        if abs(abs(omega_sum) - 2 * pi) < epsilon:
            return 1

        #Počáteční bod mimo polygon
        return 0





