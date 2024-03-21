from v2.convert_currency import convert_cur


def callback(*args):
    """
    Callback function to update the currency conversion when the selected currencies change.
    """
    global currecyinput, currencyval1, currencyval2
    convert_cur(currecyinput, currencyval1, currencyval2)