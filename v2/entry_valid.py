from v2.convert_currency import convert_cur


def entry_valid(input):
    """
    Validate the input in the currency input field.

    Parameters:
    input (str): The input value.

    Returns:
    bool: True if the input is valid, False otherwise.
    """
    global currencyval1, currencyval2, currecyinput
    if input[-1] == "." or input[-1].isdigit():
        currecyinput = input
        if currencyval1.get() != "From" and currencyval2.get() != "To":
            convert_cur(input, currencyval1, currencyval2)
            return True
        else:
            return True
    elif input == "":
        return True
    else:
        return False