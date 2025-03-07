def calc(bill, tip_perc):
    total = bill+(tip_perc * 1.01)
    total = round(total / 1)
    return total
print(calc(150, 17))