import pymysql
from os import environ
from classes.all_classes import Drink, Person
from os import environ
from unittest.mock import Mock, patch, call, MagicMock
from classes.all_classes import Person
import unittest.mock
import s as t
import unittest
from persistence.database import Database as db
from unittest.mock import MagicMock


class ComponentTest(unittest.TestCase):

    @patch("builtins.input")
    def test_selection_7(self, input):
        # arrange
        database = Mock(db())
        app = t.App(db=database)
        database.load_person.return_value = [Person("Testy", "Mctest", 20)]
        database.load_drinks.return_value = [Drink("Testy Ade", 1, "Soft Drink")]
        input.side_effect = ["7", "Testy", "Mctest", "Testy", "Mctest", "Testy Ade", "n", "n", "y", "ex"]

        # act
        app.main_menu()

        # assert
        self.assertEqual(database.round_to_db.call_count, 1)

    def test_selection_8(self, input):
        # arrange
        database = Mock(db())
        app = t.App(db=database)
        database.load_person.return_value = [Person("Testy", "Mctest", 20)]
        database.load_drinks.return_value = [Drink("Testy Ade", 1, "Soft Drink")]
        input.side_effect = ["7", "Testy", "Mctest", "Testy", "Mctest", "Testy Ade", "n", "n", "y", "ex"]

        # act
        app.main_menu()

        # assert
        self.assertEqual(database.round_to_db.call_count, 1)

