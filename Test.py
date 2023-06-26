# http://agromet.mkgp.gov.si/APP2/sl/Home/Index?id=2&archive=0&graphs=1#esri_map_iframe
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

# Create a QNetworkAccessManager instance
manager = QNetworkAccessManager()

# Define the URL
url = QUrl(
    "http://agromet.mkgp.gov.si/APP2/sl/Home/Index?id=2&archive=0&graphs=1&xml=1"
)

# Create a QNetworkRequest object and set the URL
request = QNetworkRequest(url)

# Send a GET request to the URL
reply = manager.get(request)

# Callback function to handle the reply
def handle_reply():
    if reply.error() == QNetworkAccessManager.NoError:
        # Read the XML content from the reply
        xml_content = reply.readAll().data().decode()

        # Process the XML content
        # Here, you can use an XML parser like xml.etree.ElementTree to extract the data
        print(xml_content)
    else:
        print("Request failed with error:", reply.errorString())


# Connect the finished signal of the reply to the handle_reply function
reply.finished.connect(handle_reply)

# Execute the event loop
sys.exit(app.exec_())
