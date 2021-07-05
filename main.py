from os import device_encoding
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QPoint, pyqtRemoveInputHook
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QPushButton, QSizeGrip, QWidget
from PyQt5 import uic
from PyQt5.QtGui import *
Ui_MainWindow, QtBaseClass = uic.loadUiType('./ui/mainWindows.ui')

from modules import tabs
from modules import menu
from modules.custom_grips import CustomGrip

from modules.functions import Primitive


class MyApp(QMainWindow):
	def __init__(self):
		self.newLines = 1
		super(MyApp, self).__init__(None)

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.primitive = Primitive(self, self.ui.top)

		# elimina los bordes de la ventana
		self.primitive.borderless()
		# genera una sobre al rededor de la ventana
		self.primitive.border_shadow(self.ui.App)
		# permite el resize por medio de los bordes (require actualizar con resize_grip())
		self.primitive.border_grip(self.ui.resize)


		self.style_active = "color: #3C3C3C; background-color: #E8EBEA;"
		self.style_active_close = "image: url(:/icons/assets/icons/close-file.png);"
		

		self.ui.btn_close.clicked.connect(self.close)
		self.ui.btn_maximize.clicked.connect(self.primitive.maximize_restore)
		self.ui.btn_minimize.clicked.connect(self.showMinimized)

		
		self.before_select = self.ui.file_1
		self.ui.file_1.setStyleSheet(self.ui.file_1.styleSheet()+self.style_active)
		self.ui.file_1.mousePressEvent = lambda x: self.change_actual(None, self.ui.file_1)
		self.ui.btn_close_1.setStyleSheet(self.ui.btn_close_1.styleSheet()+self.style_active_close)
		self.ui.btn_close_1.clicked.connect(lambda: tabs.remove(self))

		# stack de tabs
		self.stacked_tabs = [self.ui.file_1]

		# crear nuevo tab al dar click
		self.ui.btn_add.clicked.connect(lambda: tabs.add(self))

		# indice del tab creado
		self.tab_number = 2
		

		# self.ui.center.setStretchFactor(0, 4)
		# self.ui.center.setStretchFactor(1, 1)		
		self.ui.center.setSizes([self.ui.center.size().height(), 0])
		self.ui.document_1.setFocus()


		
		menu.file(self)
		self.ui.file.clicked.connect(lambda : self.menu(self.menu_file))
		menu.edition(self)
		self.ui.edition.clicked.connect(lambda : self.menu(self.menu_edition))
		menu.format(self)
		self.ui.format.clicked.connect(lambda : self.menu(self.menu_format))
		menu.view(self)
		self.ui.view.clicked.connect(lambda : self.menu(self.menu_view))
		menu.help(self)
		self.ui.help.clicked.connect(lambda : self.menu(self.menu_help))




	def imprimir(self):
		print("se pudo")


	def menu(self, menu):
		menu.exec_(self.pos()+ QPoint(10,96)  + self.sender().pos())


	def count(self):
		print([tab.objectName() for tab in self.stacked_tabs])


	def change_actual(self, event, sender):
		# Obtenemos el numero anterio del archivo
		before_number = self.before_select.objectName().split("_")[-1]

		# borro el estilo del anterior
		self.before_select.setStyleSheet(self.before_select.styleSheet().replace(self.style_active, ""))
		# Borrar el estilo del close anterio
		btn_before_close = self.before_select.findChild(QPushButton, "btn_close_"+before_number)
		btn_before_close.setStyleSheet(btn_before_close.styleSheet().replace(self.style_active_close, ""))

		# Obtenemos el numero del archivo
		number_actual = sender.objectName().split("_")[-1]

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

		self.moving = False

		self.count()

		

	def resizeEvent(self, event):
		self.primitive.resize_grip()		
		# self.ui.pages.setMaximumWidth(self.ui.top.width() - self.ui.basic_buttons.width() - self.ui.btn_add.width() - 21)
		# print(self.ui.top.width(), self.ui.basic_buttons.width(), self.ui.pages.width())




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