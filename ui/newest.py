# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'misa.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1049, 784)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1049, 784))
        MainWindow.setMaximumSize(QSize(1049, 784))
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QWidget#centralwidget{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0.263, y1:0.372432, x2:0.883064, y2:0.746, stop:0 rgba(188, 216, 206, 255), stop:1 rgba(83, 141, 153, 255));\n"
"\n"
"}")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.label_ime = QLabel(self.centralwidget)
        self.label_ime.setObjectName(u"label_ime")
        self.label_ime.setGeometry(QRect(200, 250, 51, 51))
        self.label_ime.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.label_prezime = QLabel(self.centralwidget)
        self.label_prezime.setObjectName(u"label_prezime")
        self.label_prezime.setGeometry(QRect(150, 320, 91, 51))
        self.label_prezime.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.label_datum = QLabel(self.centralwidget)
        self.label_datum.setObjectName(u"label_datum")
        self.label_datum.setGeometry(QRect(70, 380, 191, 51))
        self.label_datum.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.label_adresa = QLabel(self.centralwidget)
        self.label_adresa.setObjectName(u"label_adresa")
        self.label_adresa.setGeometry(QRect(610, 260, 101, 31))
        self.label_adresa.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.label_telefon = QLabel(self.centralwidget)
        self.label_telefon.setObjectName(u"label_telefon")
        self.label_telefon.setGeometry(QRect(610, 330, 81, 31))
        self.label_telefon.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.label_email = QLabel(self.centralwidget)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setGeometry(QRect(620, 390, 91, 31))
        self.label_email.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.label_tip_auto = QLabel(self.centralwidget)
        self.label_tip_auto.setObjectName(u"label_tip_auto")
        self.label_tip_auto.setGeometry(QRect(80, 540, 171, 51))
        self.label_tip_auto.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.label_br_sasije = QLabel(self.centralwidget)
        self.label_br_sasije.setObjectName(u"label_br_sasije")
        self.label_br_sasije.setGeometry(QRect(130, 610, 121, 31))
        self.label_br_sasije.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.label_osig_kuca = QLabel(self.centralwidget)
        self.label_osig_kuca.setObjectName(u"label_osig_kuca")
        self.label_osig_kuca.setGeometry(QRect(640, 550, 221, 31))
        self.label_osig_kuca.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.label_br_police = QLabel(self.centralwidget)
        self.label_br_police.setObjectName(u"label_br_police")
        self.label_br_police.setGeometry(QRect(730, 610, 121, 31))
        self.label_br_police.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.gumb_desni = QCommandLinkButton(self.centralwidget)
        self.gumb_desni.setObjectName(u"gumb_desni")
        self.gumb_desni.setGeometry(QRect(780, 30, 61, 70))
        icon = QIcon()
        icon.addFile(u"./ui/IKONE/right-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.gumb_desni.setIcon(icon)
        self.gumb_desni.setIconSize(QSize(61, 51))
        self.gumb_lijevi = QCommandLinkButton(self.centralwidget)
        self.gumb_lijevi.setObjectName(u"gumb_lijevi")
        self.gumb_lijevi.setGeometry(QRect(200, 30, 61, 70))
        icon1 = QIcon()
        icon1.addFile(u"./ui/IKONE/left-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.gumb_lijevi.setIcon(icon1)
        self.gumb_lijevi.setIconSize(QSize(61, 51))
        self.kategorija_vlasnik = QLabel(self.centralwidget)
        self.kategorija_vlasnik.setObjectName(u"kategorija_vlasnik")
        self.kategorija_vlasnik.setGeometry(QRect(410, 180, 221, 31))
        self.kategorija_vlasnik.setStyleSheet(u"font: 700 21pt \"Calibri\";")
        self.label_ukras1 = QLabel(self.centralwidget)
        self.label_ukras1.setObjectName(u"label_ukras1")
        self.label_ukras1.setGeometry(QRect(20, 166, 421, 31))
        self.label_ukras1.setAutoFillBackground(False)
        self.label_ukras1.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.kategorija_registracije = QLabel(self.centralwidget)
        self.kategorija_registracije.setObjectName(u"kategorija_registracije")
        self.kategorija_registracije.setGeometry(QRect(390, 470, 271, 31))
        self.kategorija_registracije.setStyleSheet(u"font: 700 21pt \"Calibri\";")
        self.lineEdit_ime = QLineEdit(self.centralwidget)
        self.lineEdit_ime.setObjectName(u"lineEdit_ime")
        self.lineEdit_ime.setGeometry(QRect(250, 260, 161, 31))
        font = QFont()
        font.setBold(True)
        self.lineEdit_ime.setFont(font)
        self.lineEdit_ime.setStyleSheet(u"font-size: 20px;\n"
"padding: 0px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #545454;\n"
"border-radius: 6.5px;\n"
"font-weight: bold;")
        self.lineEdit_ime.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_ime.setReadOnly(False)
        self.slika_osobne = QLabel(self.centralwidget)
        self.slika_osobne.setObjectName(u"slika_osobne")
        self.slika_osobne.setGeometry(QRect(140, 290, 50, 40))
        self.slika_osobne.setStyleSheet(u"background-image: url(./ui/IKONE/id-card.png);")
        self.slika_osobne.setPixmap(QPixmap(u"./ui/IKONE/id-card.png"))
        self.slika_osobne.setScaledContents(True)
        self.slika_osobne.setMargin(0)
        self.slika_datum = QLabel(self.centralwidget)
        self.slika_datum.setObjectName(u"slika_datum")
        self.slika_datum.setGeometry(QRect(20, 390, 41, 31))
        self.slika_datum.setStyleSheet(u"background-image: url(./ui/IKONE/calendar.png);")
        self.slika_datum.setPixmap(QPixmap(u"./ui/IKONE/calendar.png"))
        self.slika_datum.setScaledContents(True)
        self.slika_adresa = QLabel(self.centralwidget)
        self.slika_adresa.setObjectName(u"slika_adresa")
        self.slika_adresa.setGeometry(QRect(560, 250, 46, 36))
        self.slika_adresa.setStyleSheet(u"background-image: url(./ui/IKONE/PngItem_5096652.png);")
        self.slika_adresa.setPixmap(QPixmap(u"./ui/IKONE/PngItem_5096652.png"))
        self.slika_adresa.setScaledContents(True)
        self.slika_telefon = QLabel(self.centralwidget)
        self.slika_telefon.setObjectName(u"slika_telefon")
        self.slika_telefon.setGeometry(QRect(560, 320, 41, 36))
        self.slika_telefon.setStyleSheet(u"background-image: url(./ui/IKONE/telephone.png);")
        self.slika_telefon.setPixmap(QPixmap(u"./ui/IKONE/telephone.png"))
        self.slika_telefon.setScaledContents(True)
        self.slika_email = QLabel(self.centralwidget)
        self.slika_email.setObjectName(u"slika_email")
        self.slika_email.setGeometry(QRect(560, 380, 48, 41))
        self.slika_email.setStyleSheet(u"background-image: url(./ui/IKONE/message.png);")
        self.slika_email.setPixmap(QPixmap(u"./ui/IKONE/message.png"))
        self.slika_email.setScaledContents(True)
        self.slika_auto = QLabel(self.centralwidget)
        self.slika_auto.setObjectName(u"slika_auto")
        self.slika_auto.setGeometry(QRect(20, 550, 50, 40))
        self.slika_auto.setStyleSheet(u"background-image: url(./ui/IKONE/service.png);")
        self.slika_auto.setPixmap(QPixmap(u"./ui/IKONE/service.png"))
        self.slika_auto.setScaledContents(True)
        self.slika_br_sasije = QLabel(self.centralwidget)
        self.slika_br_sasije.setObjectName(u"slika_br_sasije")
        self.slika_br_sasije.setGeometry(QRect(70, 610, 50, 40))
        self.slika_br_sasije.setStyleSheet(u"background-image: url(./ui/IKONE/license-plate.png);")
        self.slika_br_sasije.setPixmap(QPixmap(u"./ui/IKONE/license-plate.png"))
        self.slika_br_sasije.setScaledContents(True)
        self.slika_osig_kuca = QLabel(self.centralwidget)
        self.slika_osig_kuca.setObjectName(u"slika_osig_kuca")
        self.slika_osig_kuca.setGeometry(QRect(590, 550, 50, 40))
        self.slika_osig_kuca.setPixmap(QPixmap(u"./ui/IKONE/car-insurance (1).png"))
        self.slika_osig_kuca.setScaledContents(True)
        self.slika_br_police = QLabel(self.centralwidget)
        self.slika_br_police.setObjectName(u"slika_br_police")
        self.slika_br_police.setGeometry(QRect(680, 610, 50, 40))
        self.slika_br_police.setPixmap(QPixmap(u"./ui/IKONE/document.png"))
        self.slika_br_police.setScaledContents(True)
        self.lineEdit_prezime = QLineEdit(self.centralwidget)
        self.lineEdit_prezime.setObjectName(u"lineEdit_prezime")
        self.lineEdit_prezime.setGeometry(QRect(250, 330, 161, 31))
        self.lineEdit_prezime.setFont(font)
        self.lineEdit_prezime.setStyleSheet(u"font-size: 20px;\n"
"padding: 0px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #545454;\n"
"border-radius: 6.5px;\n"
"font-weight: bold;")
        self.lineEdit_datum = QLineEdit(self.centralwidget)
        self.lineEdit_datum.setObjectName(u"lineEdit_datum")
        self.lineEdit_datum.setGeometry(QRect(250, 390, 161, 31))
        self.lineEdit_datum.setStyleSheet(u"font-size: 20px;\n"
"padding: 0px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #545454;\n"
"border-radius: 6.5px;\n"
"font-weight: bold;")
        self.lineEdit_adresa = QLineEdit(self.centralwidget)
        self.lineEdit_adresa.setObjectName(u"lineEdit_adresa")
        self.lineEdit_adresa.setGeometry(QRect(700, 260, 321, 31))
        self.lineEdit_adresa.setStyleSheet(u"font-size: 20px;\n"
"padding: 0px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #545454;\n"
"border-radius: 6.5px;\n"
"font-weight: bold;")
        self.lineEdit_telefon = QLineEdit(self.centralwidget)
        self.lineEdit_telefon.setObjectName(u"lineEdit_telefon")
        self.lineEdit_telefon.setGeometry(QRect(700, 330, 161, 31))
        self.lineEdit_telefon.setStyleSheet(u"font-size: 20px;\n"
"padding: 0px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #545454;\n"
"border-radius: 6.5px;\n"
"font-weight: bold;")
        self.lineEdit_tip_auta = QLineEdit(self.centralwidget)
        self.lineEdit_tip_auta.setObjectName(u"lineEdit_tip_auta")
        self.lineEdit_tip_auta.setGeometry(QRect(260, 550, 271, 31))
        self.lineEdit_tip_auta.setFont(font)
        self.lineEdit_tip_auta.setStyleSheet(u"font-size: 20px;\n"
"padding: 0px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #545454;\n"
"border-radius: 6.5px;\n"
"font-weight: bold;")
        self.lineEdit_br_sasije = QLineEdit(self.centralwidget)
        self.lineEdit_br_sasije.setObjectName(u"lineEdit_br_sasije")
        self.lineEdit_br_sasije.setGeometry(QRect(260, 610, 221, 31))
        self.lineEdit_br_sasije.setFont(font)
        self.lineEdit_br_sasije.setStyleSheet(u"font-size: 20px;\n"
"padding: 0px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #545454;\n"
"border-radius: 6.5px;\n"
"font-weight: bold;")
        self.lineEdit_osig_kuca = QLineEdit(self.centralwidget)
        self.lineEdit_osig_kuca.setObjectName(u"lineEdit_osig_kuca")
        self.lineEdit_osig_kuca.setGeometry(QRect(860, 550, 161, 31))
        self.lineEdit_osig_kuca.setFont(font)
        self.lineEdit_osig_kuca.setStyleSheet(u"font-size: 20px;\n"
"padding: 0px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #545454;\n"
"border-radius: 6.5px;\n"
"font-weight: bold;")
        self.lineEdit_br_police = QLineEdit(self.centralwidget)
        self.lineEdit_br_police.setObjectName(u"lineEdit_br_police")
        self.lineEdit_br_police.setGeometry(QRect(860, 610, 161, 31))
        self.lineEdit_br_police.setFont(font)
        self.lineEdit_br_police.setStyleSheet(u"font-size: 20px;\n"
"padding: 0px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #545454;\n"
"border-radius: 6.5px;\n"
"font-weight: bold;")
        self.label_ukras3 = QLabel(self.centralwidget)
        self.label_ukras3.setObjectName(u"label_ukras3")
        self.label_ukras3.setGeometry(QRect(20, 457, 421, 31))
        self.label_ukras3.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.label_ukras2 = QLabel(self.centralwidget)
        self.label_ukras2.setObjectName(u"label_ukras2")
        self.label_ukras2.setGeometry(QRect(630, 166, 541, 31))
        self.label_ukras2.setAutoFillBackground(False)
        self.label_ukras2.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.label_ukras4 = QLabel(self.centralwidget)
        self.label_ukras4.setObjectName(u"label_ukras4")
        self.label_ukras4.setGeometry(QRect(650, 457, 431, 31))
        self.label_ukras4.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.label_prikaz_registracije = QLabel(self.centralwidget)
        self.label_prikaz_registracije.setObjectName(u"label_prikaz_registracije")
        self.label_prikaz_registracije.setGeometry(QRect(270, 30, 501, 71))
        self.label_prikaz_registracije.setStyleSheet(u"font-size: 53px;\n"
"padding: 0px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #545454;\n"
"border-radius: 8px;\n"
"font-weight: bold;")
        self.label_prikaz_registracije.setAlignment(Qt.AlignCenter)
        self.lineEdit_email = QLineEdit(self.centralwidget)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setGeometry(QRect(700, 390, 321, 31))
        self.lineEdit_email.setStyleSheet(u"font-size: 20px;\n"
"padding: 0px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #545454;\n"
"border-radius: 6.5px;\n"
"font-weight: bold;")
        self.gumb_baza = QCommandLinkButton(self.centralwidget)
        self.gumb_baza.setObjectName(u"gumb_baza")
        self.gumb_baza.setGeometry(QRect(400, 690, 231, 60))
        self.gumb_baza.setStyleSheet(u"font: 700 20pt \"Calibri\";")
        icon2 = QIcon()
        icon2.addFile(u"./ui/IKONE/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.gumb_baza.setIcon(icon2)
        self.gumb_baza.setIconSize(QSize(51, 41))
        self.label_ukras5 = QLabel(self.centralwidget)
        self.label_ukras5.setObjectName(u"label_ukras5")
        self.label_ukras5.setGeometry(QRect(20, 690, 381, 31))
        self.label_ukras5.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.label_ukras6 = QLabel(self.centralwidget)
        self.label_ukras6.setObjectName(u"label_ukras6")
        self.label_ukras6.setGeometry(QRect(630, 690, 411, 31))
        self.label_ukras6.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.gumb_emitiranje_uzivo = QCommandLinkButton(self.centralwidget)
        self.gumb_emitiranje_uzivo.setObjectName(u"gumb_emitiranje_uzivo")
        self.gumb_emitiranje_uzivo.setGeometry(QRect(420, 100, 201, 60))
        self.gumb_emitiranje_uzivo.setStyleSheet(u"font: 700 15pt \"Calibri\";\n"
"color: #063362;")
        icon3 = QIcon()
        icon3.addFile(u"./ui/IKONE/security-camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.gumb_emitiranje_uzivo.setIcon(icon3)
        self.gumb_emitiranje_uzivo.setIconSize(QSize(41, 37))
        self.postavkeWidget = QWidget(self.centralwidget)
        self.postavkeWidget.setObjectName(u"postavkeWidget")
        self.postavkeWidget.setGeometry(QRect(70, 140, 911, 471))
        self.postavkeWidget.setAutoFillBackground(False)
        self.postavkeWidget.setStyleSheet(u"QWidget#postavkeWidget{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0.263, y1:0.372432, x2:0.883064, y2:0.746, stop:0 rgba(188, 216, 206, 255), stop:1 rgba(83, 141, 153, 255));\n"
"\n"
"}")
        self.horizontalSlider_t_confidence = QSlider(self.postavkeWidget)
        self.horizontalSlider_t_confidence.setObjectName(u"horizontalSlider_t_confidence")
        self.horizontalSlider_t_confidence.setGeometry(QRect(210, 100, 160, 22))
        self.horizontalSlider_t_confidence.setMaximum(100)
        self.horizontalSlider_t_confidence.setPageStep(1)
        self.horizontalSlider_t_confidence.setValue(0)
        self.horizontalSlider_t_confidence.setSliderPosition(0)
        self.horizontalSlider_t_confidence.setOrientation(Qt.Horizontal)
        self.horizontalSlider_t_confidence.setInvertedAppearance(False)
        self.horizontalSlider_t_confidence.setInvertedControls(False)
        self.horizontalSlider_t_confidence.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_t_iouconfidence = QSlider(self.postavkeWidget)
        self.horizontalSlider_t_iouconfidence.setObjectName(u"horizontalSlider_t_iouconfidence")
        self.horizontalSlider_t_iouconfidence.setGeometry(QRect(210, 160, 160, 22))
        self.horizontalSlider_t_iouconfidence.setMaximum(100)
        self.horizontalSlider_t_iouconfidence.setSingleStep(1)
        self.horizontalSlider_t_iouconfidence.setPageStep(1)
        self.horizontalSlider_t_iouconfidence.setOrientation(Qt.Horizontal)
        self.horizontalSlider_t_iouconfidence.setTickPosition(QSlider.TicksBelow)
        self.checkBox_t_label = QCheckBox(self.postavkeWidget)
        self.checkBox_t_label.setObjectName(u"checkBox_t_label")
        self.checkBox_t_label.setGeometry(QRect(290, 360, 81, 20))
        self.checkBox_t_label.setLayoutDirection(Qt.RightToLeft)
        self.checkBox_t_label.setStyleSheet(u"font: 20pt \"Calibri\";\n"
"")
        self.checkBox_t_confidence = QCheckBox(self.postavkeWidget)
        self.checkBox_t_confidence.setObjectName(u"checkBox_t_confidence")
        self.checkBox_t_confidence.setGeometry(QRect(40, 360, 141, 21))
        self.checkBox_t_confidence.setLayoutDirection(Qt.RightToLeft)
        self.checkBox_t_confidence.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.lineEdit = QLineEdit(self.postavkeWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(210, 240, 161, 31))
        self.lineEdit.setStyleSheet(u"font-size: 20px;\n"
"padding: 0px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #545454;\n"
"border-radius: 6.5px;\n"
"font-weight: bold;")
        self.label_t_thickness = QLabel(self.postavkeWidget)
        self.label_t_thickness.setObjectName(u"label_t_thickness")
        self.label_t_thickness.setGeometry(QRect(40, 240, 161, 21))
        self.label_t_thickness.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.label_t_resolution = QLabel(self.postavkeWidget)
        self.label_t_resolution.setObjectName(u"label_t_resolution")
        self.label_t_resolution.setGeometry(QRect(80, 290, 121, 31))
        self.label_t_resolution.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.label_t_confidence = QLabel(self.postavkeWidget)
        self.label_t_confidence.setObjectName(u"label_t_confidence")
        self.label_t_confidence.setGeometry(QRect(70, 100, 141, 21))
        self.label_t_confidence.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.label_t_iouconfidence = QLabel(self.postavkeWidget)
        self.label_t_iouconfidence.setObjectName(u"label_t_iouconfidence")
        self.label_t_iouconfidence.setGeometry(QRect(30, 150, 171, 41))
        self.label_t_iouconfidence.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.kategorija_tablica = QLabel(self.postavkeWidget)
        self.kategorija_tablica.setObjectName(u"kategorija_tablica")
        self.kategorija_tablica.setGeometry(QRect(90, 30, 261, 31))
        self.kategorija_tablica.setStyleSheet(u"font: 700 21pt \"Calibri\";")
        self.kategorija_znakova = QLabel(self.postavkeWidget)
        self.kategorija_znakova.setObjectName(u"kategorija_znakova")
        self.kategorija_znakova.setGeometry(QRect(550, 30, 271, 31))
        self.kategorija_znakova.setStyleSheet(u"font: 700 21pt \"Calibri\";")
        self.label_z_resolution = QLabel(self.postavkeWidget)
        self.label_z_resolution.setObjectName(u"label_z_resolution")
        self.label_z_resolution.setGeometry(QRect(550, 290, 121, 31))
        self.label_z_resolution.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.horizontalSlider_z_iouconfidence = QSlider(self.postavkeWidget)
        self.horizontalSlider_z_iouconfidence.setObjectName(u"horizontalSlider_z_iouconfidence")
        self.horizontalSlider_z_iouconfidence.setGeometry(QRect(680, 150, 160, 22))
        self.horizontalSlider_z_iouconfidence.setMaximum(100)
        self.horizontalSlider_z_iouconfidence.setSingleStep(1)
        self.horizontalSlider_z_iouconfidence.setPageStep(1)
        self.horizontalSlider_z_iouconfidence.setOrientation(Qt.Horizontal)
        self.horizontalSlider_z_iouconfidence.setTickPosition(QSlider.TicksBelow)
        self.label_z_thickness = QLabel(self.postavkeWidget)
        self.label_z_thickness.setObjectName(u"label_z_thickness")
        self.label_z_thickness.setGeometry(QRect(510, 240, 161, 21))
        self.label_z_thickness.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.checkBox_z_label = QCheckBox(self.postavkeWidget)
        self.checkBox_z_label.setObjectName(u"checkBox_z_label")
        self.checkBox_z_label.setGeometry(QRect(760, 360, 81, 21))
        self.checkBox_z_label.setLayoutDirection(Qt.RightToLeft)
        self.checkBox_z_label.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.checkBox_z_label.setIconSize(QSize(16, 16))
        self.checkBox_z_confidence = QCheckBox(self.postavkeWidget)
        self.checkBox_z_confidence.setObjectName(u"checkBox_z_confidence")
        self.checkBox_z_confidence.setGeometry(QRect(510, 360, 141, 21))
        self.checkBox_z_confidence.setLayoutDirection(Qt.RightToLeft)
        self.checkBox_z_confidence.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.label_z_confidence = QLabel(self.postavkeWidget)
        self.label_z_confidence.setObjectName(u"label_z_confidence")
        self.label_z_confidence.setGeometry(QRect(540, 100, 141, 21))
        self.label_z_confidence.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.horizontalSlider_z_confidence = QSlider(self.postavkeWidget)
        self.horizontalSlider_z_confidence.setObjectName(u"horizontalSlider_z_confidence")
        self.horizontalSlider_z_confidence.setGeometry(QRect(680, 100, 160, 22))
        self.horizontalSlider_z_confidence.setMaximum(100)
        self.horizontalSlider_z_confidence.setPageStep(1)
        self.horizontalSlider_z_confidence.setOrientation(Qt.Horizontal)
        self.horizontalSlider_z_confidence.setTickPosition(QSlider.TicksBelow)
        self.label_z_iouconfidence = QLabel(self.postavkeWidget)
        self.label_z_iouconfidence.setObjectName(u"label_z_iouconfidence")
        self.label_z_iouconfidence.setGeometry(QRect(500, 150, 181, 21))
        self.label_z_iouconfidence.setStyleSheet(u"font: 20pt \"Calibri\";")
        self.lineEdit_2 = QLineEdit(self.postavkeWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(210, 290, 161, 31))
        self.lineEdit_2.setStyleSheet(u"font-size: 20px;\n"
"padding: 0px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #545454;\n"
"border-radius: 6.5px;\n"
"font-weight: bold;")
        self.lineEdit_7 = QLineEdit(self.postavkeWidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(680, 240, 161, 31))
        self.lineEdit_7.setStyleSheet(u"font-size: 20px;\n"
"padding: 0px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #545454;\n"
"border-radius: 6.5px;\n"
"font-weight: bold;")
        self.lineEdit_8 = QLineEdit(self.postavkeWidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(680, 290, 161, 31))
        self.lineEdit_8.setStyleSheet(u"font-size: 20px;\n"
"padding: 0px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #545454;\n"
"border-radius: 6.5px;\n"
"font-weight: bold;")
        self.gumb_zatvori = QCommandLinkButton(self.postavkeWidget)
        self.gumb_zatvori.setObjectName(u"gumb_zatvori")
        self.gumb_zatvori.setGeometry(QRect(370, 410, 155, 60))
        self.gumb_zatvori.setStyleSheet(u"font: 700 20pt \"Calibri\";")
        icon4 = QIcon()
        icon4.addFile(u"./ui/IKONE/close-square-rounded-interface-symbol-with-a-cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.gumb_zatvori.setIcon(icon4)
        self.gumb_zatvori.setIconSize(QSize(51, 41))
        self.label_postavke_ukras5 = QLabel(self.postavkeWidget)
        self.label_postavke_ukras5.setObjectName(u"label_postavke_ukras5")
        self.label_postavke_ukras5.setGeometry(QRect(20, 410, 361, 31))
        self.label_postavke_ukras5.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.label_postavke_ukras6 = QLabel(self.postavkeWidget)
        self.label_postavke_ukras6.setObjectName(u"label_postavke_ukras6")
        self.label_postavke_ukras6.setGeometry(QRect(520, 410, 381, 31))
        self.label_postavke_ukras6.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.label_postavke_ukras3 = QLabel(self.postavkeWidget)
        self.label_postavke_ukras3.setObjectName(u"label_postavke_ukras3")
        self.label_postavke_ukras3.setGeometry(QRect(490, 190, 401, 31))
        self.label_postavke_ukras3.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.label_31 = QLineEdit(self.postavkeWidget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(380, 90, 45, 31))
        self.label_31.setStyleSheet(u"font-size: 18px;\n"
"padding: 0px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #545454;\n"
"border-radius: 6.5px;\n"
"font-weight: bold;")
        self.label_38 = QLineEdit(self.postavkeWidget)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(380, 150, 45, 31))
        self.label_38.setStyleSheet(u"font-size: 18px;\n"
"padding: 0px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #545454;\n"
"border-radius: 6.5px;\n"
"font-weight: bold;")
        self.label_39 = QLineEdit(self.postavkeWidget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(850, 140, 45, 31))
        self.label_39.setStyleSheet(u"font-size: 18px;\n"
"padding: 0px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #545454;\n"
"border-radius: 6.5px;\n"
"font-weight: bold;")
        self.label_40 = QLineEdit(self.postavkeWidget)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(850, 90, 45, 31))
        self.label_40.setStyleSheet(u"font-size: 18px;\n"
"padding: 0px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #545454;\n"
"border-radius: 6.5px;\n"
"font-weight: bold;")
        self.label_postavke_ukras1 = QLabel(self.postavkeWidget)
        self.label_postavke_ukras1.setObjectName(u"label_postavke_ukras1")
        self.label_postavke_ukras1.setGeometry(QRect(20, 190, 401, 31))
        self.label_postavke_ukras1.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.label_postavke_ukras2 = QLabel(self.postavkeWidget)
        self.label_postavke_ukras2.setObjectName(u"label_postavke_ukras2")
        self.label_postavke_ukras2.setGeometry(QRect(20, 320, 401, 31))
        self.label_postavke_ukras2.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.label_postavke_ukras4 = QLabel(self.postavkeWidget)
        self.label_postavke_ukras4.setObjectName(u"label_postavke_ukras4")
        self.label_postavke_ukras4.setGeometry(QRect(490, 320, 401, 31))
        self.label_postavke_ukras4.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(0, 0, 41, 41))
        self.toolButton.setAutoFillBackground(False)
        icon5 = QIcon()
        icon5.addFile(u"./ui/IKONE/filter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon5)
        self.toolButton.setIconSize(QSize(30, 37))
        self.toolButton.setCheckable(False)
        self.toolButton.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setArrowType(Qt.NoArrow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.label_ime.setText(QCoreApplication.translate("MainWindow", u"Ime", None))
        self.label_prezime.setText(QCoreApplication.translate("MainWindow", u"Prezime", None))
        self.label_datum.setText(QCoreApplication.translate("MainWindow", u"Godina ro\u0111enja", None))
        self.label_adresa.setText(QCoreApplication.translate("MainWindow", u"Adresa", None))
        self.label_telefon.setText(QCoreApplication.translate("MainWindow", u"Telefon", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.label_tip_auto.setText(QCoreApplication.translate("MainWindow", u"Tip automobila", None))
        self.label_br_sasije.setText(QCoreApplication.translate("MainWindow", u"Broj \u0161asije", None))
        self.label_osig_kuca.setText(QCoreApplication.translate("MainWindow", u"Osiguravaju\u0107a ku\u0107a", None))
        self.label_br_police.setText(QCoreApplication.translate("MainWindow", u"Broj police", None))
        self.gumb_desni.setText("")
        self.gumb_lijevi.setText("")
        self.kategorija_vlasnik.setText(QCoreApplication.translate("MainWindow", u"PODACI VLASNIKA", None))
        self.label_ukras1.setText(QCoreApplication.translate("MainWindow", u"___________________________________", None))
        self.kategorija_registracije.setText(QCoreApplication.translate("MainWindow", u"PODACI REGISTRACIJE", None))
        self.lineEdit_ime.setText("")
        self.slika_osobne.setText("")
        self.slika_datum.setText("")
        self.slika_adresa.setText("")
        self.slika_telefon.setText("")
        self.slika_email.setText("")
        self.slika_auto.setText("")
        self.slika_br_sasije.setText("")
        self.slika_osig_kuca.setText("")
        self.slika_br_police.setText("")
        self.lineEdit_prezime.setText("")
        self.lineEdit_datum.setText("")
        self.lineEdit_adresa.setText("")
        self.lineEdit_telefon.setText("")
        self.lineEdit_tip_auta.setText("")
        self.lineEdit_br_sasije.setText("")
        self.lineEdit_osig_kuca.setText("")
        self.lineEdit_br_police.setText("")
        self.label_ukras3.setText(QCoreApplication.translate("MainWindow", u"_________________________________", None))
        self.label_ukras2.setText(QCoreApplication.translate("MainWindow", u"____________________________________", None))
        self.label_ukras4.setText(QCoreApplication.translate("MainWindow", u"__________________________________", None))
#if QT_CONFIG(accessibility)
        self.label_prikaz_registracije.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.label_prikaz_registracije.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_prikaz_registracije.setText("")
        self.lineEdit_email.setText("")
        self.gumb_baza.setText(QCoreApplication.translate("MainWindow", u"DODAJ U BAZU", None))
        self.label_ukras5.setText(QCoreApplication.translate("MainWindow", u"___________________________________", None))
        self.label_ukras6.setText(QCoreApplication.translate("MainWindow", u"____________________________________", None))
        self.gumb_emitiranje_uzivo.setText(QCoreApplication.translate("MainWindow", u"Emitiranje u\u017eivo", None))
        self.checkBox_t_label.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.checkBox_t_confidence.setText(QCoreApplication.translate("MainWindow", u"Confidence", None))
        self.label_t_thickness.setText(QCoreApplication.translate("MainWindow", u"Line Thickness", None))
        self.label_t_resolution.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.label_t_confidence.setText(QCoreApplication.translate("MainWindow", u"Confidence", None))
        self.label_t_iouconfidence.setText(QCoreApplication.translate("MainWindow", u"IoU Confidence", None))
        self.kategorija_tablica.setText(QCoreApplication.translate("MainWindow", u"Prepoznavanje tablica", None))
        self.kategorija_znakova.setText(QCoreApplication.translate("MainWindow", u"Prepoznavanje znakova", None))
        self.label_z_resolution.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.label_z_thickness.setText(QCoreApplication.translate("MainWindow", u"Line Thickness", None))
        self.checkBox_z_label.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.checkBox_z_confidence.setText(QCoreApplication.translate("MainWindow", u"Confidence", None))
        self.label_z_confidence.setText(QCoreApplication.translate("MainWindow", u"Confidence", None))
        self.label_z_iouconfidence.setText(QCoreApplication.translate("MainWindow", u"IoU Confidence", None))
        self.gumb_zatvori.setText(QCoreApplication.translate("MainWindow", u"ZATVORI", None))
        self.label_postavke_ukras5.setText(QCoreApplication.translate("MainWindow", u"________________________________", None))
        self.label_postavke_ukras6.setText(QCoreApplication.translate("MainWindow", u"__________________________________", None))
        self.label_postavke_ukras3.setText(QCoreApplication.translate("MainWindow", u"------------------------------------", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"0,53", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"0,53", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"0,53", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"0,53", None))
        self.label_postavke_ukras1.setText(QCoreApplication.translate("MainWindow", u"------------------------------------", None))
        self.label_postavke_ukras2.setText(QCoreApplication.translate("MainWindow", u"------------------------------------", None))
        self.label_postavke_ukras4.setText(QCoreApplication.translate("MainWindow", u"------------------------------------", None))
        self.toolButton.setText("")
    # retranslateUi

