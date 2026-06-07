import age
def get_age():
    #Arrange 
    expected_err_invalid = "Please enter an integer (ie: a number which does not haave a decimal part)."
    expected_err_bel = "please enter an integer that is more than (or equal to) 12"
    expected_err_abv = "Please enter an integer that is less than 115"
    expected_int = "Thank you"

    #Act
    #invalid
    string_input = age.check_age("XLII")
    float_input = age.check_age(12.5)

    #Boundary 
    low_input = age.check_age(12)
    high_input = age.check_age(115)

    #Epected 
    expected_input_low = age.check_age(12)
    expected_input_high = age.check_age(114)
    expected_bound_high = age.check_age(113)
    expected_input = age.check_age(13)

    #Assert
    assert string_input == expected_err_invalid
    assert float_input == expected_err_invalid
    
    assert low_input == expected_err_bel
    assert high_input == expected_err_abv

    assert expected_input == expected_int
    assert expected_input_low == expected_int
    assert expected_input_high == expected_int
    assert expected_bound_high == expected_int

get_age()

