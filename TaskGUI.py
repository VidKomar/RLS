from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel,
                              QListView, QComboBox, QWidget, QVBoxLayout, QMessageBox)

from PyQt5.QtCore import QSize, Qt, QStringListModel
import matplotlib.pyplot as plt
import sys
import MainTask


def SimplePlot(data_dict, selectedQuantity):

    """
    Used for plotting temperatures ATM.
    Data is gathered from dicts.
    """
    temperaturesPlot = [float(x) for x in data_dict.get(selectedQuantity)] 
    timePlot = data_dict.get("valid_UTC")[2:]
    # tempPlot = plt.plot(timePlot, temperaturesPlot)
    fig, ax = plt.subplots()
    ax.plot(timePlot, temperaturesPlot) 
    ax.set_ylabel("Temperature [°C]")
    ax.set_xlabel("Time")
    ax.set_title("Displaying {} in two day span".format(selectedQuantity))

    plt.show()


def displaySelected(selected_infoIdx, data_dict):
    if selected_infoIdx == 0:
        SimplePlot(data_dict, "tavg")
    if selected_infoIdx == 1:
        SimplePlot(data_dict, "tx")
    if selected_infoIdx == 2:
        SimplePlot(data_dict, "tn")
    else:
        plt.plot()  # Empty
        plt.show
        

class MainW(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        # Setting small size and name
        self.setFixedSize(400, 300)
        self.setWindowTitle("Weather app.")

        # Greeting and instructions on top
        label = QLabel("Welcome to my weather app \n"
                       "Please choose information you are interested in!")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        # Choose the desired display output
        displayChoice = QComboBox()
        displayChoice.addItem("Average temperature")
        displayChoice.addItem("Maximum temperature")
        displayChoice.addItem("Minimum temperature")
        layout.addWidget(displayChoice)

        # Confirm choice of display output
        buttonConfirm = QPushButton("Confirm Choice")
        buttonConfirm.clicked.connect(self.buttonConfirm)
        layout.addWidget(buttonConfirm)

        self.setLayout(layout)     

        self.show()

    def buttonConfirm(self):
        """
        Upon button conformation, pull data.
        Model and View are seperated.
        return: 
            selected_info - Which information, the user wishes to see.
            data_dict - Pulled information from the source webpage xml file.
        """
        displayChoice = self.sender().parent().findChild(QComboBox)
        selected_infoIdx = displayChoice.currentIndex()
        # selected_info = displayChoice.currentText()
        print(selected_infoIdx)

        # Pull data from website using MainTask function
        data_dict = MainTask.pullData("http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/55.xml")

        displaySelected(selected_infoIdx, data_dict)

        return selected_infoIdx, data_dict


if __name__ == "__main__":

    app = QApplication([])  # No parameters used, as of yet
    ex = MainW()
    sys.exit(app.exec())  # Starting the event loop. exec_ is archaic.