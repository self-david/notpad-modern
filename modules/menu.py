from PyQt5.QtWidgets import QMenu, QAction
from PyQt5.QtGui import QIcon

from modules.tabs import add

def file(self):
	# menu de archivo
	self.menu_file = QMenu(self)

	new = QAction('&Nuevo', self)
	new.setShortcut('Ctrl+N')
	new.triggered.connect(lambda: add(self))
	open = QAction('Abrir', self)
	open.setShortcut('Ctrl+O')
	# open.trigger.connect()
	save = QAction('Guardar', self)
	save.setShortcut('Ctrl+S')
	# save.trigger.connect()
	save_as = QAction('Guardar Como...', self)
	save_as.setShortcut('Ctrl+Shift+S')
	# save_as.trigger.connect()
	exit = QAction('Salir', self)
	exit.setShortcut('Esc')
	exit.triggered.connect(self.close)

	self.menu_file.addActions([new, open, save, save_as])
	self.menu_file.addSeparator()
	self.menu_file.addAction(exit)


def edition(self):
	# menu de edicion
	self.menu_edition = QMenu(self)

	undo = QAction('Deshacer', self)
	undo.setShortcut('Ctrl+Z')
	# new.trigger.connect()
	redo = QAction('Rehacer', self)
	redo.setShortcut('Ctrl+Shift+Z')
	# new.trigger.connect()
	cute = QAction('Cotar', self)
	cute.setShortcut('Ctrl+X')
	# open.trigger.connect()
	copy = QAction('Copiar', self)
	copy.setShortcut('Ctrl+C')
	# save.trigger.connect()
	paste = QAction('Pegar', self)
	paste.setShortcut('Ctrl+V')
	# exit.triggered.connect(self.close)
	find = QAction('Buscar', self)
	find.setShortcut('Ctrl+F')
	# exit.triggered.connect(self.close)
	replace = QAction('Remplazar', self)
	replace.setShortcut('Ctrl+H')
	# exit.triggered.connect(self.close)

	self.menu_edition.addActions([undo, redo])
	self.menu_edition.addSeparator()
	self.menu_edition.addActions([cute, copy, paste])
	self.menu_edition.addSeparator()
	self.menu_edition.addActions([find, replace])


def format(self):
	# menu de edicion
	self.menu_format = QMenu(self)

	undo = QAction('Deshacer', self)
	undo.setShortcut('Ctrl+Z')
	# new.trigger.connect()
	redo = QAction('Rehacer', self)
	redo.setShortcut('Ctrl+Shift+Z')

	self.menu_format.addActions([undo, redo])


def view(self):
	# menu de edicion
	self.menu_view = QMenu(self)

	cmd = QAction('Linea de comandos', self)
	cmd.setShortcut('Ctrl+Z')
	# new.trigger.connect()
	redo = QAction('Rehacer', self)
	redo.setShortcut('Ctrl+Shift+Z')


	self.menu_view.addActions([cmd, redo])


def help(self):
	# menu de edicion
	self.menu_help = QMenu(self)

	undo = QAction('Deshacer', self)
	undo.setShortcut('Ctrl+Z')
	# new.trigger.connect()
	redo = QAction('Rehacer', self)
	redo.setShortcut('Ctrl+Shift+Z')
	# new.trigger.connect()
	cute = QAction('Cotar', self)
	cute.setShortcut('Ctrl+X')
	# open.trigger.connect()
	copy = QAction('Copiar', self)
	copy.setShortcut('Ctrl+C')
	# save.trigger.connect()
	paste = QAction('Pegar', self)
	paste.setShortcut('Ctrl+V')
	# exit.triggered.connect(self.close)
	find = QAction('Buscar', self)
	find.setShortcut('Ctrl+F')
	# exit.triggered.connect(self.close)
	replace = QAction('Remplazar', self)
	replace.setShortcut('Ctrl+H')
	# exit.triggered.connect(self.close)

	self.menu_help.addActions([undo, redo])
	self.menu_help.addSeparator()
	self.menu_help.addActions([cute, copy, paste])
	self.menu_help.addSeparator()
	self.menu_help.addActions([find, replace])