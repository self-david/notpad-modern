from os import pardir
from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QSizeGrip

from modules.custom_grips import CustomGrip

class Primitive:
	def __init__(self, parent, top=None):
		self.parent = parent
		self.top = top
		self.moving = False

		self.top.mouseMoveEvent = self.moveWindow
		self.top.mousePressEvent= self.mousePress
		self.top.mouseDoubleClickEvent = self.dobleClickMaximizeRestore
	

	def borderless(self):
		flags = QtCore.Qt.WindowFlags(QtCore.Qt.Dialog)
		# self.parent.setWindowFlags(flags|QtCore.Qt.FramelessWindowHint |QtCore.Qt.CustomizeWindowHint)
		self.parent.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.parent.setAttribute(QtCore.Qt.WA_TranslucentBackground)#fondo de la ventana transparente
		# self.parent.windowHandle().setParent(self.parent)


	def border_shadow(self, border):
		self.shadow = QGraphicsDropShadowEffect(self.parent)
		self.shadow.setBlurRadius(20)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QColor(0,0,0,200))
		
		border.setGraphicsEffect(self.shadow)


	def border_grip(self, resize = None):
		# CUSTOM GRIPS
		border_transparent = True
		self.parent.left_grip = CustomGrip(self.parent, QtCore.Qt.LeftEdge, border_transparent)
		self.parent.right_grip = CustomGrip(self.parent, QtCore.Qt.RightEdge, border_transparent)
		self.parent.top_grip = CustomGrip(self.parent, QtCore.Qt.TopEdge, border_transparent)
		self.parent.bottom_grip = CustomGrip(self.parent, QtCore.Qt.BottomEdge, border_transparent)
		
		# esquina inferior izquierda
		self.parent.sizegrip = QSizeGrip(resize)
		self.parent.sizegrip.setStyleSheet("width: 28px; height: 28px; margin 0px; padding: 0px;")


	def resize_grip(self):
		self.parent.left_grip.setGeometry(0, 10, 10, self.parent.height())
		self.parent.right_grip.setGeometry(self.parent.width() - 10, 10, 10, self.parent.height())
		self.parent.top_grip.setGeometry(0, 0, self.parent.width(), 10)
		self.parent.bottom_grip.setGeometry(0, self.parent.height() - 10, self.parent.width(), 10)
	

	def maximize_restore(self, event):
		# primer reajuste de las ventanas
		self.parent.ui.AppMargins.setContentsMargins(0, 0, 0, 0)
		if not self.parent.isMaximized():
			self.parent.showMaximized()
			self.parent.ui.AppMargins.setContentsMargins(0, 0, 0, 0)
			self.parent.ui.btn_maximize.setToolTip("Restore")
			self.parent.ui.resize.hide()
			self.parent.left_grip.hide()
			self.parent.right_grip.hide()
			self.parent.top_grip.hide()
			self.parent.bottom_grip.hide()
		else:
			self.parent.showNormal()
			self.parent.resize(self.parent.width()+1, self.parent.height()+1)
			self.parent.ui.AppMargins.setContentsMargins(10, 10, 10, 10)
			self.parent.ui.btn_maximize.setToolTip("Maximize")
			self.parent.ui.resize.show()
			self.parent.left_grip.show()
			self.parent.right_grip.show()
			self.parent.top_grip.show()
			self.parent.bottom_grip.show()


	def dobleClickMaximizeRestore(self, event):
		# IF DOUBLE CLICK CHANGE STATUS
		if event.type() == QtCore.QEvent.MouseButtonDblClick:
			QtCore.QTimer.singleShot(250, lambda: self.maximize_restore(event))



	def moveWindow(self, event):
		# MOVE WINDOW
		if not self.moving:
			return
		if event.buttons() == QtCore.Qt.LeftButton:
			if self.parent.isMaximized():
				self.maximize_restore(event)
			self.parent.move(event.globalPos() - self.parent.dragPos)
			event.accept()
		

	def mousePress(self, event):
		# SET DRAG POS WINDOW
		self.moving = True
		self.parent.dragPos =  event.globalPos() - self.parent.frameGeometry().topLeft()
