import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication
import sys

# Send a GET request to the XML file URL
url = 'http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/55.xml'
response = requests.get(url)
# TEMPS tavg = avg temp.; tx = max temp; tn = min temp.
# HUMIDITY rhavg, rhx, rhn
#  
 
if response.status_code == 200: # Check if the request was successful
    root = ET.fromstring(response.content) # Parse the XML content

    # Extract temperature data from the XML
    data_dict = {}
    entries = 10
    for element in root.iter():
        if element.tag in ["tavg", "tx", "tn"]: # Finding temperature markers
            tag = element.tag # Parse tags and values from XML
            value = element.text

            if tag in data_dict:
                data_dict[tag].append(value) # Add value to tag
            else:
                data_dict[tag] = [value]

            #if len(data_dict["tavg"]) >= entries: # Limiting entries for testing
            #    break
            if element == ("</data>"): # When end is reached, break
                break
            #return data_dict

    # Create the graph using matplotlib
    # 3 different temperatures
    plt.subplot(3, 1, 1)
    plt.plot(data_dict.get("tavg"))
    plt.subplot(3, 1, 2)
    plt.plot(data_dict.get("tx"))
    plt.subplot(3, 1, 3)
    plt.plot(data_dict.get("tn"))
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Variation')
    plt.show()

    # Start the PyQt5 event loop
    app = QApplication([])
    app.exec_()
    sys.exit(app.exec())
else:
    print(f'Request failed with status code: {response.status_code}')