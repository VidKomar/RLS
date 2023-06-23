import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication
import sys


# Send a GET request to the XML file URL
url = 'http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/55.xml'

# TEMPS tavg = avg temp.; tx = max temp; tn = min temp.
# HUMIDITY rhavg, rhx, rhn
#  


def pullData(url):
    response = requests.get(url)
    if response.status_code == 200:  # Check if the request was successful
        root = ET.fromstring(response.content)  # Parse the XML content

        # Extract temperature data from the XML
        data_dict = {}
        # entries = 10
        for element in root.iter():
            # if element.tag in ["tavg"]: # Test purpose - only show one temp.
            if element.tag in ["valid_UTC", "tavg", "tx", "tn"]:  # Finding temperature markers
                tag = element.tag  # Parse tags and values from XML
                value = element.text

                if tag in data_dict:
                    data_dict[tag].append(value)  # Add value to tag
                else:
                    data_dict[tag] = [value]
                
                # Two days worth of data is required...
                # timeOfData = []
                # timeOfData = timeOfData.append(str(data_dict["valid_UTC"[11:15]]))
                # timeTemp = data_dict["valid_UTC"]
                # timeOfData = timeOfData.append(str(timeTemp[11:15]))

                # if len(data_dict["tavg"]) >= entries: # Limiting entries for testing
                #    break
                if element == ("</data>"):  # When end is reached, break
                    break
        return data_dict

        # Start the PyQt5 event loop
        # app = QApplication([])
        # app.exec_()
        # sys.exit(app.exec())
    else:
        print(f'Request failed with status code: {response.status_code}')

