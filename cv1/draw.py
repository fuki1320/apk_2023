from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class Draw(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.q = QPoint()
        self.polygons = []
        self.res = []

    # Poloha kurzoru
    def mousePressEvent(self, e: QMouseEvent):
        x = int(e.position().x())
        y = int(e.position().y())

        #Vytvoření nového bodu
        self.q.setX(x)
        self.q.setY(y)

        self.repaint()

    # Vytvoření nového objektu
    def paintEvent(self, e: QPaintEvent):
        qp = QPainter(self)

        #Kreslení polygonu
        i = 0
        for pol in self.polygons:
            qp.begin(self)

            # Nastavení pera uvnitř polygonu
            if len(self.res) > 0 and self.res[i] == 1:
                qp.setPen(Qt.GlobalColor.green)
                qp.setBrush(Qt.GlobalColor.magenta)
            else:
                ##Nastavení pera mimo polygon
                qp.setPen(Qt.GlobalColor.green)
                qp.setBrush(Qt.GlobalColor.darkCyan)

            qp.drawPolygon(pol)
            i += 1
            qp.end()

        qp.begin(self)

        #Nastavení pera pro vykreslení bodu
        qp.setPen(Qt.GlobalColor.black)
        qp.setBrush(Qt.GlobalColor.darkRed)

        #Elipsa
        r = 3
        qp.drawEllipse(self.q.x() - r, self.q.y() - r, 2 * r, 2 * r)
        qp.end()

    def getQ(self):
        return self.q

    def getPolygons(self):
        return self.polygons