# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindows.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from codeeditor import CodeEditor

import sources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(924, 638)
        MainWindow.setStyleSheet(u"* {\n"
"border: none;\n"
"}\n"
"\n"
"/*BEGIN TOP*/\n"
"/******************************************************/\n"
"#top {\n"
"background: #3C3C3C;\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"}\n"
"\n"
"#basic_buttons > QPushButton, #btn_add { background: transparent; border-radius: 4px; }\n"
"#basic_buttons > QPushButton:hover, #btn_add:hover { background: #505050; }\n"
"\n"
"#btn_minimize { image: url(:/icons/assets/icons/minimize.png); }\n"
"#btn_maximize { image: url(:/icons/assets/icons/maximize.png); }\n"
"#btn_close { image: url(:/icons/assets/icons/close.png); }\n"
"#btn_add { image: url(:/icons/assets/icons/add.png); }\n"
"\n"
"#pages { padding-top: 5px; }\n"
"#pages > QPushButton {\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"background-image: url(:/icons/assets/icons/icon-top.png), url(:/icons/assets/icons/close.png);\n"
"\n"
"color: #fff;\n"
"background-color: #3C3C3C;\n"
"\n"
"text-align: left;\n"
"padding-left: 35px;\n"
"padding-right: 10p"
                        "x;\n"
"\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"}\n"
"\n"
"#pages > QPushButton:hover {\n"
"color: #3C3C3C;\n"
"background-color: #E8EBEA;\n"
"}\n"
"\n"
"/*END TOP*/\n"
"/******************************************************/\n"
"\n"
"\n"
"\n"
"/*BEGIN MENU*/\n"
"/******************************************************/\n"
"#menu {\n"
"border-bottom: 1px solid #3C3C3C;\n"
"}\n"
"\n"
"#menu > QPushButton {\n"
"background: transparent;\n"
"padding: 4px 5px;\n"
"border-radius: 2px;\n"
"color: #fff;\n"
"font-size: 9pt;\n"
"}\n"
"#menu > QPushButton:hover {\n"
"background: #505050;\n"
"}\n"
"\n"
"/*END MENU*/\n"
"/******************************************************/\n"
"\n"
"\n"
"\n"
"\n"
"/*BEGIN CENTER*/\n"
"/******************************************************/\n"
"\n"
"\n"
"CodeEditor, #document_1, #txt_cmd, #menu {\n"
"background: #1E1E1E;\n"
"font: 100 12pt \"Consolas\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#txt_cmd {\n"
"border-top: 1px solid #3C3C3C;\n"
"}\n"
"\n"
""
                        "\n"
"/*END CENTER*/\n"
"/******************************************************/\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*BEGIN BOTTOM*/\n"
"/******************************************************/\n"
"\n"
"#bottom {\n"
"background: #007ACC;\n"
"border-bottom-left-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"#bottom > QLabel {\n"
"color: #fff;\n"
"}\n"
"\n"
"#resize {\n"
"image: url(:/icons/assets/icons/resize.png);\n"
"}\n"
"\n"
"/*END BOTTOM*/\n"
"/******************************************************/")
        self.App = QWidget(MainWindow)
        self.App.setObjectName(u"App")
        self.App.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgba(255, 255, 255, 35);\n"
"    width: 20px;\n"
"    margin: 0px;\n"
" }\n"
"\n"
"\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgba(255, 255, 255, 175);\n"
"    min-height: 25px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"    height: 0px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    height: 0px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical { background: none; }\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal { backgrou"
                        "nd: none; }\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal { background: none; }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.App)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.top = QFrame(self.App)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 50))
        self.top.setMaximumSize(QSize(16777215, 50))
        self.top.setFrameShape(QFrame.StyledPanel)
        self.top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pages = QFrame(self.top)
        self.pages.setObjectName(u"pages")
        self.pages.setMinimumSize(QSize(0, 50))
        self.pages.setMaximumSize(QSize(16777215, 50))
        self.pages.setFrameShape(QFrame.StyledPanel)
        self.pages.setFrameShadow(QFrame.Raised)
        self.Layout_pages = QHBoxLayout(self.pages)
        self.Layout_pages.setSpacing(0)
        self.Layout_pages.setObjectName(u"Layout_pages")
        self.Layout_pages.setContentsMargins(1, 0, 0, 0)
        self.file_1 = QPushButton(self.pages)
        self.file_1.setObjectName(u"file_1")
        self.file_1.setMinimumSize(QSize(0, 45))
        self.file_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.Layout_pages.addWidget(self.file_1)


        self.horizontalLayout.addWidget(self.pages)

        self.btn_add = QPushButton(self.top)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMinimumSize(QSize(28, 28))
        self.btn_add.setMaximumSize(QSize(28, 28))
        self.btn_add.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_add)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.basic_buttons = QFrame(self.top)
        self.basic_buttons.setObjectName(u"basic_buttons")
        self.basic_buttons.setMinimumSize(QSize(0, 0))
        self.basic_buttons.setFrameShape(QFrame.StyledPanel)
        self.basic_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.basic_buttons)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_minimize = QPushButton(self.basic_buttons)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(28, 28))
        self.btn_minimize.setMaximumSize(QSize(28, 28))
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.basic_buttons)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(28, 28))
        self.btn_maximize.setMaximumSize(QSize(28, 28))
        self.btn_maximize.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.basic_buttons)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(28, 28))
        self.btn_close.setMaximumSize(QSize(28, 28))
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.basic_buttons)


        self.verticalLayout.addWidget(self.top)

        self.menu = QFrame(self.App)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(0, 36))
        self.menu.setMaximumSize(QSize(16777215, 36))
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.menu)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.file = QPushButton(self.menu)
        self.file.setObjectName(u"file")
        self.file.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.file)

        self.pushButton_5 = QPushButton(self.menu)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.menu)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_2 = QPushButton(self.menu)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.menu)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.menu)

        self.center = QSplitter(self.App)
        self.center.setObjectName(u"center")
        self.center.setOrientation(Qt.Vertical)
        self.center.setHandleWidth(0)
        self.stackedWidget = QStackedWidget(self.center)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.widget_layout_1 = QVBoxLayout(self.page_1)
        self.widget_layout_1.setSpacing(0)
        self.widget_layout_1.setObjectName(u"widget_layout_1")
        self.widget_layout_1.setContentsMargins(0, 0, 0, 0)
        self.document_1 = CodeEditor(self.page_1)
        self.document_1.setObjectName(u"document_1")
        self.document_1.setStyleSheet(u"")
        self.document_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.widget_layout_1.addWidget(self.document_1)

        self.stackedWidget.addWidget(self.page_1)
        self.center.addWidget(self.stackedWidget)
        self.txt_cmd = QTextEdit(self.center)
        self.txt_cmd.setObjectName(u"txt_cmd")
        self.txt_cmd.setMinimumSize(QSize(0, 0))
        self.txt_cmd.setStyleSheet(u"")
        self.txt_cmd.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.center.addWidget(self.txt_cmd)

        self.verticalLayout.addWidget(self.center)

        self.bottom = QFrame(self.App)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMinimumSize(QSize(0, 30))
        self.bottom.setMaximumSize(QSize(16777215, 30))
        self.bottom.setFrameShape(QFrame.StyledPanel)
        self.bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.bottom)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.label = QLabel(self.bottom)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.bottom)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.bottom)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(601, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.resize = QFrame(self.bottom)
        self.resize.setObjectName(u"resize")
        self.resize.setMinimumSize(QSize(30, 22))
        self.resize.setMaximumSize(QSize(22, 30))
        self.resize.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.resize.setFrameShape(QFrame.StyledPanel)
        self.resize.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.resize)


        self.verticalLayout.addWidget(self.bottom)

        MainWindow.setCentralWidget(self.App)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.file_1.setText(QCoreApplication.translate("MainWindow", u"file.txt", None))
        self.btn_add.setText("")
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.file.setText(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Ediccion", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Formato", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.document_1.setPlainText(QCoreApplication.translate("MainWindow", u"\n"
"fd\n"
"ffd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"\n"
"d\n"
"dfd\n"
"ffd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"\n"
"d\n"
"dfd\n"
"ffd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"\n"
"d\n"
"dfd\n"
"ffd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"\n"
"d\n"
"dfd\n"
"ffd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"\n"
"d\n"
"dfd\n"
"ffd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"\n"
"d\n"
"dfd\n"
"ffd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"\n"
"d\n"
"dfd\n"
"ffd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"\n"
"d\n"
"dfd\n"
"ffd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"\n"
"d\n"
"dfd\n"
"ffd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"\n"
"d\n"
"dfd\n"
"ffd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"\n"
"d\n"
"dfd\n"
"ffd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"fd\n"
"\n"
"d\n"
"d", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"line 1, column 4", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Windows (CFLF)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"UTF-8", None))
    # retranslateUi

