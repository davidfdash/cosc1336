# David Fuller
# Complete
# Display aggregate 1.8 mm change over 25 years

print("Year\tRise (in millimeters)")
print("-----------------------------------")
count = 1
rise = 1.8
while count < 26:
    print(str(count) + "\t" + str(format(rise, ",.2f")))
    count += 1
    rise += 1.8