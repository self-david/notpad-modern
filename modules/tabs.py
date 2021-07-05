from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QFrame, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import *
from modules.codeeditor import CodeEditor


def add(self):
	# Creacion del tab
	tab = QFrame(self.ui.pages)
	tab.setObjectName(u"file_"+str(self.tab_number))
	tab.setMinimumHeight(45)
	tab.setMaximumHeight(45)
	tab.setFrameShape(QFrame.StyledPanel)
	tab.setFrameShadow(QFrame.Raised)
	tab.setToolTip("Nuevo archivo *")
	tab.mousePressEvent = lambda x: self.change_actual(None, tab)
	
	file_layout = QHBoxLayout(tab)
	file_layout.setSpacing(0)
	file_layout.setObjectName(u"file_layout_"+str(self.tab_number))
	file_layout.setContentsMargins(4, 0, 5, 0)
	
	title = QLabel("Nuevo archivo *", tab)
	title.setObjectName(u"title_"+str(self.tab_number))

	btn_close = QPushButton(tab)
	btn_close.setObjectName(u"btn_close_"+str(self.tab_number))
	btn_close.setMinimumSize(QSize(28, 28))
	btn_close.setMaximumSize(QSize(28, 28))
	btn_close.setCursor(QCursor(Qt.PointingHandCursor))
	btn_close.clicked.connect(lambda: remove(self))

	file_layout.addWidget(title)
	file_layout.addWidget(btn_close)
	self.ui.Layout_pages.addWidget(tab)

	self.stacked_tabs.append(tab)

	# Creacion del text box
	widget = QWidget()
	widget.setObjectName(u"page_"+str(self.tab_number))
	# creacion del layout
	widget_layout = QVBoxLayout(widget)
	widget_layout.setSpacing(0)
	widget_layout.setObjectName(u"widget_layout_"+str(self.tab_number))
	widget_layout.setContentsMargins(0, 0, 0, 0)
	# Creacion del textbox
	textbox = CodeEditor(widget)
	textbox.setObjectName(u"document_"+str(self.tab_number))
	textbox.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

	widget_layout.addWidget(textbox)

	self.ui.stackedWidget.addWidget(widget)

	self.tab_number += 1
	


def remove(self):
	#verificar si el archivo se ha guardado

	# obtengo el indice del tab a eliminar
	number_actual = self.sender().objectName().split("_")[-1]
	
	# Elimino el tab
	tab = self.ui.top.findChild(QFrame, "file_"+number_actual)
	tab.deleteLater()
	#elimino la pagina textbox
	page = self.ui.stackedWidget.findChild(QWidget, "page_"+number_actual)
	page.deleteLater()
	# remuevo el tab del stack
	self.stacked_tabs.remove(tab)

	# si mi stack se quedo sin tab debe cerrar la ventana
	if len(self.stacked_tabs) == 0:
		self.close()
		return

	# verifico si el ultimo tab seleccionado es el mismo al que se desea eliminar
	number_before = self.before_select.objectName().split("_")[-1]
	# si es asi, entonces elimino la referencia al tab
	if number_actual == number_before:
		# Cambiar el tab seleccionado
		self.change_actual(None, self.stacked_tabs[0])
		self.before_select = self.stacked_tabs[0]




	
	
	
