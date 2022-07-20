import pytest
import logging
import homework_3 as hw3

logging.basicConfig(filename="log.txt", level=logging.DEBUG)
mylogger = logging.getLogger()


@pytest.fixture
def create_input_data_set():
    return {1: {"name": "Tal", "age": 22, "sex": "male"},
            2: {"name": "Anat", "age": 57, "sex": "female", "ID": 123456789},
            3: {"name": "Gal", "age": 35, "sex": "male", "ID": 789456123},
            4: {"name": "Limor", "age": 30, "sex": "female"},
            5: {"name": "Serge", "age": 45, "sex": "male"},
            6: {"name": "Iren", "age": 27, "sex": "female"},
            7: {"name": "Karin", "age": 42, "sex": "female"},
            8: {"name": "Itay", "age": 50, "sex": "male"},
            9: {"name": "Saimon", "age": 60, "sex": "male"},
            10: {"name": "Itay", "age": 43, "sex": "male"},
            11: {"name": "Sabina", "age": 43, "sex": "female"},
            12: {"name": "Loren", "age": 43, "sex": "female"},
            13: {"name": "Lotem", "age": 33, "sex": "female"},
            }


def test_split_male_female(create_input_data_set):
    res1, res2 = hw3.split_male_female(create_input_data_set)

    res1_expected = {"male":
                         [{'name': 'Tal', 'age': 22, 'sex': 'male'},
                          {'name': 'Gal', 'age': 35, 'sex': 'male', 'ID': 789456123},
                          {'name': 'Serge', 'age': 45, 'sex': 'male'},
                          {'name': 'Itay', 'age': 50, 'sex': 'male'},
                          {'name': 'Saimon', 'age': 60, 'sex': 'male'},
                          {'name': 'Itay', 'age': 43, 'sex': 'male'}]}

    res2_expected = {"female":
                         [{'name': 'Anat', 'age': 57, 'sex': 'female', 'ID': 123456789},
                          {'name': 'Limor', 'age': 30, 'sex': 'female'},
                          {'name': 'Iren', 'age': 27, 'sex': 'female'},
                          {'name': 'Karin', 'age': 42, 'sex': 'female'},
                          {'name': 'Sabina', 'age': 43, 'sex': 'female'},
                          {'name': 'Loren', 'age': 43, 'sex': 'female'},
                          {'name': 'Lotem', 'age': 33, 'sex': 'female'}]}

    assert res1_expected == res1
    assert res2_expected == res2


def test_find_median_average(create_input_data_set):
    exp_res = {'male': {'average': 42.5, 'median': 44.0}, 'female': {'average': 39.285714285714285, 'median': 42}}

    act_res = hw3.find_median_average(create_input_data_set)

    assert act_res == exp_res
