# https://build-system.fman.io/pyqt5-tutorial

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QListView,
                             QComboBox, QWidget, QVBoxLayout, QMessageBox)

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
        combobox.addItem("Choose and option (not me)")
        combobox.addItem("Option 1")
        combobox.addItem("Option 2")
        combobox.addItem("Option 3")

        combobox.currentIndexChanged.connect(self.ComboBoxChange)  # Call of function that notices the change
        layout.addWidget(combobox)

        #layout.addWidget(QPushButton("Submit"))
        button = QPushButton("Submit choice") # Button for "submission"
        button.clicked.connect(self.submitData)
        layout.addWidget(button)

        self.setLayout(layout)
        self.setWindowTitle("Example of Combobox")
        self.show()

    def ComboBoxChange(self, index):
        """
        Get's the information about the clicked entry on the combo box.
        """
        combobox = self.sender() 
        global selected_item # I've got a feeling that this is bad practice
        selected_item = combobox.currentText()
        print("Selected item: {}".format(selected_item))

    def submitData(self, index):
        """
        Displays a message box upon pressing the submit button.
        The user is notified of the choice he made.
        """
        alert = QMessageBox()
        alert.setText("You clicked the button and selected: \n {}".format(selected_item))
        alert.setWindowTitle("Click Conformation")
        alert.exec()

if __name__ == "__main__":

    app = QApplication([]) # No parameters used, as of yet
    ex = ComboBox()
    sys.exit(app.exec()) # Starting the event loop. exec_ is archaic.

# Adding widgets
# Also some issues with git hah

