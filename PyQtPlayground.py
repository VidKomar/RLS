from PyQt5.QtGui import *
#from PyQt5.QtWidgets import * # Boljša ideja da poimenuješ widg, ki jih rabiš -> QMainWindow ipd.
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import QSize, Qt

import sys # For command line args

class MainWindow(QMainWindow):
    # Necessary two lines!!!
    def __init__(self, *args, **kwargs): 
        super(MainWindow, self).__init__(*args, **kwargs) # Every QT widgets requires super init!
        # When you subclass a Qt class you must always call the super __init__ function to allow Qt to set up the object.
        
        self.setFixedSize(400, 300) # Limit the main window size
        self.setWindowTitle("Title line yay \o/") # Window title \o/

        label = QLabel("Centered label") # Qlabel -> simple widget
        label.setAlignment(Qt.AlignTop) # In the TOP centre!!

        pushButton = QPushButton("Press here to win!") # Is seperate window
        self.setCentralWidget(pushButton) # Set the widget, that goes in the middle of the window



app = QApplication(sys.argv) # For passing command line arguments into app. can be empty []
# Python list containing the command line arguments passed to the application.
# QApplication holds the event loop, so only one is required

# Window after the Q app. intance & Be4 we start the event loop
window = MainWindow()
window.show() # Like plt!
#pushButton.show()

app.exec_() # Starting the event loop

# Creating window
# Atleast one window -> App exit when last main window is closed!
