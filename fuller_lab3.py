#David Fuller
#complete

quantity = int(input("Enter the number of packages purchased: "))
price = 149
discountAmount = 0
totalAmount = 0

if quantity > 149:
    discountAmount = quantity * price * .4
    totalAmount = quantity * price * .6
elif quantity > 99:
    discountAmount = quantity * price * .3
    totalAmount = quantity * price * .7
elif quantity > 49:
    discountAmount = quantity * price * .2
    totalAmount = quantity * price * .8
elif quantity > 9:
    discountAmount = quantity * price * .1
    totalAmount = quantity * price * .9
else:
    totalAmount = price * quantity

print("Discount Amount: $", format(discountAmount, ',.2f'), sep="")
print("Total Amount: $", format(totalAmount, ',.2f'), sep="")
