from main import c, currecyoutput

def convert_cur(amount, fromm, too):
    """
    Convert the currency based on the given amount, source currency, and target currency.

    Parameters:
    amount (float): The amount of currency to convert.
    fromm (str): The source currency.
    too (str): The target currency.
    """
    if amount == None or fromm.get() == "From" or too.get() == "To":
        # TODO: Add implementation
        pass
    else:
        currecyoutput.set(round(c.convert(amount, fromm.get(), too.get()), 5))