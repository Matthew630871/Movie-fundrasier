#I don't understand what is going wrong here.
#I have asked the ai for help it spat this out. But i am still unsure as to what and why noting is happening

import age_v2

import tkinter as tk
from tkinter import ttk, messagebox
def test_get_age():
    #Arrange 
    ERROR = -1
    CHILD_PRICE = 7.50
    ADULT_PRICE = 10.50
    SENIOR_PRICE = 6.50

    #Act
    #invalid
    string_input = age_v2.check_age("XLII")
    float_input = age_v2.check_age(12.5)

    #Boundary 
    low_input = age_v2.check_age(12)
    high_input = age_v2.check_age(115)

    #Epected 
    expected_input_low = age_v2.check_age(12)
    expected_input_high = age_v2.check_age(114)
    expected_adult = age_v2.check_age(55)
    expected_bound_high = age_v2.check_age(113)
    expected_input = age_v2.check_age(13)

    #Assert
    assert string_input == ERROR
    assert float_input == ERROR
    
    assert low_input == ERROR
    assert high_input == ERROR

    assert expected_input == CHILD_PRICE
    assert expected_input_low == CHILD_PRICE
    assert expected_adult == ADULT_PRICE
    assert expected_input_high == SENIOR_PRICE
    assert expected_bound_high == SENIOR_PRICE



