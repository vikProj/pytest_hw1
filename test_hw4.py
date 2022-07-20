import pytest
import logging
import homework_4 as hw4

logging.basicConfig(filename="log.txt", level=logging.DEBUG)
mylogger = logging.getLogger()


def test_create_valid_date():
    date = hw4.Date(1, 1, 2018)
    mylogger.log(logging.DEBUG, "in te okay")
    assert date


def test_create_valid_date_leap_year():
    date = hw4.Date(29, 2, 2016)
    assert date


def test_create_not_valid_day():
    pytest.raises(ValueError, hw4.Date, *(31, 4, 2018))


def test_create_not_valid_month():
    pytest.raises(ValueError, hw4.Date, *(5, 20, 2018))


def test_create_not_valid_year():
    pytest.raises(ValueError, hw4.Date, *(5, 1, 888))


def test_get_next_day():
    date = hw4.Date(1, 1, 2018)

    assert date.getNextDay() == hw4.Date(2, 1, 2018)


def test_get_next_days():
    date = hw4.Date(15, 1, 2018)

    assert date.getNextDays(20) == hw4.Date(4, 2, 2018)


def test_get_next_days_leap_year():
    date = hw4.Date(20, 2, 2016)

    assert date.getNextDays(20) == hw4.Date(11, 3, 2016)


def test_less_than_for_year():
    date1 = hw4.Date(2, 2, 2014)
    date2 = hw4.Date(20, 2, 2016)

    assert date1 < date2


def test_less_than_for_month():
    date1 = hw4.Date(2, 2, 2016)
    date2 = hw4.Date(20, 4, 2016)

    assert date1 < date2


def test_less_than_for_day():
    date1 = hw4.Date(2, 2, 2014)
    date2 = hw4.Date(20, 2, 2014)

    assert date1 < date2


def test_less_eq_than():
    date1 = hw4.Date(20, 2, 2014)
    date2 = hw4.Date(20, 2, 2014)

    assert date1 <= date2


def test_compare_eq():
    date1 = hw4.Date(20, 2, 2014)
    date2 = hw4.Date(20, 2, 2014)

    assert date1 == date2


def test_compare_not_eq():
    date1 = hw4.Date(20, 2, 2019)
    date2 = hw4.Date(20, 2, 2014)

    assert date1 != date2


def test_greater_than_for_year():
    date1 = hw4.Date(2, 2, 2014)
    date2 = hw4.Date(20, 2, 2016)

    assert date2 > date1


def test_greater_than_for_month():
    date1 = hw4.Date(2, 2, 2016)
    date2 = hw4.Date(20, 4, 2016)

    assert date2 > date1


def test_greater_than_for_day():
    date1 = hw4.Date(2, 2, 2014)
    date2 = hw4.Date(20, 2, 2014)

    assert date2 > date1


def test_greater_eq_than():
    date1 = hw4.Date(20, 2, 2014)
    date2 = hw4.Date(20, 2, 2014)

    assert date2 >= date1


def test_sub_1():
    date1 = hw4.Date(20, 3, 2014)
    date2 = hw4.Date(20, 2, 2014)

    assert (date1 - date2) == 28


def test_sub_2():
    date1 = hw4.Date(25, 3, 2014)
    date2 = hw4.Date(20, 3, 2014)

    assert (date1 - date2) == 5


def test_sub_3():
    date1 = hw4.Date(25, 12, 2015)
    date2 = hw4.Date(15, 1, 2016)

    assert (date1 - date2) == 21
