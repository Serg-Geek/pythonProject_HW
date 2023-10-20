
import pytest
from main import ListComparer

@pytest.fixture
def list_comparer():
    return ListComparer()

def test_compare_lists_greater_average(list_comparer):
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    assert list_comparer.compare_lists(list1, list2) == "Второй список имеет большее среднее значение"

def test_compare_lists_less_average(list_comparer):
    list1 = [4, 5, 6]
    list2 = [1, 2, 3]
    assert list_comparer.compare_lists(list1, list2) == "Первый список имеет большее среднее значение"

def test_compare_lists_equal_average(list_comparer):
    list1 = [1, 2, 3]
    list2 = [3, 2, 3, 1, 2,1 ]
    assert list_comparer.compare_lists(list1, list2) == "Средние значения равны"
