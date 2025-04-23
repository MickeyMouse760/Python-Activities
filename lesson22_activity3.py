countrycode={'india':'0091',
             'austrialia':'0025',
             'nepal':'00977'}
print(countrycode)
print("\nCountry code for India -")
print(countrycode.get('india','not found'))
print("\ncountry code for Japan")
print(countrycode.get('Japan', 'not found'))