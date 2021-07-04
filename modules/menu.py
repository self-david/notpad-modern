from PyQt5.QtWidgets import QMenu, QAction
from PyQt5.QtGui import QIcon

def file(self):
	# menu de archivo
	self.menu_file = QMenu(self)

	new = QAction(QIcon(':/icons/assets/icons/icon.png'), '&Nuevo', self)
	new.setShortcut('Ctrl+N')
	# new.trigger.connect()
	open = QAction(QIcon(':/icons/assets/icons/icon.png'), 'Abrir', self)
	open.setShortcut('Ctrl+O')
	# open.trigger.connect()
	save = QAction(QIcon(':/icons/assets/icons/icon.png'), 'Guardar', self)
	save.setShortcut('Ctrl+S')
	# save.trigger.connect()
	save_as = QAction(QIcon(':/icons/assets/icons/icon.png'), 'Guardar Como...', self)
	save_as.setShortcut('Ctrl+Shift+S')
	# save_as.trigger.connect()
	exit = QAction(QIcon(':/icons/assets/icons/close.png'), '&Salir', self)
	exit.setShortcut('Esc')
	exit.triggered.connect(self.close)

	self.menu_file.addActions([new, open, save, save_as])
	self.menu_file.addSeparator()
	self.menu_file.addAction(exit)


def edition(self):
	# menu de edicion
	self.menu_edition = QMenu(self)

	new = QAction(QIcon(':/icons/assets/icons/icon.png'), 'Deshacer', self)
	new.setShortcut('Ctrl+Z')
	# new.trigger.connect()
	new2 = QAction(QIcon(':/icons/assets/icons/icon.png'), 'Rehacer', self)
	new2.setShortcut('Ctrl+Shift+Z')
	# new.trigger.connect()
	open = QAction(QIcon(':/icons/assets/icons/icon.png'), 'jaja', self)
	open.setShortcut('Ctrl+O')
	# open.trigger.connect()
	save = QAction(QIcon(':/icons/assets/icons/icon.png'), 'No', self)
	save.setShortcut('Ctrl+S')
	# save.trigger.connect()
	exit = QAction(QIcon(':/icons/assets/icons/close.png'), '&Salir', self)
	exit.setShortcut('Esc')
	exit.triggered.connect(self.close)

	self.menu_edition.addActions([new, new2, open, save])
	self.menu_edition.addSeparator()
	self.menu_edition.addAction(exit)