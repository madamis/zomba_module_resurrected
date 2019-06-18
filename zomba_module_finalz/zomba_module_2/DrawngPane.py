import psycopg2
import osgeo.ogr
import shapely
import shapely.wkt
#import geopandas as gpd
import sys, math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout
from shapely.geometry import Polygon


class Bord(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setLayout(QVBoxLayout())
        self.resize(200,400)
        self.pen = QtGui.QPen(QtGui.QColor(0,0,0))                      # set lineColor
        self.pen.setWidth(3)                                            # set lineWidth
        self.brush = QtGui.QBrush(QtGui.QColor(55,55,55,55))        # set fillColor
        #self.polygon = self.developers()
        #canvas = QgsMapCanvas()# polygon with n points, radius, angle of the first point

    def developers(self):
        try:
            connection = psycopg2.connect(user='postgres', password='12345678', host='localhost', port='5432',
                                          database='zomba_malawi')
            cursor = connection.cursor()
            query = """SELECT plot_number, st_astext((ST_Dump(ST_Force2D(ST_SetSRID(geom,4326)))).geom) AS geom FROM finale_plot where plot_number = 10101;"""
            cursor.execute(query)
            polygon = QtGui.QPolygon()
            rows_list = []
            for c in cursor:
                data = {'code':c[0],'geom':c[1]}
                rows_list.append(data)
            #gdf = gpd.GeoDataFrame(rows_list, crs='epsg:4326').set_index('code')
            #gdf.head()
            print(rows_list)


        except(Exception, psycopg2.Error) as error:
            if (connection):
                print('faileed to connect', error)
        finally:
            '''closing database connection'''
            if (connection):
                cursor.close()
                connection.close()
                print("psql is closed")

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        print(self.polygon)
        painter.drawPolygon(self.polygon)
