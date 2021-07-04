import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, pyqtRemoveInputHook, Qt
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QGraphicsDropShadowEffect, QPushButton, QFrame, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.uic.properties import QtGui
Ui_MainWindow, QtBaseClass = uic.loadUiType('m.ui')
from codeeditor import CodeEditor


class MyApp(QMainWindow):
	def __init__(self):
		self.newLines = 1
		super(MyApp, self).__init__(None)
		# menuBar = self.menuBar()
		# fileMenu = menuBar.addMenu('&File')

		# # New Action
		# self.newAction = QAction('&New', self)
		# self.newAction.triggered.connect(self.NewCall)
		# fileMenu.addAction(self.newAction)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)


		flags = QtCore.Qt.WindowFlags(QtCore.Qt.Dialog)
		self.setWindowFlags(flags|QtCore.Qt.FramelessWindowHint |QtCore.Qt.CustomizeWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)#fondo de la ventana transparente

		self.style_active = "color: #3C3C3C; background-color: #E8EBEA;"
		self.style_active_close = "image: url(:/icons/assets/icons/close-file.png);"
		
		# DROP SHADOW
		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(20)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QColor(0,0,0,200))
		self.ui.App.setGraphicsEffect(self.shadow)


		self.ui.btn_close.clicked.connect(self.close)
		self.ui.btn_maximize.clicked.connect(self.maximized)
		self.ui.btn_minimize.clicked.connect(self.showMinimized)

		self.ui.top.mouseMoveEvent = self.moveWindow
		self.ui.top.mouseDoubleClickEvent = self.maximized
		
		self.before_select = self.ui.file_1
		self.ui.file_1.setStyleSheet(self.ui.file_1.styleSheet()+self.style_active)
		self.ui.btn_close_1.setStyleSheet(self.ui.btn_close_1.styleSheet()+self.style_active_close)
		
		self.ui.file_1.mousePressEvent = lambda x: self.change_actual(None, self.ui.file_1)


		self.ui.btn_add.clicked.connect(self.add)


		self.file_number = 2
		

		# self.ui.center.setStretchFactor(0, 4)
		# self.ui.center.setStretchFactor(1, 1)		
		self.ui.center.setSizes([self.ui.center.size().height(), 0])
		self.ui.document_1.setFocus()



	def add(self):
    	# Creacion del header file
		block = QFrame(self.ui.pages)
		block.setObjectName(u"file_"+str(self.file_number))
		block.setMinimumHeight(45)
		block.setMaximumHeight(45)
		block.setFrameShape(QFrame.StyledPanel)
		block.setFrameShadow(QFrame.Raised)

		block.mousePressEvent = lambda x: self.change_actual(None, block)

		file_layout = QHBoxLayout(block)
		file_layout.setSpacing(0)
		file_layout.setObjectName(u"file_layout_"+str(self.file_number))
		file_layout.setContentsMargins(0, 0, 5, 0)
		
		self.lbl_1 = QLabel("Nuevo archivo *", block)
		self.lbl_1.setObjectName(u"lbl_1")

		btn_close = QPushButton(block)
		btn_close.setObjectName(u"btn_close_"+str(self.file_number))
		btn_close.setMinimumSize(QSize(28, 28))
		btn_close.setMaximumSize(QSize(28, 28))
		btn_close.setCursor(QCursor(Qt.PointingHandCursor))

		file_layout.addWidget(self.lbl_1)
		file_layout.addWidget(btn_close)
		self.ui.Layout_pages.addWidget(block)




		# Creacion del text box
		widget = QWidget()
		widget.setObjectName(u"page_"+str(self.file_number))
		# creacion del layout
		widget_layout = QVBoxLayout(widget)
		widget_layout.setSpacing(0)
		widget_layout.setObjectName(u"widget_layout_"+str(self.file_number))
		widget_layout.setContentsMargins(0, 0, 0, 0)
		# Creacion del textbox
		textbox = CodeEditor(widget)
		textbox.setObjectName(u"document_"+str(self.file_number))
		textbox.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

		widget_layout.addWidget(textbox)


		self.ui.stackedWidget.addWidget(widget)


		self.file_number += 1
	
	def change_actual(self, event, sender):
		# Obtenemos el numero anterio del archivo
		before_number = self.before_select.objectName().split("_")[-1]
		# Obtenemos el numero del archivo
		number_actual = sender.objectName().split("_")[-1]

		# borro el estilo del anterior
		self.before_select.setStyleSheet(self.before_select.styleSheet().replace(self.style_active, ""))
		# Borrar el estilo del close anterio
		btn_before_close = self.before_select.findChild(QPushButton, "btn_close_"+before_number)
		btn_before_close.setStyleSheet(btn_before_close.styleSheet().replace(self.style_active_close, ""))


		# agrego el estilo al nuevo
		sender.setStyleSheet(sender.styleSheet()+self.style_active)
		# Agregar el estilo al nuevo close
		btn_close = sender.findChild(QPushButton, "btn_close_"+number_actual)
		btn_close.setStyleSheet(btn_close.styleSheet()+self.style_active_close)

		# cambio el nuevo por el anterior
		self.before_select = sender

		# obtengo el textbox actual
		page = self.ui.stackedWidget.findChild(QWidget, "page_"+number_actual)
		self.ui.stackedWidget.setCurrentWidget(page)


		
	def maximized(self, event):
		if not self.isMaximized():
			self.showMaximized()
		else:
			self.showNormal()
	

	def moveWindow(self, event):
		# MOVE WINDOW
		if event.buttons() == QtCore.Qt.LeftButton:
			if self.isMaximized():
				self.showNormal()
			self.move(event.globalPos() - self.dragPos)
			event.accept()


	def mousePressEvent(self, event):
		# SET DRAG POS WINDOW
		self.dragPos =  event.globalPos() - self.frameGeometry().topLeft()



if __name__ == '__main__':
	pyqtRemoveInputHook()
	app = QApplication(sys.argv)
	window = MyApp()
	window.setWindowTitle('PyEditor')
	# window.showMaximized()
	window.show()
	sys.exit(app.exec())

	# pyside6-rcc sources.qrc -o sources_rc.py
	# pyside6-uic mainWindows.ui > main_ui.py