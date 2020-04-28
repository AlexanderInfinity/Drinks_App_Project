
from classes.all_classes import Person

import unittest.mock

class PersonTests(unittest.TestCase):

    def test_person_ID(self):
        # Arrange
        expected_outcome = "Name: Alex Wallwork Age: 24 ID: Set"
        testy = Person("Alex", "Wallwork", "24", 100)
        # Act
        actual_outcome = testy.get_person_info()
        # Assert
        self.assertEqual(expected_outcome,actual_outcome)

    def test_person_no_ID(self):
        # Arrange
        expected_outcome = "Name: Alex Wallwork Age: 24 ID: None"
        testy = Person("Alex", "Wallwork", "24")
        # Act
        actual_outcome = Person.get_person_info(testy)
        # Assert
        self.assertEqual(expected_outcome,actual_outcome)

