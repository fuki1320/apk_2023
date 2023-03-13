from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from math import *
import shapefile


class Input():
    def __init__(self):
        self.polygons = []
        pass

    def loadFile(self, w, h):
        path = QFileDialog.getOpenFileName(None, "Select Shapefile", "", "SHP files (*.shp)")[0]

        if path == '':
            return self.polygons

        #Otevření shp
        with shapefile.Reader(path) as shp:
            features = shp.shapes()

        #Min a max souřadnice
        min_x = inf
        max_x = -inf
        min_y = inf
        max_y = -inf

        #Úprava polygonu
        polygons_jtsk = []
        for pol_shp in features:
            #Souřadnice polygonu
            pol = QPolygon()
            pol_coords = pol_shp.points

            #Uložení vrcholů polygonu jako QPoint
            for vertex in pol_coords[:-1]:

                q_point = QPoint()
                x = int(vertex[0])
                y = int(vertex[1])
                q_point.setX(x)
                q_point.setY(y)
                pol.append(q_point)

                if x < min_x:
                    min_x = x
                if y < min_y:
                    min_y = y
                if x > max_x:
                    max_x = x
                if y > max_y:
                    max_y = y

            #Přidání polygonů do seznamu jako QPolygons
            polygons_jtsk.append(pol)

        #Dimenze
        x_dim = max_x - min_x
        y_dim = max_y - min_y

        #Výpočet měřítka dle delší strany
        window_size_x = w
        window_size_y = h

        if window_size_x / window_size_y < x_dim / y_dim:
            scale = window_size_x / x_dim
            y_d = window_size_y * (window_size_x / x_dim) / (window_size_y / y_dim)
        else:
            scale = window_size_y / y_dim
            y_d = window_size_y

        #Transformace polygonu
        for pol in polygons_jtsk:
            transformed_pol = QPolygon()
            for point in pol:
                new_point = QPoint()
                new_point.setX(int((point.x() - min_x) * scale))
                new_point.setY(int(y_d - (point.y() - min_y) * scale))
                transformed_pol.append(new_point)
            self.polygons.append(transformed_pol)

        return self.polygons
