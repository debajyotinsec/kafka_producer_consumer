
import codecs

PURCHASE_ORDER_NUMBER_SKIP_LIST = [
    '4289951', '4333313', '4289979', '4289988', '2213167', '1378144',
    '1349546', 
    ]

def date_transformation(date_variable):
    DEFAULT_DATE_LOW_VALUE = '0001-01-01'
    if len(date_variable.strip()) == 0:
        date_variable = DEFAULT_DATE_LOW_VALUE
    return date_variable
    

def transform_hex_null(hex_null_variable):
    print ("hex value is --->{}<---".format(hex_null_variable))
    if hex_null_variable is None:
        print ("----->found none<------")
    passascii_txt = codecs.decode(hex_null_variable, "cp500")
    print ("hex_null_variable--->{}<--->passascii_txt--->{}<--".format(hex_null_variable,passascii_txt))
    return passascii_txt


