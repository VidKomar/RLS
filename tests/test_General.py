import unittest
from unittest.mock import patch
from TaskMain import getCitiesData


class GetCitiesDataTestCase(unittest.TestCase):
    @patch("TaskMain.requests.get")
    @patch("TaskMain.BeautifulSoup")
    def test_get_cities_data(self, mock_soup, mock_get):
        # Mock the response and soup object
        mock_get.return_value.content = "Mocked response"
        mock_soup.return_value.find_all.return_value = [
            # Simulate finding anchor tags with XML links
            type(
                "MockAnchor",
                (object,),
                {"has_attr": lambda self, attr: True, "href": "test.xml"},
            ),
            type(
                "MockAnchor",
                (object,),
                {"has_attr": lambda self, attr: True, "href": "test2.xml"},
            ),
        ]

        # Call the function
        result = getCitiesData()

        # Assert the expected behavior
        self.assertEqual(
            mock_get.call_args[0][0],
            "http://agromet.mkgp.gov.si/APP2/sl/Home/Index?id=2&archive=0&graphs=1#esri_map_iframe",
        )
        self.assertEqual(
            result,
            [
                "http://agromet.mkgp.gov.si/test.xml",
                "http://agromet.mkgp.gov.si/test2.xml",
            ],
        )


if __name__ == "__main__":
    unittest.main()
