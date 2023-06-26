import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re

# Send a GET request to the XML file URL
url = "http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/55.xml"

# TEMPS tavg = avg temp.; tx = max temp; tn = min temp.
# HUMIDITY rhavg, rhx, rhn
#


def pullData(url):
    response = requests.get(url)
    if response.status_code == 200:  # Check if the request was successful
        root = ET.fromstring(response.content)  # Parse the XML content

        # Extract temperature data from the XML
        data_dict = {}
        for element in root.iter():
            # Finding temperature, humidity,
            # rainfall, dew point temp., Leaf Wetness markers
            if element.tag in [
                "valid_UTC",
                "tavg",
                "tx",
                "tn",
                "rhavg",
                "rhx",
                "rhn",
                "td",
                "rr",
                "lwavg",
            ]:
                tag = element.tag  # Parse tags and values from XML
                value = element.text

                if tag in data_dict:
                    data_dict[tag].insert(0, value)  # Add value to tag
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
        print(f"Request failed with status code: {response.status_code}")


def getCitiesData():
    """
    # URL http://agromet.mkgp.gov.si/APP2/sl/Home/Index?id=2&archive=0&graphs=1#esri_map_iframe
    """
    # URL of the webpage
    url = "http://agromet.mkgp.gov.si/APP2/sl/Home/Index?id=2&archive=0&graphs=1#esri_map_iframe"

    response = requests.get(url)
    # Parse the webpage content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all anchor tags (links) in the webpage
    links = soup.find_all("a")

    # Collect all links that end with ".xml"
    xml_files = []
    for link in links:
        if link.has_attr("href") and link["href"].endswith(".xml"):
            xml_files.append("http://agromet.mkgp.gov.si" + link["href"])
    # logging.info(xml_files)
    # print(xml_files)
