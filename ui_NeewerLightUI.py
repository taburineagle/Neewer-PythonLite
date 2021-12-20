# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NeewerLightUIcSMJnw.ui'
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
        MainWindow.setMinimumSize(QSize(590, 521))
        MainWindow.setMaximumSize(QSize(590, 521))
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
        self.Slider_CCT_Hue.setMaximum(56)
        self.Slider_CCT_Hue.setValue(56)
        self.Slider_CCT_Hue.setOrientation(Qt.Horizontal)
        self.TFL_CCT_Hue = QLabel(self.CCT)
        self.TFL_CCT_Hue.setObjectName(u"TFL_CCT_Hue")
        self.TFL_CCT_Hue.setGeometry(QRect(10, 40, 440, 17))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TFL_CCT_Hue.setFont(font)
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
        self.TFL_CCT_Bright.setFont(font)
        self.Slider_CCT_Bright = QSlider(self.CCT)
        self.Slider_CCT_Bright.setObjectName(u"Slider_CCT_Bright")
        self.Slider_CCT_Bright.setGeometry(QRect(10, 70, 551, 16))
        self.Slider_CCT_Bright.setMaximum(100)
        self.Slider_CCT_Bright.setValue(100)
        self.Slider_CCT_Bright.setOrientation(Qt.Horizontal)

        # DRAW THE LINEAR GRADIENT TO INDICATE THE COLOR TEMPERATURE VALUE IN THE CCT TAB
        # NEW DEFAULT OF 5600K FOR LIGHTS THAT DON'T SCALE UP TO 8500K
        mySceneCCT = QGraphicsScene(self)

        gradient = QLinearGradient(0, 0, 532, 31)
        gradient.setColorAt(0.0, QColor(255, 187, 120, 255)) # 3200K
        gradient.setColorAt(0.25, QColor(255, 204, 153, 255)) # 3800K
        gradient.setColorAt(0.50, QColor(255, 217, 182, 255)) # 4400K
        gradient.setColorAt(0.75, QColor(255, 228, 206, 255)) # 5000K
        gradient.setColorAt(1.0, QColor(255, 238, 227, 255)) # 5600K
    
        mySceneCCT.setBackgroundBrush(gradient)
        
        self.CCT_Temp_Gradient_BG = QGraphicsView(mySceneCCT, self.CCT)        
        self.CCT_Temp_Gradient_BG.setObjectName(u"CCT_Temp_Gradient_BG")
        self.CCT_Temp_Gradient_BG.setGeometry(QRect(9, 10, 552, 31))
        self.CCT_Temp_Gradient_BG.setFrameShape(QFrame.NoFrame)
        self.CCT_Temp_Gradient_BG.setFrameShadow(QFrame.Sunken)
        self.CCT_Temp_Gradient_BG.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.turnOnButton = QPushButton(self.CCT)
        self.turnOnButton.setObjectName(u"turnOnButton")
        self.turnOnButton.setGeometry(QRect(10, 126, 261, 31))
        self.turnOffButton = QPushButton(self.CCT)
        self.turnOffButton.setObjectName(u"turnOffButton")
        self.turnOffButton.setGeometry(QRect(290, 126, 261, 31))
        self.ColorModeTabWidget.addTab(self.CCT, "")
        self.CCT_Temp_Gradient_BG.raise_()
        self.TFL_CCT_Hue.raise_()
        self.TFV_CCT_Hue.raise_()
        self.TFV_CCT_Bright.raise_()
        self.TFL_CCT_Bright.raise_()
        self.Slider_CCT_Bright.raise_()
        self.Slider_CCT_Hue.raise_()
        self.turnOnButton.raise_()
        self.turnOffButton.raise_()
        self.HSI = QWidget()
        self.HSI.setObjectName(u"HSI")
        self.TFV_HSI_1_H = QLabel(self.HSI)
        self.TFV_HSI_1_H.setObjectName(u"TFV_HSI_1_H")
        self.TFV_HSI_1_H.setGeometry(QRect(510, 40, 51, 20))
        self.TFV_HSI_1_H.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Slider_HSI_2_S = QSlider(self.HSI)
        self.Slider_HSI_2_S.setObjectName(u"Slider_HSI_2_S")
        self.Slider_HSI_2_S.setGeometry(QRect(10, 70, 551, 16))
        self.Slider_HSI_2_S.setMaximum(100)
        self.Slider_HSI_2_S.setValue(100)
        self.Slider_HSI_2_S.setOrientation(Qt.Horizontal)
        self.TFV_HSI_2_S = QLabel(self.HSI)
        self.TFV_HSI_2_S.setObjectName(u"TFV_HSI_2_S")
        self.TFV_HSI_2_S.setGeometry(QRect(510, 90, 51, 20))
        self.TFV_HSI_2_S.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.TFL_HSI_2_S = QLabel(self.HSI)
        self.TFL_HSI_2_S.setObjectName(u"TFL_HSI_2_S")
        self.TFL_HSI_2_S.setGeometry(QRect(10, 90, 440, 17))
        self.TFL_HSI_2_S.setFont(font)
        self.TFL_HSI_1_H = QLabel(self.HSI)
        self.TFL_HSI_1_H.setObjectName(u"TFL_HSI_1_H")
        self.TFL_HSI_1_H.setGeometry(QRect(10, 40, 440, 17))
        self.TFL_HSI_1_H.setFont(font)
        self.Slider_HSI_1_H = QSlider(self.HSI)
        self.Slider_HSI_1_H.setObjectName(u"Slider_HSI_1_H")
        self.Slider_HSI_1_H.setGeometry(QRect(10, 20, 551, 16))
        self.Slider_HSI_1_H.setMaximum(360)
        self.Slider_HSI_1_H.setValue(240)
        self.Slider_HSI_1_H.setOrientation(Qt.Horizontal)
        self.TFL_HSI_3_L = QLabel(self.HSI)
        self.TFL_HSI_3_L.setObjectName(u"TFL_HSI_3_L")
        self.TFL_HSI_3_L.setGeometry(QRect(10, 140, 481, 17))
        self.TFL_HSI_3_L.setFont(font)
        self.Slider_HSI_3_L = QSlider(self.HSI)
        self.Slider_HSI_3_L.setObjectName(u"Slider_HSI_3_L")
        self.Slider_HSI_3_L.setGeometry(QRect(10, 120, 551, 16))
        self.Slider_HSI_3_L.setMaximum(100)
        self.Slider_HSI_3_L.setSliderPosition(100)
        self.Slider_HSI_3_L.setOrientation(Qt.Horizontal)
        self.TFV_HSI_3_L = QLabel(self.HSI)
        self.TFV_HSI_3_L.setObjectName(u"TFV_HSI_3_L")
        self.TFV_HSI_3_L.setGeometry(QRect(510, 140, 51, 20))
        self.TFV_HSI_3_L.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        # DRAW THE LINEAR GRADIENT TO INDICATE THE HUE VALUE IN THE HSI TAB
        mySceneHSI = QGraphicsScene(self)

        gradient = QLinearGradient(0, 0, 532, 31)
        gradient.setColorAt(0.0, QColor(255, 0, 0, 255))
        gradient.setColorAt(0.16, QColor(255, 255, 0, 255))
        gradient.setColorAt(0.33, QColor(0, 255, 0, 255))
        gradient.setColorAt(0.49, QColor(0, 255, 255, 255))
        gradient.setColorAt(0.66, QColor(0, 0, 255, 255))
        gradient.setColorAt(0.83, QColor(255, 0, 255, 255))
        gradient.setColorAt(1.0, QColor(255, 0, 0, 255))
    
        mySceneHSI.setBackgroundBrush(gradient)
        
        self.HSI_Hue_Gradient_BG = QGraphicsView(mySceneHSI, self.HSI)        
        self.HSI_Hue_Gradient_BG.setObjectName(u"HSI_Hue_Gradient_BG")
        self.HSI_Hue_Gradient_BG.setGeometry(QRect(9, 10, 552, 31))
        self.HSI_Hue_Gradient_BG.setFrameShape(QFrame.NoFrame)
        self.HSI_Hue_Gradient_BG.setFrameShadow(QFrame.Sunken)
        self.HSI_Hue_Gradient_BG.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.ColorModeTabWidget.addTab(self.HSI, "")
        self.HSI_Hue_Gradient_BG.raise_()
        self.TFV_HSI_1_H.raise_()
        self.Slider_HSI_2_S.raise_()
        self.TFV_HSI_2_S.raise_()
        self.TFL_HSI_2_S.raise_()
        self.TFL_HSI_1_H.raise_()
        self.TFL_HSI_3_L.raise_()
        self.Slider_HSI_3_L.raise_()
        self.TFV_HSI_3_L.raise_()
        self.Slider_HSI_1_H.raise_()
        self.ANM = QWidget()
        self.ANM.setObjectName(u"ANM")
        self.TFL_A_policeAnim = QLabel(self.ANM)
        self.TFL_A_policeAnim.setObjectName(u"TFL_A_policeAnim")
        self.TFL_A_policeAnim.setGeometry(QRect(10, 46, 40, 40))
        self.TFL_C_lightningAnim = QLabel(self.ANM)
        self.TFL_C_lightningAnim.setObjectName(u"TFL_C_lightningAnim")
        self.TFL_C_lightningAnim.setGeometry(QRect(10, 126, 40, 40))
        self.TFL_B_partyAnim = QLabel(self.ANM)
        self.TFL_B_partyAnim.setObjectName(u"TFL_B_partyAnim")
        self.TFL_B_partyAnim.setGeometry(QRect(10, 84, 40, 40))
        self.Button_1_police_A = QPushButton(self.ANM)
        self.Button_1_police_A.setObjectName(u"Button_1_police_A")
        self.Button_1_police_A.setGeometry(QRect(50, 50, 160, 31))
        self.Button_2_party_A = QPushButton(self.ANM)
        self.Button_2_party_A.setObjectName(u"Button_2_party_A")
        self.Button_2_party_A.setGeometry(QRect(50, 90, 160, 31))
        self.Button_3_lightning_A = QPushButton(self.ANM)
        self.Button_3_lightning_A.setObjectName(u"Button_3_lightning_A")
        self.Button_3_lightning_A.setGeometry(QRect(50, 130, 160, 31))
        self.Button_1_police_B = QPushButton(self.ANM)
        self.Button_1_police_B.setObjectName(u"Button_1_police_B")
        self.Button_1_police_B.setGeometry(QRect(220, 50, 160, 31))
        self.Button_2_party_B = QPushButton(self.ANM)
        self.Button_2_party_B.setObjectName(u"Button_2_party_B")
        self.Button_2_party_B.setGeometry(QRect(220, 90, 160, 31))
        self.Button_3_lightning_B = QPushButton(self.ANM)
        self.Button_3_lightning_B.setObjectName(u"Button_3_lightning_B")
        self.Button_3_lightning_B.setGeometry(QRect(220, 130, 160, 31))
        self.Button_1_police_C = QPushButton(self.ANM)
        self.Button_1_police_C.setObjectName(u"Button_1_police_C")
        self.Button_1_police_C.setGeometry(QRect(390, 50, 160, 31))
        self.Button_3_lightning_C = QPushButton(self.ANM)
        self.Button_3_lightning_C.setObjectName(u"Button_3_lightning_C")
        self.Button_3_lightning_C.setGeometry(QRect(390, 130, 160, 31))
        self.Button_2_party_C = QPushButton(self.ANM)
        self.Button_2_party_C.setObjectName(u"Button_2_party_C")
        self.Button_2_party_C.setGeometry(QRect(390, 90, 160, 31))
        self.TFL_ANM_Brightness = QLabel(self.ANM)
        self.TFL_ANM_Brightness.setObjectName(u"TFL_ANM_Brightness")
        self.TFL_ANM_Brightness.setGeometry(QRect(10, 25, 300, 17))
        self.TFL_ANM_Brightness.setFont(font)
        self.Slider_ANM_Brightness = QSlider(self.ANM)
        self.Slider_ANM_Brightness.setObjectName(u"Slider_ANM_Brightness")
        self.Slider_ANM_Brightness.setGeometry(QRect(10, 10, 551, 16))
        self.Slider_ANM_Brightness.setMaximum(100)
        self.Slider_ANM_Brightness.setSliderPosition(100)
        self.Slider_ANM_Brightness.setOrientation(Qt.Horizontal)
        self.TFV_ANM_Brightness = QLabel(self.ANM)
        self.TFV_ANM_Brightness.setObjectName(u"TFV_ANM_Brightness")
        self.TFV_ANM_Brightness.setGeometry(QRect(510, 25, 51, 20))
        self.TFV_ANM_Brightness.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ColorModeTabWidget.addTab(self.ANM, "")
        self.lightPrefs = QWidget()
        self.lightPrefs.setObjectName(u"lightPrefs")
        self.customNameDescription = QLabel(self.lightPrefs)
        self.customNameDescription.setObjectName(u"customNameDescription")
        self.customNameDescription.setGeometry(QRect(10, 14, 541, 16))
        self.customNameDescription.setFont(font)
        self.customNameTF = QLineEdit(self.lightPrefs)
        self.customNameTF.setObjectName(u"customNameTF")
        self.customNameTF.setGeometry(QRect(10, 34, 541, 20))
        self.customNameTF.setMaxLength(80)
        self.widerRangeCheck = QCheckBox(self.lightPrefs)
        self.widerRangeCheck.setObjectName(u"widerRangeCheck")
        self.widerRangeCheck.setGeometry(QRect(10, 70, 541, 31))
        self.widerRangeCheck.setFont(font)
        self.savePrefsButton = QPushButton(self.lightPrefs)
        self.savePrefsButton.setObjectName(u"savePrefsButton")
        self.savePrefsButton.setGeometry(QRect(416, 130, 141, 23))
        self.onlyCCTModeCheck = QCheckBox(self.lightPrefs)
        self.onlyCCTModeCheck.setObjectName(u"onlyCCTModeCheck")
        self.onlyCCTModeCheck.setGeometry(QRect(10, 120, 401, 31))
        self.onlyCCTModeCheck.setFont(font)
        self.ColorModeTabWidget.addTab(self.lightPrefs, "")
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
        self.lightTableTF.setGeometry(QRect(14, 8, 371, 16))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.lightTableTF.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.Slider_CCT_Bright.valueChanged.connect(self.TFV_CCT_Bright.setNum)
        self.Slider_HSI_3_L.valueChanged.connect(self.TFV_HSI_3_L.setNum)
        self.Slider_HSI_2_S.valueChanged.connect(self.TFV_HSI_2_S.setNum)
        self.Slider_HSI_1_H.valueChanged.connect(self.TFV_HSI_1_H.setNum)
        self.Slider_ANM_Brightness.valueChanged.connect(self.TFV_ANM_Brightness.setNum)

        self.ColorModeTabWidget.setCurrentIndex(0)
        self.ColorModeTabWidget.setTabEnabled(3, False) # disable the Prefs tab by default


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NeewerLite-Python 0.5a by Zach Glenwright", None))
        self.tryConnectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.TFL_CCT_Hue.setText(QCoreApplication.translate("MainWindow", u"Color Temperature", None))
        self.TFV_CCT_Hue.setText(QCoreApplication.translate("MainWindow", u"5600K", None))
        self.TFV_CCT_Bright.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.TFL_CCT_Bright.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.turnOnButton.setText(QCoreApplication.translate("MainWindow", u"Turn Light(s) On", None))
        self.turnOffButton.setText(QCoreApplication.translate("MainWindow", u"Turn Light(s) Off", None))
        self.ColorModeTabWidget.setTabText(self.ColorModeTabWidget.indexOf(self.CCT), QCoreApplication.translate("MainWindow", u"CCT Mode / Power", None))
        self.TFV_HSI_1_H.setText(QCoreApplication.translate("MainWindow", u"240", None))
        self.TFV_HSI_2_S.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.TFL_HSI_2_S.setText(QCoreApplication.translate("MainWindow", u"Saturation", None))
        self.TFL_HSI_1_H.setText(QCoreApplication.translate("MainWindow", u"Hue", None))
        self.TFL_HSI_3_L.setText(QCoreApplication.translate("MainWindow", u"Intensity (Brightness)", None))
        self.TFV_HSI_3_L.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.ColorModeTabWidget.setTabText(self.ColorModeTabWidget.indexOf(self.HSI), QCoreApplication.translate("MainWindow", u"HSI Mode", None))
        self.TFL_A_policeAnim.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><font size=\"8\">&#x1F6A8;</font></p></body></html>", None))
        self.TFL_C_lightningAnim.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><font size=\"8\">&#x26A1;</font></p></body></html>", None))
        self.TFL_B_partyAnim.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><font size=\"8\">&#x1F389;</font></p></body></html>", None))
        self.Button_1_police_A.setText(QCoreApplication.translate("MainWindow", u"(1) Squad Car", None))
        self.Button_2_party_A.setText(QCoreApplication.translate("MainWindow", u"(4) Fireworks", None))
        self.Button_3_lightning_A.setText(QCoreApplication.translate("MainWindow", u"(7) Lightning", None))
        self.Button_1_police_B.setText(QCoreApplication.translate("MainWindow", u"(2) Ambulance", None))
        self.Button_2_party_B.setText(QCoreApplication.translate("MainWindow", u"(5) Party", None))
        self.Button_3_lightning_B.setText(QCoreApplication.translate("MainWindow", u"(8) Paparazzi", None))
        self.Button_1_police_C.setText(QCoreApplication.translate("MainWindow", u"(3) Fire Engine", None))
        self.Button_3_lightning_C.setText(QCoreApplication.translate("MainWindow", u"(9) Screen", None))
        self.Button_2_party_C.setText(QCoreApplication.translate("MainWindow", u"(6) Candle Light", None))
        self.TFL_ANM_Brightness.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.TFV_ANM_Brightness.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.ColorModeTabWidget.setTabText(self.ColorModeTabWidget.indexOf(self.ANM), QCoreApplication.translate("MainWindow", u"Animation / Scene", None))
        self.customNameDescription.setText(QCoreApplication.translate("MainWindow", u"Custom Name for this light: (optional)", None))
        self.widerRangeCheck.setText(QCoreApplication.translate("MainWindow", u"Allow wider range of color temperatures for the CCT slider\n"
"(for lights that support it, like the SL-80)", None))
        self.savePrefsButton.setText(QCoreApplication.translate("MainWindow", u"Save Preferences", None))
        self.onlyCCTModeCheck.setText(QCoreApplication.translate("MainWindow", u"This light can only use CCT mode\n"
"(for SNL-660 and other Neewer LED/Ring lights)", None))
        self.ColorModeTabWidget.setTabText(self.ColorModeTabWidget.indexOf(self.lightPrefs), QCoreApplication.translate("MainWindow", u"Light Preferences", None))
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

