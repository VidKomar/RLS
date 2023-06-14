from PyQt5.QtGui import *
from PyQt5.QtWidgets import * # Boljša ideja da poimenuješ widg ipd.
from PyQt5.QtCore import *

import sys

class MainWindow(QMainWindow):
    # Necessary two lines!!!
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs) # Every QT widgets requires super init!

        self.setWindowTitle("Title line yay \o/") # Window title \o/

        label = QLabel("Centered label") # Qlabel -> simple widget
        label.setAlignment(Qt.AlignCenter) # In the centre!!

        self.setCentralWidget(label) # Set the widget, that goes in the middle of the window

app = QApplication(sys.argv) # For passing command arguments into app

# Window after the Q app. intance & Be4 we start the event loop
window = MainWindow()
window.show() # Like plt!

app.exec_() # Starting the event loop

# Creating window
# Atleast one window -> App exit when last main window is closed!
