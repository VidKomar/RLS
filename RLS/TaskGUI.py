from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel,
                              QListView, QComboBox, QWidget, QVBoxLayout, QMessageBox)

from PyQt5.QtCore import QSize, Qt, QStringListModel
import matplotlib.pyplot as plt
import sys, logging
import MainTask


def SimplePlot(data_dict, selectedQuantity):

    """
    Used for plotting weather variables.
    Data is gathered from dicts.
    """
    temperaturesPlot = [float(x) for x in data_dict.get(selectedQuantity)]
    timePlot = data_dict.get("valid_UTC")[2:]  # Solve this issue pls
    # tempPlot = plt.plot(timePlot, temperaturesPlot)
    fig, ax = plt.subplots(figsize=(15, 8))
    ax.plot(timePlot, temperaturesPlot) 
    ax.set_ylabel("Temperature [°C]")  # !!!
    ax.set_xlabel("Time")
    fig.autofmt_xdate(rotation=45)

    # Showing every other label
    plt.setp(ax.get_xticklabels()[::2], visible=False)  
    ax.set_title("Displaying {} in two day span".format(selectedQuantity))

    plt.show()


def displaySelected(selected_infoIdx, data_dict):
    # Instead of all the if, plot by dict. keys!
    logging.info("TestLog")
    logging.info(data_dict.keys())

    # Plotting selected information
    SimplePlot(data_dict, list(data_dict.keys())[selected_infoIdx+1])

    """  if selected_infoIdx == 0:
        SimplePlot(data_dict, "tavg")
    if selected_infoIdx == 1:
        SimplePlot(data_dict, "tx")
    if selected_infoIdx == 2:
        SimplePlot(data_dict, "tn")
    if selected_infoIdx == 3:
        SimplePlot(data_dict, "rhavg")
    if selected_infoIdx == 4:
        SimplePlot(data_dict, "rhx")
    if selected_infoIdx == 5:
        SimplePlot(data_dict, "rhn")
    if selected_infoIdx == 6:
        SimplePlot(data_dict, "td")
    if selected_infoIdx == 7:
        SimplePlot(data_dict, "rr")
    if selected_infoIdx == 8:
        SimplePlot(data_dict, "lwavg")
    else:
        plt.plot()  # Empty
        plt.show"""
       

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
        displayChoice.addItem("Average relative humidity")
        displayChoice.addItem("Maximum relative humidity")
        displayChoice.addItem("Minimum relative humidity")
        displayChoice.addItem("Dew point temperature")
        displayChoice.addItem("Rainfall")
        displayChoice.addItem("Leaf Wetness")
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
        selected_info = displayChoice.currentText()
        #print(selected_infoIdx)

        MainTask.getCitiesData()

        # Pull data from website using MainTask function
        data_dict = MainTask.pullData("http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/55.xml")

        displaySelected(selected_infoIdx, data_dict)

        return selected_infoIdx, data_dict


if __name__ == "__main__":

    app = QApplication([])  # No parameters used, as of yet
    ex = MainW()
    sys.exit(app.exec())  # Starting the event loop. exec_ is archaic.
