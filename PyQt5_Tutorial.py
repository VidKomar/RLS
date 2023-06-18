# https://build-system.fman.io/pyqt5-tutorial

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QListView,
                             QComboBox, QWidget, QVBoxLayout)

import sys

class ComboBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout() # Vertical layout

        label = QLabel("Select an option:") # Label for Combobox instructions
        layout.addWidget(label)

        combobox = QComboBox() #Different options
        combobox.addItem("Choose and option.")
        combobox.addItem("Option 1")
        combobox.addItem("Option 2")
        combobox.addItem("Option 3")

        combobox.currentIndexChanged.connect(self.ComboBoxChange) 
        layout.addWidget(combobox)

        self.setLayout(layout)
        self.setWindowTitle("Example of Combobox")
        self.show()

    def ComboBoxChange(self, index):
        combobox = self.sender()
        selected_item = combobox.currentText()
        print("Selected item: {}".format(selected_item))



if __name__ == "__main__":

    app = QApplication([]) # No parameters used, as of yet
    ex = ComboBox()
    sys.exit(app.exec()) # Starting the event loop. exec_ is archaic.

# Adding widgets
# Also some issues with git hah

