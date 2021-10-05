# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NeewerLightUIzTWPrP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(590, 521)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tryConnectButton = QPushButton(self.centralwidget)
        self.tryConnectButton.setObjectName(u"tryConnectButton")
        self.tryConnectButton.setEnabled(False)
        self.tryConnectButton.setGeometry(QRect(500, 4, 81, 22))
        self.ColorModeTabWidget = QTabWidget(self.centralwidget)
        self.ColorModeTabWidget.setObjectName(u"ColorModeTabWidget")
        self.ColorModeTabWidget.setGeometry(QRect(10, 300, 571, 201))
        self.CCT = QWidget()
        self.CCT.setObjectName(u"CCT")
        self.Slider_CCT_Hue = QSlider(self.CCT)
        self.Slider_CCT_Hue.setObjectName(u"Slider_CCT_Hue")
        self.Slider_CCT_Hue.setGeometry(QRect(10, 20, 551, 16))
        self.Slider_CCT_Hue.setMinimum(32)
        self.Slider_CCT_Hue.setMaximum(85)
        self.Slider_CCT_Hue.setValue(56)
        self.Slider_CCT_Hue.setOrientation(Qt.Horizontal)
        self.TFL_CCT_Hue = QLabel(self.CCT)
        self.TFL_CCT_Hue.setObjectName(u"TFL_CCT_Hue")
        self.TFL_CCT_Hue.setGeometry(QRect(10, 40, 440, 17))
        self.TFV_CCT_Hue = QLabel(self.CCT)
        self.TFV_CCT_Hue.setObjectName(u"TFV_CCT_Hue")
        self.TFV_CCT_Hue.setGeometry(QRect(510, 40, 51, 20))
        self.TFV_CCT_Hue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.TFV_CCT_Bright = QLabel(self.CCT)
        self.TFV_CCT_Bright.setObjectName(u"TFV_CCT_Bright")
        self.TFV_CCT_Bright.setGeometry(QRect(510, 90, 51, 20))
        self.TFV_CCT_Bright.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.TFL_CCT_Bright = QLabel(self.CCT)
        self.TFL_CCT_Bright.setObjectName(u"TFL_CCT_Bright")
        self.TFL_CCT_Bright.setGeometry(QRect(10, 90, 440, 17))
        self.Slider_CCT_Bright = QSlider(self.CCT)
        self.Slider_CCT_Bright.setObjectName(u"Slider_CCT_Bright")
        self.Slider_CCT_Bright.setGeometry(QRect(10, 70, 551, 16))
        self.Slider_CCT_Bright.setMaximum(100)
        self.Slider_CCT_Bright.setValue(100)
        self.Slider_CCT_Bright.setOrientation(Qt.Horizontal)

        # DRAW THE LINEAR GRADIENT TO INDICATE THE COLOR TEMPERATURE VALUE IN THE CCT TAB
        mySceneCCT = QGraphicsScene(self)

        gradient = QLinearGradient(0, 0, 532, 31)
        gradient.setColorAt(0.0, QColor(255, 187, 120, 255))
        gradient.setColorAt(0.16, QColor(255, 209, 163, 255))
        gradient.setColorAt(0.33, QColor(255, 227, 202, 255))
        gradient.setColorAt(0.49, QColor(255, 240, 233, 255))
        gradient.setColorAt(0.66, QColor(252, 247, 255, 255))
        gradient.setColorAt(0.83, QColor(233, 237, 255, 255))
        gradient.setColorAt(1.0, QColor(221, 230, 255, 255))
    
        mySceneCCT.setBackgroundBrush(gradient)
        
        self.CCT_Temp_Gradient_BG = QGraphicsView(mySceneCCT, self.CCT)        
        self.CCT_Temp_Gradient_BG.setObjectName(u"CCT_Temp_Gradient_BG")
        self.CCT_Temp_Gradient_BG.setGeometry(QRect(9, 10, 552, 31))
        self.CCT_Temp_Gradient_BG.setFrameShape(QFrame.NoFrame)
        self.CCT_Temp_Gradient_BG.setFrameShadow(QFrame.Sunken)
        self.CCT_Temp_Gradient_BG.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.ColorModeTabWidget.addTab(self.CCT, "")
        self.CCT_Temp_Gradient_BG.raise_()
        self.TFL_CCT_Hue.raise_()
        self.TFV_CCT_Hue.raise_()
        self.TFV_CCT_Bright.raise_()
        self.TFL_CCT_Bright.raise_()
        self.Slider_CCT_Bright.raise_()
        self.Slider_CCT_Hue.raise_()
        self.HSL = QWidget()
        self.HSL.setObjectName(u"HSL")
        self.TFV_HSL_1_H = QLabel(self.HSL)
        self.TFV_HSL_1_H.setObjectName(u"TFV_HSL_1_H")
        self.TFV_HSL_1_H.setGeometry(QRect(510, 40, 51, 20))
        self.TFV_HSL_1_H.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Slider_HSL_2_S = QSlider(self.HSL)
        self.Slider_HSL_2_S.setObjectName(u"Slider_HSL_2_S")
        self.Slider_HSL_2_S.setGeometry(QRect(10, 70, 551, 16))
        self.Slider_HSL_2_S.setMaximum(100)
        self.Slider_HSL_2_S.setValue(100)
        self.Slider_HSL_2_S.setOrientation(Qt.Horizontal)
        self.TFV_HSL_2_S = QLabel(self.HSL)
        self.TFV_HSL_2_S.setObjectName(u"TFV_HSL_2_S")
        self.TFV_HSL_2_S.setGeometry(QRect(510, 90, 51, 20))
        self.TFV_HSL_2_S.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.TFL_HSL_2_S = QLabel(self.HSL)
        self.TFL_HSL_2_S.setObjectName(u"TFL_HSL_2_S")
        self.TFL_HSL_2_S.setGeometry(QRect(10, 90, 440, 17))
        self.TFL_HSL_1_H = QLabel(self.HSL)
        self.TFL_HSL_1_H.setObjectName(u"TFL_HSL_1_H")
        self.TFL_HSL_1_H.setGeometry(QRect(10, 40, 440, 17))
        self.Slider_HSL_1_H = QSlider(self.HSL)
        self.Slider_HSL_1_H.setObjectName(u"Slider_HSL_1_H")
        self.Slider_HSL_1_H.setGeometry(QRect(10, 20, 551, 16))
        self.Slider_HSL_1_H.setMaximum(360)
        self.Slider_HSL_1_H.setValue(240)
        self.Slider_HSL_1_H.setOrientation(Qt.Horizontal)
        self.TFL_HSL_3_L = QLabel(self.HSL)
        self.TFL_HSL_3_L.setObjectName(u"TFL_HSL_3_L")
        self.TFL_HSL_3_L.setGeometry(QRect(10, 140, 481, 17))
        self.Slider_HSL_3_L = QSlider(self.HSL)
        self.Slider_HSL_3_L.setObjectName(u"Slider_HSL_3_L")
        self.Slider_HSL_3_L.setGeometry(QRect(10, 120, 551, 16))
        self.Slider_HSL_3_L.setMaximum(100)
        self.Slider_HSL_3_L.setSliderPosition(100)
        self.Slider_HSL_3_L.setOrientation(Qt.Horizontal)
        self.TFV_HSL_3_L = QLabel(self.HSL)
        self.TFV_HSL_3_L.setObjectName(u"TFV_HSL_3_L")
        self.TFV_HSL_3_L.setGeometry(QRect(510, 140, 51, 20))
        self.TFV_HSL_3_L.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        # DRAW THE LINEAR GRADIENT TO INDICATE THE HUE VALUE IN THE HSL TAB
        mySceneHSL = QGraphicsScene(self)

        gradient = QLinearGradient(0, 0, 532, 31)
        gradient.setColorAt(0.0, QColor(255, 0, 0, 255))
        gradient.setColorAt(0.16, QColor(255, 255, 0, 255))
        gradient.setColorAt(0.33, QColor(0, 255, 0, 255))
        gradient.setColorAt(0.49, QColor(0, 255, 255, 255))
        gradient.setColorAt(0.66, QColor(0, 0, 255, 255))
        gradient.setColorAt(0.83, QColor(255, 0, 255, 255))
        gradient.setColorAt(1.0, QColor(255, 0, 0, 255))
    
        mySceneHSL.setBackgroundBrush(gradient)
        
        self.HSL_Hue_Gradient_BG = QGraphicsView(mySceneHSL, self.HSL)        
        self.HSL_Hue_Gradient_BG.setObjectName(u"HSL_Hue_Gradient_BG")
        self.HSL_Hue_Gradient_BG.setGeometry(QRect(9, 10, 552, 31))
        self.HSL_Hue_Gradient_BG.setFrameShape(QFrame.NoFrame)
        self.HSL_Hue_Gradient_BG.setFrameShadow(QFrame.Sunken)
        self.HSL_Hue_Gradient_BG.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.ColorModeTabWidget.addTab(self.HSL, "")
        self.HSL_Hue_Gradient_BG.raise_()
        self.TFV_HSL_1_H.raise_()
        self.Slider_HSL_2_S.raise_()
        self.TFV_HSL_2_S.raise_()
        self.TFL_HSL_2_S.raise_()
        self.TFL_HSL_1_H.raise_()
        self.TFL_HSL_3_L.raise_()
        self.Slider_HSL_3_L.raise_()
        self.TFV_HSL_3_L.raise_()
        self.Slider_HSL_1_H.raise_()
        self.ANM = QWidget()
        self.ANM.setObjectName(u"ANM")
        self.TFL_A_policeAnim = QLabel(self.ANM)
        self.TFL_A_policeAnim.setObjectName(u"TFL_A_policeAnim")
        self.TFL_A_policeAnim.setGeometry(QRect(10, 20, 40, 40))
        self.TFL_C_lightningAnim = QLabel(self.ANM)
        self.TFL_C_lightningAnim.setObjectName(u"TFL_C_lightningAnim")
        self.TFL_C_lightningAnim.setGeometry(QRect(10, 120, 40, 40))
        self.TFL_B_partyAnim = QLabel(self.ANM)
        self.TFL_B_partyAnim.setObjectName(u"TFL_B_partyAnim")
        self.TFL_B_partyAnim.setGeometry(QRect(10, 70, 40, 40))
        self.Button_1_police_A = QPushButton(self.ANM)
        self.Button_1_police_A.setObjectName(u"Button_1_police_A")
        self.Button_1_police_A.setGeometry(QRect(60, 20, 40, 40))
        self.Button_2_party_A = QPushButton(self.ANM)
        self.Button_2_party_A.setObjectName(u"Button_2_party_A")
        self.Button_2_party_A.setGeometry(QRect(60, 70, 40, 40))
        self.Button_3_lightning_A = QPushButton(self.ANM)
        self.Button_3_lightning_A.setObjectName(u"Button_3_lightning_A")
        self.Button_3_lightning_A.setGeometry(QRect(60, 120, 40, 40))
        self.Button_1_police_B = QPushButton(self.ANM)
        self.Button_1_police_B.setObjectName(u"Button_1_police_B")
        self.Button_1_police_B.setGeometry(QRect(110, 20, 40, 40))
        self.Button_2_party_B = QPushButton(self.ANM)
        self.Button_2_party_B.setObjectName(u"Button_2_party_B")
        self.Button_2_party_B.setGeometry(QRect(110, 70, 40, 40))
        self.Button_3_lightning_B = QPushButton(self.ANM)
        self.Button_3_lightning_B.setObjectName(u"Button_3_lightning_B")
        self.Button_3_lightning_B.setGeometry(QRect(110, 120, 40, 40))
        self.Button_1_police_C = QPushButton(self.ANM)
        self.Button_1_police_C.setObjectName(u"Button_1_police_C")
        self.Button_1_police_C.setGeometry(QRect(160, 20, 40, 40))
        self.Button_3_lightning_C = QPushButton(self.ANM)
        self.Button_3_lightning_C.setObjectName(u"Button_3_lightning_C")
        self.Button_3_lightning_C.setGeometry(QRect(160, 120, 40, 40))
        self.Button_2_party_C = QPushButton(self.ANM)
        self.Button_2_party_C.setObjectName(u"Button_2_party_C")
        self.Button_2_party_C.setGeometry(QRect(160, 70, 40, 40))
        self.Slider_ANM_Brightness = QSlider(self.ANM)
        self.Slider_ANM_Brightness.setObjectName(u"Slider_ANM_Brightness")
        self.Slider_ANM_Brightness.setGeometry(QRect(220, 20, 331, 20))
        self.Slider_ANM_Brightness.setMaximum(100)
        self.Slider_ANM_Brightness.setSliderPosition(100)
        self.Slider_ANM_Brightness.setOrientation(Qt.Horizontal)
        self.TFL_ANM_Brightness = QLabel(self.ANM)
        self.TFL_ANM_Brightness.setObjectName(u"TFL_ANM_Brightness")
        self.TFL_ANM_Brightness.setGeometry(QRect(220, 40, 300, 17))
        self.TFV_ANM_Brightness = QLabel(self.ANM)
        self.TFV_ANM_Brightness.setObjectName(u"TFV_ANM_Brightness")
        self.TFV_ANM_Brightness.setGeometry(QRect(520, 40, 31, 20))
        self.TFV_ANM_Brightness.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.turnOnButton = QPushButton(self.ANM)
        self.turnOnButton.setObjectName(u"turnOnButton")
        self.turnOnButton.setGeometry(QRect(260, 100, 111, 41))
        self.turnOffButton = QPushButton(self.ANM)
        self.turnOffButton.setObjectName(u"turnOffButton")
        self.turnOffButton.setGeometry(QRect(400, 100, 111, 41))
        self.ColorModeTabWidget.addTab(self.ANM, "")
        self.scanCommandButton = QPushButton(self.centralwidget)
        self.scanCommandButton.setObjectName(u"scanCommandButton")
        self.scanCommandButton.setGeometry(QRect(416, 4, 81, 22))
        self.lightTable = QTableWidget(self.centralwidget)
        if (self.lightTable.columnCount() < 4):
            self.lightTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.lightTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.lightTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.lightTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.lightTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.lightTable.setObjectName(u"lightTable")
        self.lightTable.setGeometry(QRect(10, 32, 571, 261))
        self.lightTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.lightTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lightTable.setAlternatingRowColors(True)
        self.lightTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.lightTable.setColumnCount(4)
        self.lightTable.setColumnWidth(0, 120)
        self.lightTable.setColumnWidth(1, 160)
        self.lightTable.setColumnWidth(2, 70)
        self.lightTable.setColumnWidth(3, 204)
        self.lightTable.verticalHeader().setStretchLastSection(False)
        self.lightTableTF = QLabel(self.centralwidget)
        self.lightTableTF.setObjectName(u"lightTableTF")
        self.lightTableTF.setGeometry(QRect(14, 8, 391, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lightTableTF.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.Slider_CCT_Bright.valueChanged.connect(self.TFV_CCT_Bright.setNum)
        self.Slider_HSL_3_L.valueChanged.connect(self.TFV_HSL_3_L.setNum)
        self.Slider_HSL_2_S.valueChanged.connect(self.TFV_HSL_2_S.setNum)
        self.Slider_HSL_1_H.valueChanged.connect(self.TFV_HSL_1_H.setNum)
        self.Slider_ANM_Brightness.valueChanged.connect(self.TFV_ANM_Brightness.setNum)

        self.ColorModeTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NeewerLite-Python 0.02a by Zach Glenwright", None))
        self.tryConnectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.TFL_CCT_Hue.setText(QCoreApplication.translate("MainWindow", u"Color Temperature", None))
        self.TFV_CCT_Hue.setText(QCoreApplication.translate("MainWindow", u"5600K", None))
        self.TFV_CCT_Bright.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.TFL_CCT_Bright.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.ColorModeTabWidget.setTabText(self.ColorModeTabWidget.indexOf(self.CCT), QCoreApplication.translate("MainWindow", u"CCT Mode", None))
        self.TFV_HSL_1_H.setText(QCoreApplication.translate("MainWindow", u"240", None))
        self.TFV_HSL_2_S.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.TFL_HSL_2_S.setText(QCoreApplication.translate("MainWindow", u"Saturation", None))
        self.TFL_HSL_1_H.setText(QCoreApplication.translate("MainWindow", u"Hue", None))
        self.TFL_HSL_3_L.setText(QCoreApplication.translate("MainWindow", u"Luminance (Brightness)", None))
        self.TFV_HSL_3_L.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.ColorModeTabWidget.setTabText(self.ColorModeTabWidget.indexOf(self.HSL), QCoreApplication.translate("MainWindow", u"HSL Mode", None))
        self.TFL_A_policeAnim.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><font size=\"8\">&#x1F6A8;</font></p></body></html>", None))
        self.TFL_C_lightningAnim.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><font size=\"8\">&#x26A1;</font></p></body></html>", None))
        self.TFL_B_partyAnim.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><font size=\"8\">&#x1F389;</font></p></body></html>", None))
        self.Button_1_police_A.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.Button_2_party_A.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.Button_3_lightning_A.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.Button_1_police_B.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.Button_2_party_B.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.Button_3_lightning_B.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.Button_1_police_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.Button_3_lightning_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.Button_2_party_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.TFL_ANM_Brightness.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.TFV_ANM_Brightness.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.turnOnButton.setText(QCoreApplication.translate("MainWindow", u"Turn On", None))
        self.turnOffButton.setText(QCoreApplication.translate("MainWindow", u"Turn Off", None))
        self.ColorModeTabWidget.setTabText(self.ColorModeTabWidget.indexOf(self.ANM), QCoreApplication.translate("MainWindow", u"Animation Mode / Power", None))
        self.scanCommandButton.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        ___qtablewidgetitem = self.lightTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Light Name", None));
        ___qtablewidgetitem1 = self.lightTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"MAC Address", None));
        ___qtablewidgetitem2 = self.lightTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Linked", None));
        ___qtablewidgetitem3 = self.lightTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.lightTableTF.setText(QCoreApplication.translate("MainWindow", u"Available Neewer Lights to Control:", None))
    # retranslateUi

