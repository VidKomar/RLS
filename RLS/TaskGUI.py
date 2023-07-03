from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QListView,
    QComboBox,
    QWidget,
    QVBoxLayout,
    QMessageBox,
)

from PyQt5.QtCore import QSize, Qt, QStringListModel
import matplotlib.pyplot as plt
import logging
import sys, logging
import TaskMain

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def SimplePlot(data_dict, selectedQuantity, location):

    """
    Used for plotting weather variables.
    Data is gathered from dicts.
    """
    temperaturesPlot = [float(x) for x in data_dict.get(selectedQuantity)]
    timePlot = data_dict.get("valid_UTC")[2:]  # Solve this issue pls
    # tempPlot = plt.plot(timePlot, temperaturesPlot)
    fig, ax = plt.subplots(figsize=(15, 8))
    ax.plot(timePlot, temperaturesPlot)
    ax.set_ylabel("Applicable unit")  # !!!
    ax.set_xlabel("Time")
    fig.autofmt_xdate(rotation=45)

    # Showing every other label
    plt.setp(ax.get_xticklabels()[::2], visible=False)
    ax.set_title(
        "Displaying {} in two day span @ {}".format(selectedQuantity, location)
    )

    plt.show()


def displaySelected(selected_infoIdx, data_dict, location):
    # Instead of all the if, plot by dict. keys!
    # logging.info("TestLog")
    logging.info(data_dict.keys())
    # logging.info(data_dict.values())

    # Plotting selected information
    # Needs rethinking
    SimplePlot(data_dict, list(data_dict.keys())[selected_infoIdx + 2], location)

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
        label = QLabel(
            "Welcome to my weather app \n"
            "Please choose information you are interested in!"
        )
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        # Choose the desired location
        self.displayLocation = QComboBox()
        listOfCities = TaskMain.pullSpecificData("domain_shortTitle")
        for i in listOfCities:
            self.displayLocation.addItem(i)
        layout.addWidget(self.displayLocation)

        # Choose the desired display output
        self.displayChoice = QComboBox()
        self.displayChoice.addItem("Average temperature")
        self.displayChoice.addItem("Maximum temperature")
        self.displayChoice.addItem("Minimum temperature")
        self.displayChoice.addItem("Average relative humidity")
        self.displayChoice.addItem("Maximum relative humidity")
        self.displayChoice.addItem("Minimum relative humidity")
        self.displayChoice.addItem("Dew point temperature")
        self.displayChoice.addItem("Rainfall")
        self.displayChoice.addItem("Leaf Wetness")
        layout.addWidget(self.displayChoice)

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
        # Residual code for future reference
        # displayChoice = self.sender().parent().findChild(QComboBox)
        # displayChoice.currentText() To get combobx text
        # displayChoice.currentIndex() To get combobx text idx
        # print(selected_infoIdx)

        selectedlocation = self.displayLocation.currentText()
        selectedlocationIdx = self.displayLocation.currentIndex()
        selectedChoice = self.displayChoice.currentText()

        logging.info("Selected location {}".format(selectedlocation))

        xml_locations = TaskMain.getCitiesData()
        logging.info("{}".format(xml_locations))

        # Selecting from all cities to show data for selection only!
        DATA = {}

        # print("Selected city is: {}".format(selectedLocation))

        # Pull data from website using TaskMain function
        data_dict = TaskMain.pullData(
            "http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/55.xml"
        )

        displaySelected(selectedlocationIdx, data_dict, selectedlocation)

        # return selected_infoIdx, data_dict


# def physicalEntity():


if __name__ == "__main__":

    app = QApplication([])  # No parameters used, as of yet
    ex = MainW()
    sys.exit(app.exec())  # Starting the event loop. exec_ is archaic.
