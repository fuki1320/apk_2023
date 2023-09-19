from draw import Draw
from algorithms import *
from PyQt6 import QtCore, QtWidgets


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(963, 537)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MainForm)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Canvas = Draw(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Canvas.sizePolicy().hasHeightForWidth())
        self.Canvas.setSizePolicy(sizePolicy)
        self.Canvas.setObjectName("Canvas")
        self.horizontalLayout.addWidget(self.Canvas)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(MainForm)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.comboBox = QtWidgets.QComboBox(MainForm)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(MainForm)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(MainForm)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(MainForm)
        self.pushButton_3.clicked.connect(self.openFile)
        self.pushButton.clicked.connect(self.analyse)
        self.pushButton_2.clicked.connect(self.clear)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "MainForm"))
        self.pushButton_3.setText(_translate("MainForm", "Select File"))
        self.comboBox.setItemText(0, _translate("MainForm", "Winding number"))
        self.comboBox.setItemText(1, _translate("MainForm", "Ray crossing"))
        self.pushButton.setText(_translate("MainForm", "Analyse"))
        self.pushButton_2.setText(_translate("MainForm", "Clear"))

    def openFile(self):
        width = self.Canvas.frameSize().width()
        height = self.Canvas.frameSize().height()
        self.Canvas.loadData()
        self.Canvas.rescaleData(width, height)

    def analyse(self):
        q = self.Canvas.getPoint()
        polygons = self.Canvas.getPolygons()

        # analyze position
        a = Algorithms()

        for index, pol in enumerate(polygons):
            if self.comboBox.currentIndex() == 0:
                result = a.windingNumber(q, pol)
                self.Canvas.setResult(result)
            if self.comboBox.currentIndex() == 1:
                result = a.rayCrossing(q, pol)
                self.Canvas.setResult(result)

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
