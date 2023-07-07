import unittest
import pytest
from foo1 import foo2, search_filter, word_search_percent


result = search_filter()

class TestSerach(unittest.TestCase):
    def test_correct_answer(self):
        expected = [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}]
        res = result
        self.assertEqual(res, expected, "uncorrect result")

    def test_list_equal(self):
        expected = [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}]
        res = result
        self.assertListEqual(res, expected)

    def test_bool(self):
        self.assertTrue(result)

    def test_is_not(self):
        expected = [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}]
        res = result
        self.assertIsNot(res, expected)

    def test_is_not_none(self):
        res = result
        self.assertIsNotNone(res)

    def test_rus_in(self):
        expected = {'visit1': ['Москва', 'Россия']}
        res = result
        self.assertIn(expected, res)

    def test_not_in(self):
        expected = {'visit2': ['Дели', 'Индия']}
        res = result
        self.assertNotIn(expected, res)

    def test_is_instance(self):
        res = result
        expected = list
        self.assertIsInstance(res, expected)

    def test_is_not_instance(self):
        res = result
        expected = dict
        self.assertNotIsInstance(res, expected)


result_foo2 = foo2()

class TestUnique_ID:

    def test_is_instance(self):
        res = result_foo2
        expected = list
        assert isinstance(res, expected)

    def test_len(self):
        res = result_foo2
        expected = 6
        assert len(res) == expected, "wrong length"

    def test_in(self):
        res = result_foo2
        expected = 213
        assert expected in res, "213 should be in"

    def test_not_none(self):
        res = result_foo2
        expected = None
        assert res != expected, "not None"

    def test_sum(self):
        res = sum(result_foo2)
        expected = sum([213, 15, 54, 119, 98, 35])
        assert res == expected, "test sum"


    @pytest.mark.parametrize("num",[
        (213),
        (15),
        (54),
        (119),
        (98),
        (35)
    ])
    def test_in_parametrize(self, num):
        res = result_foo2
        assert num in res

res_percent  = word_search_percent()

class TestSearchWords(unittest.TestCase):
    def test_not_none(self):
        res = res_percent
        self.assertIsNotNone(res)

    @unittest.skipIf(len(res_percent) < 2, "too short")
    def test_skip(self):
        self.assertTrue(res_percent)

    @unittest.skipUnless(len(res_percent) > 100, "too long")
    def test_skip2(self):
        res = res_percent
        expected = str
        self.assertIsInstance(res, expected, "must be string")

    @unittest.expectedFailure
    def test_expect_fail(self):
        res = res_percent
        self.assertFalse(res)

    @unittest.skip("При временной потере актуальности теста, но сохранить как пример")
    def test_skip3(self):
        self.fail("test skip")

    def test_regex(self):
        res = ''.join(str(i) for i in res_percent)
        reg = r"Поисковых запросов из\s\d+\sслов\(а\)\s-\s\d+\%"
        self.assertRegex(res, reg)

    