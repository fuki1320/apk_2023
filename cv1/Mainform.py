from draw import Draw
from algorithm import *
from input import *
from PyQt6 import QtCore, QtWidgets



 class Ui_MainForm(object):
  def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainForm)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Canvas = Draw(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding
        QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Canvas.sizePolicy().hasHeightForWidth())
        self.Canvas.setSizePolicy(sizePolicy)
        self.Canvas.setObjectName("Canvas")
        self.horizontalLayout.addWidget(self.Canvas)
        MainForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuDraw = QtWidgets.QMenu(self.menubar)
        self.menuDraw.setObjectName("menuDraw")
        self.menuAnalyze = QtWidgets.QMenu(self.menubar)
        self.menuAnalyze.setObjectName("menuAnalyze")
        MainForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainForm)
        self.statusbar.setObjectName("statusbar")
        MainForm.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainForm)
        self.toolBar.setObjectName("toolBar")
        MainForm.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(MainForm)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/open_file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtGui.QAction(MainForm)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        self.actionPoint_Polygon = QtGui.QAction(MainForm)
        self.actionPoint_Polygon.setCheckable(True)
        self.actionPoint_Polygon.setChecked(True)
        self.actionPoint_Polygon.setObjectName("actionPoint_Polygon")
        self.actionClear = QtGui.QAction(MainForm)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/clear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear.setIcon(icon2)
        self.actionClear.setObjectName("actionClear")
        self.actionPoint_and_polygon_position = QtGui.QAction(MainForm)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/polygon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPoint_and_polygon_position.setIcon(icon3)
        self.actionPoint_and_polygon_position.setObjectName("actionPoint_and_polygon_position")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuDraw.addAction(self.actionPoint_Polygon)
        self.menuDraw.addAction(self.actionClear)
        self.menuAnalyze.addAction(self.actionPoint_and_polygon_position)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDraw.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPoint_and_polygon_position)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        #Propojení menu s funkcionalitou
        self.actionPoint_Polygon.triggered.connect(self.switchSourceClick)
        self.actionPoint_and_polygon_position.triggered.connect(self.analyzeClick)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Point and polygon position"))
        self.menuFile.setTitle(_translate("MainForm", "File"))
        self.menuDraw.setTitle(_translate("MainForm", "Draw"))
        self.menuAnalyze.setTitle(_translate("MainForm", "Analyze"))
        self.toolBar.setWindowTitle(_translate("MainForm", "toolBar"))
        self.actionOpen.setText(_translate("MainForm", "Open"))
        self.actionExit.setText(_translate("MainForm", "Exit"))
        self.actionPoint_Polygon.setItemText(0, _translate("MainForm", "Winding number"))
        self.actionPoint_Polygon.setItemText(1, _translate("MainForm", "Ray crossing"))
        self.actionClear.setText(_translate("MainForm", "Clear"))
        self.actionPoint_and_polygon_position.setText(_translate("MainForm", "Point and polygon position"))
        self.actionPoint_and_polygon_position.setShortcut(_translate("MainForm", "Ctrl+A"))

    def selectfile(self):
        self.Canvas.res = []
        w = self.Canvas.frameGeometry().width()
        h = self.Canvas.frameGeometry().height()
        self.Canvas.polygons = Input().loadFile(w, h)
        self.Canvas.repaint()

    def analyse(self):
        q = self.Canvas.getQ()
        polygons = self.Canvas.getPolygons()
        self.Canvas.res = []

        if self.comboBox.currentIndex() == 0:
            a = Winding_number()
        else:
            a = Ray_crossing()

        for pol in polygons:
            res = a.getPositionPointAndPolygon(q, pol)
            self.Canvas.res.append(res)

        self.Canvas.repaint()

    def clear(self):
        self.Canvas.polygons = []
        self.Canvas.res = []
        self.Canvas.q = QPoint()
        self.Canvas.repaint()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QWidget()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec())
