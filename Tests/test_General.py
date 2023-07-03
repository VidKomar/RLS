import TaskMain


def test_addition():
    assert 2 + 2 == 4


#  Test for dictionary order


def test_getCitiesData_returns_strings(self):
    cities_data = TaskMain.getCitiesData()
    for city in cities_data:
        self.assertIsInstance(city, str)
