cost_price=int(input("What was the price when you bought the item?"))
sales_price=int(input("What is the price you are selling the item for?"))
if sales_price>cost_price:
    print("Yay! You are making a profit of:",sales_price-cost_price)
else:
    print("Sorry! You have lost",sales_price-cost_price)
    