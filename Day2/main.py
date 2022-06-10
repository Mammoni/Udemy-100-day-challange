print("Welcome to tip calculator\n")
bill = float(input("What was the total bill?: "))
percenatge = float(input("What percentage tip would you like to give?: "))
split = int(input("How many people to split the bill?: "))
total_bill = "{:.2f}".format(round(bill/split,2))
percent = percenatge/100
tip = "{:.2f}".format(round((bill / split) * (percent),3))
print(f"Thus everyone's share of the total bill is ${total_bill} plus a ${tip} tip")
