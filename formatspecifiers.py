#FORMAT SPECIFIERS

price1 = 3.1427
price2 = -76.4578

print(f"The price is ${price1:10}")  #10 spaces to right
print(f"The price is ${price2:10}")  #10 spaces to right

print(f"The price is ${price1:>10}")  #justify right
print(f"The price is ${price2:<10}")  #justify left
print(f"The price is ${price1:^10}")  #justify center