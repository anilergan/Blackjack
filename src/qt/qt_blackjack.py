# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_blackjack.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
from qt.resource import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(865, 815)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(865, 815))
        MainWindow.setMaximumSize(QSize(865, 815))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"background-color: transparent;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedwidget_content = QStackedWidget(self.centralwidget)
        self.stackedwidget_content.setObjectName(u"stackedwidget_content")
        sizePolicy.setHeightForWidth(self.stackedwidget_content.sizePolicy().hasHeightForWidth())
        self.stackedwidget_content.setSizePolicy(sizePolicy)
        self.stackedwidget_content.setMinimumSize(QSize(865, 815))
        self.stackedwidget_content.setMaximumSize(QSize(16777215, 16777215))
        self.stackedwidget_content.setStyleSheet(u"#page_1_menu  {\n"
"background-color:rgba(59,82,63,255);\n"
"}\n"
"\n"
"#page_2_game {\n"
"background-color: rgb(19,19,19)\n"
"}\n"
"\n"
"")
        self.stackedwidget_content.setFrameShape(QFrame.Shape.StyledPanel)
        self.stackedwidget_content.setFrameShadow(QFrame.Shadow.Raised)
        self.page_1_menu = QWidget()
        self.page_1_menu.setObjectName(u"page_1_menu")
        self.page_1_menu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.page_1_menu.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QGroupBox {\n"
"color: rgba(212,185,58,255);\n"
"background-color: transparent;\n"
"font: 700 16pt \"Arial\";\n"
"border:  2px solid rgb(45, 20, 9);\n"
"border-radius: 25px;\n"
"margin: 10px 0 0 0;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-position: top center; /* Ba\u015fl\u0131\u011f\u0131 ortalamak i\u00e7in */\n"
"    subcontrol-origin: margin;\n"
"	\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.page_1_menu)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(10, 20, 10, 20)
        self.frame_game_header = QFrame(self.page_1_menu)
        self.frame_game_header.setObjectName(u"frame_game_header")
        self.frame_game_header.setMinimumSize(QSize(0, 70))
        self.frame_game_header.setStyleSheet(u"#frame_game_header{\n"
"border:none;\n"
"}")
        self.frame_game_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_game_header.setFrameShadow(QFrame.Shadow.Raised)
        self.game_header = QLabel(self.frame_game_header)
        self.game_header.setObjectName(u"game_header")
        self.game_header.setGeometry(QRect(29, 0, 781, 60))
        self.game_header.setMinimumSize(QSize(0, 60))
        self.game_header.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setFamilies([u"Forte"])
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        self.game_header.setFont(font)
        self.game_header.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.game_header.setStyleSheet(u"\n"
"color: black;\n"
"font: 36pt \"Forte\";\n"
"\n"
"\n"
"")
        self.game_header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.by_anil_ergan = QLabel(self.frame_game_header)
        self.by_anil_ergan.setObjectName(u"by_anil_ergan")
        self.by_anil_ergan.setGeometry(QRect(149, 50, 541, 20))
        self.by_anil_ergan.setStyleSheet(u"font: italic 8pt \"Arial\";\n"
"color: rgb(12,12,12)")
        self.by_anil_ergan.raise_()
        self.game_header.raise_()

        self.verticalLayout_2.addWidget(self.frame_game_header)

        self.game_image = QLabel(self.page_1_menu)
        self.game_image.setObjectName(u"game_image")
        self.game_image.setMinimumSize(QSize(200, 200))
        self.game_image.setMaximumSize(QSize(200, 200))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        self.game_image.setFont(font1)
        self.game_image.setPixmap(QPixmap(u":/icons/game.png"))
        self.game_image.setScaledContents(True)
        self.game_image.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_2.addWidget(self.game_image, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_game_selection = QFrame(self.page_1_menu)
        self.frame_game_selection.setObjectName(u"frame_game_selection")
        self.frame_game_selection.setMinimumSize(QSize(0, 200))
        self.frame_game_selection.setStyleSheet(u"\n"
"#frame_game_selection, #frame_agent_game_selection, #frame_agent_game_selection_inner{\n"
"border:none;\n"
"}\n"
"\n"
"#frame_spacer{\n"
"border:none;\n"
"}\n"
"QPushButton::hover {\n"
"border: 2px solid rgba(212,185,58,255);\n"
"background-color: rgba(212,185,58,25);\n"
"}\n"
"\n"
"QPushButton{\n"
"font: 16pt \"Arial\";\n"
"border: 2px solid  rgb(120,124,116);\n"
"border-radius: 20px;\n"
"color: rgba(212,185,58,255);\n"
"background-color: rgba(39,52,45,255);\n"
"}\n"
"\n"
"#button_train_agent::hover {\n"
"border: 2px solid rgba(212,185,58,255);\n"
"background-color: rgba(48, 12, 20, 100);\n"
"}\n"
"\n"
"#button_train_agent{\n"
"font: 16pt \"Arial\";\n"
"border: 2px solid  rgb(120,124,116);\n"
"border-radius: 20px;\n"
"color: rgba(212,185,58,255);\n"
"background-color: rgba(48, 12, 20, 255);\n"
"}")
        self.frame_game_selection.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_game_selection.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_game_selection)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 30, 10, 10)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)

        self.button_train_agent = QPushButton(self.frame_game_selection)
        self.button_train_agent.setObjectName(u"button_train_agent")
        self.button_train_agent.setMinimumSize(QSize(200, 40))
        self.button_train_agent.setMaximumSize(QSize(200, 40))
        self.button_train_agent.setFont(font1)
        self.button_train_agent.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_train_agent.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_train_agent.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.button_train_agent, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_one_player_game = QPushButton(self.frame_game_selection)
        self.button_one_player_game.setObjectName(u"button_one_player_game")
        self.button_one_player_game.setMinimumSize(QSize(200, 40))
        self.button_one_player_game.setMaximumSize(QSize(200, 40))
        self.button_one_player_game.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_one_player_game.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_one_player_game.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.button_one_player_game, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_agent_game = QFrame(self.frame_game_selection)
        self.frame_agent_game.setObjectName(u"frame_agent_game")
        self.frame_agent_game.setMinimumSize(QSize(0, 100))
        self.frame_agent_game.setStyleSheet(u"#frame_agent_game{\n"
"border:none;\n"
"\n"
"}")
        self.frame_agent_game.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_agent_game.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_agent_game)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_agent_game = QLabel(self.frame_agent_game)
        self.label_agent_game.setObjectName(u"label_agent_game")
        self.label_agent_game.setStyleSheet(u"	font: 700 20pt \"Forte\";\n"
"	color: rgb(120,124,116);")

        self.verticalLayout_20.addWidget(self.label_agent_game, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget_agent_game_selection = QStackedWidget(self.frame_agent_game)
        self.stackedWidget_agent_game_selection.setObjectName(u"stackedWidget_agent_game_selection")
        self.stackedWidget_agent_game_selection.setMinimumSize(QSize(250, 125))
        self.stackedWidget_agent_game_selection.setMaximumSize(QSize(250, 125))
        self.stackedWidget_agent_game_selection.setStyleSheet(u"#page_1_agent_game_selection, #page_2_single_agent, #page_3_multiple_agent{\n"
"background-color:  rgba(120,124,116,25);\n"
"border:  2px solid rgb(120,124,116);\n"
"border-radius: 20px;\n"
"\n"
"}")
        self.page_1_agent_game_selection = QWidget()
        self.page_1_agent_game_selection.setObjectName(u"page_1_agent_game_selection")
        self.verticalLayout_7 = QVBoxLayout(self.page_1_agent_game_selection)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.button_one_player_game_2 = QPushButton(self.page_1_agent_game_selection)
        self.button_one_player_game_2.setObjectName(u"button_one_player_game_2")
        self.button_one_player_game_2.setMinimumSize(QSize(200, 40))
        self.button_one_player_game_2.setMaximumSize(QSize(200, 40))
        self.button_one_player_game_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_one_player_game_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_one_player_game_2.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.button_one_player_game_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_one_player_game_3 = QPushButton(self.page_1_agent_game_selection)
        self.button_one_player_game_3.setObjectName(u"button_one_player_game_3")
        self.button_one_player_game_3.setMinimumSize(QSize(200, 40))
        self.button_one_player_game_3.setMaximumSize(QSize(200, 40))
        self.button_one_player_game_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_one_player_game_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_one_player_game_3.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.button_one_player_game_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget_agent_game_selection.addWidget(self.page_1_agent_game_selection)
        self.page_2_single_agent = QWidget()
        self.page_2_single_agent.setObjectName(u"page_2_single_agent")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.page_2_single_agent.sizePolicy().hasHeightForWidth())
        self.page_2_single_agent.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.page_2_single_agent)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.button_single_agent_back = QPushButton(self.page_2_single_agent)
        self.button_single_agent_back.setObjectName(u"button_single_agent_back")
        self.button_single_agent_back.setMinimumSize(QSize(0, 30))
        self.button_single_agent_back.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_single_agent_back.setStyleSheet(u"QPushButton::hover {\n"
"border-radius: 0px;\n"
"border-top-left-radius: 20px;\n"
"border-top-right-radius: 20px;\n"
"background-color: rgba(120,124,116,50);\n"
"}\n"
"\n"
"QPushButton{\n"
"font: 16pt \"Arial\";\n"
"border: 2px solid rgba(212,185,58,0);\n"
"color: rgb(120,124,116);\n"
"background-color: transparent;\n"
"}")

        self.verticalLayout_6.addWidget(self.button_single_agent_back)

        self.comboBox_agent_selection = QComboBox(self.page_2_single_agent)
        self.comboBox_agent_selection.addItem("")
        self.comboBox_agent_selection.addItem("")
        self.comboBox_agent_selection.addItem("")
        self.comboBox_agent_selection.addItem("")
        self.comboBox_agent_selection.setObjectName(u"comboBox_agent_selection")
        sizePolicy1.setHeightForWidth(self.comboBox_agent_selection.sizePolicy().hasHeightForWidth())
        self.comboBox_agent_selection.setSizePolicy(sizePolicy1)
        self.comboBox_agent_selection.setMinimumSize(QSize(0, 0))
        self.comboBox_agent_selection.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_agent_selection.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_agent_selection.setStyleSheet(u"QComboBox {\n"
"    font: 14pt \"Arial\";\n"
"    color: rgba(212,185,58,255);\n"
"    background-color: transparent;\n"
"	border:none;\n"
"\n"
"}\n"
"\n"
"QComboBox::hover{\n"
"	background-color:  rgba(212,185,58,25);\n"
"	border-bottom-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"	border-right: 2px solid rgba(212,185,58,255);\n"
"	border-left: 2px solid rgba(212,185,58,255);\n"
"	border-bottom: 2px solid rgba(212,185,58,255);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid rgba(212,185,58,255); /* Genel kenarl\u0131k */\n"
"    background-color: rgba(39,52,45,255); /* Arka plan rengi */\n"
"    color: rgb(120,124,116); /* Genel metin rengi */\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"/* Se\u00e7ili \u00f6\u011feyi \u00f6zelle\u015ftirmek i\u00e7in eklenebilecek k\u0131s\u0131m */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	color: rgba(136,182,189,255);\n"
"\n"
"}\n"
"\n"
"")

        self.verticalLayout_6.addWidget(self.comboBox_agent_selection)

        self.stackedWidget_agent_game_selection.addWidget(self.page_2_single_agent)
        self.page_3_multiple_agent = QWidget()
        self.page_3_multiple_agent.setObjectName(u"page_3_multiple_agent")
        self.verticalLayout_15 = QVBoxLayout(self.page_3_multiple_agent)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.button_single_agent_back_2 = QPushButton(self.page_3_multiple_agent)
        self.button_single_agent_back_2.setObjectName(u"button_single_agent_back_2")
        self.button_single_agent_back_2.setMinimumSize(QSize(0, 30))
        self.button_single_agent_back_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_single_agent_back_2.setStyleSheet(u"QPushButton::hover {\n"
"border-radius: 0px;\n"
"border-top-left-radius: 20px;\n"
"border-top-right-radius: 20px;\n"
"background-color: rgba(120,124,116,50);\n"
"}\n"
"\n"
"QPushButton{\n"
"font: 16pt \"Arial\";\n"
"border: 2px solid rgba(212,185,58,0);\n"
"color: rgb(120,124,116);\n"
"background-color: transparent;\n"
"}")

        self.verticalLayout_15.addWidget(self.button_single_agent_back_2)

        self.comboBox_agent_selection_2 = QComboBox(self.page_3_multiple_agent)
        self.comboBox_agent_selection_2.addItem("")
        self.comboBox_agent_selection_2.addItem("")
        self.comboBox_agent_selection_2.addItem("")
        self.comboBox_agent_selection_2.addItem("")
        self.comboBox_agent_selection_2.setObjectName(u"comboBox_agent_selection_2")
        sizePolicy1.setHeightForWidth(self.comboBox_agent_selection_2.sizePolicy().hasHeightForWidth())
        self.comboBox_agent_selection_2.setSizePolicy(sizePolicy1)
        self.comboBox_agent_selection_2.setMinimumSize(QSize(0, 0))
        self.comboBox_agent_selection_2.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_agent_selection_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_agent_selection_2.setStyleSheet(u"QComboBox {\n"
"    font: 14pt \"Arial\";\n"
"    color: rgba(212,185,58,255);\n"
"    background-color: transparent;\n"
"	border:none;\n"
"\n"
"}\n"
"\n"
"QComboBox::hover{\n"
"	background-color:  rgba(212,185,58,25);\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	border-right: 2px solid rgba(212,185,58,255);\n"
"	border-left: 2px solid rgba(212,185,58,255);\n"
"\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid rgba(212,185,58,255); /* Genel kenarl\u0131k */\n"
"    background-color: rgba(39,52,45,255); /* Arka plan rengi */\n"
"    color: rgb(120,124,116); /* Genel metin rengi */\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"/* Se\u00e7ili \u00f6\u011feyi \u00f6zelle\u015ftirmek i\u00e7in eklenebilecek k\u0131s\u0131m */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	color: rgba(136,182,189,255);\n"
"\n"
"}\n"
"\n"
"")

        self.verticalLayout_15.addWidget(self.comboBox_agent_selection_2)

        self.comboBox_agent_selection_3 = QComboBox(self.page_3_multiple_agent)
        self.comboBox_agent_selection_3.addItem("")
        self.comboBox_agent_selection_3.addItem("")
        self.comboBox_agent_selection_3.addItem("")
        self.comboBox_agent_selection_3.addItem("")
        self.comboBox_agent_selection_3.setObjectName(u"comboBox_agent_selection_3")
        sizePolicy1.setHeightForWidth(self.comboBox_agent_selection_3.sizePolicy().hasHeightForWidth())
        self.comboBox_agent_selection_3.setSizePolicy(sizePolicy1)
        self.comboBox_agent_selection_3.setMinimumSize(QSize(0, 0))
        self.comboBox_agent_selection_3.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_agent_selection_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_agent_selection_3.setStyleSheet(u"QComboBox {\n"
"    font: 14pt \"Arial\";\n"
"    color: rgba(212,185,58,255);\n"
"    background-color: transparent;\n"
"	border:none;\n"
"\n"
"}\n"
"\n"
"QComboBox::hover{\n"
"	background-color:  rgba(212,185,58,25);\n"
"	border-bottom-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"	border-right: 2px solid rgba(212,185,58,255);\n"
"	border-left: 2px solid rgba(212,185,58,255);\n"
"	border-bottom: 2px solid rgba(212,185,58,255);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid rgba(212,185,58,255); /* Genel kenarl\u0131k */\n"
"    background-color: rgba(39,52,45,255); /* Arka plan rengi */\n"
"    color: rgb(120,124,116); /* Genel metin rengi */\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"/* Se\u00e7ili \u00f6\u011feyi \u00f6zelle\u015ftirmek i\u00e7in eklenebilecek k\u0131s\u0131m */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	color: rgba(136,182,189,255);\n"
"\n"
"}\n"
"\n"
"")

        self.verticalLayout_15.addWidget(self.comboBox_agent_selection_3)

        self.stackedWidget_agent_game_selection.addWidget(self.page_3_multiple_agent)

        self.verticalLayout_20.addWidget(self.stackedWidget_agent_game_selection, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame_agent_game)


        self.verticalLayout_2.addWidget(self.frame_game_selection)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.button_exit = QPushButton(self.page_1_menu)
        self.button_exit.setObjectName(u"button_exit")
        self.button_exit.setMinimumSize(QSize(90, 35))
        self.button_exit.setMaximumSize(QSize(90, 35))
        self.button_exit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_exit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_exit.setStyleSheet(u"\n"
"#button_exit{\n"
"font: 16pt \"Arial\";\n"
"border: 2px solid rgba(212, 68, 58,255);\n"
"border-radius: 15px;\n"
"color: rgba(212, 68, 58,255);\n"
"background-color: rgba(212, 68, 58,50)\n"
"}\n"
"\n"
"#button_exit::hover {\n"
"background-color:rgba(212, 68, 58,100)\n"
"\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.button_exit, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.stackedwidget_content.addWidget(self.page_1_menu)
        self.page_2_game = QWidget()
        self.page_2_game.setObjectName(u"page_2_game")
        self.page_2_game.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.page_2_game)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 20, 0, 20)
        self.frame_announce = QFrame(self.page_2_game)
        self.frame_announce.setObjectName(u"frame_announce")
        self.frame_announce.setMinimumSize(QSize(0, 50))
        self.frame_announce.setStyleSheet(u"#frame_announce{\n"
"border:none;}")
        self.frame_announce.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_announce.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_announce)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.frame_announce_inner = QFrame(self.frame_announce)
        self.frame_announce_inner.setObjectName(u"frame_announce_inner")
        self.frame_announce_inner.setMinimumSize(QSize(0, 55))
        self.frame_announce_inner.setMaximumSize(QSize(16777215, 55))
        self.frame_announce_inner.setStyleSheet(u"#frame_announce_inner{\n"
"border-radius: 25px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.85 rgb(48, 12, 20),  stop:1 rgba(212,185,58,40));\n"
"\n"
"}\n"
"\n"
"#label_announce {\n"
"font: 700 28pt \"Forte\";\n"
"}\n"
"\n"
"#label_cd {\n"
"font: 700 34pt \"Forte\";\n"
"color: rgba(212,185,58,255);\n"
"}\n"
"")
        self.frame_announce_inner.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_announce_inner.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_announce_inner)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.label_announce = QLabel(self.frame_announce_inner)
        self.label_announce.setObjectName(u"label_announce")
        self.label_announce.setMinimumSize(QSize(0, 50))
        self.label_announce.setMaximumSize(QSize(16777215, 50))
        self.label_announce.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_announce.setScaledContents(False)
        self.label_announce.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_announce)

        self.label_cd = QLabel(self.frame_announce_inner)
        self.label_cd.setObjectName(u"label_cd")
        self.label_cd.setEnabled(True)
        self.label_cd.setMinimumSize(QSize(50, 50))
        self.label_cd.setMaximumSize(QSize(50, 50))
        self.label_cd.setTextFormat(Qt.TextFormat.PlainText)
        self.label_cd.setScaledContents(False)
        self.label_cd.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_cd)


        self.horizontalLayout_8.addWidget(self.frame_announce_inner)


        self.verticalLayout_4.addWidget(self.frame_announce)

        self.frame_content = QFrame(self.page_2_game)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setMinimumSize(QSize(0, 0))
        self.frame_content.setMaximumSize(QSize(16777209, 700))
        self.frame_content.setStyleSheet(u"#frame_content{\n"
"border:none;\n"
"}")
        self.frame_content.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_content)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 10, 0)
        self.frame_game = QFrame(self.frame_content)
        self.frame_game.setObjectName(u"frame_game")
        self.frame_game.setMinimumSize(QSize(600, 700))
        self.frame_game.setMaximumSize(QSize(600, 700))
        self.frame_game.setToolTipDuration(0)
        self.frame_game.setStyleSheet(u"#frame_game * {\n"
"background-color: transparent;\n"
"color: rgba(212,185,58,255);\n"
"font: 13pt \"Forte\";\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"\n"
"#frame_game {\n"
"background-color:  rgba(39,52,45,255);\n"
"border-right: 30px solid rgb(45, 20, 9);\n"
"border-top: 30px solid rgb(45, 20, 9);\n"
"border-bottom: 30px solid rgb(45, 20, 9);\n"
"border-bottom-right-radius: 350px;\n"
"border-top-right-radius: 350px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame_game.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_game.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_game.setLineWidth(0)
        self.gridLayout = QGridLayout(self.frame_game)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_table = QFrame(self.frame_game)
        self.frame_table.setObjectName(u"frame_table")
        self.frame_table.setMinimumSize(QSize(590, 330))
        self.frame_table.setMaximumSize(QSize(600, 330))
        self.frame_table.setStyleSheet(u"\n"
"#label_blackjack_text_1, #label_blackjack_text_2, #label_blackjack_text_3, #label_blackjack_text_4, #label_blackjack_text_5, #label_blackjack_text_6, #label_blackjack_text_7, #label_blackjack_text_8, #label_blackjack_text_9, #label_blackjack_text_10{\n"
"font: 28pt \"Forte\";\n"
"color: rgba(212,185,58,40);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame_table.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_table.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_dealer_cards = QFrame(self.frame_table)
        self.frame_dealer_cards.setObjectName(u"frame_dealer_cards")
        self.frame_dealer_cards.setGeometry(QRect(5, 5, 210, 320))
        self.frame_dealer_cards.setMinimumSize(QSize(210, 0))
        self.frame_dealer_cards.setMaximumSize(QSize(210, 16777215))
        self.frame_dealer_cards.setStyleSheet(u"#frame_dealer_cards{\n"
"border-top-right-radius: 160px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-right-radius:160px;\n"
"border-bottom-left-radius: 0px;\n"
"background: rgba(212,185,58,20);\n"
"}\n"
"\n"
"#frame_dealer_cards * {\n"
"background-color: transparent;\n"
"border:none;\n"
"}\n"
"\n"
"#label_dealer_total {\n"
"font: 16pt \"Forte\";\n"
"color: white;\n"
"}\n"
"\n"
"#frame_dealer_budget * {\n"
"font: 16pt \"Forte\";\n"
"color: rgba(212,185,58,255);\n"
"}\n"
"\n"
"#label_dealer_total {\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 0, 0, 0), stop: 0.7 rgba(255,255,255,25), stop:0.85 rgba(255,255,255,55), stop:1 rgba(255,255,255,105));\n"
"border:1 solid rgb(144,144,144)\n"
"}\n"
"\n"
"#label_dealer_budget_text {\n"
"font: 10pt \"Forte\";\n"
"}\n"
"\n"
"\n"
"#label_dealer_total_text {\n"
"font: 10pt \"Forte\";\n"
"color: rgba(255,255,255,150)\n"
"}")
        self.frame_dealer_cards.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dealer_cards.setFrameShadow(QFrame.Shadow.Raised)
        self.label_dealer_card9 = QLabel(self.frame_dealer_cards)
        self.label_dealer_card9.setObjectName(u"label_dealer_card9")
        self.label_dealer_card9.setGeometry(QRect(130, 120, 48, 58))
        self.label_dealer_card9.setPixmap(QPixmap(u":/cards/resources/8.png"))
        self.label_dealer_card9.setScaledContents(True)
        self.label_dealer_card4 = QLabel(self.frame_dealer_cards)
        self.label_dealer_card4.setObjectName(u"label_dealer_card4")
        self.label_dealer_card4.setGeometry(QRect(55, 130, 48, 58))
        self.label_dealer_card4.setPixmap(QPixmap(u":/cards/resources/8.png"))
        self.label_dealer_card4.setScaledContents(True)
        self.label_dealer_card6 = QLabel(self.frame_dealer_cards)
        self.label_dealer_card6.setObjectName(u"label_dealer_card6")
        self.label_dealer_card6.setGeometry(QRect(85, 130, 48, 58))
        self.label_dealer_card6.setPixmap(QPixmap(u":/cards/resources/8.png"))
        self.label_dealer_card6.setScaledContents(True)
        self.label_dealer_card2 = QLabel(self.frame_dealer_cards)
        self.label_dealer_card2.setObjectName(u"label_dealer_card2")
        self.label_dealer_card2.setGeometry(QRect(25, 130, 48, 58))
        self.label_dealer_card2.setPixmap(QPixmap(u":/cards/resources/8.png"))
        self.label_dealer_card2.setScaledContents(True)
        self.label_dealer_card5 = QLabel(self.frame_dealer_cards)
        self.label_dealer_card5.setObjectName(u"label_dealer_card5")
        self.label_dealer_card5.setGeometry(QRect(70, 120, 48, 58))
        self.label_dealer_card5.setPixmap(QPixmap(u":/cards/resources/8.png"))
        self.label_dealer_card5.setScaledContents(True)
        self.label_dealer_card7 = QLabel(self.frame_dealer_cards)
        self.label_dealer_card7.setObjectName(u"label_dealer_card7")
        self.label_dealer_card7.setGeometry(QRect(100, 120, 48, 58))
        self.label_dealer_card7.setPixmap(QPixmap(u":/cards/resources/8.png"))
        self.label_dealer_card7.setScaledContents(True)
        self.label_dealer_card8 = QLabel(self.frame_dealer_cards)
        self.label_dealer_card8.setObjectName(u"label_dealer_card8")
        self.label_dealer_card8.setGeometry(QRect(115, 130, 48, 58))
        self.label_dealer_card8.setPixmap(QPixmap(u":/cards/resources/8.png"))
        self.label_dealer_card8.setScaledContents(True)
        self.label_dealer_card1 = QLabel(self.frame_dealer_cards)
        self.label_dealer_card1.setObjectName(u"label_dealer_card1")
        self.label_dealer_card1.setGeometry(QRect(10, 120, 48, 58))
        self.label_dealer_card1.setPixmap(QPixmap(u":/cards/resources/8.png"))
        self.label_dealer_card1.setScaledContents(True)
        self.label_dealer_card10 = QLabel(self.frame_dealer_cards)
        self.label_dealer_card10.setObjectName(u"label_dealer_card10")
        self.label_dealer_card10.setGeometry(QRect(145, 130, 48, 58))
        self.label_dealer_card10.setPixmap(QPixmap(u":/cards/resources/8.png"))
        self.label_dealer_card10.setScaledContents(True)
        self.label_dealer_card3 = QLabel(self.frame_dealer_cards)
        self.label_dealer_card3.setObjectName(u"label_dealer_card3")
        self.label_dealer_card3.setGeometry(QRect(40, 120, 48, 58))
        self.label_dealer_card3.setPixmap(QPixmap(u":/cards/resources/8.png"))
        self.label_dealer_card3.setScaledContents(True)
        self.frame_dealer_total_inner = QFrame(self.frame_dealer_cards)
        self.frame_dealer_total_inner.setObjectName(u"frame_dealer_total_inner")
        self.frame_dealer_total_inner.setGeometry(QRect(70, 210, 50, 50))
        self.frame_dealer_total_inner.setMinimumSize(QSize(50, 50))
        self.frame_dealer_total_inner.setMaximumSize(QSize(50, 50))
        self.frame_dealer_total_inner.setStyleSheet(u"")
        self.frame_dealer_total_inner.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dealer_total_inner.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_dealer_total_inner)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_dealer_total_text = QLabel(self.frame_dealer_total_inner)
        self.label_dealer_total_text.setObjectName(u"label_dealer_total_text")
        self.label_dealer_total_text.setMaximumSize(QSize(60, 16777215))
        self.label_dealer_total_text.setStyleSheet(u"#label_stand{\n"
"	font: 13pt \"Forte\";\n"
"	color: rgba(255,255,255,150);\n"
"	background-color: transparent;\n"
"}")
        self.label_dealer_total_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_dealer_total_text, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_dealer_total = QLabel(self.frame_dealer_total_inner)
        self.label_dealer_total.setObjectName(u"label_dealer_total")
        self.label_dealer_total.setMinimumSize(QSize(30, 25))
        self.label_dealer_total.setMaximumSize(QSize(30, 25))
        self.label_dealer_total.setStyleSheet(u"")
        self.label_dealer_total.setScaledContents(True)
        self.label_dealer_total.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_dealer_total, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_13)

        self.label_dealer_status = QLabel(self.frame_dealer_cards)
        self.label_dealer_status.setObjectName(u"label_dealer_status")
        self.label_dealer_status.setGeometry(QRect(70, 45, 50, 50))
        self.label_dealer_status.setMinimumSize(QSize(50, 50))
        self.label_dealer_status.setMaximumSize(QSize(50, 50))
        self.label_dealer_status.setScaledContents(True)
        self.label_dealer_deck_top = QLabel(self.frame_dealer_cards)
        self.label_dealer_deck_top.setObjectName(u"label_dealer_deck_top")
        self.label_dealer_deck_top.setGeometry(QRect(10, 35, 55, 65))
        self.label_dealer_deck_top.setPixmap(QPixmap(u":/cards/resources/deck.png"))
        self.label_dealer_deck_top.setScaledContents(True)
        self.label_dealer_deck_bot = QLabel(self.frame_dealer_cards)
        self.label_dealer_deck_bot.setObjectName(u"label_dealer_deck_bot")
        self.label_dealer_deck_bot.setGeometry(QRect(10, 210, 55, 65))
        self.label_dealer_deck_bot.setPixmap(QPixmap(u":/cards/resources/deck.png"))
        self.label_dealer_deck_bot.setScaledContents(True)
        self.frame_dealer_total_inner.raise_()
        self.label_dealer_status.raise_()
        self.label_dealer_card1.raise_()
        self.label_dealer_card2.raise_()
        self.label_dealer_card3.raise_()
        self.label_dealer_card4.raise_()
        self.label_dealer_card5.raise_()
        self.label_dealer_card6.raise_()
        self.label_dealer_card7.raise_()
        self.label_dealer_card8.raise_()
        self.label_dealer_card9.raise_()
        self.label_dealer_card10.raise_()
        self.label_dealer_deck_top.raise_()
        self.label_dealer_deck_bot.raise_()
        self.label_blackjack_text_1 = QLabel(self.frame_table)
        self.label_blackjack_text_1.setObjectName(u"label_blackjack_text_1")
        self.label_blackjack_text_1.setGeometry(QRect(130, 10, 45, 45))
        self.label_blackjack_text_1.setMinimumSize(QSize(45, 45))
        self.label_blackjack_text_1.setMaximumSize(QSize(30, 30))
        self.label_blackjack_text_1.setStyleSheet(u"")
        self.label_blackjack_text_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_blackjack_text_2 = QLabel(self.frame_table)
        self.label_blackjack_text_2.setObjectName(u"label_blackjack_text_2")
        self.label_blackjack_text_2.setGeometry(QRect(157, 33, 45, 45))
        self.label_blackjack_text_2.setMinimumSize(QSize(45, 45))
        self.label_blackjack_text_2.setMaximumSize(QSize(30, 30))
        self.label_blackjack_text_2.setStyleSheet(u"")
        self.label_blackjack_text_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_blackjack_text_3 = QLabel(self.frame_table)
        self.label_blackjack_text_3.setObjectName(u"label_blackjack_text_3")
        self.label_blackjack_text_3.setGeometry(QRect(180, 65, 45, 45))
        self.label_blackjack_text_3.setMinimumSize(QSize(45, 45))
        self.label_blackjack_text_3.setMaximumSize(QSize(30, 30))
        self.label_blackjack_text_3.setStyleSheet(u"")
        self.label_blackjack_text_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_blackjack_text_4 = QLabel(self.frame_table)
        self.label_blackjack_text_4.setObjectName(u"label_blackjack_text_4")
        self.label_blackjack_text_4.setGeometry(QRect(193, 102, 45, 45))
        self.label_blackjack_text_4.setMinimumSize(QSize(45, 45))
        self.label_blackjack_text_4.setMaximumSize(QSize(30, 30))
        self.label_blackjack_text_4.setStyleSheet(u"")
        self.label_blackjack_text_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_blackjack_text_5 = QLabel(self.frame_table)
        self.label_blackjack_text_5.setObjectName(u"label_blackjack_text_5")
        self.label_blackjack_text_5.setGeometry(QRect(200, 140, 45, 45))
        self.label_blackjack_text_5.setMinimumSize(QSize(45, 45))
        self.label_blackjack_text_5.setMaximumSize(QSize(30, 30))
        self.label_blackjack_text_5.setStyleSheet(u"")
        self.label_blackjack_text_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_blackjack_text_6 = QLabel(self.frame_table)
        self.label_blackjack_text_6.setObjectName(u"label_blackjack_text_6")
        self.label_blackjack_text_6.setGeometry(QRect(193, 178, 45, 45))
        self.label_blackjack_text_6.setMinimumSize(QSize(45, 45))
        self.label_blackjack_text_6.setMaximumSize(QSize(30, 30))
        self.label_blackjack_text_6.setStyleSheet(u"")
        self.label_blackjack_text_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_blackjack_text_7 = QLabel(self.frame_table)
        self.label_blackjack_text_7.setObjectName(u"label_blackjack_text_7")
        self.label_blackjack_text_7.setGeometry(QRect(180, 215, 45, 45))
        self.label_blackjack_text_7.setMinimumSize(QSize(45, 45))
        self.label_blackjack_text_7.setMaximumSize(QSize(30, 30))
        self.label_blackjack_text_7.setStyleSheet(u"")
        self.label_blackjack_text_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_blackjack_text_8 = QLabel(self.frame_table)
        self.label_blackjack_text_8.setObjectName(u"label_blackjack_text_8")
        self.label_blackjack_text_8.setGeometry(QRect(157, 247, 45, 45))
        self.label_blackjack_text_8.setMinimumSize(QSize(45, 45))
        self.label_blackjack_text_8.setMaximumSize(QSize(30, 30))
        self.label_blackjack_text_8.setStyleSheet(u"")
        self.label_blackjack_text_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_blackjack_text_9 = QLabel(self.frame_table)
        self.label_blackjack_text_9.setObjectName(u"label_blackjack_text_9")
        self.label_blackjack_text_9.setGeometry(QRect(130, 275, 45, 45))
        self.label_blackjack_text_9.setMinimumSize(QSize(45, 45))
        self.label_blackjack_text_9.setMaximumSize(QSize(30, 30))
        self.label_blackjack_text_9.setStyleSheet(u"")
        self.label_blackjack_text_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_seat1_chips = QFrame(self.frame_table)
        self.frame_seat1_chips.setObjectName(u"frame_seat1_chips")
        self.frame_seat1_chips.setGeometry(QRect(250, 260, 106, 60))
        self.frame_seat1_chips.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_chips.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_seat1_chips)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_seat1_chips_image = QLabel(self.frame_seat1_chips)
        self.label_seat1_chips_image.setObjectName(u"label_seat1_chips_image")
        self.label_seat1_chips_image.setMinimumSize(QSize(40, 40))
        self.label_seat1_chips_image.setMaximumSize(QSize(40, 40))
        self.label_seat1_chips_image.setStyleSheet(u"")
        self.label_seat1_chips_image.setScaledContents(True)

        self.horizontalLayout_26.addWidget(self.label_seat1_chips_image)

        self.label_seat1_chips_image_2 = QLabel(self.frame_seat1_chips)
        self.label_seat1_chips_image_2.setObjectName(u"label_seat1_chips_image_2")
        self.label_seat1_chips_image_2.setMinimumSize(QSize(40, 40))
        self.label_seat1_chips_image_2.setMaximumSize(QSize(40, 40))
        self.label_seat1_chips_image_2.setScaledContents(True)

        self.horizontalLayout_26.addWidget(self.label_seat1_chips_image_2)

        self.frame_seat2_chips = QFrame(self.frame_table)
        self.frame_seat2_chips.setObjectName(u"frame_seat2_chips")
        self.frame_seat2_chips.setGeometry(QRect(250, 10, 106, 60))
        self.frame_seat2_chips.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_chips.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_seat2_chips)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_seat2_chips_image = QLabel(self.frame_seat2_chips)
        self.label_seat2_chips_image.setObjectName(u"label_seat2_chips_image")
        self.label_seat2_chips_image.setMinimumSize(QSize(40, 40))
        self.label_seat2_chips_image.setMaximumSize(QSize(40, 40))
        self.label_seat2_chips_image.setStyleSheet(u"")
        self.label_seat2_chips_image.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.label_seat2_chips_image)

        self.label_seat2_chips_image_2 = QLabel(self.frame_seat2_chips)
        self.label_seat2_chips_image_2.setObjectName(u"label_seat2_chips_image_2")
        self.label_seat2_chips_image_2.setMinimumSize(QSize(40, 40))
        self.label_seat2_chips_image_2.setMaximumSize(QSize(40, 40))
        self.label_seat2_chips_image_2.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.label_seat2_chips_image_2)


        self.gridLayout.addWidget(self.frame_table, 1, 0, 1, 1)

        self.frame_seat1 = QFrame(self.frame_game)
        self.frame_seat1.setObjectName(u"frame_seat1")
        self.frame_seat1.setMinimumSize(QSize(360, 150))
        self.frame_seat1.setMaximumSize(QSize(360, 150))
        self.frame_seat1.setStyleSheet(u"#frame_seat1_gainloss, #frame_seat1_budget{\n"
"border:none;\n"
"}\n"
"\n"
"#frame_seat1_cards {\n"
"background-color: rgba(0,0,0,40);\n"
"border-radius: 20;\n"
"}\n"
"\n"
"#frame_seat1_cards * {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#label_seat1_total {\n"
"font: 16pt \"Forte\";\n"
"color: white;\n"
"}\n"
"\n"
"#frame_seat1_budget * {\n"
"font: 16pt \"Forte\";\n"
"color: rgba(212,185,58,255);\n"
"}\n"
"\n"
"#frame_seat1_budget_amount {\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 0), stop: 0.7 rgba(212,185,58,25), stop:0.85 rgba(212,185,58,50), stop:1 rgba(212,185,58,75));\n"
"border: 1 solid rgb(104,102,50);\n"
"}\n"
"\n"
"#label_seat1_budget_text {\n"
"font: 10pt \"Forte\";\n"
"}\n"
"\n"
"#label_seat1_total {\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 0), stop: 0.7 rgba(255,255,255,25), stop:0.85 rgba(255,255,255,50), stop:1 rgba(255,255,"
                        "255,75));\n"
"border:1 solid rgb(144,144,144)\n"
"}\n"
"\n"
"#label_seat1_total_text {\n"
"font: 10pt \"Forte\";\n"
"color: rgba(255,255,255,150)\n"
"}\n"
"\n"
"\n"
"")
        self.frame_seat1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_seat1)
        self.horizontalLayout_20.setSpacing(5)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(10, 0, 0, 5)
        self.frame_seat1_gainloss = QFrame(self.frame_seat1)
        self.frame_seat1_gainloss.setObjectName(u"frame_seat1_gainloss")
        self.frame_seat1_gainloss.setMinimumSize(QSize(60, 140))
        self.frame_seat1_gainloss.setMaximumSize(QSize(60, 140))
        self.frame_seat1_gainloss.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_gainloss.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_seat1_gainloss)
        self.verticalLayout_22.setSpacing(5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 5, 0, 20)
        self.label_seat1_budget_chips = QLabel(self.frame_seat1_gainloss)
        self.label_seat1_budget_chips.setObjectName(u"label_seat1_budget_chips")
        self.label_seat1_budget_chips.setMinimumSize(QSize(50, 50))
        self.label_seat1_budget_chips.setMaximumSize(QSize(50, 50))
        self.label_seat1_budget_chips.setStyleSheet(u"")
        self.label_seat1_budget_chips.setLineWidth(1)
        self.label_seat1_budget_chips.setScaledContents(True)
        self.label_seat1_budget_chips.setMargin(0)

        self.verticalLayout_22.addWidget(self.label_seat1_budget_chips, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_21)

        self.label_seat1_martini = QLabel(self.frame_seat1_gainloss)
        self.label_seat1_martini.setObjectName(u"label_seat1_martini")
        self.label_seat1_martini.setMinimumSize(QSize(50, 50))
        self.label_seat1_martini.setMaximumSize(QSize(50, 50))
        self.label_seat1_martini.setScaledContents(True)

        self.verticalLayout_22.addWidget(self.label_seat1_martini, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_20.addWidget(self.frame_seat1_gainloss)

        self.frame_seat1_cards = QFrame(self.frame_seat1)
        self.frame_seat1_cards.setObjectName(u"frame_seat1_cards")
        self.frame_seat1_cards.setMinimumSize(QSize(210, 140))
        self.frame_seat1_cards.setMaximumSize(QSize(210, 140))
        self.frame_seat1_cards.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_cards.setFrameShadow(QFrame.Shadow.Raised)
        self.label_seat1_card10 = QLabel(self.frame_seat1_cards)
        self.label_seat1_card10.setObjectName(u"label_seat1_card10")
        self.label_seat1_card10.setGeometry(QRect(150, 65, 48, 58))
        self.label_seat1_card10.setPixmap(QPixmap(u":/cards/resources/5.png"))
        self.label_seat1_card10.setScaledContents(True)
        self.label_seat1_card1 = QLabel(self.frame_seat1_cards)
        self.label_seat1_card1.setObjectName(u"label_seat1_card1")
        self.label_seat1_card1.setGeometry(QRect(15, 20, 48, 58))
        self.label_seat1_card1.setStyleSheet(u"background: transparent;")
        self.label_seat1_card1.setPixmap(QPixmap(u":/cards/resources/9.png"))
        self.label_seat1_card1.setScaledContents(True)
        self.label_seat1_card3 = QLabel(self.frame_seat1_cards)
        self.label_seat1_card3.setObjectName(u"label_seat1_card3")
        self.label_seat1_card3.setGeometry(QRect(45, 30, 48, 58))
        self.label_seat1_card3.setStyleSheet(u"background: transparent;")
        self.label_seat1_card3.setPixmap(QPixmap(u":/cards/resources/king.png"))
        self.label_seat1_card3.setScaledContents(True)
        self.label_seat1_card6 = QLabel(self.frame_seat1_cards)
        self.label_seat1_card6.setObjectName(u"label_seat1_card6")
        self.label_seat1_card6.setGeometry(QRect(90, 45, 48, 58))
        self.label_seat1_card6.setStyleSheet(u"background: transparent;")
        self.label_seat1_card6.setPixmap(QPixmap(u":/cards/resources/4.png"))
        self.label_seat1_card6.setScaledContents(True)
        self.label_seat1_card5 = QLabel(self.frame_seat1_cards)
        self.label_seat1_card5.setObjectName(u"label_seat1_card5")
        self.label_seat1_card5.setGeometry(QRect(75, 40, 48, 58))
        self.label_seat1_card5.setStyleSheet(u"background: transparent;")
        self.label_seat1_card5.setPixmap(QPixmap(u":/cards/resources/10.png"))
        self.label_seat1_card5.setScaledContents(True)
        self.label_seat1_card7 = QLabel(self.frame_seat1_cards)
        self.label_seat1_card7.setObjectName(u"label_seat1_card7")
        self.label_seat1_card7.setGeometry(QRect(105, 50, 48, 58))
        self.label_seat1_card7.setStyleSheet(u"background: transparent;")
        self.label_seat1_card7.setPixmap(QPixmap(u":/cards/resources/10.png"))
        self.label_seat1_card7.setScaledContents(True)
        self.label_seat1_card4 = QLabel(self.frame_seat1_cards)
        self.label_seat1_card4.setObjectName(u"label_seat1_card4")
        self.label_seat1_card4.setGeometry(QRect(60, 35, 48, 58))
        self.label_seat1_card4.setStyleSheet(u"background: transparent;")
        self.label_seat1_card4.setPixmap(QPixmap(u":/cards/resources/10.png"))
        self.label_seat1_card4.setScaledContents(True)
        self.label_seat1_card9 = QLabel(self.frame_seat1_cards)
        self.label_seat1_card9.setObjectName(u"label_seat1_card9")
        self.label_seat1_card9.setGeometry(QRect(135, 60, 48, 58))
        self.label_seat1_card9.setPixmap(QPixmap(u":/cards/resources/9.png"))
        self.label_seat1_card9.setScaledContents(True)
        self.label_seat1_card2 = QLabel(self.frame_seat1_cards)
        self.label_seat1_card2.setObjectName(u"label_seat1_card2")
        self.label_seat1_card2.setGeometry(QRect(30, 25, 48, 58))
        self.label_seat1_card2.setMinimumSize(QSize(0, 0))
        self.label_seat1_card2.setMaximumSize(QSize(16777215, 16777215))
        self.label_seat1_card2.setStyleSheet(u"background: transparent;")
        self.label_seat1_card2.setPixmap(QPixmap(u":/cards/resources/2.png"))
        self.label_seat1_card2.setScaledContents(True)
        self.label_seat1_card8 = QLabel(self.frame_seat1_cards)
        self.label_seat1_card8.setObjectName(u"label_seat1_card8")
        self.label_seat1_card8.setGeometry(QRect(120, 55, 48, 58))
        self.label_seat1_card8.setPixmap(QPixmap(u":/cards/resources/7.png"))
        self.label_seat1_card8.setScaledContents(True)
        self.frame_seat1_total = QFrame(self.frame_seat1_cards)
        self.frame_seat1_total.setObjectName(u"frame_seat1_total")
        self.frame_seat1_total.setGeometry(QRect(160, 10, 50, 50))
        self.frame_seat1_total.setMinimumSize(QSize(50, 50))
        self.frame_seat1_total.setMaximumSize(QSize(50, 50))
        self.frame_seat1_total.setStyleSheet(u"#frame_seat1_total{\n"
"border:none;\n"
"}")
        self.frame_seat1_total.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_total.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_seat1_total)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 5)
        self.label_seat1_total = QLabel(self.frame_seat1_total)
        self.label_seat1_total.setObjectName(u"label_seat1_total")
        self.label_seat1_total.setMinimumSize(QSize(30, 25))
        self.label_seat1_total.setMaximumSize(QSize(30, 25))
        self.label_seat1_total.setStyleSheet(u"")
        self.label_seat1_total.setScaledContents(True)
        self.label_seat1_total.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_seat1_total, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_seat1_total_text = QLabel(self.frame_seat1_total)
        self.label_seat1_total_text.setObjectName(u"label_seat1_total_text")
        self.label_seat1_total_text.setStyleSheet(u"#label_stand{\n"
"	font: 13pt \"Forte\";\n"
"	color: rgba(255,255,255,150);\n"
"	background-color: transparent;\n"
"}")
        self.label_seat1_total_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_seat1_total_text)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.label_seat1_card1.raise_()
        self.label_seat1_card2.raise_()
        self.label_seat1_card3.raise_()
        self.label_seat1_card4.raise_()
        self.label_seat1_card5.raise_()
        self.label_seat1_card6.raise_()
        self.label_seat1_card7.raise_()
        self.label_seat1_card8.raise_()
        self.label_seat1_card9.raise_()
        self.label_seat1_card10.raise_()
        self.frame_seat1_total.raise_()

        self.horizontalLayout_20.addWidget(self.frame_seat1_cards)

        self.frame_seat1_budget = QFrame(self.frame_seat1)
        self.frame_seat1_budget.setObjectName(u"frame_seat1_budget")
        self.frame_seat1_budget.setMinimumSize(QSize(60, 140))
        self.frame_seat1_budget.setMaximumSize(QSize(60, 140))
        self.frame_seat1_budget.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_budget.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_seat1_budget)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 10, 0, 20)
        self.frame_seat1_budget_amount = QFrame(self.frame_seat1_budget)
        self.frame_seat1_budget_amount.setObjectName(u"frame_seat1_budget_amount")
        self.frame_seat1_budget_amount.setMinimumSize(QSize(50, 25))
        self.frame_seat1_budget_amount.setMaximumSize(QSize(50, 25))
        self.frame_seat1_budget_amount.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_budget_amount.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_seat1_budget_amount)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_seat1_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.frame_seat1_spacer)

        self.label_seat1_budget_dollar = QLabel(self.frame_seat1_budget_amount)
        self.label_seat1_budget_dollar.setObjectName(u"label_seat1_budget_dollar")
        self.label_seat1_budget_dollar.setMinimumSize(QSize(15, 0))
        self.label_seat1_budget_dollar.setMaximumSize(QSize(15, 16777215))
        self.label_seat1_budget_dollar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_seat1_budget_dollar)

        self.label_seat1_budget_amount = QLabel(self.frame_seat1_budget_amount)
        self.label_seat1_budget_amount.setObjectName(u"label_seat1_budget_amount")
        self.label_seat1_budget_amount.setMinimumSize(QSize(0, 0))
        self.label_seat1_budget_amount.setMaximumSize(QSize(16777215, 16777215))
        self.label_seat1_budget_amount.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_seat1_budget_amount.setScaledContents(True)

        self.horizontalLayout_25.addWidget(self.label_seat1_budget_amount)

        self.frame_seat1_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.frame_seat1_spacer_2)


        self.verticalLayout_11.addWidget(self.frame_seat1_budget_amount, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_seat1_budget_text = QLabel(self.frame_seat1_budget)
        self.label_seat1_budget_text.setObjectName(u"label_seat1_budget_text")
        self.label_seat1_budget_text.setStyleSheet(u"#label_stand{\n"
"	font: 13pt \"Forte\";\n"
"	color: rgba(255,255,255,150);\n"
"	background-color: transparent;\n"
"}")
        self.label_seat1_budget_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_seat1_budget_text)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_11)

        self.label_seat1_status = QLabel(self.frame_seat1_budget)
        self.label_seat1_status.setObjectName(u"label_seat1_status")
        self.label_seat1_status.setMinimumSize(QSize(50, 50))
        self.label_seat1_status.setMaximumSize(QSize(50, 50))
        self.label_seat1_status.setScaledContents(True)

        self.verticalLayout_11.addWidget(self.label_seat1_status, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_20.addWidget(self.frame_seat1_budget)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_13)


        self.gridLayout.addWidget(self.frame_seat1, 2, 0, 1, 1, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.frame_seat2 = QFrame(self.frame_game)
        self.frame_seat2.setObjectName(u"frame_seat2")
        self.frame_seat2.setMinimumSize(QSize(360, 150))
        self.frame_seat2.setMaximumSize(QSize(360, 150))
        self.frame_seat2.setStyleSheet(u"#frame_seat2_gainloss, #frame_seat2_budget{\n"
"border:none;\n"
"}\n"
"\n"
"#frame_seat2_cards {\n"
"background-color: rgba(0,0,0,40);\n"
"border-radius: 20\n"
"}\n"
"\n"
"#frame_seat2_cards * {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#label_seat2_total {\n"
"font: 16pt \"Forte\";\n"
"color: white;\n"
"}\n"
"\n"
"#frame_seat2_budget * {\n"
"font: 16pt \"Forte\";\n"
"color: rgba(212,185,58,255);\n"
"}\n"
"\n"
"#frame_seat2_budget_amount {\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 0, 0, 0), stop: 0.7 rgba(212,185,58,25), stop:0.85 rgba(212,185,58,55), stop:1 rgba(212,185,58,105));\n"
"border: 1 solid rgb(104,102,50);\n"
"}\n"
"\n"
"#label_seat2_budget_text {\n"
"font: 10pt \"Forte\";\n"
"}\n"
"\n"
"#label_seat2_total {\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 0, 0, 0), stop: 0.7 rgba(255,255,255,25), stop:0.85 rgba(255,255,255,55), stop:1 rgba(255,255,"
                        "255,105));\n"
"border:1 solid rgb(144,144,144)\n"
"}\n"
"\n"
"#label_seat2_total_text {\n"
"font: 10pt \"Forte\";\n"
"color: rgba(255,255,255,150)\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame_seat2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_seat2)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 5, 0, 0)
        self.frame_seat2_gainloss = QFrame(self.frame_seat2)
        self.frame_seat2_gainloss.setObjectName(u"frame_seat2_gainloss")
        self.frame_seat2_gainloss.setMinimumSize(QSize(60, 140))
        self.frame_seat2_gainloss.setMaximumSize(QSize(60, 140))
        self.frame_seat2_gainloss.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_gainloss.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_seat2_gainloss)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 20, 0, 5)
        self.label_seat2_budget_chips = QLabel(self.frame_seat2_gainloss)
        self.label_seat2_budget_chips.setObjectName(u"label_seat2_budget_chips")
        self.label_seat2_budget_chips.setMinimumSize(QSize(50, 50))
        self.label_seat2_budget_chips.setMaximumSize(QSize(50, 50))
        self.label_seat2_budget_chips.setStyleSheet(u"")
        self.label_seat2_budget_chips.setLineWidth(1)
        self.label_seat2_budget_chips.setScaledContents(True)
        self.label_seat2_budget_chips.setMargin(0)

        self.verticalLayout_13.addWidget(self.label_seat2_budget_chips, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_17)

        self.label_seat2_martini = QLabel(self.frame_seat2_gainloss)
        self.label_seat2_martini.setObjectName(u"label_seat2_martini")
        self.label_seat2_martini.setMinimumSize(QSize(50, 50))
        self.label_seat2_martini.setMaximumSize(QSize(50, 50))
        self.label_seat2_martini.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.label_seat2_martini, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.frame_seat2_gainloss)

        self.frame_seat2_cards = QFrame(self.frame_seat2)
        self.frame_seat2_cards.setObjectName(u"frame_seat2_cards")
        self.frame_seat2_cards.setMinimumSize(QSize(210, 140))
        self.frame_seat2_cards.setMaximumSize(QSize(210, 140))
        self.frame_seat2_cards.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_cards.setFrameShadow(QFrame.Shadow.Raised)
        self.label_seat3_card9 = QLabel(self.frame_seat2_cards)
        self.label_seat3_card9.setObjectName(u"label_seat3_card9")
        self.label_seat3_card9.setGeometry(QRect(135, 25, 48, 58))
        self.label_seat3_card9.setPixmap(QPixmap(u":/cards/resources/king.png"))
        self.label_seat3_card9.setScaledContents(True)
        self.label_seat3_card6 = QLabel(self.frame_seat2_cards)
        self.label_seat3_card6.setObjectName(u"label_seat3_card6")
        self.label_seat3_card6.setGeometry(QRect(90, 40, 48, 58))
        self.label_seat3_card6.setPixmap(QPixmap(u":/cards/resources/king.png"))
        self.label_seat3_card6.setScaledContents(True)
        self.label_seat3_card10 = QLabel(self.frame_seat2_cards)
        self.label_seat3_card10.setObjectName(u"label_seat3_card10")
        self.label_seat3_card10.setGeometry(QRect(150, 20, 48, 58))
        self.label_seat3_card10.setPixmap(QPixmap(u":/cards/resources/king.png"))
        self.label_seat3_card10.setScaledContents(True)
        self.label_seat3_card3 = QLabel(self.frame_seat2_cards)
        self.label_seat3_card3.setObjectName(u"label_seat3_card3")
        self.label_seat3_card3.setGeometry(QRect(45, 55, 48, 58))
        self.label_seat3_card3.setPixmap(QPixmap(u":/cards/resources/king.png"))
        self.label_seat3_card3.setScaledContents(True)
        self.label_seat3_card1 = QLabel(self.frame_seat2_cards)
        self.label_seat3_card1.setObjectName(u"label_seat3_card1")
        self.label_seat3_card1.setGeometry(QRect(15, 65, 48, 58))
        self.label_seat3_card1.setPixmap(QPixmap(u":/cards/resources/10.png"))
        self.label_seat3_card1.setScaledContents(True)
        self.label_seat3_card5 = QLabel(self.frame_seat2_cards)
        self.label_seat3_card5.setObjectName(u"label_seat3_card5")
        self.label_seat3_card5.setGeometry(QRect(75, 45, 48, 58))
        self.label_seat3_card5.setPixmap(QPixmap(u":/cards/resources/king.png"))
        self.label_seat3_card5.setScaledContents(True)
        self.label_seat3_card2 = QLabel(self.frame_seat2_cards)
        self.label_seat3_card2.setObjectName(u"label_seat3_card2")
        self.label_seat3_card2.setGeometry(QRect(30, 60, 48, 58))
        self.label_seat3_card2.setPixmap(QPixmap(u":/cards/resources/8.png"))
        self.label_seat3_card2.setScaledContents(True)
        self.label_seat3_card4 = QLabel(self.frame_seat2_cards)
        self.label_seat3_card4.setObjectName(u"label_seat3_card4")
        self.label_seat3_card4.setGeometry(QRect(60, 50, 48, 58))
        self.label_seat3_card4.setPixmap(QPixmap(u":/cards/resources/king.png"))
        self.label_seat3_card4.setScaledContents(True)
        self.label_seat3_card8 = QLabel(self.frame_seat2_cards)
        self.label_seat3_card8.setObjectName(u"label_seat3_card8")
        self.label_seat3_card8.setGeometry(QRect(120, 30, 48, 58))
        self.label_seat3_card8.setPixmap(QPixmap(u":/cards/resources/king.png"))
        self.label_seat3_card8.setScaledContents(True)
        self.label_seat3_card7 = QLabel(self.frame_seat2_cards)
        self.label_seat3_card7.setObjectName(u"label_seat3_card7")
        self.label_seat3_card7.setGeometry(QRect(105, 35, 48, 58))
        self.label_seat3_card7.setPixmap(QPixmap(u":/cards/resources/king.png"))
        self.label_seat3_card7.setScaledContents(True)
        self.frame_seat2_total = QFrame(self.frame_seat2_cards)
        self.frame_seat2_total.setObjectName(u"frame_seat2_total")
        self.frame_seat2_total.setGeometry(QRect(160, 80, 50, 50))
        self.frame_seat2_total.setMinimumSize(QSize(50, 50))
        self.frame_seat2_total.setMaximumSize(QSize(50, 50))
        self.frame_seat2_total.setStyleSheet(u"border:none;\n"
"background-color:transparent;\n"
"color:transparent;")
        self.frame_seat2_total.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_total.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_seat2_total)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 5, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.label_seat2_total_text = QLabel(self.frame_seat2_total)
        self.label_seat2_total_text.setObjectName(u"label_seat2_total_text")
        self.label_seat2_total_text.setMaximumSize(QSize(60, 16777215))
        self.label_seat2_total_text.setStyleSheet(u"#label_stand{\n"
"	font: 13pt \"Forte\";\n"
"	color: rgba(255,255,255,150);\n"
"	background-color: transparent;\n"
"}")
        self.label_seat2_total_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_seat2_total_text, 0, Qt.AlignmentFlag.AlignVCenter)

        self.label_seat2_total = QLabel(self.frame_seat2_total)
        self.label_seat2_total.setObjectName(u"label_seat2_total")
        self.label_seat2_total.setMinimumSize(QSize(30, 25))
        self.label_seat2_total.setMaximumSize(QSize(30, 25))
        self.label_seat2_total.setStyleSheet(u"")
        self.label_seat2_total.setScaledContents(True)
        self.label_seat2_total.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_seat2_total, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_seat3_card1.raise_()
        self.label_seat3_card2.raise_()
        self.label_seat3_card3.raise_()
        self.label_seat3_card4.raise_()
        self.label_seat3_card5.raise_()
        self.label_seat3_card6.raise_()
        self.label_seat3_card7.raise_()
        self.label_seat3_card8.raise_()
        self.label_seat3_card9.raise_()
        self.label_seat3_card10.raise_()
        self.frame_seat2_total.raise_()

        self.horizontalLayout_6.addWidget(self.frame_seat2_cards)

        self.frame_seat2_budget = QFrame(self.frame_seat2)
        self.frame_seat2_budget.setObjectName(u"frame_seat2_budget")
        self.frame_seat2_budget.setMinimumSize(QSize(60, 140))
        self.frame_seat2_budget.setMaximumSize(QSize(60, 140))
        self.frame_seat2_budget.setStyleSheet(u"border:none;\n"
"background-color:transparent;\n"
"color:transparent;")
        self.frame_seat2_budget.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_budget.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_seat2_budget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 20, 0, 10)
        self.label_seat2_status = QLabel(self.frame_seat2_budget)
        self.label_seat2_status.setObjectName(u"label_seat2_status")
        self.label_seat2_status.setMinimumSize(QSize(50, 50))
        self.label_seat2_status.setMaximumSize(QSize(44, 50))
        self.label_seat2_status.setScaledContents(True)

        self.verticalLayout_9.addWidget(self.label_seat2_status, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_5)

        self.label_seat2_budget_text = QLabel(self.frame_seat2_budget)
        self.label_seat2_budget_text.setObjectName(u"label_seat2_budget_text")
        self.label_seat2_budget_text.setStyleSheet(u"")
        self.label_seat2_budget_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_seat2_budget_text, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_seat2_budget_amount = QFrame(self.frame_seat2_budget)
        self.frame_seat2_budget_amount.setObjectName(u"frame_seat2_budget_amount")
        self.frame_seat2_budget_amount.setMinimumSize(QSize(50, 25))
        self.frame_seat2_budget_amount.setMaximumSize(QSize(50, 25))
        self.frame_seat2_budget_amount.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_budget_amount.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_seat2_budget_amount)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_seat2_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.frame_seat2_spacer_2)

        self.label_seat2_budget_dollar = QLabel(self.frame_seat2_budget_amount)
        self.label_seat2_budget_dollar.setObjectName(u"label_seat2_budget_dollar")
        self.label_seat2_budget_dollar.setMinimumSize(QSize(15, 0))
        self.label_seat2_budget_dollar.setMaximumSize(QSize(15, 16777215))
        self.label_seat2_budget_dollar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_seat2_budget_dollar)

        self.label_seat2_budget_amount = QLabel(self.frame_seat2_budget_amount)
        self.label_seat2_budget_amount.setObjectName(u"label_seat2_budget_amount")
        self.label_seat2_budget_amount.setMinimumSize(QSize(0, 0))
        self.label_seat2_budget_amount.setMaximumSize(QSize(16777215, 16777215))
        self.label_seat2_budget_amount.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_seat2_budget_amount.setScaledContents(True)

        self.horizontalLayout_24.addWidget(self.label_seat2_budget_amount)

        self.frame_seat2_spacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.frame_seat2_spacer_1)


        self.verticalLayout_9.addWidget(self.frame_seat2_budget_amount, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.frame_seat2_budget)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_14)


        self.gridLayout.addWidget(self.frame_seat2, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_4.addWidget(self.frame_game, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.frame_options = QFrame(self.frame_content)
        self.frame_options.setObjectName(u"frame_options")
        self.frame_options.setMinimumSize(QSize(230, 700))
        self.frame_options.setMaximumSize(QSize(230, 700))
        self.frame_options.setStyleSheet(u"#frame_options{\n"
"border: none;\n"
"background:  rgb(48, 12, 20);\n"
"background: rgb(45, 20, 9);\n"
"border-radius:25px;\n"
"}\n"
"\n"
"#frame_options * {\n"
"	background-color:transparent;\n"
"	border:  none;\n"
"}\n"
"\n"
"#groupbox_bet {\n"
"	font: 700 20pt \"Forte\";\n"
"	color:  rgba(212,185,58,75);\n"
"	background-color: rgba(33,44,38,150);\n"
"	border-radius: 20px;	\n"
"    margin-top: 0.9em;\n"
"}\n"
"\n"
"#groupbox_bet::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* Ba\u015fl\u0131\u011f\u0131 ortalamak i\u00e7in */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"\n"
"#groupbox_bet QLabel {\n"
"	background-color: transparent;\n"
"	font: 700 12pt \"Forte\";\n"
"	color: rgba(212,185,58,75)\n"
"}\n"
"\n"
"#groupbox_bet #label_stake_amount {\n"
"	font: 700 16pt \"Forte\";\n"
"}\n"
"\n"
"\n"
"#groupbox_bet QSlider {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#groupbox_bet QSlider::groove:horizontal {\n"
"    height: 20px;\n"
"    background-color:"
                        " rgba(0,0,0,20);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#groupbox_bet #frame_stake {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#groupbox_bet #label_bet_info {\n"
"	font: 10pt \"Forte\";\n"
"	color: rgba(212,185,58,35);\n"
"}\n"
"\n"
"\n"
"/* --------------------------------------------------------*/\n"
"\n"
"\n"
"#groupbox_move {\n"
"	font: 700 20pt \"Forte\";\n"
"	color: rgba(212,185,58,75);\n"
"	background-color: rgba(33,44,38,150);\n"
"	border-radius: 20px;	\n"
"    margin-top: 0.9em;\n"
"}\n"
"\n"
"#groupbox_move::title{\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* Ba\u015fl\u0131\u011f\u0131 ortalamak i\u00e7in */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"\n"
"#frame_button_hit {\n"
"	background-color:  transparent;\n"
"	border-top-left-radius:  20px;	\n"
"	border-bottom-left-radius:  20px;	\n"
"}\n"
"\n"
"#frame_button_stand {\n"
"	background-color:  transparent;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"#frame_button_double {\n"
"	background-color"
                        ":  transparent;\n"
"	border-top-right-radius:  20px;	\n"
"	border-bottom-right-radius:  20px;	\n"
"}\n"
"\n"
"")
        self.frame_options.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_options.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_options.setMidLineWidth(0)
        self.verticalLayout_18 = QVBoxLayout(self.frame_options)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(10, 20, 10, 20)
        self.frame = QFrame(self.frame_options)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QPushButton::hover {\n"
"border: 2px solid rgba(212,185,58,255);\n"
"background-color: rgba(212,185,58,25);\n"
"}\n"
"\n"
"QPushButton{\n"
"font: 16pt \"Arial\";\n"
"border: 2px solid  rgb(120,124,116);\n"
"border-radius: 15px;\n"
"color: rgba(212,185,58,255);\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.button_reset = QPushButton(self.frame)
        self.button_reset.setObjectName(u"button_reset")
        self.button_reset.setMinimumSize(QSize(80, 35))
        self.button_reset.setMaximumSize(QSize(80, 35))
        self.button_reset.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.button_reset)

        self.button_menu = QPushButton(self.frame)
        self.button_menu.setObjectName(u"button_menu")
        self.button_menu.setMinimumSize(QSize(80, 35))
        self.button_menu.setMaximumSize(QSize(80, 35))
        self.button_menu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.button_menu)


        self.verticalLayout_18.addWidget(self.frame)

        self.frame_round = QFrame(self.frame_options)
        self.frame_round.setObjectName(u"frame_round")
        self.frame_round.setMinimumSize(QSize(100, 25))
        self.frame_round.setMaximumSize(QSize(100, 25))
#if QT_CONFIG(tooltip)
        self.frame_round.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.frame_round.setStyleSheet(u"#frame_round {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#frame_round * {\n"
"background-color: transparent;\n"
"color: rgba(212,185,58,255);\n"
"font: 16pt \"Forte\";\n"
"}\n"
"\n"
"")
        self.frame_round.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_round.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_round)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(8, 0, 0, 0)
        self.label_round = QLabel(self.frame_round)
        self.label_round.setObjectName(u"label_round")
        self.label_round.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_round.setStyleSheet(u"")
        self.label_round.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_round)

        self.label_round_number = QLabel(self.frame_round)
        self.label_round_number.setObjectName(u"label_round_number")
        self.label_round_number.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_round_number.setStyleSheet(u"")
        self.label_round_number.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_round_number)

        self.horizontalspacer_round = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalspacer_round)


        self.verticalLayout_18.addWidget(self.frame_round)

        self.line = QFrame(self.frame_options)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(195, 2))
        self.line.setMaximumSize(QSize(195, 2))
        self.line.setStyleSheet(u"#line {\n"
"background-color: rgba(212,185,58,255);\n"
"border-radius: 1px;\n"
"}")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_18.addWidget(self.line)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_14)

        self.groupbox_board = QGroupBox(self.frame_options)
        self.groupbox_board.setObjectName(u"groupbox_board")
        self.groupbox_board.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupbox_board.sizePolicy().hasHeightForWidth())
        self.groupbox_board.setSizePolicy(sizePolicy2)
        self.groupbox_board.setMinimumSize(QSize(200, 0))
        self.groupbox_board.setMaximumSize(QSize(200, 16777215))
        self.groupbox_board.setStyleSheet(u"QGroupBox {\n"
"	font: 700 20pt \"Forte\";\n"
"	color:  rgba(212,185,58,255);\n"
"	background-color: rgb(33,44,38);\n"
"	border-radius: 20px;	\n"
"    margin-top: 0.9em;\n"
"	border: 1px solid rgb(212,185,58)\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* Ba\u015fl\u0131\u011f\u0131 ortalamak i\u00e7in */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QLabel {\n"
"	background-color: transparent;\n"
"	font: 700 12pt \"Forte\";\n"
"	color: rgba(212,185,58, 100)\n"
"}\n"
"\n"
"    QTableWidget {\n"
"        background-color: transparent;\n"
"        gridline-color: rgba(212,185,58,0); /* H\u00fccre i\u00e7 kenarl\u0131klar\u0131 */\n"
"		font: 14pt \"Forte\";\n"
"		margin-top: 5px;\n"
"    }\n"
"\n"
"    QHeaderView::section {\n"
"        background-color: transparent;\n"
"        color: rgba(212,185,58,255);\n"
"        font-family: Forte;\n"
"        border: none;\n"
"	    font: 10pt \"Forte\";\n"
"    }\n"
"\n"
"    QTableCornerButton::se"
                        "ction {\n"
"        background-color: transparent;\n"
"        border: none;\n"
"    }\n"
"\n"
"    QTableWidget::item {\n"
"        background-color: transparent;\n"
"        color: rgb(255, 255, 255);\n"
"        font-family: Forte;\n"
"        border: 1px solid rgba(103,100,46,255);\n"
"		margin:2px;\n"
"		border-radius: 10px;\n"
"    }\n"
"\n"
"\n"
"")
        self.verticalLayout_19 = QVBoxLayout(self.groupbox_board)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(5, 3, 5, 3)
        self.frame_board_status = QFrame(self.groupbox_board)
        self.frame_board_status.setObjectName(u"frame_board_status")
        self.frame_board_status.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_board_status.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_board_status)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 0)
        self.label_status = QLabel(self.frame_board_status)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMinimumSize(QSize(0, 20))
        self.label_status.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setFamilies([u"Forte"])
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(False)
        self.label_status.setFont(font2)
        self.label_status.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"	font: 700 14pt \"Forte\";\n"
"	color: rgba(255,255,255, 200)\n"
"}")

        self.verticalLayout_5.addWidget(self.label_status)

        self.frame_player_status = QFrame(self.frame_board_status)
        self.frame_player_status.setObjectName(u"frame_player_status")
        self.frame_player_status.setMinimumSize(QSize(0, 100))
        self.frame_player_status.setMaximumSize(QSize(16777215, 100))
        self.frame_player_status.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_player_status.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_player_status)
        self.verticalLayout_25.setSpacing(5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(5, 5, 5, 5)
        self.frame_status_dealer = QFrame(self.frame_player_status)
        self.frame_status_dealer.setObjectName(u"frame_status_dealer")
        self.frame_status_dealer.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_status_dealer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_status_dealer)
        self.horizontalLayout_38.setSpacing(5)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_status_dealer_text = QLabel(self.frame_status_dealer)
        self.label_status_dealer_text.setObjectName(u"label_status_dealer_text")
        self.label_status_dealer_text.setMinimumSize(QSize(0, 15))
        self.label_status_dealer_text.setMaximumSize(QSize(16777215, 15))
        self.label_status_dealer_text.setStyleSheet(u"")

        self.horizontalLayout_38.addWidget(self.label_status_dealer_text)

        self.label_status_dealer = QLabel(self.frame_status_dealer)
        self.label_status_dealer.setObjectName(u"label_status_dealer")
        self.label_status_dealer.setMinimumSize(QSize(0, 15))
        self.label_status_dealer.setMaximumSize(QSize(16777215, 15))
        self.label_status_dealer.setStyleSheet(u"")

        self.horizontalLayout_38.addWidget(self.label_status_dealer)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_9)


        self.verticalLayout_25.addWidget(self.frame_status_dealer)

        self.frame_status_seat1 = QFrame(self.frame_player_status)
        self.frame_status_seat1.setObjectName(u"frame_status_seat1")
        self.frame_status_seat1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_status_seat1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_status_seat1)
        self.horizontalLayout_37.setSpacing(5)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_status_botseat_text = QLabel(self.frame_status_seat1)
        self.label_status_botseat_text.setObjectName(u"label_status_botseat_text")
        self.label_status_botseat_text.setMinimumSize(QSize(0, 15))
        self.label_status_botseat_text.setMaximumSize(QSize(16777215, 15))
        self.label_status_botseat_text.setStyleSheet(u"")

        self.horizontalLayout_37.addWidget(self.label_status_botseat_text)

        self.label_status_seat1 = QLabel(self.frame_status_seat1)
        self.label_status_seat1.setObjectName(u"label_status_seat1")
        self.label_status_seat1.setMinimumSize(QSize(0, 15))
        self.label_status_seat1.setMaximumSize(QSize(16777215, 15))
        self.label_status_seat1.setStyleSheet(u"")

        self.horizontalLayout_37.addWidget(self.label_status_seat1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_8)


        self.verticalLayout_25.addWidget(self.frame_status_seat1)

        self.frame_status_seat2 = QFrame(self.frame_player_status)
        self.frame_status_seat2.setObjectName(u"frame_status_seat2")
        self.frame_status_seat2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_status_seat2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_status_seat2)
        self.horizontalLayout_29.setSpacing(5)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_status_topseat_text = QLabel(self.frame_status_seat2)
        self.label_status_topseat_text.setObjectName(u"label_status_topseat_text")
        self.label_status_topseat_text.setMinimumSize(QSize(0, 15))
        self.label_status_topseat_text.setMaximumSize(QSize(16777215, 15))
        self.label_status_topseat_text.setStyleSheet(u"")

        self.horizontalLayout_29.addWidget(self.label_status_topseat_text)

        self.label_status_seat2 = QLabel(self.frame_status_seat2)
        self.label_status_seat2.setObjectName(u"label_status_seat2")
        self.label_status_seat2.setMinimumSize(QSize(0, 15))
        self.label_status_seat2.setMaximumSize(QSize(16777215, 15))
        self.label_status_seat2.setStyleSheet(u"")

        self.horizontalLayout_29.addWidget(self.label_status_seat2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_5)


        self.verticalLayout_25.addWidget(self.frame_status_seat2)


        self.verticalLayout_5.addWidget(self.frame_player_status)


        self.verticalLayout_19.addWidget(self.frame_board_status)

        self.frame_board_nextround = QFrame(self.groupbox_board)
        self.frame_board_nextround.setObjectName(u"frame_board_nextround")
        self.frame_board_nextround.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_board_nextround.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_board_nextround)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 20, 10, 10)
        self.button_next_round = QPushButton(self.frame_board_nextround)
        self.button_next_round.setObjectName(u"button_next_round")
        self.button_next_round.setEnabled(True)
        self.button_next_round.setMinimumSize(QSize(130, 35))
        self.button_next_round.setMaximumSize(QSize(130, 35))
        self.button_next_round.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_next_round.setStyleSheet(u"QPushButton{\n"
"font: 16pt \"Arial\";\n"
"border: 2px solid  rgba(120,124,116,0.1);\n"
"border-radius: 15px;\n"
"color: rgba(212,185,58,0.1);\n"
"background-color:  rgba(45, 20, 9,0);\n"
"}")

        self.horizontalLayout_3.addWidget(self.button_next_round)


        self.verticalLayout_19.addWidget(self.frame_board_nextround)


        self.verticalLayout_18.addWidget(self.groupbox_board, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_12)

        self.groupbox_bet = QGroupBox(self.frame_options)
        self.groupbox_bet.setObjectName(u"groupbox_bet")
        self.groupbox_bet.setEnabled(True)
        self.groupbox_bet.setMinimumSize(QSize(200, 100))
        self.groupbox_bet.setMaximumSize(QSize(200, 100))
        self.groupbox_bet.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.groupbox_bet)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 5, 10, 10)
        self.frame_stake = QFrame(self.groupbox_bet)
        self.frame_stake.setObjectName(u"frame_stake")
        self.frame_stake.setMinimumSize(QSize(0, 25))
        self.frame_stake.setMaximumSize(QSize(16777215, 25))
        self.frame_stake.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_stake.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_stake)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_stake = QLabel(self.frame_stake)
        self.label_stake.setObjectName(u"label_stake")

        self.horizontalLayout_19.addWidget(self.label_stake)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_2)

        self.frame_bet_amount = QFrame(self.frame_stake)
        self.frame_bet_amount.setObjectName(u"frame_bet_amount")
        self.frame_bet_amount.setMinimumSize(QSize(100, 25))
        self.frame_bet_amount.setMaximumSize(QSize(100, 25))
        self.frame_bet_amount.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_bet_amount.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_bet_amount)
        self.horizontalLayout_23.setSpacing(3)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_3)

        self.label_stake_amount = QLabel(self.frame_bet_amount)
        self.label_stake_amount.setObjectName(u"label_stake_amount")
        self.label_stake_amount.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_stake_amount.setScaledContents(True)

        self.horizontalLayout_23.addWidget(self.label_stake_amount)

        self.label_stake_dollar = QLabel(self.frame_bet_amount)
        self.label_stake_dollar.setObjectName(u"label_stake_dollar")
        self.label_stake_dollar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_stake_dollar)


        self.horizontalLayout_19.addWidget(self.frame_bet_amount)


        self.verticalLayout_8.addWidget(self.frame_stake)

        self.slider_bet = QSlider(self.groupbox_bet)
        self.slider_bet.setObjectName(u"slider_bet")
        self.slider_bet.setEnabled(True)
        self.slider_bet.setMinimumSize(QSize(180, 20))
        self.slider_bet.setMaximumSize(QSize(180, 20))
        self.slider_bet.setMinimum(1)
        self.slider_bet.setMaximum(10)
        self.slider_bet.setSingleStep(1)
        self.slider_bet.setPageStep(1)
        self.slider_bet.setSliderPosition(1)
        self.slider_bet.setTracking(True)
        self.slider_bet.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_8.addWidget(self.slider_bet)

        self.label_bet_info = QLabel(self.groupbox_bet)
        self.label_bet_info.setObjectName(u"label_bet_info")
        self.label_bet_info.setStyleSheet(u"")
        self.label_bet_info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_bet_info)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)


        self.verticalLayout_18.addWidget(self.groupbox_bet, 0, Qt.AlignmentFlag.AlignHCenter)

        self.groupbox_move = QGroupBox(self.frame_options)
        self.groupbox_move.setObjectName(u"groupbox_move")
        self.groupbox_move.setEnabled(True)
        self.groupbox_move.setMinimumSize(QSize(200, 100))
        self.groupbox_move.setMaximumSize(QSize(200, 100))
        self.groupbox_move.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.groupbox_move)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_button_hit = QFrame(self.groupbox_move)
        self.frame_button_hit.setObjectName(u"frame_button_hit")
        self.frame_button_hit.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_button_hit.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_button_hit)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.button_hit = QPushButton(self.frame_button_hit)
        self.button_hit.setObjectName(u"button_hit")
        sizePolicy1.setHeightForWidth(self.button_hit.sizePolicy().hasHeightForWidth())
        self.button_hit.setSizePolicy(sizePolicy1)
        self.button_hit.setMinimumSize(QSize(50, 50))
        self.button_hit.setMaximumSize(QSize(16777215, 16777215))
        self.button_hit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/hit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_hit.setIcon(icon)
        self.button_hit.setIconSize(QSize(40, 40))

        self.verticalLayout_21.addWidget(self.button_hit)


        self.horizontalLayout.addWidget(self.frame_button_hit)

        self.frame_button_stand = QFrame(self.groupbox_move)
        self.frame_button_stand.setObjectName(u"frame_button_stand")
        self.frame_button_stand.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_button_stand.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_button_stand)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.button_stand = QPushButton(self.frame_button_stand)
        self.button_stand.setObjectName(u"button_stand")
        sizePolicy1.setHeightForWidth(self.button_stand.sizePolicy().hasHeightForWidth())
        self.button_stand.setSizePolicy(sizePolicy1)
        self.button_stand.setMinimumSize(QSize(50, 50))
        self.button_stand.setMaximumSize(QSize(16777215, 16777215))
        self.button_stand.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/stand.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_stand.setIcon(icon1)
        self.button_stand.setIconSize(QSize(40, 40))

        self.verticalLayout_23.addWidget(self.button_stand)


        self.horizontalLayout.addWidget(self.frame_button_stand)

        self.frame_button_double = QFrame(self.groupbox_move)
        self.frame_button_double.setObjectName(u"frame_button_double")
        self.frame_button_double.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_button_double.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_button_double)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.button_double = QPushButton(self.frame_button_double)
        self.button_double.setObjectName(u"button_double")
        sizePolicy1.setHeightForWidth(self.button_double.sizePolicy().hasHeightForWidth())
        self.button_double.setSizePolicy(sizePolicy1)
        self.button_double.setMinimumSize(QSize(50, 50))
        self.button_double.setMaximumSize(QSize(16777215, 16777215))
        self.button_double.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/double-up.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_double.setIcon(icon2)
        self.button_double.setIconSize(QSize(50, 50))

        self.verticalLayout_24.addWidget(self.button_double)


        self.horizontalLayout.addWidget(self.frame_button_double)


        self.verticalLayout_18.addWidget(self.groupbox_move, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_4.addWidget(self.frame_options)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.stackedwidget_content.addWidget(self.page_2_game)

        self.verticalLayout.addWidget(self.stackedwidget_content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedwidget_content.setCurrentIndex(1)
        self.stackedWidget_agent_game_selection.setCurrentIndex(0)
        self.comboBox_agent_selection.setCurrentIndex(-1)
        self.comboBox_agent_selection_2.setCurrentIndex(-1)
        self.comboBox_agent_selection_3.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.game_header.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Blackjack</p></body></html>", None))
        self.by_anil_ergan.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Developed by An\u0131l ERGAN</p></body></html>", None))
        self.game_image.setText("")
        self.button_train_agent.setText(QCoreApplication.translate("MainWindow", u"Train Agent", None))
        self.button_one_player_game.setText(QCoreApplication.translate("MainWindow", u"One Player", None))
        self.label_agent_game.setText(QCoreApplication.translate("MainWindow", u"Agent Game", None))
        self.button_one_player_game_2.setText(QCoreApplication.translate("MainWindow", u"Single Agent", None))
        self.button_one_player_game_3.setText(QCoreApplication.translate("MainWindow", u"Multiple Agent", None))
        self.button_single_agent_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.comboBox_agent_selection.setItemText(0, QCoreApplication.translate("MainWindow", u"Monte Carlo Agent", None))
        self.comboBox_agent_selection.setItemText(1, QCoreApplication.translate("MainWindow", u"Q-Learning Agent", None))
        self.comboBox_agent_selection.setItemText(2, QCoreApplication.translate("MainWindow", u"SARSA Agent", None))
        self.comboBox_agent_selection.setItemText(3, QCoreApplication.translate("MainWindow", u"Policy Gradient Agent", None))

        self.comboBox_agent_selection.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Agent", None))
        self.button_single_agent_back_2.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.comboBox_agent_selection_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Monte Carlo Agent", None))
        self.comboBox_agent_selection_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Q-Learning Agent", None))
        self.comboBox_agent_selection_2.setItemText(2, QCoreApplication.translate("MainWindow", u"SARSA Agent", None))
        self.comboBox_agent_selection_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Policy Gradient Agent", None))

        self.comboBox_agent_selection_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Agent 1", None))
        self.comboBox_agent_selection_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Monte Carlo Agent", None))
        self.comboBox_agent_selection_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Q-Learning Agent", None))
        self.comboBox_agent_selection_3.setItemText(2, QCoreApplication.translate("MainWindow", u"SARSA Agent", None))
        self.comboBox_agent_selection_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Policy Gradient Agent", None))

        self.comboBox_agent_selection_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Agent 2", None))
        self.button_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(tooltip)
        self.label_announce.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Welcome to Blackjack!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_announce.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_announce.setText("")
#if QT_CONFIG(whatsthis)
        self.label_cd.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>10</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_cd.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_dealer_card9.setText("")
        self.label_dealer_card4.setText("")
        self.label_dealer_card6.setText("")
        self.label_dealer_card2.setText("")
        self.label_dealer_card5.setText("")
        self.label_dealer_card7.setText("")
        self.label_dealer_card8.setText("")
        self.label_dealer_card1.setText("")
        self.label_dealer_card10.setText("")
        self.label_dealer_card3.setText("")
        self.label_dealer_total_text.setText(QCoreApplication.translate("MainWindow", u"total", None))
        self.label_dealer_total.setText("")
        self.label_dealer_status.setText("")
        self.label_dealer_deck_top.setText("")
        self.label_dealer_deck_bot.setText("")
        self.label_blackjack_text_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>B</p></body></html>", None))
        self.label_blackjack_text_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>L</p></body></html>", None))
        self.label_blackjack_text_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>A</p></body></html>", None))
        self.label_blackjack_text_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>C</p></body></html>", None))
        self.label_blackjack_text_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K</p></body></html>", None))
        self.label_blackjack_text_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>J</p></body></html>", None))
        self.label_blackjack_text_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>A</p></body></html>", None))
        self.label_blackjack_text_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>C</p></body></html>", None))
        self.label_blackjack_text_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K</p></body></html>", None))
        self.label_seat1_chips_image.setText("")
        self.label_seat1_chips_image_2.setText("")
        self.label_seat2_chips_image.setText("")
        self.label_seat2_chips_image_2.setText("")
        self.label_seat1_budget_chips.setText("")
        self.label_seat1_martini.setText("")
        self.label_seat1_card10.setText("")
        self.label_seat1_card1.setText("")
        self.label_seat1_card3.setText("")
        self.label_seat1_card6.setText("")
        self.label_seat1_card5.setText("")
        self.label_seat1_card7.setText("")
        self.label_seat1_card4.setText("")
        self.label_seat1_card9.setText("")
        self.label_seat1_card2.setText("")
        self.label_seat1_card8.setText("")
        self.label_seat1_total.setText("")
        self.label_seat1_total_text.setText(QCoreApplication.translate("MainWindow", u"total", None))
        self.label_seat1_budget_dollar.setText(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_seat1_budget_amount.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.label_seat1_budget_text.setText(QCoreApplication.translate("MainWindow", u"budget", None))
        self.label_seat1_status.setText("")
        self.label_seat2_budget_chips.setText("")
        self.label_seat2_martini.setText("")
        self.label_seat3_card9.setText("")
        self.label_seat3_card6.setText("")
        self.label_seat3_card10.setText("")
        self.label_seat3_card3.setText("")
        self.label_seat3_card1.setText("")
        self.label_seat3_card5.setText("")
        self.label_seat3_card2.setText("")
        self.label_seat3_card4.setText("")
        self.label_seat3_card8.setText("")
        self.label_seat3_card7.setText("")
        self.label_seat2_total_text.setText(QCoreApplication.translate("MainWindow", u"total", None))
        self.label_seat2_total.setText("")
        self.label_seat2_status.setText("")
        self.label_seat2_budget_text.setText(QCoreApplication.translate("MainWindow", u"budget", None))
        self.label_seat2_budget_dollar.setText(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_seat2_budget_amount.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.button_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.button_menu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_round.setText(QCoreApplication.translate("MainWindow", u"Round:", None))
        self.label_round_number.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.groupbox_board.setTitle(QCoreApplication.translate("MainWindow", u"Board", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_status_dealer_text.setText(QCoreApplication.translate("MainWindow", u"dealer:", None))
        self.label_status_dealer.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_status_botseat_text.setText(QCoreApplication.translate("MainWindow", u"player", None))
        self.label_status_seat1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_status_topseat_text.setText(QCoreApplication.translate("MainWindow", u"agent", None))
        self.label_status_seat2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.button_next_round.setText(QCoreApplication.translate("MainWindow", u"Next Round", None))
        self.groupbox_bet.setTitle(QCoreApplication.translate("MainWindow", u"Place Your Bet!", None))
        self.label_stake.setText(QCoreApplication.translate("MainWindow", u"Stake", None))
        self.label_stake_amount.setText("")
        self.label_stake_dollar.setText(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_bet_info.setText(QCoreApplication.translate("MainWindow", u"drag the coin horizontal", None))
        self.groupbox_move.setTitle(QCoreApplication.translate("MainWindow", u"Move", None))
        self.button_hit.setText("")
#if QT_CONFIG(shortcut)
        self.button_hit.setShortcut(QCoreApplication.translate("MainWindow", u"Q", None))
#endif // QT_CONFIG(shortcut)
        self.button_stand.setText("")
#if QT_CONFIG(shortcut)
        self.button_stand.setShortcut(QCoreApplication.translate("MainWindow", u"W", None))
#endif // QT_CONFIG(shortcut)
        self.button_double.setText("")
#if QT_CONFIG(shortcut)
        self.button_double.setShortcut(QCoreApplication.translate("MainWindow", u"E", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

