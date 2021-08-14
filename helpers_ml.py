
def sci_num(x):
    #SCIENTIFIC NOTATION sci_num() 
    # Use str.format() on a number with ""{:e}" as str to format the number in scientific notation.
    # To only include a certain number of digits after the decimal point, use "{:.Ne}", where N is the desired number of digits.

    # scientific_notation = "{:.2e}".format(x)
    # Format `x` in scientific notation with 2 digits

    return "{:.2e}".format(x)