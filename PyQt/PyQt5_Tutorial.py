# https://build-system.fman.io/pyqt5-tutorial

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QListView


app = QApplication([]) # No parameters used, as of yet
label = QLabel('Hello World!')
label.show()

app.exec() # Starting the event loop. exec_ is archaic.

# Adding widgets