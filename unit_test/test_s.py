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

class MainTests(unittest.TestCase):

    @patch("builtins.input", return_value=unittest.mock)
    @patch("s.App.selection_1a", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    def test_selection_1_search(self, selection_1a, mock_input):
        # Arrange
        mock_input.side_effect = ["stringy"]
        # load_person_mock.side_effect = ["Testy"]
        mock_input = "S"
        database = Mock(db())
        app = t.App(db=database)
        database.load_person.return_value = ["Testy"]
        # Act
        app.selection_1(mock_input)
        # Assert
        self.assertEqual(selection_1a.call_count, 1)
        selection_1a.assert_called_with("Stringy", database.load_person.return_value)

    @patch("s.App.selection_1b", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    def test_selection_1_all(self, selection_1b):
        # Arrange
        mock_input = "a"
        database = Mock(db())
        app = t.App(db=database)
        database.load_person.return_value = ["Testy"]
        # Act
        app.selection_1(mock_input)
        # Assert
        self.assertEqual(selection_1b.call_count, 1)
        selection_1b.assert_called_with(database.load_person.return_value)

    @patch("s.App.main_menu", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    def test_selection_1_exit_to_main(self, main_menu):
        # Arrange
        mock_input = ""
        database = Mock(db())
        app = t.App(db=database)
        # Act
        app.selection_1(mock_input)
        # Assert
        self.assertEqual(main_menu.call_count, 1)

    @patch("builtins.input", return_value=unittest.mock)
    @patch("s.App.selection_1a", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    def test_selection_1a_searcher(self, selection_1c, mock_input):
        # Arrange
        mock_input.side_effect = ["stringy"]
        # load_person_mock.side_effect = ["Testy"]
        mock_input = "S"
        database = Mock(db())
        app = t.App(db=database)
        database.load_person.return_value = ["Testy"]
        # Act
        app.selection_1a(mock_input)
        # Assert
        self.assertEqual(selection_1c.call_count, 1)

    @patch("builtins.input", return_value=unittest.mock)
    @patch("s.App.main_menu", return_value=unittest.mock)
    def test_selection_1a_searcher_Exit(self, main_menu, mock_input):
        # Arrange
        database = Mock(db())
        app = t.App(db=database)
        database.load_person.return_value = [Person("Stringy", "Testy", 10)]
        # Act
        app.selection_1a("Ex", [Person("Stringy", "Testy", 10)])
        # Assert
        self.assertEqual(main_menu.call_count, 1)

    @patch("persistence.database.Database.load_person", return_value=unittest.mock)  # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    @patch("s.App.selection_1c", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    def test_selection_1b(self, selection_1c, mock_person_list):
        # Arrange
        database = Mock(db())
        app = t.App(db=database)
        database.load_person.return_value = [Person("Gary", "McTest", 10)]
        # Act
        app.selection_1b([Person("Gary", "McTest", 10)])
        # Assert
        self.assertEqual(selection_1c.call_count, 1)

    @patch("s.App.selection_2", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    def test_selection_2c(self, selection_2):
        # Arrange
        database = Mock(db())
        app = t.App(db=database)
        mock_input = "s"
        # Act
        app.selection_2(mock_input)
        # Assert
        self.assertEqual(selection_2.call_count, 1)

    @patch("builtins.input", return_value=unittest.mock)
    @patch("s.App.selection_2a", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    def test_selection_2_search(self, selection_2a, mock_input):
        # Arrange
        mock_input.side_effect = ["stringy", "dingy"]
        # load_person_mock.side_effect = ["Testy"]
        database = Mock(db())
        app = t.App(db=database)
        database.load_drinks.return_value = ["Testy", "Test"]
        # Act
        app.selection_2("S")
        # Assert
        self.assertEqual(selection_2a.call_count, 1)
        selection_2a.assert_called_with("Stringy", ["Testy", "Test"])

    @patch("s.App.selection_2b", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    def test_selection_2_all(self, selection_2b):
        # Arrange
        # load_person_mock.side_effect = ["Testy"]
        database = Mock(db())
        app = t.App(db=database)
        database.load_drinks.return_value = ["Testy", "Test"]
        # Act
        app.selection_2("a")
        # Assert
        self.assertEqual(selection_2b.call_count, 1)
        selection_2b.assert_called_with(["Testy", "Test"])

    @patch("s.App.main_menu", return_value=unittest.mock)  # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    def test_selection_2_exit(self, main_menu):
        # Arrange
        # load_person_mock.side_effect = ["Testy"]
        database = Mock(db())
        app = t.App(db=database)
        database.load_drinks.return_value = ["Testy", "Test"]
        # Act
        app.selection_2("")
        # Assert
        self.assertEqual(main_menu.call_count, 1)

    @patch("builtins.input", return_value=unittest.mock)
    @patch("s.App.selection_2a", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    def test_selection_2a_search(self, selection_2a, mock_input):
        # Arrange
        database = Mock(db())
        app = t.App(db=database)
        database.load_drinks.return_value = ["Testy", "Test"]
        # Act
        app.selection_2a("testy", ["Testy", "Test"])
        # Assert
        self.assertEqual(selection_2a.call_count, 1)

    @patch("builtins.input", return_value=unittest.mock)
    @patch("s.App.main_menu", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    def test_selection_2a_exit(self, main_menu, mock_input):
        # Arrange
        database = Mock(db())
        app = t.App(db=database)
        database.load_drinks.return_value = [Drink("Testy", "Test", 10)]
        # Act
        app.selection_2a("Ex", [Drink("Testy", "Test", 10)])
        # Assert
        self.assertEqual(main_menu.call_count, 1)

    @patch("builtins.input", return_value=unittest.mock)
    @patch("s.App.selection_3a", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    def test_selection_3_adding(self, selection_3a, mock_input):
        # Arrange
        database = Mock(db())
        app = t.App(db=database)
        database.load_drinks.return_value = [Drink("Testy", "Test", 10)]
        mock_input.side_effect = "Gary", "McTest", 10
        # Act
        app.selection_3()
        # Assert
        self.assertEqual(selection_3a.call_count, 1)
        selection_3a.assert_called_with("Gary", "Mctest", 10)

#### CAN't PATCH title ######
    @patch("builtins.input")
    @patch("s.App.main_menu", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    def test_selection_3_exit(self, main_menu, mock_input):
        # Arrange
        mock_input.side_effect = ["Ex"]
        database = Mock(db())
        app = t.App(db=database)
        # Act
        app.selection_3()
        # Assert
        self.assertEqual(main_menu.call_count, 1)


    @patch("builtins.input", return_value=unittest.mock)
    @patch("builtins.input", return_value=unittest.mock)
    @patch("builtins.input", return_value=unittest.mock)
    @patch("s.App.selection_3b", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    def test_selection_3a(self, selection_3b, mock_input1, mock_input2, mock_input3):
        # Arrange
        mock_input1.side_effect = "Gary"
        mock_input2.side_effect = "McTest"
        mock_input3.side_effect = 10
        app = t.App("fake")
        # Act
        app.selection_3a(mock_input1.side_effect, mock_input2.side_effect, mock_input3.side_effect)
        # Assert
        self.assertEqual(selection_3b.call_count, 1)

    @patch("s.App.selection_3", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    @patch("builtins.input", return_value=unittest.mock)
    def test_selection_3b(self, selection_3, db):
        selection_3.side_effect = [Person("Garyo", "McTest", 10)]
        app = t.App("fake")
        app.selection_3b(selection_3.side_effect)
        self.assertEqual(db.call_count, 1)

    @patch("s.App.selection_4a", return_value=unittest.mock)
    def test_selection4(self, selection_4a):
        mock_input1 = "Water"
        mock_input2 = "1"
        mock_input3 = "Soft Drink"
        app = t.App("fake")
        app.selection_4(mock_input1, mock_input2, mock_input3)
        self.assertEqual(selection_4a.call_count, 1)

    @patch("builtins.input", return_value=unittest.mock)
    @patch("s.App.selection_4", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    def test_selection_4b_drink_input_getter_alc(self, selection_4, mock_input):
        # Arrange
        database = Mock(db())
        app = t.App(db=database)
        mock_input.side_effect = "Lager", "y", "a"
        # Act
        app.selection_4b_drink_input_getter()
        # Assert
        self.assertEqual(selection_4.call_count, 1)
        selection_4.assert_called_with("Lager", 0, "Alcoholic")

    @patch("builtins.input", return_value=unittest.mock)
    @patch("s.App.selection_4", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    def test_selection_4b_drink_input_getter_soft(self, selection_4, mock_input):
        # Arrange
        database = Mock(db())
        app = t.App(db=database)
        mock_input.side_effect = "Pepsi Max", "n", "s"
        # Act
        app.selection_4b_drink_input_getter()
        # Assert
        self.assertEqual(selection_4.call_count, 1)
        selection_4.assert_called_with("Pepsi Max", 1, "Soft Drink")

################# Issue with title again ###############
    @patch("builtins.input", return_value=unittest.mock)
    @patch("s.App.main_menu", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    def test_selection_4b_drink_input_exit(self, main_menu, mock_input):
        # Arrange
        database = Mock(db())
        app = t.App(db=database)
        mock_input.side_effect = ["ex"]
        # Act
        app.selection_4b_drink_input_getter()
        # Assert
        self.assertEqual(main_menu.call_count, 1)

    @patch("s.App.selection_4b_drink_input_getter", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    @patch("s.App.selection_4", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    def test_selection_4a(self, selection_4, selection_4b_drink_input_getter):
        database = Mock(db())
        app = t.App("fake")
        database.load_drinks.return_value = [Drink("Testy", "Test", 10)]
        selection_4.side_effect = [Person("Garyo", "McTest", 10)]

        app.selection_4a([Person("Garyo", "McTest", 10)])

        self.assertEqual(selection_4b_drink_input_getter.call_count, 1)

    @patch("persistence.database.Database.load_person", return_value=unittest.mock)  # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    @patch("builtins.input", return_value=unittest.mock)
    @patch("s.App.selection_5a", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    def test_selection_5(self, selection_5a, mock_input, load_person):

        database = Mock(db())
        app = t.App(database)
        mock_input.side_effect = ["Testy"]
        database.load_person.return_value = [Person("Testy", "Test", 10)]

        app.selection_5()

        self.assertEqual(selection_5a.call_count, 1)







