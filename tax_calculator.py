def calculate_tax_monthly(amount):
    amount = amount * 12
    return calculate_tax_annually(amount) / 12

def calculate_tax_annually(amount):
    tax = 0
    #if amount in range(0, 600000):
    #    return 0
    if amount in range(600000, 1200000):
        taxableAmount = amount - 600000
        tax = taxableAmount * 0.025
        #return tax
    elif amount in range(1200000, 2400000):
        taxableAmount = amount - 1200000
        tax = taxableAmount * 0.125
        tax = tax + 15000
        #return tax
    elif amount in range(2400000, 3600000):
        taxableAmount = amount - 2400000
        tax = taxableAmount * 0.20
        tax = tax + 165000
        #return tax
    elif amount in range(3600000, 6000000):
        taxableAmount = amount - 3600000
        tax = taxableAmount * 0.25
        tax = tax + 405000
        #return tax
    elif amount in range(6000000, 12000000):
        taxableAmount = amount - 6000000
        tax = taxableAmount * 0.325
        tax = tax + 1005000
        #return tax
    else:
        taxableAmount = amount - 12000000
        tax = taxableAmount * 0.35
        tax = tax + 2955000
        #return tax
    return tax
#calculate_tax_monthly(calculate_tax_annually(700000))
