# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
import resources_rc
import resources2_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 800)
        MainWindow.setMinimumSize(QSize(850, 800))
        MainWindow.setMaximumSize(QSize(850, 800))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(850, 800))
        self.centralwidget.setMaximumSize(QSize(850, 800))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedwidget_content = QStackedWidget(self.centralwidget)
        self.stackedwidget_content.setObjectName(u"stackedwidget_content")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedwidget_content.sizePolicy().hasHeightForWidth())
        self.stackedwidget_content.setSizePolicy(sizePolicy)
        self.stackedwidget_content.setMinimumSize(QSize(0, 0))
        self.stackedwidget_content.setMaximumSize(QSize(16777215, 16777215))
        self.stackedwidget_content.setStyleSheet(u"\n"
"\n"
"#page_1_menu  {\n"
"background-color:rgba(59,82,63,255);\n"
"}\n"
"\n"
"#page_2_game {\n"
"background-color: rgba(52,14,16,255);\n"
"background-color: rgb(60,27,12);\n"
"background-color: rgb(68,11,20);\n"
"}\n"
"\n"
"QFrame * {\n"
"border: None;\n"
"}\n"
"\n"
"")
        self.stackedwidget_content.setFrameShape(QFrame.Shape.StyledPanel)
        self.stackedwidget_content.setFrameShadow(QFrame.Shadow.Raised)
        self.page_1_menu = QWidget()
        self.page_1_menu.setObjectName(u"page_1_menu")
        self.page_1_menu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.page_1_menu.setStyleSheet(u"QPushButton::hover {\n"
"border: 2px solid rgba(212,185,58,255);\n"
"background-color: rgba(212,185,58,25);\n"
"}\n"
"\n"
"QPushButton{\n"
"font: 18pt \"Arial\";\n"
"border: 2px solid  rgb(120,124,116);\n"
"border-radius: 25px;\n"
"color: rgba(212,185,58,255);\n"
"background-color: rgba(39,52,45,255);\n"
"}\n"
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
"}\n"
"\n"
"#frame_menu_buttons {\n"
"border: None\n"
"}\n"
"\n"
"#frame_play_buttons{\n"
"border-radius: 25px;\n"
"background-color: rgba(120,124,116, 55);\n"
"border: 3px solid rgb(120,124,116);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.page_1_menu)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(10, 20, 10, 10)
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_9)

        self.frame = QFrame(self.page_1_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 80))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.game_header = QLabel(self.frame)
        self.game_header.setObjectName(u"game_header")
        self.game_header.setGeometry(QRect(0, 0, 828, 80))
        self.game_header.setMinimumSize(QSize(0, 80))
        self.game_header.setMaximumSize(QSize(16777215, 80))
        font = QFont()
        font.setFamilies([u"Forte"])
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        self.game_header.setFont(font)
        self.game_header.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.game_header.setStyleSheet(u"\n"
"color: rgb(12,16,25);\n"
"color: rgb(0,0,0);\n"
"font: 48pt \"Forte\";\n"
"\n"
"\n"
"")
        self.game_header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.by_anil_ergan = QLabel(self.frame)
        self.by_anil_ergan.setObjectName(u"by_anil_ergan")
        self.by_anil_ergan.setGeometry(QRect(0, 60, 828, 12))
        self.by_anil_ergan.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: black;")

        self.verticalLayout_2.addWidget(self.frame)

        self.stackedwidget_options = QStackedWidget(self.page_1_menu)
        self.stackedwidget_options.setObjectName(u"stackedwidget_options")
        self.stackedwidget_options.setMinimumSize(QSize(0, 300))
        self.stackedwidget_options.setStyleSheet(u"#page_1_blackjack  {\n"
"background-color:transparent;\n"
"}\n"
"\n"
"#page_2_agent_game_options {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"#page_3_train_agent_options {\n"
"background-color: transparent;\n"
"\n"
"}\n"
"\n"
"QFrame * {\n"
"border: None;\n"
"}\n"
"\n"
"\n"
"QPushButton::hover {\n"
"border: 2px solid rgba(212,185,58,255);\n"
"background-color: rgba(212,185,58,25);\n"
"}\n"
"\n"
"QPushButton{\n"
"font: 18pt \"Arial\";\n"
"border: 2px solid  rgb(120,124,116);\n"
"border-radius: 20px;\n"
"color: rgba(212,185,58,255);\n"
"background-color: rgba(39,52,45,255);\n"
"}\n"
"")
        self.page_1_blackjack = QWidget()
        self.page_1_blackjack.setObjectName(u"page_1_blackjack")
        self.verticalLayout_15 = QVBoxLayout(self.page_1_blackjack)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.game_image = QLabel(self.page_1_blackjack)
        self.game_image.setObjectName(u"game_image")
        self.game_image.setMinimumSize(QSize(250, 250))
        self.game_image.setMaximumSize(QSize(250, 250))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        self.game_image.setFont(font1)
        self.game_image.setPixmap(QPixmap(u":/icons/blackjack.png"))
        self.game_image.setScaledContents(True)
        self.game_image.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_15.addWidget(self.game_image, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stackedwidget_options.addWidget(self.page_1_blackjack)
        self.page_2_agent_game_options = QWidget()
        self.page_2_agent_game_options.setObjectName(u"page_2_agent_game_options")
        self.page_2_agent_game_options.setStyleSheet(u"QLabel {\n"
"    font: 24pt \"Forte\"; /* \u0130stedi\u011finiz font ve punto */\n"
"    color: rgba(212,185,58,255); /* Metin rengi */\n"
"color: rgb(39,52,45);\n"
"\n"
"}\n"
"\n"
"\n"
"/* QComboBox Genel Stili */\n"
"QComboBox {\n"
"    font: 16pt \"Arial\"; /* \u0130stedi\u011finiz font ve punto */\n"
"    color: rgba(212,185,58,255);; /* Metin rengi */\n"
"    background-color: rgba(39,52,45,255); /* Arka plan rengi */\n"
"    border: 2px solid rgb(120,124,116); /* Kenarl\u0131k */\n"
"    border-radius:20px; /* Tam yuvarlak k\u00f6\u015feler */\n"
"    padding: 5px 10px; /* \u0130\u00e7 bo\u015fluk */\n"
"    min-width: 150px; /* Minimum geni\u015flik */\n"
"}\n"
"\n"
"/* QComboBox Hover Durumu */\n"
"QComboBox:hover {\n"
"    background-color: rgba(120,124,116,50); /* Hafif arka plan de\u011fi\u015fikli\u011fi */\n"
"}\n"
"\n"
"/* QComboBox A\u00e7\u0131l\u0131r Men\u00fc (Drop-down) Butonu */\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"	marg"
                        "in: 5 5 5 0;\n"
"    width: 15px;\n"
"    border-left: 2px solid rgb(120,124,116);\n"
"    background-color: rgb(120,124,116); /* Ana arka plan rengi */\n"
"    border-bottom-right-radius: 12px;; /* Tam yuvarlak k\u00f6\u015feler */\n"
"	border-top-right-radius: 12px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout_5 = QHBoxLayout(self.page_2_agent_game_options)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox_agent_game_options = QGroupBox(self.page_2_agent_game_options)
        self.groupBox_agent_game_options.setObjectName(u"groupBox_agent_game_options")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_agent_game_options.sizePolicy().hasHeightForWidth())
        self.groupBox_agent_game_options.setSizePolicy(sizePolicy1)
        self.groupBox_agent_game_options.setMinimumSize(QSize(250, 0))
        self.groupBox_agent_game_options.setMaximumSize(QSize(250, 16777215))
        self.groupBox_agent_game_options.setStyleSheet(u"#frame_agent_game_options{\n"
"\n"
"}\n"
"\n"
"QGroupBox {\n"
"	font: 700 27pt \"Forte\";\n"
"	color:  rgba(212,185,58,255);\n"
"    margin-top: 0.9em;\n"
"	border-radius: 25px;\n"
"	background-color: rgba(120,124,116, 55);\n"
"	border: 3px solid rgb(120,124,116);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* Ba\u015fl\u0131\u011f\u0131 ortalamak i\u00e7in */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"")
        self.verticalLayout_23 = QVBoxLayout(self.groupBox_agent_game_options)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(10, 10, 10, 10)
        self.label_agent_game_mode_text = QLabel(self.groupBox_agent_game_options)
        self.label_agent_game_mode_text.setObjectName(u"label_agent_game_mode_text")

        self.verticalLayout_23.addWidget(self.label_agent_game_mode_text)

        self.frame_agent_game_mode = QFrame(self.groupBox_agent_game_options)
        self.frame_agent_game_mode.setObjectName(u"frame_agent_game_mode")
        self.frame_agent_game_mode.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_agent_game_mode.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_agent_game_mode)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.combobox_agent_game_mode = QComboBox(self.frame_agent_game_mode)
        self.combobox_agent_game_mode.addItem("")
        self.combobox_agent_game_mode.addItem("")
        self.combobox_agent_game_mode.addItem("")
        self.combobox_agent_game_mode.setObjectName(u"combobox_agent_game_mode")
        self.combobox_agent_game_mode.setMinimumSize(QSize(174, 40))
        self.combobox_agent_game_mode.setMaximumSize(QSize(180, 40))
        self.combobox_agent_game_mode.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.combobox_agent_game_mode.setStyleSheet(u"")

        self.horizontalLayout_47.addWidget(self.combobox_agent_game_mode, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_agent_game_mode_info = QLabel(self.frame_agent_game_mode)
        self.label_agent_game_mode_info.setObjectName(u"label_agent_game_mode_info")
        self.label_agent_game_mode_info.setMinimumSize(QSize(30, 30))
        self.label_agent_game_mode_info.setMaximumSize(QSize(30, 30))
        self.label_agent_game_mode_info.setCursor(QCursor(Qt.CursorShape.BusyCursor))
        self.label_agent_game_mode_info.setPixmap(QPixmap(u":/info/info.png"))
        self.label_agent_game_mode_info.setScaledContents(True)

        self.horizontalLayout_47.addWidget(self.label_agent_game_mode_info, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_23.addWidget(self.frame_agent_game_mode)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_2)

        self.label_agent_selection_text = QLabel(self.groupBox_agent_game_options)
        self.label_agent_selection_text.setObjectName(u"label_agent_selection_text")

        self.verticalLayout_23.addWidget(self.label_agent_selection_text)

        self.frame_agent_selection = QFrame(self.groupBox_agent_game_options)
        self.frame_agent_selection.setObjectName(u"frame_agent_selection")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_agent_selection.sizePolicy().hasHeightForWidth())
        self.frame_agent_selection.setSizePolicy(sizePolicy2)
        self.frame_agent_selection.setMinimumSize(QSize(0, 40))
        self.frame_agent_selection.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_agent_selection.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_agent_selection)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.combobox_agent_selection = QComboBox(self.frame_agent_selection)
        self.combobox_agent_selection.addItem("")
        self.combobox_agent_selection.setObjectName(u"combobox_agent_selection")
        self.combobox_agent_selection.setMinimumSize(QSize(174, 40))
        self.combobox_agent_selection.setMaximumSize(QSize(180, 40))
        self.combobox_agent_selection.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_38.addWidget(self.combobox_agent_selection, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_agent_selection_info = QLabel(self.frame_agent_selection)
        self.label_agent_selection_info.setObjectName(u"label_agent_selection_info")
        self.label_agent_selection_info.setMinimumSize(QSize(30, 30))
        self.label_agent_selection_info.setMaximumSize(QSize(30, 30))
        self.label_agent_selection_info.setCursor(QCursor(Qt.CursorShape.BusyCursor))
        self.label_agent_selection_info.setPixmap(QPixmap(u":/info/info.png"))
        self.label_agent_selection_info.setScaledContents(True)

        self.horizontalLayout_38.addWidget(self.label_agent_selection_info, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_23.addWidget(self.frame_agent_selection)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_5)

        self.button_agent_game_options_play = QPushButton(self.groupBox_agent_game_options)
        self.button_agent_game_options_play.setObjectName(u"button_agent_game_options_play")
        self.button_agent_game_options_play.setMinimumSize(QSize(100, 40))
        self.button_agent_game_options_play.setMaximumSize(QSize(100, 40))
        self.button_agent_game_options_play.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_agent_game_options_play.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_agent_game_options_play.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.button_agent_game_options_play, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_5.addWidget(self.groupBox_agent_game_options)

        self.stackedwidget_options.addWidget(self.page_2_agent_game_options)
        self.page_3_train_agent_options = QWidget()
        self.page_3_train_agent_options.setObjectName(u"page_3_train_agent_options")
        self.stackedwidget_options.addWidget(self.page_3_train_agent_options)

        self.verticalLayout_2.addWidget(self.stackedwidget_options)

        self.verticalSpacer1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer1)

        self.frame_menu_buttons = QFrame(self.page_1_menu)
        self.frame_menu_buttons.setObjectName(u"frame_menu_buttons")
        self.frame_menu_buttons.setMinimumSize(QSize(0, 0))
        self.frame_menu_buttons.setStyleSheet(u"")
        self.frame_menu_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_menu_buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_menu_buttons)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 50, -1, 10)
        self.button_train_agent = QPushButton(self.frame_menu_buttons)
        self.button_train_agent.setObjectName(u"button_train_agent")
        self.button_train_agent.setMinimumSize(QSize(200, 50))
        self.button_train_agent.setMaximumSize(QSize(200, 50))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(18)
        font2.setBold(False)
        font2.setItalic(False)
        self.button_train_agent.setFont(font2)
        self.button_train_agent.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_train_agent.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_train_agent.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(52,14,16,255);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.button_train_agent, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_play_buttons = QFrame(self.frame_menu_buttons)
        self.frame_play_buttons.setObjectName(u"frame_play_buttons")
        self.frame_play_buttons.setMinimumSize(QSize(245, 0))
        self.frame_play_buttons.setMaximumSize(QSize(245, 16777215))
        self.frame_play_buttons.setStyleSheet(u"")
        self.frame_play_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_play_buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_play_buttons)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 10, 0, 10)
        self.button_one_player_game = QPushButton(self.frame_play_buttons)
        self.button_one_player_game.setObjectName(u"button_one_player_game")
        self.button_one_player_game.setMinimumSize(QSize(225, 50))
        self.button_one_player_game.setMaximumSize(QSize(225, 50))
        self.button_one_player_game.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_one_player_game.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_one_player_game.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.button_one_player_game, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_agent_game = QPushButton(self.frame_play_buttons)
        self.button_agent_game.setObjectName(u"button_agent_game")
        self.button_agent_game.setMinimumSize(QSize(225, 50))
        self.button_agent_game.setMaximumSize(QSize(225, 50))
        self.button_agent_game.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_agent_game.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_agent_game.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.button_agent_game, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame_play_buttons, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_8)

        self.button_exit = QPushButton(self.frame_menu_buttons)
        self.button_exit.setObjectName(u"button_exit")
        self.button_exit.setMinimumSize(QSize(90, 35))
        self.button_exit.setMaximumSize(QSize(90, 35))
        self.button_exit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_exit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_exit.setStyleSheet(u"\n"
"#button_exit{\n"
"font: 16pt \"Arial\";\n"
"border: 2px solid  rgb(176,100,116);\n"
"border-radius: 15px;\n"
"color: rgb(176,100,116);\n"
"background-color: rgba(144,12,36,40);\n"
"}\n"
"\n"
"#button_exit::hover {\n"
"border: 2px solid rgb(144,12,36);\n"
"background-color: rgba(144,12,36,100);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.button_exit, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_menu_buttons)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.stackedwidget_content.addWidget(self.page_1_menu)
        self.page_2_game = QWidget()
        self.page_2_game.setObjectName(u"page_2_game")
        self.page_2_game.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.page_2_game)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.frame_announce = QFrame(self.page_2_game)
        self.frame_announce.setObjectName(u"frame_announce")
        sizePolicy1.setHeightForWidth(self.frame_announce.sizePolicy().hasHeightForWidth())
        self.frame_announce.setSizePolicy(sizePolicy1)
        self.frame_announce.setMinimumSize(QSize(0, 60))
        self.frame_announce.setStyleSheet(u"#frame_announce_inner {\n"
"border-top-right-radius: 30px;\n"
"border-bottom-right-radius: 30px;\n"
"background-color: rgb(45, 20, 9);\n"
"}\n"
"\n"
"#frame_announce_inner * {\n"
"font: 700 32pt \"Forte\";;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"border: 2px solid rgba(212,185,58,255);\n"
"background-color: rgba(212,185,58,75);\n"
"}\n"
"\n"
"QPushButton{\n"
"font: 16pt \"Arial\";\n"
"border: 2px solid  rgb(120,124,116);\n"
"background-color: rgba(120,124,116,75);\n"
"border-radius: 15px;\n"
"color: rgba(212,185,58,255);\n"
"}\n"
"\n"
"#label_cd {\n"
"font: 700 32pt \"Forte\";\n"
"color: white;\n"
"background-color:  rgba(39,52,45,255);\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"#label_announce{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(39,52,45,255),  stop:0.80 rgba(39,52,45,155), stop:1 rgba(39,52,45,0));\n"
"border-radius: 25px;\n"
"padding: 0 0 0 3;\n"
"color:white;\n"
"}")
        self.frame_announce.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_announce.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_announce)
        self.horizontalLayout_41.setSpacing(10)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 30, 0)
        self.frame_announce_inner = QFrame(self.frame_announce)
        self.frame_announce_inner.setObjectName(u"frame_announce_inner")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_announce_inner.sizePolicy().hasHeightForWidth())
        self.frame_announce_inner.setSizePolicy(sizePolicy3)
        self.frame_announce_inner.setMinimumSize(QSize(620, 50))
        self.frame_announce_inner.setMaximumSize(QSize(16777215, 60))
        self.frame_announce_inner.setStyleSheet(u"")
        self.frame_announce_inner.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_announce_inner.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_announce_inner)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 0, 2, 0)
        self.label_announce = QLabel(self.frame_announce_inner)
        self.label_announce.setObjectName(u"label_announce")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_announce.sizePolicy().hasHeightForWidth())
        self.label_announce.setSizePolicy(sizePolicy4)
        self.label_announce.setMinimumSize(QSize(0, 50))
        self.label_announce.setMaximumSize(QSize(16777215, 50))
        self.label_announce.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_announce.setStyleSheet(u"padding: 0 0 0 10px;")
        self.label_announce.setScaledContents(False)
        self.label_announce.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_announce)

        self.label_cd = QLabel(self.frame_announce_inner)
        self.label_cd.setObjectName(u"label_cd")
        self.label_cd.setEnabled(True)
        self.label_cd.setMinimumSize(QSize(50, 50))
        self.label_cd.setMaximumSize(QSize(50, 50))
        self.label_cd.setStyleSheet(u"")
        self.label_cd.setTextFormat(Qt.TextFormat.PlainText)
        self.label_cd.setScaledContents(False)
        self.label_cd.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_cd, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayout_41.addWidget(self.frame_announce_inner)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_4)

        self.button_reset = QPushButton(self.frame_announce)
        self.button_reset.setObjectName(u"button_reset")
        self.button_reset.setMinimumSize(QSize(80, 30))
        self.button_reset.setMaximumSize(QSize(80, 25))
        self.button_reset.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_41.addWidget(self.button_reset)

        self.button_menu = QPushButton(self.frame_announce)
        self.button_menu.setObjectName(u"button_menu")
        self.button_menu.setMinimumSize(QSize(80, 30))
        self.button_menu.setMaximumSize(QSize(80, 25))
        self.button_menu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_41.addWidget(self.button_menu)


        self.verticalLayout_4.addWidget(self.frame_announce)

        self.frame_content = QFrame(self.page_2_game)
        self.frame_content.setObjectName(u"frame_content")
        sizePolicy1.setHeightForWidth(self.frame_content.sizePolicy().hasHeightForWidth())
        self.frame_content.setSizePolicy(sizePolicy1)
        self.frame_content.setMinimumSize(QSize(0, 0))
        self.frame_content.setMaximumSize(QSize(16777215, 16777215))
        self.frame_content.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_content)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 10, 0)
        self.frame_game = QFrame(self.frame_content)
        self.frame_game.setObjectName(u"frame_game")
        self.frame_game.setMinimumSize(QSize(620, 700))
        self.frame_game.setMaximumSize(QSize(620, 700))
        self.frame_game.setToolTipDuration(0)
        self.frame_game.setStyleSheet(u"#frame_game * {\n"
"background-color: transparent;\n"
"color: rgba(212,185,58,255);\n"
"font: 13pt \"Forte\";\n"
"}\n"
"\n"
"\n"
"#frame_game {\n"
"background-color:  rgba(39,52,45,255);\n"
"border-right: 30px solid rgb(45, 20, 9);\n"
"border-top: 30px solid rgb(45, 20, 9);\n"
"border-bottom: 30px solid rgb(45, 20, 9);\n"
"border-bottom-right-radius: 50px;\n"
"border-top-right-radius: 50px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame_game.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_game.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_game.setLineWidth(0)
        self.verticalLayout_21 = QVBoxLayout(self.frame_game)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_seat2 = QFrame(self.frame_game)
        self.frame_seat2.setObjectName(u"frame_seat2")
        sizePolicy1.setHeightForWidth(self.frame_seat2.sizePolicy().hasHeightForWidth())
        self.frame_seat2.setSizePolicy(sizePolicy1)
        self.frame_seat2.setMinimumSize(QSize(590, 140))
        self.frame_seat2.setMaximumSize(QSize(590, 150))
        self.frame_seat2.setStyleSheet(u"#frame_seat2_cards {\n"
"background-color: rgba(255,255,255,10);\n"
"border-radius: 20\n"
"}\n"
"\n"
"#frame_seat2_cards * {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#label_seat2_total {\n"
"font: 18pt \"Forte\";\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#frame_seat2_budget * {\n"
"font: 18pt \"Forte\";\n"
"color: rgba(212,185,58,200);\n"
"}\n"
"\n"
"#frame_seat2_stake_amount * {\n"
"font: 18pt \"Forte\";\n"
"color: rgba(212,58,58,200);\n"
"}\n"
"\n"
"#frame_seat2_budget_amount {\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 0, 0, 0), stop: 0.7 rgba(212,185,58,25), stop:0.85 rgba(212,185,58,55), stop:1 rgba(212,185,58,105));\n"
"border: 1 solid rgb(104,102,50);\n"
"}\n"
"\n"
"#frame_seat2_stake_amount {\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 0), stop: 0.7 rgba(212,58,58,25), stop:0.85 rgba(212,58,58,55), stop:1 rgba(212,58,58,105))"
                        ";\n"
"border: 1 solid rgba(112,51,47,255);\n"
"}\n"
"\n"
"\n"
"\n"
"#label_seat2_total {\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 0, 0, 0), stop: 0.7 rgba(255,255,255,25), stop:0.85 rgba(255,255,255,55), stop:1 rgba(255,255,255,105));\n"
"border:1 solid rgb(144,144,144)\n"
"}\n"
"\n"
"#label_seat2_total_text {\n"
"font: 11pt \"Forte\";\n"
"color: rgba(255,255,255,150)\n"
"}\n"
"\n"
"\n"
"#label_seat2_budget_text {\n"
"font: 11pt \"Forte\";\n"
"}\n"
"\n"
"\n"
"#label_seat2_stake_text {\n"
"font: 11pt \"Forte\";\n"
"color: rgba(212,58,58,200);\n"
"\n"
"}\n"
"")
        self.frame_seat2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_seat2)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 10, 0)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.frame_seat2_budget_2 = QFrame(self.frame_seat2)
        self.frame_seat2_budget_2.setObjectName(u"frame_seat2_budget_2")
        self.frame_seat2_budget_2.setMinimumSize(QSize(60, 140))
        self.frame_seat2_budget_2.setMaximumSize(QSize(60, 16777215))
        self.frame_seat2_budget_2.setStyleSheet(u"")
        self.frame_seat2_budget_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_budget_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_seat2_budget_2)
        self.verticalLayout_22.setSpacing(10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 10, 0, 0)
        self.label_seat2_martini = QLabel(self.frame_seat2_budget_2)
        self.label_seat2_martini.setObjectName(u"label_seat2_martini")
        self.label_seat2_martini.setMinimumSize(QSize(50, 50))
        self.label_seat2_martini.setMaximumSize(QSize(50, 50))
        self.label_seat2_martini.setStyleSheet(u"")
        self.label_seat2_martini.setScaledContents(True)

        self.verticalLayout_22.addWidget(self.label_seat2_martini, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.label_seat2_budget_chips = QLabel(self.frame_seat2_budget_2)
        self.label_seat2_budget_chips.setObjectName(u"label_seat2_budget_chips")
        self.label_seat2_budget_chips.setMinimumSize(QSize(50, 50))
        self.label_seat2_budget_chips.setMaximumSize(QSize(50, 50))
        self.label_seat2_budget_chips.setStyleSheet(u"")
        self.label_seat2_budget_chips.setLineWidth(1)
        self.label_seat2_budget_chips.setScaledContents(True)
        self.label_seat2_budget_chips.setMargin(0)

        self.verticalLayout_22.addWidget(self.label_seat2_budget_chips, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addWidget(self.frame_seat2_budget_2)

        self.frame_seat2_budget = QFrame(self.frame_seat2)
        self.frame_seat2_budget.setObjectName(u"frame_seat2_budget")
        sizePolicy1.setHeightForWidth(self.frame_seat2_budget.sizePolicy().hasHeightForWidth())
        self.frame_seat2_budget.setSizePolicy(sizePolicy1)
        self.frame_seat2_budget.setMinimumSize(QSize(60, 141))
        self.frame_seat2_budget.setMaximumSize(QSize(60, 16777215))
        self.frame_seat2_budget.setStyleSheet(u"")
        self.frame_seat2_budget.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_budget.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_seat2_budget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 5, 0, 0)
        self.label_seat2_stake_text = QLabel(self.frame_seat2_budget)
        self.label_seat2_stake_text.setObjectName(u"label_seat2_stake_text")
        self.label_seat2_stake_text.setMinimumSize(QSize(50, 0))
        self.label_seat2_stake_text.setMaximumSize(QSize(50, 16777215))
        self.label_seat2_stake_text.setStyleSheet(u"")
        self.label_seat2_stake_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_seat2_stake_text, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.frame_seat2_stake_amount = QFrame(self.frame_seat2_budget)
        self.frame_seat2_stake_amount.setObjectName(u"frame_seat2_stake_amount")
        self.frame_seat2_stake_amount.setMinimumSize(QSize(45, 30))
        self.frame_seat2_stake_amount.setMaximumSize(QSize(45, 30))
        self.frame_seat2_stake_amount.setStyleSheet(u"")
        self.frame_seat2_stake_amount.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_stake_amount.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_seat2_stake_amount)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frame_seat2_spacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.frame_seat2_spacer_5)

        self.label_seat2_stake_dollar = QLabel(self.frame_seat2_stake_amount)
        self.label_seat2_stake_dollar.setObjectName(u"label_seat2_stake_dollar")
        self.label_seat2_stake_dollar.setMinimumSize(QSize(0, 0))
        self.label_seat2_stake_dollar.setMaximumSize(QSize(15, 16777215))
        self.label_seat2_stake_dollar.setScaledContents(True)
        self.label_seat2_stake_dollar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_45.addWidget(self.label_seat2_stake_dollar)

        self.label_seat2_stake_amount = QLabel(self.frame_seat2_stake_amount)
        self.label_seat2_stake_amount.setObjectName(u"label_seat2_stake_amount")
        self.label_seat2_stake_amount.setMinimumSize(QSize(0, 0))
        self.label_seat2_stake_amount.setMaximumSize(QSize(16777215, 16777215))
        self.label_seat2_stake_amount.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_seat2_stake_amount.setStyleSheet(u"")
        self.label_seat2_stake_amount.setScaledContents(True)

        self.horizontalLayout_45.addWidget(self.label_seat2_stake_amount)

        self.frame_seat2_spacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.frame_seat2_spacer_6)


        self.verticalLayout_9.addWidget(self.frame_seat2_stake_amount, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_seat2_budget_text = QLabel(self.frame_seat2_budget)
        self.label_seat2_budget_text.setObjectName(u"label_seat2_budget_text")
        self.label_seat2_budget_text.setMinimumSize(QSize(50, 11))
        self.label_seat2_budget_text.setMaximumSize(QSize(50, 11))
        self.label_seat2_budget_text.setStyleSheet(u"")
        self.label_seat2_budget_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_seat2_budget_text, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_seat2_budget_amount = QFrame(self.frame_seat2_budget)
        self.frame_seat2_budget_amount.setObjectName(u"frame_seat2_budget_amount")
        self.frame_seat2_budget_amount.setMinimumSize(QSize(45, 30))
        self.frame_seat2_budget_amount.setMaximumSize(QSize(45, 30))
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


        self.horizontalLayout_6.addWidget(self.frame_seat2_budget, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_seat2_total = QFrame(self.frame_seat2)
        self.frame_seat2_total.setObjectName(u"frame_seat2_total")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_seat2_total.sizePolicy().hasHeightForWidth())
        self.frame_seat2_total.setSizePolicy(sizePolicy5)
        self.frame_seat2_total.setMinimumSize(QSize(0, 140))
        self.frame_seat2_total.setMaximumSize(QSize(50, 16777215))
        self.frame_seat2_total.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_total.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_seat2_total)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 10, 0, 0)
        self.label_seat2_status = QLabel(self.frame_seat2_total)
        self.label_seat2_status.setObjectName(u"label_seat2_status")
        self.label_seat2_status.setMinimumSize(QSize(46, 46))
        self.label_seat2_status.setMaximumSize(QSize(46, 46))
        self.label_seat2_status.setScaledContents(True)

        self.verticalLayout_10.addWidget(self.label_seat2_status, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_seat2_total_text = QLabel(self.frame_seat2_total)
        self.label_seat2_total_text.setObjectName(u"label_seat2_total_text")
        self.label_seat2_total_text.setMaximumSize(QSize(60, 16777215))
        self.label_seat2_total_text.setStyleSheet(u"#label_stand{\n"
"	font: 13pt \"Forte\";\n"
"	color: rgba(255,255,255,150);\n"
"	background-color: transparent;\n"
"}")
        self.label_seat2_total_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_seat2_total_text, 0, Qt.AlignmentFlag.AlignBottom)

        self.label_seat2_total = QLabel(self.frame_seat2_total)
        self.label_seat2_total.setObjectName(u"label_seat2_total")
        self.label_seat2_total.setMinimumSize(QSize(40, 30))
        self.label_seat2_total.setMaximumSize(QSize(40, 30))
        self.label_seat2_total.setStyleSheet(u"")
        self.label_seat2_total.setScaledContents(True)
        self.label_seat2_total.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_seat2_total, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.frame_seat2_total, 0, Qt.AlignmentFlag.AlignVCenter)

        self.frame_seat2_cards = QFrame(self.frame_seat2)
        self.frame_seat2_cards.setObjectName(u"frame_seat2_cards")
        self.frame_seat2_cards.setMinimumSize(QSize(260, 140))
        self.frame_seat2_cards.setMaximumSize(QSize(260, 140))
        self.frame_seat2_cards.setStyleSheet(u"")
        self.frame_seat2_cards.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_cards.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_seat2_cards)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(5)
        self.gridLayout_6.setContentsMargins(2, 5, 1, 5)
        self.frame_seat2_card9 = QFrame(self.frame_seat2_cards)
        self.frame_seat2_card9.setObjectName(u"frame_seat2_card9")
        self.frame_seat2_card9.setMinimumSize(QSize(50, 60))
        self.frame_seat2_card9.setMaximumSize(QSize(50, 60))
        self.frame_seat2_card9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_card9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_seat2_card9)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_seat2_card9 = QLabel(self.frame_seat2_card9)
        self.label_seat2_card9.setObjectName(u"label_seat2_card9")
        self.label_seat2_card9.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_seat2_card9)


        self.gridLayout_6.addWidget(self.frame_seat2_card9, 1, 1, 1, 1)

        self.frame_seat2_card10 = QFrame(self.frame_seat2_cards)
        self.frame_seat2_card10.setObjectName(u"frame_seat2_card10")
        self.frame_seat2_card10.setMinimumSize(QSize(50, 60))
        self.frame_seat2_card10.setMaximumSize(QSize(50, 60))
        self.frame_seat2_card10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_card10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_seat2_card10)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_seat2_card10 = QLabel(self.frame_seat2_card10)
        self.label_seat2_card10.setObjectName(u"label_seat2_card10")
        self.label_seat2_card10.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_seat2_card10)


        self.gridLayout_6.addWidget(self.frame_seat2_card10, 1, 0, 1, 1)

        self.frame_seat2_card8 = QFrame(self.frame_seat2_cards)
        self.frame_seat2_card8.setObjectName(u"frame_seat2_card8")
        self.frame_seat2_card8.setMinimumSize(QSize(50, 60))
        self.frame_seat2_card8.setMaximumSize(QSize(50, 60))
        self.frame_seat2_card8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_card8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_seat2_card8)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_seat2_card8 = QLabel(self.frame_seat2_card8)
        self.label_seat2_card8.setObjectName(u"label_seat2_card8")
        self.label_seat2_card8.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.label_seat2_card8)


        self.gridLayout_6.addWidget(self.frame_seat2_card8, 1, 2, 1, 1)

        self.frame_seat2_card6 = QFrame(self.frame_seat2_cards)
        self.frame_seat2_card6.setObjectName(u"frame_seat2_card6")
        self.frame_seat2_card6.setMinimumSize(QSize(50, 60))
        self.frame_seat2_card6.setMaximumSize(QSize(50, 60))
        self.frame_seat2_card6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_card6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_seat2_card6)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_seat2_card6 = QLabel(self.frame_seat2_card6)
        self.label_seat2_card6.setObjectName(u"label_seat2_card6")
        self.label_seat2_card6.setScaledContents(True)

        self.horizontalLayout_32.addWidget(self.label_seat2_card6)


        self.gridLayout_6.addWidget(self.frame_seat2_card6, 1, 4, 1, 1)

        self.frame_seat2_card7 = QFrame(self.frame_seat2_cards)
        self.frame_seat2_card7.setObjectName(u"frame_seat2_card7")
        self.frame_seat2_card7.setMinimumSize(QSize(50, 60))
        self.frame_seat2_card7.setMaximumSize(QSize(50, 60))
        self.frame_seat2_card7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_card7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_seat2_card7)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_seat2_card7 = QLabel(self.frame_seat2_card7)
        self.label_seat2_card7.setObjectName(u"label_seat2_card7")
        self.label_seat2_card7.setScaledContents(True)

        self.horizontalLayout_31.addWidget(self.label_seat2_card7)


        self.gridLayout_6.addWidget(self.frame_seat2_card7, 1, 3, 1, 1)

        self.frame_seat2_card1 = QFrame(self.frame_seat2_cards)
        self.frame_seat2_card1.setObjectName(u"frame_seat2_card1")
        self.frame_seat2_card1.setMinimumSize(QSize(50, 60))
        self.frame_seat2_card1.setMaximumSize(QSize(50, 60))
        self.frame_seat2_card1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_card1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_seat2_card1)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_seat2_card1 = QLabel(self.frame_seat2_card1)
        self.label_seat2_card1.setObjectName(u"label_seat2_card1")
        self.label_seat2_card1.setScaledContents(True)

        self.horizontalLayout_33.addWidget(self.label_seat2_card1)


        self.gridLayout_6.addWidget(self.frame_seat2_card1, 2, 4, 1, 1)

        self.frame_seat2_card2 = QFrame(self.frame_seat2_cards)
        self.frame_seat2_card2.setObjectName(u"frame_seat2_card2")
        self.frame_seat2_card2.setMinimumSize(QSize(50, 60))
        self.frame_seat2_card2.setMaximumSize(QSize(50, 60))
        self.frame_seat2_card2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_card2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_seat2_card2)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_seat2_card2 = QLabel(self.frame_seat2_card2)
        self.label_seat2_card2.setObjectName(u"label_seat2_card2")
        self.label_seat2_card2.setScaledContents(True)

        self.horizontalLayout_34.addWidget(self.label_seat2_card2)


        self.gridLayout_6.addWidget(self.frame_seat2_card2, 2, 3, 1, 1)

        self.frame_seat2_card3 = QFrame(self.frame_seat2_cards)
        self.frame_seat2_card3.setObjectName(u"frame_seat2_card3")
        self.frame_seat2_card3.setMinimumSize(QSize(50, 60))
        self.frame_seat2_card3.setMaximumSize(QSize(50, 60))
        self.frame_seat2_card3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_card3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_seat2_card3)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_seat2_card3 = QLabel(self.frame_seat2_card3)
        self.label_seat2_card3.setObjectName(u"label_seat2_card3")
        self.label_seat2_card3.setScaledContents(True)

        self.horizontalLayout_35.addWidget(self.label_seat2_card3)


        self.gridLayout_6.addWidget(self.frame_seat2_card3, 2, 2, 1, 1)

        self.frame_seat2_card4 = QFrame(self.frame_seat2_cards)
        self.frame_seat2_card4.setObjectName(u"frame_seat2_card4")
        self.frame_seat2_card4.setMinimumSize(QSize(50, 60))
        self.frame_seat2_card4.setMaximumSize(QSize(50, 60))
        self.frame_seat2_card4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_card4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_seat2_card4)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_seat2_card4 = QLabel(self.frame_seat2_card4)
        self.label_seat2_card4.setObjectName(u"label_seat2_card4")
        self.label_seat2_card4.setScaledContents(True)

        self.horizontalLayout_36.addWidget(self.label_seat2_card4)


        self.gridLayout_6.addWidget(self.frame_seat2_card4, 2, 1, 1, 1)

        self.frame_seat2_card5 = QFrame(self.frame_seat2_cards)
        self.frame_seat2_card5.setObjectName(u"frame_seat2_card5")
        self.frame_seat2_card5.setMinimumSize(QSize(50, 60))
        self.frame_seat2_card5.setMaximumSize(QSize(50, 60))
        self.frame_seat2_card5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_card5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_seat2_card5)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_seat2_card5 = QLabel(self.frame_seat2_card5)
        self.label_seat2_card5.setObjectName(u"label_seat2_card5")
        self.label_seat2_card5.setScaledContents(True)

        self.horizontalLayout_40.addWidget(self.label_seat2_card5)


        self.gridLayout_6.addWidget(self.frame_seat2_card5, 2, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.frame_seat2_cards, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_21.addWidget(self.frame_seat2)

        self.frame_table = QFrame(self.frame_game)
        self.frame_table.setObjectName(u"frame_table")
        self.frame_table.setMinimumSize(QSize(600, 330))
        self.frame_table.setMaximumSize(QSize(600, 330))
        self.frame_table.setStyleSheet(u"#frame_dealer_cards {\n"
"background-color: rgba(212,185,58,20);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#frame_dealer_cards * {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#label_dealer_total {\n"
"font: 18pt \"Forte\";\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"#label_dealer_total {\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 0, 0, 0), stop: 0.7 rgba(255,255,255,25), stop:0.85 rgba(255,255,255,55), stop:1 rgba(255,255,255,105));\n"
"border:1 solid rgb(144,144,144)\n"
"}\n"
"\n"
"#label_dealer_total_text {\n"
"font: 10pt \"Forte\";\n"
"color: rgba(255,255,255,150)\n"
"}\n"
"\n"
"\n"
"#label_deck_1, #label_deck_2 {\n"
"border:1 solid rgb(144,144,144);\n"
"border-radius: 8px;\n"
"background-color: rgba(144,144,144,20);\n"
"\n"
"}\n"
"\n"
"\n"
"#frame_blackjack_text *{\n"
"	font: 24pt \"Forte\";\n"
"	color: rgba(212,185,58,30);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame_table.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_table.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_table)
        self.horizontalLayout_28.setSpacing(5)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(5, 5, 5, 5)
        self.frame_dealer_cards = QFrame(self.frame_table)
        self.frame_dealer_cards.setObjectName(u"frame_dealer_cards")
        self.frame_dealer_cards.setMinimumSize(QSize(140, 260))
        self.frame_dealer_cards.setMaximumSize(QSize(140, 260))
        self.frame_dealer_cards.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dealer_cards.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_dealer_cards)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.frame_dealer_card2 = QFrame(self.frame_dealer_cards)
        self.frame_dealer_card2.setObjectName(u"frame_dealer_card2")
        self.frame_dealer_card2.setMinimumSize(QSize(60, 50))
        self.frame_dealer_card2.setMaximumSize(QSize(60, 50))
        self.frame_dealer_card2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dealer_card2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_dealer_card2)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_dealer_card2 = QLabel(self.frame_dealer_card2)
        self.label_dealer_card2.setObjectName(u"label_dealer_card2")
        self.label_dealer_card2.setMinimumSize(QSize(60, 50))
        self.label_dealer_card2.setMaximumSize(QSize(60, 50))
        self.label_dealer_card2.setScaledContents(True)

        self.horizontalLayout_13.addWidget(self.label_dealer_card2)


        self.gridLayout_4.addWidget(self.frame_dealer_card2, 1, 1, 1, 1)

        self.frame_dealer_card8 = QFrame(self.frame_dealer_cards)
        self.frame_dealer_card8.setObjectName(u"frame_dealer_card8")
        self.frame_dealer_card8.setMinimumSize(QSize(60, 50))
        self.frame_dealer_card8.setMaximumSize(QSize(60, 50))
        self.frame_dealer_card8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dealer_card8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_dealer_card8)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_dealer_card8 = QLabel(self.frame_dealer_card8)
        self.label_dealer_card8.setObjectName(u"label_dealer_card8")
        self.label_dealer_card8.setMinimumSize(QSize(60, 50))
        self.label_dealer_card8.setMaximumSize(QSize(60, 50))
        self.label_dealer_card8.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_dealer_card8)


        self.gridLayout_4.addWidget(self.frame_dealer_card8, 2, 0, 1, 1)

        self.frame_dealer_card3 = QFrame(self.frame_dealer_cards)
        self.frame_dealer_card3.setObjectName(u"frame_dealer_card3")
        self.frame_dealer_card3.setMinimumSize(QSize(60, 50))
        self.frame_dealer_card3.setMaximumSize(QSize(60, 50))
        self.frame_dealer_card3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dealer_card3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_dealer_card3)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_dealer_card3 = QLabel(self.frame_dealer_card3)
        self.label_dealer_card3.setObjectName(u"label_dealer_card3")
        self.label_dealer_card3.setMinimumSize(QSize(60, 50))
        self.label_dealer_card3.setMaximumSize(QSize(60, 50))
        self.label_dealer_card3.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.label_dealer_card3)


        self.gridLayout_4.addWidget(self.frame_dealer_card3, 2, 1, 1, 1)

        self.frame_dealer_card5 = QFrame(self.frame_dealer_cards)
        self.frame_dealer_card5.setObjectName(u"frame_dealer_card5")
        self.frame_dealer_card5.setMinimumSize(QSize(60, 50))
        self.frame_dealer_card5.setMaximumSize(QSize(60, 50))
        self.frame_dealer_card5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dealer_card5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_dealer_card5)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_dealer_card5 = QLabel(self.frame_dealer_card5)
        self.label_dealer_card5.setObjectName(u"label_dealer_card5")
        self.label_dealer_card5.setMinimumSize(QSize(60, 50))
        self.label_dealer_card5.setMaximumSize(QSize(60, 50))
        self.label_dealer_card5.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_dealer_card5)


        self.gridLayout_4.addWidget(self.frame_dealer_card5, 4, 1, 1, 1)

        self.frame_dealer_card10 = QFrame(self.frame_dealer_cards)
        self.frame_dealer_card10.setObjectName(u"frame_dealer_card10")
        self.frame_dealer_card10.setMinimumSize(QSize(60, 50))
        self.frame_dealer_card10.setMaximumSize(QSize(60, 50))
        self.frame_dealer_card10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dealer_card10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_dealer_card10)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_dealer_card10 = QLabel(self.frame_dealer_card10)
        self.label_dealer_card10.setObjectName(u"label_dealer_card10")
        self.label_dealer_card10.setMinimumSize(QSize(60, 50))
        self.label_dealer_card10.setMaximumSize(QSize(60, 50))
        self.label_dealer_card10.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.label_dealer_card10)


        self.gridLayout_4.addWidget(self.frame_dealer_card10, 4, 0, 1, 1)

        self.frame_dealer_card4 = QFrame(self.frame_dealer_cards)
        self.frame_dealer_card4.setObjectName(u"frame_dealer_card4")
        self.frame_dealer_card4.setMinimumSize(QSize(60, 50))
        self.frame_dealer_card4.setMaximumSize(QSize(60, 50))
        self.frame_dealer_card4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dealer_card4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_dealer_card4)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_dealer_card4 = QLabel(self.frame_dealer_card4)
        self.label_dealer_card4.setObjectName(u"label_dealer_card4")
        self.label_dealer_card4.setMinimumSize(QSize(60, 50))
        self.label_dealer_card4.setMaximumSize(QSize(60, 50))
        self.label_dealer_card4.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_dealer_card4)


        self.gridLayout_4.addWidget(self.frame_dealer_card4, 3, 1, 1, 1)

        self.frame_dealer_card9 = QFrame(self.frame_dealer_cards)
        self.frame_dealer_card9.setObjectName(u"frame_dealer_card9")
        self.frame_dealer_card9.setMinimumSize(QSize(60, 50))
        self.frame_dealer_card9.setMaximumSize(QSize(60, 50))
        self.frame_dealer_card9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dealer_card9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_dealer_card9)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_dealer_card9 = QLabel(self.frame_dealer_card9)
        self.label_dealer_card9.setObjectName(u"label_dealer_card9")
        self.label_dealer_card9.setMinimumSize(QSize(60, 50))
        self.label_dealer_card9.setMaximumSize(QSize(60, 50))
        self.label_dealer_card9.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_dealer_card9)


        self.gridLayout_4.addWidget(self.frame_dealer_card9, 3, 0, 1, 1)

        self.frame_dealer_card1 = QFrame(self.frame_dealer_cards)
        self.frame_dealer_card1.setObjectName(u"frame_dealer_card1")
        self.frame_dealer_card1.setMinimumSize(QSize(60, 50))
        self.frame_dealer_card1.setMaximumSize(QSize(60, 50))
        self.frame_dealer_card1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dealer_card1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_dealer_card1)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_dealer_card1 = QLabel(self.frame_dealer_card1)
        self.label_dealer_card1.setObjectName(u"label_dealer_card1")
        self.label_dealer_card1.setMinimumSize(QSize(60, 50))
        self.label_dealer_card1.setMaximumSize(QSize(60, 50))
        self.label_dealer_card1.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_dealer_card1)


        self.gridLayout_4.addWidget(self.frame_dealer_card1, 0, 1, 1, 1)

        self.frame_dealer_card7 = QFrame(self.frame_dealer_cards)
        self.frame_dealer_card7.setObjectName(u"frame_dealer_card7")
        self.frame_dealer_card7.setMinimumSize(QSize(60, 50))
        self.frame_dealer_card7.setMaximumSize(QSize(60, 50))
        self.frame_dealer_card7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dealer_card7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_dealer_card7)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_dealer_card7 = QLabel(self.frame_dealer_card7)
        self.label_dealer_card7.setObjectName(u"label_dealer_card7")
        self.label_dealer_card7.setMinimumSize(QSize(60, 50))
        self.label_dealer_card7.setMaximumSize(QSize(60, 50))
        self.label_dealer_card7.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_dealer_card7)


        self.gridLayout_4.addWidget(self.frame_dealer_card7, 1, 0, 1, 1)

        self.frame_dealer_card6 = QFrame(self.frame_dealer_cards)
        self.frame_dealer_card6.setObjectName(u"frame_dealer_card6")
        self.frame_dealer_card6.setMinimumSize(QSize(60, 50))
        self.frame_dealer_card6.setMaximumSize(QSize(60, 50))
        self.frame_dealer_card6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dealer_card6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_dealer_card6)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_dealer_card6 = QLabel(self.frame_dealer_card6)
        self.label_dealer_card6.setObjectName(u"label_dealer_card6")
        self.label_dealer_card6.setMinimumSize(QSize(60, 50))
        self.label_dealer_card6.setMaximumSize(QSize(60, 50))
        self.label_dealer_card6.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_dealer_card6)


        self.gridLayout_4.addWidget(self.frame_dealer_card6, 0, 0, 1, 1)


        self.horizontalLayout_28.addWidget(self.frame_dealer_cards)

        self.frame_blackjack_text = QFrame(self.frame_table)
        self.frame_blackjack_text.setObjectName(u"frame_blackjack_text")
        self.frame_blackjack_text.setMinimumSize(QSize(25, 280))
        self.frame_blackjack_text.setMaximumSize(QSize(25, 280))
        self.frame_blackjack_text.setStyleSheet(u"")
        self.frame_blackjack_text.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_blackjack_text.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_blackjack_text)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.labe_blackjack_text = QLabel(self.frame_blackjack_text)
        self.labe_blackjack_text.setObjectName(u"labe_blackjack_text")
        self.labe_blackjack_text.setMinimumSize(QSize(25, 25))
        self.labe_blackjack_text.setMaximumSize(QSize(25, 25))
        self.labe_blackjack_text.setStyleSheet(u"")
        self.labe_blackjack_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.labe_blackjack_text)

        self.labe_blackjack_text_2 = QLabel(self.frame_blackjack_text)
        self.labe_blackjack_text_2.setObjectName(u"labe_blackjack_text_2")
        self.labe_blackjack_text_2.setMinimumSize(QSize(25, 25))
        self.labe_blackjack_text_2.setMaximumSize(QSize(25, 25))
        self.labe_blackjack_text_2.setStyleSheet(u"")
        self.labe_blackjack_text_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.labe_blackjack_text_2)

        self.labe_blackjack_text_3 = QLabel(self.frame_blackjack_text)
        self.labe_blackjack_text_3.setObjectName(u"labe_blackjack_text_3")
        self.labe_blackjack_text_3.setMinimumSize(QSize(25, 25))
        self.labe_blackjack_text_3.setMaximumSize(QSize(25, 25))
        self.labe_blackjack_text_3.setStyleSheet(u"")
        self.labe_blackjack_text_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.labe_blackjack_text_3)

        self.labe_blackjack_text_4 = QLabel(self.frame_blackjack_text)
        self.labe_blackjack_text_4.setObjectName(u"labe_blackjack_text_4")
        self.labe_blackjack_text_4.setMinimumSize(QSize(25, 25))
        self.labe_blackjack_text_4.setMaximumSize(QSize(25, 25))
        self.labe_blackjack_text_4.setStyleSheet(u"")
        self.labe_blackjack_text_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.labe_blackjack_text_4)

        self.labe_blackjack_text_5 = QLabel(self.frame_blackjack_text)
        self.labe_blackjack_text_5.setObjectName(u"labe_blackjack_text_5")
        self.labe_blackjack_text_5.setMinimumSize(QSize(25, 25))
        self.labe_blackjack_text_5.setMaximumSize(QSize(25, 25))
        self.labe_blackjack_text_5.setStyleSheet(u"")
        self.labe_blackjack_text_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.labe_blackjack_text_5)

        self.labe_blackjack_text_6 = QLabel(self.frame_blackjack_text)
        self.labe_blackjack_text_6.setObjectName(u"labe_blackjack_text_6")
        self.labe_blackjack_text_6.setMinimumSize(QSize(25, 25))
        self.labe_blackjack_text_6.setMaximumSize(QSize(25, 25))
        self.labe_blackjack_text_6.setStyleSheet(u"")
        self.labe_blackjack_text_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.labe_blackjack_text_6)

        self.labe_blackjack_text_7 = QLabel(self.frame_blackjack_text)
        self.labe_blackjack_text_7.setObjectName(u"labe_blackjack_text_7")
        self.labe_blackjack_text_7.setMinimumSize(QSize(25, 25))
        self.labe_blackjack_text_7.setMaximumSize(QSize(25, 25))
        self.labe_blackjack_text_7.setStyleSheet(u"")
        self.labe_blackjack_text_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.labe_blackjack_text_7)

        self.labe_blackjack_text_8 = QLabel(self.frame_blackjack_text)
        self.labe_blackjack_text_8.setObjectName(u"labe_blackjack_text_8")
        self.labe_blackjack_text_8.setMinimumSize(QSize(25, 25))
        self.labe_blackjack_text_8.setMaximumSize(QSize(25, 25))
        self.labe_blackjack_text_8.setStyleSheet(u"")
        self.labe_blackjack_text_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.labe_blackjack_text_8)

        self.labe_blackjack_text_9 = QLabel(self.frame_blackjack_text)
        self.labe_blackjack_text_9.setObjectName(u"labe_blackjack_text_9")
        self.labe_blackjack_text_9.setMinimumSize(QSize(25, 25))
        self.labe_blackjack_text_9.setMaximumSize(QSize(25, 25))
        self.labe_blackjack_text_9.setStyleSheet(u"")
        self.labe_blackjack_text_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.labe_blackjack_text_9)


        self.horizontalLayout_28.addWidget(self.frame_blackjack_text)

        self.frame_dealer_total = QFrame(self.frame_table)
        self.frame_dealer_total.setObjectName(u"frame_dealer_total")
        self.frame_dealer_total.setMinimumSize(QSize(55, 220))
        self.frame_dealer_total.setMaximumSize(QSize(55, 220))
        self.frame_dealer_total.setStyleSheet(u"")
        self.frame_dealer_total.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dealer_total.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_dealer_total)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_deck_1 = QPushButton(self.frame_dealer_total)
        self.label_deck_1.setObjectName(u"label_deck_1")
        self.label_deck_1.setMinimumSize(QSize(50, 72))
        self.label_deck_1.setMaximumSize(QSize(50, 72))
        self.label_deck_1.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_deck_1.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/deck/card-deck.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.label_deck_1.setIcon(icon)
        self.label_deck_1.setIconSize(QSize(65, 65))

        self.verticalLayout_7.addWidget(self.label_deck_1, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_dealer_total_inner = QFrame(self.frame_dealer_total)
        self.frame_dealer_total_inner.setObjectName(u"frame_dealer_total_inner")
        self.frame_dealer_total_inner.setMinimumSize(QSize(50, 80))
        self.frame_dealer_total_inner.setMaximumSize(QSize(50, 80))
        self.frame_dealer_total_inner.setStyleSheet(u"")
        self.frame_dealer_total_inner.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dealer_total_inner.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_dealer_total_inner)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_13)

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
        self.label_dealer_total.setMinimumSize(QSize(40, 30))
        self.label_dealer_total.setMaximumSize(QSize(40, 30))
        self.label_dealer_total.setStyleSheet(u"")
        self.label_dealer_total.setScaledContents(True)
        self.label_dealer_total.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_dealer_total, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_14)


        self.verticalLayout_7.addWidget(self.frame_dealer_total_inner, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_deck_2 = QPushButton(self.frame_dealer_total)
        self.label_deck_2.setObjectName(u"label_deck_2")
        self.label_deck_2.setMinimumSize(QSize(50, 72))
        self.label_deck_2.setMaximumSize(QSize(50, 72))
        self.label_deck_2.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_deck_2.setStyleSheet(u"")
        self.label_deck_2.setIcon(icon)
        self.label_deck_2.setIconSize(QSize(65, 65))

        self.verticalLayout_7.addWidget(self.label_deck_2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_28.addWidget(self.frame_dealer_total)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_16)

        self.frame_table_inner = QFrame(self.frame_table)
        self.frame_table_inner.setObjectName(u"frame_table_inner")
        self.frame_table_inner.setMinimumSize(QSize(300, 320))
        self.frame_table_inner.setMaximumSize(QSize(300, 320))
        self.frame_table_inner.setStyleSheet(u"QLabel {\n"
"	font: italic 18pt \"Forte\";\n"
"}")
        self.frame_table_inner.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_table_inner.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_seat2_chips = QFrame(self.frame_table_inner)
        self.frame_seat2_chips.setObjectName(u"frame_seat2_chips")
        self.frame_seat2_chips.setGeometry(QRect(40, 10, 150, 60))
        self.frame_seat2_chips.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat2_chips.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_seat2_chips)
        self.horizontalLayout_27.setSpacing(1)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_seat2_chips_count = QLabel(self.frame_seat2_chips)
        self.label_seat2_chips_count.setObjectName(u"label_seat2_chips_count")
        self.label_seat2_chips_count.setMinimumSize(QSize(40, 40))
        self.label_seat2_chips_count.setMaximumSize(QSize(40, 40))
        self.label_seat2_chips_count.setScaledContents(True)
        self.label_seat2_chips_count.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.horizontalLayout_27.addWidget(self.label_seat2_chips_count)

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

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_13)

        self.frame_seat1_chips = QFrame(self.frame_table_inner)
        self.frame_seat1_chips.setObjectName(u"frame_seat1_chips")
        self.frame_seat1_chips.setGeometry(QRect(40, 250, 150, 60))
        self.frame_seat1_chips.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_chips.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_seat1_chips)
        self.horizontalLayout_26.setSpacing(1)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_seat1_chips_count = QLabel(self.frame_seat1_chips)
        self.label_seat1_chips_count.setObjectName(u"label_seat1_chips_count")
        self.label_seat1_chips_count.setMinimumSize(QSize(40, 40))
        self.label_seat1_chips_count.setMaximumSize(QSize(40, 40))
        self.label_seat1_chips_count.setStyleSheet(u"")
        self.label_seat1_chips_count.setScaledContents(True)
        self.label_seat1_chips_count.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.horizontalLayout_26.addWidget(self.label_seat1_chips_count)

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

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_9)

        self.label_seat1_text = QLabel(self.frame_table_inner)
        self.label_seat1_text.setObjectName(u"label_seat1_text")
        self.label_seat1_text.setGeometry(QRect(180, 300, 100, 25))
        self.label_seat1_text.setMinimumSize(QSize(100, 25))
        self.label_seat1_text.setMaximumSize(QSize(100, 25))
        self.label_seat1_text.setStyleSheet(u"color: rgba(255,255,255,30);\n"
"")
        self.label_seat1_text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_seat2_text = QLabel(self.frame_table_inner)
        self.label_seat2_text.setObjectName(u"label_seat2_text")
        self.label_seat2_text.setGeometry(QRect(180, 0, 100, 25))
        self.label_seat2_text.setMinimumSize(QSize(100, 25))
        self.label_seat2_text.setMaximumSize(QSize(100, 25))
        self.label_seat2_text.setStyleSheet(u"#label_seat2_text {\n"
"color: rgba(255,255,255,30);\n"
"\n"
"}")
        self.label_seat2_text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.frame_table_inner)


        self.verticalLayout_21.addWidget(self.frame_table)

        self.frame_seat1 = QFrame(self.frame_game)
        self.frame_seat1.setObjectName(u"frame_seat1")
        sizePolicy1.setHeightForWidth(self.frame_seat1.sizePolicy().hasHeightForWidth())
        self.frame_seat1.setSizePolicy(sizePolicy1)
        self.frame_seat1.setMinimumSize(QSize(590, 150))
        self.frame_seat1.setMaximumSize(QSize(590, 150))
        self.frame_seat1.setStyleSheet(u"#frame_seat1_cards {\n"
"background-color: rgba(255,255,255,10);\n"
"border-radius: 20;\n"
"}\n"
"\n"
"\n"
"#frame_seat1_cards * {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#label_seat1_total {\n"
"font: 18pt \"Forte\";\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#frame_seat1_budget * {\n"
"font: 18pt \"Forte\";\n"
"color: rgba(212,185,58,200);\n"
"}\n"
"\n"
"#frame_seat1_stake_amount * {\n"
"font: 18pt \"Forte\";\n"
"color: rgba(212,58,58,200);\n"
"}\n"
"\n"
"#frame_seat1_budget_amount {\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 0), stop: 0.7 rgba(212,185,58,25), stop:0.85 rgba(212,185,58,55), stop:1 rgba(212,185,58,105));\n"
"border: 1 solid rgb(104,102,50);\n"
"}\n"
"\n"
"#frame_seat1_stake_amount {\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 0), stop: 0.7 rgba(212,58,58,25), stop:0.85 rgba(212,58,58,55), stop:1 rgba(212,58,58"
                        ",105));\n"
"border: 1 solid rgba(112,51,47,255);\n"
"}\n"
"\n"
"\n"
"#label_seat1_total {\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 0), stop: 0.7 rgba(255,255,255,25), stop:0.85 rgba(255,255,255,55), stop:1 rgba(255,255,255,105));\n"
"border:1 solid rgb(144,144,144)\n"
"}\n"
"\n"
"#label_seat1_total_text {\n"
"font: 11pt \"Forte\";\n"
"color: rgba(255,255,255,150)\n"
"}\n"
"\n"
"#label_seat1_budget_text {\n"
"font: 11pt \"Forte\";\n"
"}\n"
"\n"
"#label_seat1_stake_text {\n"
"font: 11pt \"Forte\";\n"
"color: rgba(212,58,58,200);\n"
"\n"
"}\n"
"\n"
"")
        self.frame_seat1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_seat1)
        self.horizontalLayout_20.setSpacing(5)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 10, 5)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_7)

        self.frame_seat1_cocktail = QFrame(self.frame_seat1)
        self.frame_seat1_cocktail.setObjectName(u"frame_seat1_cocktail")
        sizePolicy1.setHeightForWidth(self.frame_seat1_cocktail.sizePolicy().hasHeightForWidth())
        self.frame_seat1_cocktail.setSizePolicy(sizePolicy1)
        self.frame_seat1_cocktail.setMinimumSize(QSize(60, 140))
        self.frame_seat1_cocktail.setMaximumSize(QSize(60, 16777215))
        self.frame_seat1_cocktail.setStyleSheet(u"")
        self.frame_seat1_cocktail.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_cocktail.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_seat1_cocktail)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 5, 0, 10)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)

        self.label_seat1_budget_chips = QLabel(self.frame_seat1_cocktail)
        self.label_seat1_budget_chips.setObjectName(u"label_seat1_budget_chips")
        self.label_seat1_budget_chips.setMinimumSize(QSize(50, 50))
        self.label_seat1_budget_chips.setMaximumSize(QSize(50, 50))
        self.label_seat1_budget_chips.setStyleSheet(u"")
        self.label_seat1_budget_chips.setLineWidth(1)
        self.label_seat1_budget_chips.setScaledContents(True)
        self.label_seat1_budget_chips.setMargin(0)

        self.verticalLayout_13.addWidget(self.label_seat1_budget_chips, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_seat1_martini = QLabel(self.frame_seat1_cocktail)
        self.label_seat1_martini.setObjectName(u"label_seat1_martini")
        self.label_seat1_martini.setMinimumSize(QSize(50, 50))
        self.label_seat1_martini.setMaximumSize(QSize(50, 50))
        self.label_seat1_martini.setStyleSheet(u"")
        self.label_seat1_martini.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.label_seat1_martini, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_20.addWidget(self.frame_seat1_cocktail)

        self.frame_seat1_budget = QFrame(self.frame_seat1)
        self.frame_seat1_budget.setObjectName(u"frame_seat1_budget")
        self.frame_seat1_budget.setMinimumSize(QSize(60, 140))
        self.frame_seat1_budget.setMaximumSize(QSize(60, 16777215))
        self.frame_seat1_budget.setStyleSheet(u"")
        self.frame_seat1_budget.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_budget.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_seat1_budget)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 5, 0, 0)
        self.frame_seat1_budget_amount = QFrame(self.frame_seat1_budget)
        self.frame_seat1_budget_amount.setObjectName(u"frame_seat1_budget_amount")
        self.frame_seat1_budget_amount.setMinimumSize(QSize(45, 30))
        self.frame_seat1_budget_amount.setMaximumSize(QSize(45, 30))
        self.frame_seat1_budget_amount.setStyleSheet(u"")
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
        self.label_seat1_budget_dollar.setMinimumSize(QSize(0, 0))
        self.label_seat1_budget_dollar.setMaximumSize(QSize(15, 16777215))
        self.label_seat1_budget_dollar.setScaledContents(True)
        self.label_seat1_budget_dollar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_seat1_budget_dollar)

        self.label_seat1_budget_amount = QLabel(self.frame_seat1_budget_amount)
        self.label_seat1_budget_amount.setObjectName(u"label_seat1_budget_amount")
        self.label_seat1_budget_amount.setMinimumSize(QSize(0, 0))
        self.label_seat1_budget_amount.setMaximumSize(QSize(16777215, 16777215))
        self.label_seat1_budget_amount.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_seat1_budget_amount.setStyleSheet(u"")
        self.label_seat1_budget_amount.setScaledContents(True)

        self.horizontalLayout_25.addWidget(self.label_seat1_budget_amount)

        self.frame_seat1_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.frame_seat1_spacer_2)


        self.verticalLayout_11.addWidget(self.frame_seat1_budget_amount, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_seat1_budget_text = QLabel(self.frame_seat1_budget)
        self.label_seat1_budget_text.setObjectName(u"label_seat1_budget_text")
        self.label_seat1_budget_text.setMinimumSize(QSize(50, 0))
        self.label_seat1_budget_text.setMaximumSize(QSize(50, 16777215))
        self.label_seat1_budget_text.setStyleSheet(u"#label_stand{\n"
"	font: 13pt \"Forte\";\n"
"	color: rgba(255,255,255,150);\n"
"	background-color: transparent;\n"
"}")
        self.label_seat1_budget_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_seat1_budget_text, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_seat1_stake_amount = QFrame(self.frame_seat1_budget)
        self.frame_seat1_stake_amount.setObjectName(u"frame_seat1_stake_amount")
        self.frame_seat1_stake_amount.setMinimumSize(QSize(45, 30))
        self.frame_seat1_stake_amount.setMaximumSize(QSize(45, 30))
        self.frame_seat1_stake_amount.setStyleSheet(u"")
        self.frame_seat1_stake_amount.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_stake_amount.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_seat1_stake_amount)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_seat1_spacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.frame_seat1_spacer_3)

        self.label_seat1_stake_dollar = QLabel(self.frame_seat1_stake_amount)
        self.label_seat1_stake_dollar.setObjectName(u"label_seat1_stake_dollar")
        self.label_seat1_stake_dollar.setMinimumSize(QSize(0, 0))
        self.label_seat1_stake_dollar.setMaximumSize(QSize(15, 16777215))
        self.label_seat1_stake_dollar.setScaledContents(True)
        self.label_seat1_stake_dollar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_43.addWidget(self.label_seat1_stake_dollar)

        self.label_seat1_stake_amount = QLabel(self.frame_seat1_stake_amount)
        self.label_seat1_stake_amount.setObjectName(u"label_seat1_stake_amount")
        self.label_seat1_stake_amount.setMinimumSize(QSize(0, 0))
        self.label_seat1_stake_amount.setMaximumSize(QSize(16777215, 16777215))
        self.label_seat1_stake_amount.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_seat1_stake_amount.setStyleSheet(u"")
        self.label_seat1_stake_amount.setScaledContents(True)

        self.horizontalLayout_43.addWidget(self.label_seat1_stake_amount)

        self.frame_seat1_spacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.frame_seat1_spacer_4)


        self.verticalLayout_11.addWidget(self.frame_seat1_stake_amount, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_seat1_stake_text = QLabel(self.frame_seat1_budget)
        self.label_seat1_stake_text.setObjectName(u"label_seat1_stake_text")
        self.label_seat1_stake_text.setMinimumSize(QSize(50, 0))
        self.label_seat1_stake_text.setMaximumSize(QSize(50, 16777215))
        self.label_seat1_stake_text.setStyleSheet(u"#label_stand{\n"
"	font: 13pt \"Forte\";\n"
"	color: rgba(255,255,255,150);\n"
"	background-color: transparent;\n"
"}")
        self.label_seat1_stake_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_seat1_stake_text, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)


        self.horizontalLayout_20.addWidget(self.frame_seat1_budget, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_seat1_total = QFrame(self.frame_seat1)
        self.frame_seat1_total.setObjectName(u"frame_seat1_total")
        self.frame_seat1_total.setMinimumSize(QSize(50, 140))
        self.frame_seat1_total.setMaximumSize(QSize(50, 16777215))
        self.frame_seat1_total.setStyleSheet(u"")
        self.frame_seat1_total.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_total.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_seat1_total)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 5, 0, 10)
        self.label_seat1_total = QLabel(self.frame_seat1_total)
        self.label_seat1_total.setObjectName(u"label_seat1_total")
        self.label_seat1_total.setMinimumSize(QSize(40, 30))
        self.label_seat1_total.setMaximumSize(QSize(40, 30))
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

        self.verticalLayout_12.addWidget(self.label_seat1_total_text, 0, Qt.AlignmentFlag.AlignTop)

        self.label_seat1_status = QLabel(self.frame_seat1_total)
        self.label_seat1_status.setObjectName(u"label_seat1_status")
        self.label_seat1_status.setMinimumSize(QSize(46, 46))
        self.label_seat1_status.setMaximumSize(QSize(46, 46))
        self.label_seat1_status.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.label_seat1_status, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_20.addWidget(self.frame_seat1_total)

        self.frame_seat1_cards = QFrame(self.frame_seat1)
        self.frame_seat1_cards.setObjectName(u"frame_seat1_cards")
        self.frame_seat1_cards.setMinimumSize(QSize(260, 140))
        self.frame_seat1_cards.setMaximumSize(QSize(260, 140))
        self.frame_seat1_cards.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_cards.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_seat1_cards)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(0)
        self.gridLayout_9.setVerticalSpacing(5)
        self.gridLayout_9.setContentsMargins(2, 5, 2, 5)
        self.frame_seat1_card8 = QFrame(self.frame_seat1_cards)
        self.frame_seat1_card8.setObjectName(u"frame_seat1_card8")
        self.frame_seat1_card8.setMinimumSize(QSize(50, 60))
        self.frame_seat1_card8.setMaximumSize(QSize(50, 60))
        self.frame_seat1_card8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_card8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_seat1_card8)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.label_seat1_card8 = QLabel(self.frame_seat1_card8)
        self.label_seat1_card8.setObjectName(u"label_seat1_card8")
        self.label_seat1_card8.setScaledContents(True)

        self.horizontalLayout_67.addWidget(self.label_seat1_card8)


        self.gridLayout_9.addWidget(self.frame_seat1_card8, 2, 2, 1, 1)

        self.frame_seat1_card7 = QFrame(self.frame_seat1_cards)
        self.frame_seat1_card7.setObjectName(u"frame_seat1_card7")
        self.frame_seat1_card7.setMinimumSize(QSize(50, 60))
        self.frame_seat1_card7.setMaximumSize(QSize(50, 60))
        self.frame_seat1_card7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_card7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_seat1_card7)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.label_seat1_card7 = QLabel(self.frame_seat1_card7)
        self.label_seat1_card7.setObjectName(u"label_seat1_card7")
        self.label_seat1_card7.setScaledContents(True)

        self.horizontalLayout_68.addWidget(self.label_seat1_card7)


        self.gridLayout_9.addWidget(self.frame_seat1_card7, 2, 1, 1, 1)

        self.frame_seat1_card1 = QFrame(self.frame_seat1_cards)
        self.frame_seat1_card1.setObjectName(u"frame_seat1_card1")
        self.frame_seat1_card1.setMinimumSize(QSize(50, 60))
        self.frame_seat1_card1.setMaximumSize(QSize(50, 60))
        self.frame_seat1_card1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_card1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_seat1_card1)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_seat1_card1 = QLabel(self.frame_seat1_card1)
        self.label_seat1_card1.setObjectName(u"label_seat1_card1")
        self.label_seat1_card1.setScaledContents(True)

        self.horizontalLayout_22.addWidget(self.label_seat1_card1)


        self.gridLayout_9.addWidget(self.frame_seat1_card1, 1, 0, 1, 1)

        self.frame_seat1_card4 = QFrame(self.frame_seat1_cards)
        self.frame_seat1_card4.setObjectName(u"frame_seat1_card4")
        self.frame_seat1_card4.setMinimumSize(QSize(50, 60))
        self.frame_seat1_card4.setMaximumSize(QSize(50, 60))
        self.frame_seat1_card4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_card4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_seat1_card4)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label_seat1_card4 = QLabel(self.frame_seat1_card4)
        self.label_seat1_card4.setObjectName(u"label_seat1_card4")
        self.label_seat1_card4.setScaledContents(True)

        self.horizontalLayout_64.addWidget(self.label_seat1_card4)


        self.gridLayout_9.addWidget(self.frame_seat1_card4, 1, 3, 1, 1)

        self.frame_seat1_card9 = QFrame(self.frame_seat1_cards)
        self.frame_seat1_card9.setObjectName(u"frame_seat1_card9")
        self.frame_seat1_card9.setMinimumSize(QSize(50, 60))
        self.frame_seat1_card9.setMaximumSize(QSize(50, 60))
        self.frame_seat1_card9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_card9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_seat1_card9)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.label_seat1_card9 = QLabel(self.frame_seat1_card9)
        self.label_seat1_card9.setObjectName(u"label_seat1_card9")
        self.label_seat1_card9.setScaledContents(True)

        self.horizontalLayout_66.addWidget(self.label_seat1_card9)


        self.gridLayout_9.addWidget(self.frame_seat1_card9, 2, 3, 1, 1)

        self.frame_seat1_card5 = QFrame(self.frame_seat1_cards)
        self.frame_seat1_card5.setObjectName(u"frame_seat1_card5")
        self.frame_seat1_card5.setMinimumSize(QSize(50, 60))
        self.frame_seat1_card5.setMaximumSize(QSize(50, 60))
        self.frame_seat1_card5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_card5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_seat1_card5)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_seat1_card5 = QLabel(self.frame_seat1_card5)
        self.label_seat1_card5.setObjectName(u"label_seat1_card5")
        self.label_seat1_card5.setScaledContents(True)

        self.horizontalLayout_63.addWidget(self.label_seat1_card5)


        self.gridLayout_9.addWidget(self.frame_seat1_card5, 1, 4, 1, 1)

        self.frame_seat1_card2 = QFrame(self.frame_seat1_cards)
        self.frame_seat1_card2.setObjectName(u"frame_seat1_card2")
        self.frame_seat1_card2.setMinimumSize(QSize(50, 60))
        self.frame_seat1_card2.setMaximumSize(QSize(50, 60))
        self.frame_seat1_card2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_card2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_seat1_card2)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_seat1_card2 = QLabel(self.frame_seat1_card2)
        self.label_seat1_card2.setObjectName(u"label_seat1_card2")
        self.label_seat1_card2.setMinimumSize(QSize(0, 0))
        self.label_seat1_card2.setMaximumSize(QSize(16777215, 16777215))
        self.label_seat1_card2.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.label_seat1_card2)


        self.gridLayout_9.addWidget(self.frame_seat1_card2, 1, 1, 1, 1)

        self.frame_seat1_card6 = QFrame(self.frame_seat1_cards)
        self.frame_seat1_card6.setObjectName(u"frame_seat1_card6")
        self.frame_seat1_card6.setMinimumSize(QSize(50, 60))
        self.frame_seat1_card6.setMaximumSize(QSize(50, 60))
        self.frame_seat1_card6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_card6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_seat1_card6)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.label_seat1_card6 = QLabel(self.frame_seat1_card6)
        self.label_seat1_card6.setObjectName(u"label_seat1_card6")
        self.label_seat1_card6.setScaledContents(True)

        self.horizontalLayout_69.addWidget(self.label_seat1_card6)


        self.gridLayout_9.addWidget(self.frame_seat1_card6, 2, 0, 1, 1)

        self.frame_seat1_card10 = QFrame(self.frame_seat1_cards)
        self.frame_seat1_card10.setObjectName(u"frame_seat1_card10")
        self.frame_seat1_card10.setMinimumSize(QSize(50, 60))
        self.frame_seat1_card10.setMaximumSize(QSize(50, 60))
        self.frame_seat1_card10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_card10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_seat1_card10)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_seat1_card10 = QLabel(self.frame_seat1_card10)
        self.label_seat1_card10.setObjectName(u"label_seat1_card10")
        self.label_seat1_card10.setScaledContents(True)

        self.horizontalLayout_65.addWidget(self.label_seat1_card10)


        self.gridLayout_9.addWidget(self.frame_seat1_card10, 2, 4, 1, 1)

        self.frame_seat1_card3 = QFrame(self.frame_seat1_cards)
        self.frame_seat1_card3.setObjectName(u"frame_seat1_card3")
        self.frame_seat1_card3.setMinimumSize(QSize(50, 60))
        self.frame_seat1_card3.setMaximumSize(QSize(50, 60))
        self.frame_seat1_card3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_seat1_card3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_seat1_card3)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.label_seat1_card3 = QLabel(self.frame_seat1_card3)
        self.label_seat1_card3.setObjectName(u"label_seat1_card3")
        self.label_seat1_card3.setScaledContents(True)

        self.horizontalLayout_62.addWidget(self.label_seat1_card3)


        self.gridLayout_9.addWidget(self.frame_seat1_card3, 1, 2, 1, 1)


        self.horizontalLayout_20.addWidget(self.frame_seat1_cards, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_21.addWidget(self.frame_seat1)


        self.horizontalLayout_4.addWidget(self.frame_game)

        self.frame_options = QFrame(self.frame_content)
        self.frame_options.setObjectName(u"frame_options")
        sizePolicy5.setHeightForWidth(self.frame_options.sizePolicy().hasHeightForWidth())
        self.frame_options.setSizePolicy(sizePolicy5)
        self.frame_options.setStyleSheet(u"#groupbox_bet {\n"
"	font: 700 24pt \"Forte\";\n"
"	color:  rgba(212,185,58,80);\n"
"	background-color: rgba(33,44,38,180);\n"
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
"	color: rgba(212,185,58,70)\n"
"}\n"
"\n"
"#groupbox_bet #frame_stake * {\n"
"	font: 700 16pt \"Forte\";\n"
"}\n"
"\n"
"#groupbox_bet #label_stake_amount {\n"
"	font: 700 22pt \"Forte\";\n"
"}\n"
"\n"
"#groupbox_bet QPushButton::hover {\n"
"	background-color:rgba(212, 185, 58,50);\n"
"}\n"
"\n"
"\n"
"#groupbox_bet QSlider {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#groupbox_bet QSlider::groove:horizontal {\n"
"    height: 20px;\n"
"    background-color: rgba(0,0,0,20);\n"
"    border-radius: 10px;\n"
"}\n"
""
                        "\n"
"#groupbox_bet #frame_stake {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#groupbox_bet #label_bet_info {\n"
"\n"
"	font: 10pt \"Forte\";\n"
"	color: rgba(212,185,58,35);\n"
"\n"
"}\n"
"\n"
"\n"
"/* --------------------------------------------------------*/\n"
"\n"
"\n"
"#groupbox_move {\n"
"	font: 700 24pt \"Forte\";\n"
"	color: rgba(212,185,58,80);\n"
"	background-color: rgba(33,44,38,180);\n"
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
"#groupbox_move #label_stake_amount {\n"
"	font: 700 16pt \"Forte\";\n"
"}\n"
"\n"
"\n"
"\n"
"#groupbox_move #frame_stake {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#groupbox_move #frame_stand_hit {\n"
"	font: 700 16pt \"Forte\";\n"
"	color:  rgb(150,150,150);\n"
"	background-color:  transparent;\n"
"	border-radius: 10px;	\n"
"}"
                        "\n"
"\n"
"#frame_stake_amount QLabel {\n"
"\n"
"	font: 10pt \"Forte\";\n"
"	color: rgba(212,185,58,0);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame_options.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_options.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_options.setMidLineWidth(0)
        self.verticalLayout_18 = QVBoxLayout(self.frame_options)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.groupbox_board = QGroupBox(self.frame_options)
        self.groupbox_board.setObjectName(u"groupbox_board")
        self.groupbox_board.setEnabled(True)
        self.groupbox_board.setMinimumSize(QSize(200, 300))
        self.groupbox_board.setMaximumSize(QSize(200, 300))
        self.groupbox_board.setStyleSheet(u"QGroupBox {\n"
"	font: 700 24pt \"Forte\";\n"
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
"QGroupBox QLineEdit {\n"
"	background-color: rgba(212,185,58,40);\n"
"	border-radius: 10px;	\n"
"	font: 700 16pt \"Forte\";\n"
"	color: rgba(212,185,58,255);\n"
"\n"
"}\n"
"\n"
"QGroupBox QLabel {\n"
"	background-color: transparent;\n"
"	font: 700 16pt \"Forte\";\n"
"	color: rgba(212,185,58, 100)\n"
"}\n"
"\n"
"#label_stake_amount {\n"
"	font: 700 16pt \"Forte\";\n"
"}\n"
"\n"
"\n"
"QGroupBox QPushButton {\n"
"	background-color: rgba(212, 185, 58,20);\n"
"	border-radius: 10px;\n"
"	font: 700 16pt \"Forte\";\n"
"	color: rgb(212, 185, 58);\n"
"}\n"
"\n"
"QGroupBox QPushButton::hover {\n"
"	bac"
                        "kground-color:rgba(212, 185, 58,50);\n"
"}\n"
"\n"
"\n"
"\n"
"QGroupBox QSlider {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QGroupBox QSlider::groove:horizontal {\n"
"    border: 1px solid rgb(212, 185, 58);\n"
"    height: 10px;\n"
"    background: rgba(212, 185, 58, 40);\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QGroupBox QSlider::handle:horizontal {\n"
"    background: rgb(180,180,180);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    /* margin: -5px 0; Handle, groove'da ortalanacak */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QGroupBox QSlider::handle:horizontal:pressed {\n"
"    background: rgb(212, 185, 58);\n"
"}\n"
"\n"
"\n"
"#frame_stake {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"Line {\n"
"background-color: rgba(212,185,58,255);\n"
"}\n"
"\n"
"#label_board_announce_icon {\n"
"font: 700 28pt \"Forte\";\n"
"color: white;\n"
"background-color:  rgba(39,52,45,255);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"#label_board_announce_player {\n"
"background-color: qlineargradient(spread:"
                        "pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(39,52,45,255),  stop:0.50 rgba(39,52,45,155), stop:1 rgba(39,52,45,0));\n"
"border-radius: 15px;\n"
"padding: 6 0 0 3;\n"
"color:white;\n"
"font: 700 28pt \"Forte\";\n"
"}\n"
"\n"
"#frame_board_announce {\n"
"background-color: rgba(212,185,58,55);\n"
"border-radius: 15px;\n"
"}\n"
"")
        self.verticalLayout_19 = QVBoxLayout(self.groupbox_board)
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(5, 0, 5, 3)
        self.frame_board_status = QFrame(self.groupbox_board)
        self.frame_board_status.setObjectName(u"frame_board_status")
        sizePolicy1.setHeightForWidth(self.frame_board_status.sizePolicy().hasHeightForWidth())
        self.frame_board_status.setSizePolicy(sizePolicy1)
        self.frame_board_status.setMinimumSize(QSize(0, 0))
        self.frame_board_status.setMaximumSize(QSize(16777215, 16777215))
        self.frame_board_status.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_board_status.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_board_status)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 0, 10, 10)
        self.label_status = QLabel(self.frame_board_status)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMinimumSize(QSize(0, 20))
        self.label_status.setMaximumSize(QSize(16777215, 20))
        font3 = QFont()
        font3.setFamilies([u"Forte"])
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setItalic(False)
        self.label_status.setFont(font3)
        self.label_status.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"	font: 700 18pt \"Forte\";\n"
"	color: rgba(255,255,255, 200)\n"
"}")

        self.verticalLayout_5.addWidget(self.label_status)

        self.frame_status_dealer = QFrame(self.frame_board_status)
        self.frame_status_dealer.setObjectName(u"frame_status_dealer")
        self.frame_status_dealer.setStyleSheet(u"")
        self.frame_status_dealer.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_status_dealer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_status_dealer)
        self.horizontalLayout_46.setSpacing(5)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_status_dealer_text = QLabel(self.frame_status_dealer)
        self.label_status_dealer_text.setObjectName(u"label_status_dealer_text")
        self.label_status_dealer_text.setMinimumSize(QSize(0, 15))
        self.label_status_dealer_text.setMaximumSize(QSize(16777215, 15))
        self.label_status_dealer_text.setStyleSheet(u"")

        self.horizontalLayout_46.addWidget(self.label_status_dealer_text)

        self.label_status_dealer = QLabel(self.frame_status_dealer)
        self.label_status_dealer.setObjectName(u"label_status_dealer")
        self.label_status_dealer.setMinimumSize(QSize(0, 15))
        self.label_status_dealer.setMaximumSize(QSize(16777215, 15))
        self.label_status_dealer.setStyleSheet(u"")

        self.horizontalLayout_46.addWidget(self.label_status_dealer)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_14)


        self.verticalLayout_5.addWidget(self.frame_status_dealer)

        self.frame_status_seat1 = QFrame(self.frame_board_status)
        self.frame_status_seat1.setObjectName(u"frame_status_seat1")
        self.frame_status_seat1.setStyleSheet(u"")
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


        self.verticalLayout_5.addWidget(self.frame_status_seat1)

        self.frame_status_seat2 = QFrame(self.frame_board_status)
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


        self.verticalLayout_5.addWidget(self.frame_status_seat2)


        self.verticalLayout_19.addWidget(self.frame_board_status)

        self.frame_board_lp = QFrame(self.groupbox_board)
        self.frame_board_lp.setObjectName(u"frame_board_lp")
        sizePolicy1.setHeightForWidth(self.frame_board_lp.sizePolicy().hasHeightForWidth())
        self.frame_board_lp.setSizePolicy(sizePolicy1)
        self.frame_board_lp.setMinimumSize(QSize(0, 0))
        self.frame_board_lp.setMaximumSize(QSize(16777215, 16777215))
        self.frame_board_lp.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_board_lp.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_board_lp)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(10, 10, 10, 10)
        self.frame_lp_lt = QFrame(self.frame_board_lp)
        self.frame_lp_lt.setObjectName(u"frame_lp_lt")
        self.frame_lp_lt.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_lp_lt.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_lp_lt)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_lp = QLabel(self.frame_lp_lt)
        self.label_lp.setObjectName(u"label_lp")
        self.label_lp.setMinimumSize(QSize(0, 15))
        self.label_lp.setMaximumSize(QSize(16777215, 15))
        self.label_lp.setFont(font3)
        self.label_lp.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"	font: 700 18pt \"Forte\";\n"
"	color: rgba(255,255,255, 200)\n"
"}")
        self.label_lp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_17.addWidget(self.label_lp)

        self.label_lp_lt = QLabel(self.frame_lp_lt)
        self.label_lp_lt.setObjectName(u"label_lp_lt")
        self.label_lp_lt.setMinimumSize(QSize(0, 20))
        self.label_lp_lt.setMaximumSize(QSize(16777215, 20))
        font4 = QFont()
        font4.setFamilies([u"Forte"])
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setItalic(False)
        self.label_lp_lt.setFont(font4)
        self.label_lp_lt.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"	font: 700 16pt \"Forte\";\n"
"	color: rgba(255,255,255, 150)\n"
"}")
        self.label_lp_lt.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_17.addWidget(self.label_lp_lt)


        self.verticalLayout_14.addWidget(self.frame_lp_lt)

        self.frame_lp_dealer = QFrame(self.frame_board_lp)
        self.frame_lp_dealer.setObjectName(u"frame_lp_dealer")
        self.frame_lp_dealer.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_lp_dealer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_lp_dealer)
        self.horizontalLayout_39.setSpacing(5)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_lp_dealer_text = QLabel(self.frame_lp_dealer)
        self.label_lp_dealer_text.setObjectName(u"label_lp_dealer_text")
        self.label_lp_dealer_text.setMinimumSize(QSize(0, 15))
        self.label_lp_dealer_text.setMaximumSize(QSize(16777215, 15))
        self.label_lp_dealer_text.setStyleSheet(u"")

        self.horizontalLayout_39.addWidget(self.label_lp_dealer_text)

        self.label_lp_latest_dealer = QLabel(self.frame_lp_dealer)
        self.label_lp_latest_dealer.setObjectName(u"label_lp_latest_dealer")
        self.label_lp_latest_dealer.setMinimumSize(QSize(0, 15))
        self.label_lp_latest_dealer.setMaximumSize(QSize(16777215, 15))
        self.label_lp_latest_dealer.setStyleSheet(u"")

        self.horizontalLayout_39.addWidget(self.label_lp_latest_dealer)

        self.label_lp_slash_3 = QLabel(self.frame_lp_dealer)
        self.label_lp_slash_3.setObjectName(u"label_lp_slash_3")
        self.label_lp_slash_3.setMinimumSize(QSize(0, 15))
        self.label_lp_slash_3.setMaximumSize(QSize(16777215, 15))
        self.label_lp_slash_3.setStyleSheet(u"")

        self.horizontalLayout_39.addWidget(self.label_lp_slash_3)

        self.label_lp_total_dealer = QLabel(self.frame_lp_dealer)
        self.label_lp_total_dealer.setObjectName(u"label_lp_total_dealer")
        self.label_lp_total_dealer.setMinimumSize(QSize(0, 15))
        self.label_lp_total_dealer.setMaximumSize(QSize(16777215, 15))
        self.label_lp_total_dealer.setStyleSheet(u"")

        self.horizontalLayout_39.addWidget(self.label_lp_total_dealer)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_10)


        self.verticalLayout_14.addWidget(self.frame_lp_dealer)

        self.frame_lp_seat1 = QFrame(self.frame_board_lp)
        self.frame_lp_seat1.setObjectName(u"frame_lp_seat1")
        self.frame_lp_seat1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_lp_seat1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_lp_seat1)
        self.horizontalLayout_42.setSpacing(6)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_lp_botseat = QLabel(self.frame_lp_seat1)
        self.label_lp_botseat.setObjectName(u"label_lp_botseat")
        self.label_lp_botseat.setMinimumSize(QSize(0, 15))
        self.label_lp_botseat.setMaximumSize(QSize(16777215, 15))
        self.label_lp_botseat.setStyleSheet(u"")

        self.horizontalLayout_42.addWidget(self.label_lp_botseat)

        self.label_lp_latest_seat1 = QLabel(self.frame_lp_seat1)
        self.label_lp_latest_seat1.setObjectName(u"label_lp_latest_seat1")
        self.label_lp_latest_seat1.setMinimumSize(QSize(0, 15))
        self.label_lp_latest_seat1.setMaximumSize(QSize(16777215, 15))
        self.label_lp_latest_seat1.setStyleSheet(u"")

        self.horizontalLayout_42.addWidget(self.label_lp_latest_seat1)

        self.label_lp_slash_2 = QLabel(self.frame_lp_seat1)
        self.label_lp_slash_2.setObjectName(u"label_lp_slash_2")
        self.label_lp_slash_2.setMinimumSize(QSize(0, 15))
        self.label_lp_slash_2.setMaximumSize(QSize(16777215, 15))
        self.label_lp_slash_2.setStyleSheet(u"")

        self.horizontalLayout_42.addWidget(self.label_lp_slash_2)

        self.label_lp_total_seat1 = QLabel(self.frame_lp_seat1)
        self.label_lp_total_seat1.setObjectName(u"label_lp_total_seat1")
        self.label_lp_total_seat1.setMinimumSize(QSize(0, 15))
        self.label_lp_total_seat1.setMaximumSize(QSize(16777215, 15))
        self.label_lp_total_seat1.setStyleSheet(u"")

        self.horizontalLayout_42.addWidget(self.label_lp_total_seat1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_11)


        self.verticalLayout_14.addWidget(self.frame_lp_seat1)

        self.frame_lp_seat2 = QFrame(self.frame_board_lp)
        self.frame_lp_seat2.setObjectName(u"frame_lp_seat2")
        self.frame_lp_seat2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_lp_seat2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_lp_seat2)
        self.horizontalLayout_44.setSpacing(6)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_lp_topseat = QLabel(self.frame_lp_seat2)
        self.label_lp_topseat.setObjectName(u"label_lp_topseat")
        self.label_lp_topseat.setMinimumSize(QSize(0, 15))
        self.label_lp_topseat.setMaximumSize(QSize(16777215, 15))
        self.label_lp_topseat.setStyleSheet(u"")

        self.horizontalLayout_44.addWidget(self.label_lp_topseat)

        self.label_lp_latest_seat2 = QLabel(self.frame_lp_seat2)
        self.label_lp_latest_seat2.setObjectName(u"label_lp_latest_seat2")
        self.label_lp_latest_seat2.setMinimumSize(QSize(0, 15))
        self.label_lp_latest_seat2.setMaximumSize(QSize(16777215, 15))
        self.label_lp_latest_seat2.setStyleSheet(u"")

        self.horizontalLayout_44.addWidget(self.label_lp_latest_seat2)

        self.label_lp_slash = QLabel(self.frame_lp_seat2)
        self.label_lp_slash.setObjectName(u"label_lp_slash")
        self.label_lp_slash.setMinimumSize(QSize(0, 15))
        self.label_lp_slash.setMaximumSize(QSize(16777215, 15))
        self.label_lp_slash.setStyleSheet(u"")

        self.horizontalLayout_44.addWidget(self.label_lp_slash)

        self.label_lp_total_seat2 = QLabel(self.frame_lp_seat2)
        self.label_lp_total_seat2.setObjectName(u"label_lp_total_seat2")
        self.label_lp_total_seat2.setMinimumSize(QSize(0, 15))
        self.label_lp_total_seat2.setMaximumSize(QSize(16777215, 15))
        self.label_lp_total_seat2.setStyleSheet(u"")

        self.horizontalLayout_44.addWidget(self.label_lp_total_seat2)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_12)


        self.verticalLayout_14.addWidget(self.frame_lp_seat2)


        self.verticalLayout_19.addWidget(self.frame_board_lp)


        self.verticalLayout_18.addWidget(self.groupbox_board)

        self.groupbox_bet = QGroupBox(self.frame_options)
        self.groupbox_bet.setObjectName(u"groupbox_bet")
        self.groupbox_bet.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.groupbox_bet.sizePolicy().hasHeightForWidth())
        self.groupbox_bet.setSizePolicy(sizePolicy1)
        self.groupbox_bet.setMinimumSize(QSize(200, 0))
        self.groupbox_bet.setMaximumSize(QSize(200, 16777215))
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

        self.frame_stake_amount = QFrame(self.groupbox_bet)
        self.frame_stake_amount.setObjectName(u"frame_stake_amount")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_stake_amount.sizePolicy().hasHeightForWidth())
        self.frame_stake_amount.setSizePolicy(sizePolicy6)
        self.frame_stake_amount.setMinimumSize(QSize(180, 20))
        self.frame_stake_amount.setMaximumSize(QSize(16777215, 20))
        self.frame_stake_amount.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_stake_amount.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_stake_amount)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_stake_amount_1 = QLabel(self.frame_stake_amount)
        self.label_stake_amount_1.setObjectName(u"label_stake_amount_1")
        self.label_stake_amount_1.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.label_stake_amount_1)

        self.label_stake_amount_3 = QLabel(self.frame_stake_amount)
        self.label_stake_amount_3.setObjectName(u"label_stake_amount_3")
        self.label_stake_amount_3.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.label_stake_amount_3)

        self.label_stake_amount_4 = QLabel(self.frame_stake_amount)
        self.label_stake_amount_4.setObjectName(u"label_stake_amount_4")
        self.label_stake_amount_4.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.label_stake_amount_4)

        self.label_stake_amount_5 = QLabel(self.frame_stake_amount)
        self.label_stake_amount_5.setObjectName(u"label_stake_amount_5")
        self.label_stake_amount_5.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.label_stake_amount_5)

        self.label_stake_amount_6 = QLabel(self.frame_stake_amount)
        self.label_stake_amount_6.setObjectName(u"label_stake_amount_6")
        self.label_stake_amount_6.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.label_stake_amount_6)

        self.label_stake_amount_7 = QLabel(self.frame_stake_amount)
        self.label_stake_amount_7.setObjectName(u"label_stake_amount_7")
        self.label_stake_amount_7.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.label_stake_amount_7)

        self.label_stake_amount_8 = QLabel(self.frame_stake_amount)
        self.label_stake_amount_8.setObjectName(u"label_stake_amount_8")
        self.label_stake_amount_8.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.label_stake_amount_8)

        self.label_stake_amount_2 = QLabel(self.frame_stake_amount)
        self.label_stake_amount_2.setObjectName(u"label_stake_amount_2")
        self.label_stake_amount_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.label_stake_amount_2)

        self.label_stake_amount_9 = QLabel(self.frame_stake_amount)
        self.label_stake_amount_9.setObjectName(u"label_stake_amount_9")
        self.label_stake_amount_9.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.label_stake_amount_9)

        self.label_stake_amount_10 = QLabel(self.frame_stake_amount)
        self.label_stake_amount_10.setObjectName(u"label_stake_amount_10")
        self.label_stake_amount_10.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.label_stake_amount_10)


        self.verticalLayout_8.addWidget(self.frame_stake_amount)

        self.label_bet_info = QLabel(self.groupbox_bet)
        self.label_bet_info.setObjectName(u"label_bet_info")
        self.label_bet_info.setStyleSheet(u"")
        self.label_bet_info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_bet_info)


        self.verticalLayout_18.addWidget(self.groupbox_bet)

        self.groupbox_move = QGroupBox(self.frame_options)
        self.groupbox_move.setObjectName(u"groupbox_move")
        self.groupbox_move.setEnabled(True)
        self.groupbox_move.setMinimumSize(QSize(200, 100))
        self.groupbox_move.setMaximumSize(QSize(200, 100))
        self.groupbox_move.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.groupbox_move)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.button_hit = QPushButton(self.groupbox_move)
        self.button_hit.setObjectName(u"button_hit")
        sizePolicy3.setHeightForWidth(self.button_hit.sizePolicy().hasHeightForWidth())
        self.button_hit.setSizePolicy(sizePolicy3)
        self.button_hit.setMinimumSize(QSize(65, 0))
        self.button_hit.setMaximumSize(QSize(65, 16777215))
        self.button_hit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_hit.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/deck/hit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_hit.setIcon(icon1)
        self.button_hit.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.button_hit)

        self.button_stand = QPushButton(self.groupbox_move)
        self.button_stand.setObjectName(u"button_stand")
        sizePolicy3.setHeightForWidth(self.button_stand.sizePolicy().hasHeightForWidth())
        self.button_stand.setSizePolicy(sizePolicy3)
        self.button_stand.setMinimumSize(QSize(65, 0))
        self.button_stand.setMaximumSize(QSize(65, 16777215))
        self.button_stand.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.button_stand.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/deck/stand.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_stand.setIcon(icon2)
        self.button_stand.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.button_stand)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.button_double = QPushButton(self.groupbox_move)
        self.button_double.setObjectName(u"button_double")
        self.button_double.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.button_double.sizePolicy().hasHeightForWidth())
        self.button_double.setSizePolicy(sizePolicy3)
        self.button_double.setMinimumSize(QSize(65, 0))
        self.button_double.setMaximumSize(QSize(65, 16777215))
        self.button_double.setCursor(QCursor(Qt.CursorShape.ClosedHandCursor))
        self.button_double.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/deck/double-up.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_double.setIcon(icon3)
        self.button_double.setIconSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.button_double)


        self.verticalLayout_18.addWidget(self.groupbox_move)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_10)


        self.horizontalLayout_4.addWidget(self.frame_options)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.stackedwidget_content.addWidget(self.page_2_game)

        self.verticalLayout.addWidget(self.stackedwidget_content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedwidget_content.setCurrentIndex(1)
        self.stackedwidget_options.setCurrentIndex(1)
        self.combobox_agent_game_mode.setCurrentIndex(0)
        self.combobox_agent_selection.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.game_header.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Blackjack</p></body></html>", None))
        self.by_anil_ergan.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">by An\u0131l ERGAN</p></body></html>", None))
        self.game_image.setText("")
        self.groupBox_agent_game_options.setTitle(QCoreApplication.translate("MainWindow", u"Agent Game Options", None))
        self.label_agent_game_mode_text.setText(QCoreApplication.translate("MainWindow", u"Agent Game Mode", None))
        self.combobox_agent_game_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"Agent vs Dealer", None))
        self.combobox_agent_game_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"Agent/Player vs Dealer", None))
        self.combobox_agent_game_mode.setItemText(2, QCoreApplication.translate("MainWindow", u"Agent/Agent vs Dealer", None))

        self.combobox_agent_game_mode.setCurrentText(QCoreApplication.translate("MainWindow", u"Agent vs Dealer", None))
#if QT_CONFIG(tooltip)
        self.label_agent_game_mode_info.setToolTip(QCoreApplication.translate("MainWindow", u"Info", None))
#endif // QT_CONFIG(tooltip)
        self.label_agent_game_mode_info.setText("")
        self.label_agent_selection_text.setText(QCoreApplication.translate("MainWindow", u"Agent Selection", None))
        self.combobox_agent_selection.setItemText(0, QCoreApplication.translate("MainWindow", u"Rubi001", None))

        self.combobox_agent_selection.setCurrentText(QCoreApplication.translate("MainWindow", u"Rubi001", None))
#if QT_CONFIG(tooltip)
        self.label_agent_selection_info.setToolTip(QCoreApplication.translate("MainWindow", u"Info ", None))
#endif // QT_CONFIG(tooltip)
        self.label_agent_selection_info.setText("")
        self.button_agent_game_options_play.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.button_train_agent.setText(QCoreApplication.translate("MainWindow", u"Train an Agent", None))
        self.button_one_player_game.setText(QCoreApplication.translate("MainWindow", u"One Player Game", None))
        self.button_agent_game.setText(QCoreApplication.translate("MainWindow", u"Agent Game", None))
        self.button_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(tooltip)
        self.label_announce.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_announce.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_announce.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.label_cd.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>10</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_cd.setText("")
        self.button_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.button_menu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_seat2_martini.setText("")
        self.label_seat2_budget_chips.setText("")
        self.label_seat2_stake_text.setText(QCoreApplication.translate("MainWindow", u"stake", None))
        self.label_seat2_stake_dollar.setText("")
        self.label_seat2_stake_amount.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.label_seat2_budget_text.setText(QCoreApplication.translate("MainWindow", u"budget", None))
        self.label_seat2_budget_dollar.setText("")
        self.label_seat2_budget_amount.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.label_seat2_status.setText("")
        self.label_seat2_total_text.setText(QCoreApplication.translate("MainWindow", u"total", None))
        self.label_seat2_total.setText("")
        self.label_seat2_card9.setText("")
        self.label_seat2_card10.setText("")
        self.label_seat2_card8.setText("")
        self.label_seat2_card6.setText("")
        self.label_seat2_card7.setText("")
        self.label_seat2_card1.setText("")
        self.label_seat2_card2.setText("")
        self.label_seat2_card3.setText("")
        self.label_seat2_card4.setText("")
        self.label_seat2_card5.setText("")
        self.label_dealer_card2.setText("")
        self.label_dealer_card8.setText("")
        self.label_dealer_card3.setText("")
        self.label_dealer_card5.setText("")
        self.label_dealer_card10.setText("")
        self.label_dealer_card4.setText("")
        self.label_dealer_card9.setText("")
        self.label_dealer_card1.setText("")
        self.label_dealer_card7.setText("")
        self.label_dealer_card6.setText("")
        self.labe_blackjack_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>B</p></body></html>", None))
        self.labe_blackjack_text_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>L</p></body></html>", None))
        self.labe_blackjack_text_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>A</p></body></html>", None))
        self.labe_blackjack_text_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>C</p></body></html>", None))
        self.labe_blackjack_text_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K</p></body></html>", None))
        self.labe_blackjack_text_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>J</p></body></html>", None))
        self.labe_blackjack_text_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>A</p></body></html>", None))
        self.labe_blackjack_text_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>C</p></body></html>", None))
        self.labe_blackjack_text_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>K</p></body></html>", None))
        self.label_deck_1.setText("")
        self.label_dealer_total_text.setText(QCoreApplication.translate("MainWindow", u"total", None))
        self.label_dealer_total.setText("")
        self.label_deck_2.setText("")
        self.label_seat2_chips_count.setText("")
        self.label_seat2_chips_image.setText("")
        self.label_seat2_chips_image_2.setText("")
        self.label_seat1_chips_count.setText("")
        self.label_seat1_chips_image.setText("")
        self.label_seat1_chips_image_2.setText("")
        self.label_seat1_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>S  E  A  T  1</p></body></html>", None))
        self.label_seat2_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>S E A T 2</p></body></html>", None))
        self.label_seat1_budget_chips.setText("")
        self.label_seat1_martini.setText("")
        self.label_seat1_budget_dollar.setText("")
        self.label_seat1_budget_amount.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.label_seat1_budget_text.setText(QCoreApplication.translate("MainWindow", u"budget", None))
        self.label_seat1_stake_dollar.setText("")
        self.label_seat1_stake_amount.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.label_seat1_stake_text.setText(QCoreApplication.translate("MainWindow", u"stake", None))
        self.label_seat1_total.setText("")
        self.label_seat1_total_text.setText(QCoreApplication.translate("MainWindow", u"total", None))
        self.label_seat1_status.setText("")
        self.label_seat1_card8.setText("")
        self.label_seat1_card7.setText("")
        self.label_seat1_card1.setText("")
        self.label_seat1_card4.setText("")
        self.label_seat1_card9.setText("")
        self.label_seat1_card5.setText("")
        self.label_seat1_card2.setText("")
        self.label_seat1_card6.setText("")
        self.label_seat1_card10.setText("")
        self.label_seat1_card3.setText("")
        self.groupbox_board.setTitle(QCoreApplication.translate("MainWindow", u"Board", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_status_dealer_text.setText(QCoreApplication.translate("MainWindow", u"dealer:", None))
        self.label_status_dealer.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_status_botseat_text.setText(QCoreApplication.translate("MainWindow", u"seat 1: ", None))
        self.label_status_seat1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_status_topseat_text.setText(QCoreApplication.translate("MainWindow", u"seat 2:", None))
        self.label_status_seat2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_lp.setText(QCoreApplication.translate("MainWindow", u"Loss & Profit", None))
        self.label_lp_lt.setText(QCoreApplication.translate("MainWindow", u"latest / total", None))
        self.label_lp_dealer_text.setText(QCoreApplication.translate("MainWindow", u"dealer:", None))
        self.label_lp_latest_dealer.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_lp_slash_3.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_lp_total_dealer.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_lp_botseat.setText(QCoreApplication.translate("MainWindow", u"seat1:", None))
        self.label_lp_latest_seat1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_lp_slash_2.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_lp_total_seat1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_lp_topseat.setText(QCoreApplication.translate("MainWindow", u"seat2:", None))
        self.label_lp_latest_seat2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_lp_slash.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_lp_total_seat2.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(tooltip)
        self.groupbox_bet.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.groupbox_bet.setTitle(QCoreApplication.translate("MainWindow", u"Place Your Bet!", None))
        self.label_stake.setText(QCoreApplication.translate("MainWindow", u"Stake", None))
        self.label_stake_amount.setText("")
        self.label_stake_dollar.setText(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_stake_amount_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_stake_amount_3.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_stake_amount_4.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_stake_amount_5.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_stake_amount_6.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_stake_amount_7.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_stake_amount_8.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_stake_amount_2.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_stake_amount_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.label_stake_amount_10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_bet_info.setText(QCoreApplication.translate("MainWindow", u"drag the coin horizontal", None))
        self.groupbox_move.setTitle(QCoreApplication.translate("MainWindow", u"Move", None))
        self.button_hit.setText("")
        self.button_stand.setText("")
        self.button_double.setText("")
    # retranslateUi

