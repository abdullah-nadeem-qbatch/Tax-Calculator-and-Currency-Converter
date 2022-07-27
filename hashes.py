#from locale import currency
currencies = {
    'USD': {'PKR': 232, 'EURO': 0.99, 'AUD': 1.44, 'UAE': 3.67, 'RIYAL': 3.76},
    'PKR': {'USD': 0.0043, 'EURO': 0.0042, 'AUD': 0.0062, 'UAE': 0.016, 'RIYAL': 0.016},
    'EURO' :{'USD': 1.01, 'PKR': 235, 'AUD': 1.46, 'UAE': 3.72, 'RIYAL': 3.81},
    'AUD': {'USD': 0.69, 'PKR': 161, 'EURO': 0.68, 'UAE': 2.55, 'RIYAL': 2.61},
    'UAE': {'USD': 0.27, 'PKR': 63, 'EURO': 0.27, 'AUD': 0.39, 'RIYAL': 1.02},
    'RIYAL': {'USD': 0.27, 'PKR': 62, 'EURO': 0.26, 'AUD': 0.38, 'UAE': 0.98}
}

for i in currencies['USD']:
    print(currencies['USD'][i])

'''
hash_USD = {
    'currency':'USD',
    'conversions':{'PKR': 232, 'EURO': 0.99, 'AUD': 1.44, 'UAE': 3.67, 'RIYAL': 3.76}
}

#for i in hash_USD['conversions']:
#    print(hash_USD['conversions'][i])

#print(hash_USD['conversions'])

hash_PKR = {
    'currency':'PKR',
    'conversions': {'USD': 0.0043,
    'EURO': 0.0042,
    'AUD': 0.0062,
    'UAE': 0.016,
    'RIYAL': 0.016}
}

hash_EURO = {
    'currency':'EURO',
    'conversions': {'USD': 1.01,
    'PKR': 235,
    'AUD': 1.46,
    'UAE': 3.72,
    'RIYAL': 3.81}
}

hash_AUD = {
    'currency':'AUD',
    'conversions': {'USD': 0.69,
    'PKR': 161,
    'EURO': 0.68,
    'UAE': 2.55,
    'RIYAL': 2.61}
}

hash_UAE = {
    'currency':'UAE',
    'conversions': {'USD': 0.27,
    'PKR': 63,
    'EURO': 0.27,
    'AUD': 0.39,
    'RIYAL': 1.02}
}

hash_RIYAL = {
    'currency':'RIYAL',
    'conversions': {'USD': 0.27,
    'PKR': 62,
    'EURO': 0.26,
    'AUD': 0.38,
    'UAE': 0.98}
}
'''