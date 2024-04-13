import unittest
from string_utils import StringUtils

class TestStringUtils(unittest.TestCase):

    def setUp(self):
        self.string_utils = StringUtils()

    # Позитивные тесты capitilize
    def test_capitalize_first_letter(self):
        # Проверяем, что первая буква становится заглавной
        result = self.string_utils.capitilize("hello")
        self.assertEqual(result, "Hello")

    def test_capitalize_empty_string(self):
        # Проверяем, что пустая строка остается пустой
        result = self.string_utils.capitilize("")
        self.assertEqual(result, "")

    def test_capitalize_single_letter(self):
        # Проверяем, что если входная строка состоит из одной буквы, она станет заглавной
        result = self.string_utils.capitilize("a")
        self.assertEqual(result, "A")

    # Негативные тесты capitilize
    def test_capitalize_with_numbers(self):
        # Проверяем, что метод работает только с буквами
        result = self.string_utils.capitilize("123hello")
        self.assertEqual(result, "123hello")  # Ожидаемый результат - без изменений, так как в начале числа

    def test_capitalize_with_symbols(self):
        # Проверяем, что метод работает только с буквами
        result = self.string_utils.capitilize("!@#$hello")
        self.assertEqual(result, "!@#$hello")  # Ожидаемый результат - без изменений, так как в начале символы

    def test_capitalize_with_whitespace(self):
        # Проверяем, что метод работает с пробельными символами
        result = self.string_utils.capitilize("  hello")
        self.assertEqual(result, "  hello")  # Ожидаемый результат - без изменений, так как пробелы в начале строки

    # Позитивные тесты trim
    def test_trim_no_whitespace(self):
        # Проверяем, что строка без пробелов в начале остается неизменной
        result = self.string_utils.trim("hello")
        self.assertEqual(result, "hello")

    def test_trim_with_whitespace(self):
        # Проверяем, что пробелы в начале строки удаляются
        result = self.string_utils.trim("   hello")
        self.assertEqual(result, "hello")

    def test_trim_empty_string(self):
        # Проверяем, что пустая строка остается пустой
        result = self.string_utils.trim("")
        self.assertEqual(result, "")

    # Негативные тесты trim
    def test_trim_whitespace_only(self):
        # Проверяем, что если строка состоит только из пробелов, она становится пустой
        result = self.string_utils.trim("    ")
        self.assertEqual(result, "")

    def test_trim_no_string(self):
        # Проверяем, что если аргумент - не строка, метод вызывает ошибку
        with self.assertRaises(AttributeError):
            self.string_utils.trim(123)

    # Позитивные тесты to_list
    def test_to_list_default_delimeter(self):
        # Проверяем, что строка с разделителем запятой разбивается на список
        result = self.string_utils.to_list("apple,banana,orange")
        self.assertEqual(result, ["apple", "banana", "orange"])

    def test_to_list_custom_delimeter(self):
        # Проверяем, что строка с пользовательским разделителем разбивается на список
        result = self.string_utils.to_list("apple|banana|orange", "|")
        self.assertEqual(result, ["apple", "banana", "orange"])

    def test_to_list_empty_string(self):
        # Проверяем, что пустая строка возвращает пустой список
        result = self.string_utils.to_list("")
        self.assertEqual(result, [])

    # Негативные тесты to_list
    def test_to_list_no_delimeter(self):
        # Проверяем, что строка без разделителя возвращает список с одним элементом
        result = self.string_utils.to_list("apple")
        self.assertEqual(result, ["apple"])

    def test_to_list_invalid_delimeter(self):
        # Проверяем, что если разделитель не является строкой, вызывается ошибка
        with self.assertRaises(TypeError):
            self.string_utils.to_list("apple,banana,orange", 123)

    def test_to_list_invalid_input(self):
        # Проверяем, что если входной аргумент не строка, вызывается ошибка
        with self.assertRaises(AttributeError):
            self.string_utils.to_list(123)
    
    # Позитивные тесты contains
    def test_contains_true(self):
        # Проверяем, что символ присутствует в строке
        result = self.string_utils.contains("hello", "e")
        self.assertTrue(result)

    def test_contains_false(self):
        # Проверяем, что символ отсутствует в строке
        result = self.string_utils.contains("hello", "z")
        self.assertFalse(result)

    def test_contains_empty_string(self):
        # Проверяем, что если строка пустая, метод возвращает False
        result = self.string_utils.contains("", "a")
        self.assertFalse(result)

    # Негативные тесты contains
    def test_contains_invalid_input(self):
        # Проверяем, что если входные данные не являются строками, вызывается ошибка
        with self.assertRaises(AttributeError):
            self.string_utils.contains(123, "a")

    def test_contains_invalid_symbol(self):
        # Проверяем, что если символ не является строкой, вызывается ошибка
        with self.assertRaises(TypeError):
            self.string_utils.contains("hello", 123)

    # Позитивные тесты delete_symbol
    def test_delete_symbol_single_occurrence(self):
        # Проверяем удаление символа, когда он встречается только один раз в строке
        result = self.string_utils.delete_symbol("hello", "e")
        self.assertEqual(result, "hllo")

    def test_delete_symbol_multiple_occurrences(self):
        # Проверяем удаление символа, когда он встречается несколько раз в строке
        result = self.string_utils.delete_symbol("hello world", "o")
        self.assertEqual(result, "hell wrld")

    def test_delete_symbol_empty_string(self):
        # Проверяем удаление символа из пустой строки
        result = self.string_utils.delete_symbol("", "a")
        self.assertEqual(result, "")

    # Негативные тесты delete_symbol
    def test_delete_symbol_symbol_not_found(self):
        # Проверяем, что если символ не найден в строке, строка остается неизменной
        result = self.string_utils.delete_symbol("hello", "z")
        self.assertEqual(result, "hello")

    def test_delete_symbol_invalid_input(self):
        # Проверяем, что если входные данные не являются строками, вызывается ошибка
        with self.assertRaises(AttributeError):
            self.string_utils.delete_symbol(123, "a")

    def test_delete_symbol_invalid_symbol(self):
        # Проверяем, что если символ не является строкой, вызывается ошибка
        with self.assertRaises(TypeError):
            self.string_utils.delete_symbol("hello", 123)

    # Позитивные тесты starts_with
    def test_starts_with_true(self):
        # Проверяем, что строка начинается с указанного символа
        result = self.string_utils.starts_with("SkyPro", "S")
        self.assertTrue(result)

    def test_starts_with_false(self):
        # Проверяем, что строка не начинается с указанного символа
        result = self.string_utils.starts_with("SkyPro", "P")
        self.assertFalse(result)

    def test_starts_with_empty_string(self):
        # Проверяем, что если строка пустая, метод возвращает False
        result = self.string_utils.starts_with("", "S")
        self.assertFalse(result)

    # Негативные тесты starts_with
    def test_starts_with_invalid_input(self):
        # Проверяем, что если входные данные не являются строками, вызывается ошибка
        with self.assertRaises(AttributeError):
            self.string_utils.starts_with(123, "S")

    def test_starts_with_invalid_symbol(self):
        # Проверяем, что если символ не является строкой, вызывается ошибка
        with self.assertRaises(TypeError):
            self.string_utils.starts_with("SkyPro", 123)

    # Позитивные тесты end_with
    def test_end_with_true(self):
        # Проверяем, что строка заканчивается указанным символом
        result = self.string_utils.end_with("SkyPro", "o")
        self.assertTrue(result)

    def test_end_with_false(self):
        # Проверяем, что строка не заканчивается указанным символом
        result = self.string_utils.end_with("SkyPro", "y")
        self.assertFalse(result)

    def test_end_with_empty_string(self):
        # Проверяем, что если строка пустая, метод возвращает False
        result = self.string_utils.end_with("", "o")
        self.assertFalse(result)

    # Негативные тесты end_with
    def test_end_with_invalid_input(self):
        # Проверяем, что если входные данные не являются строками, вызывается ошибка
        with self.assertRaises(AttributeError):
            self.string_utils.end_with(123, "o")

    def test_end_with_invalid_symbol(self):
        # Проверяем, что если символ не является строкой, вызывается ошибка
        with self.assertRaises(TypeError):
            self.string_utils.end_with("SkyPro", 123)

    # Позитивные тесты is_empty
    def test_is_empty_true(self):
        # Проверяем, что метод возвращает True для пустой строки
        result = self.string_utils.is_empty("")
        self.assertTrue(result)

    def test_is_empty_false(self):
        # Проверяем, что метод возвращает False для непустой строки
        result = self.string_utils.is_empty("hello")
        self.assertFalse(result)

    def test_is_empty_whitespace(self):
        # Проверяем, что метод возвращает True для строки из пробельных символов
        result = self.string_utils.is_empty("    ")
        self.assertTrue(result)

    # Негативные тесты is_empty
    def test_is_empty_whitespace_only(self):
        # Проверяем, что метод возвращает False для строки, содержащей только пробельные символы
        result = self.string_utils.is_empty(" \n\t\r")
        self.assertFalse(result)

    # Позитивные тесты list_to_string
    def test_list_to_string_default_joiner(self):
        # Проверяем, что список преобразуется в строку с указанным разделителем (по умолчанию ", ")
        result = self.string_utils.list_to_string(["apple", "banana", "orange"])
        self.assertEqual(result, "apple, banana, orange")

    def test_list_to_string_custom_joiner(self):
        # Проверяем, что список преобразуется в строку с пользовательским разделителем
        result = self.string_utils.list_to_string(["apple", "banana", "orange"], "|")
        self.assertEqual(result, "apple|banana|orange")

    def test_list_to_string_empty_list(self):
        # Проверяем, что пустой список преобразуется в пустую строку
        result = self.string_utils.list_to_string([])
        self.assertEqual(result, "")

    def test_list_to_string_single_element(self):
        # Проверяем, что список с одним элементом преобразуется в строку без разделителя
        result = self.string_utils.list_to_string(["apple"])
        self.assertEqual(result, "apple")

    # Негативные тесты list_to_string
    def test_list_to_string_invalid_joiner(self):
        # Проверяем, что если разделитель не является строкой, вызывается ошибка
        with self.assertRaises(TypeError):
            self.string_utils.list_to_string(["apple", "banana", "orange"], 123)

if __name__ == '__main__':
    unittest.main()