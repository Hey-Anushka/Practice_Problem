# Line 1 of the input is a whole number, line 2 is a decimal number.
whole_text = input()
decimal_text = input()

whole_text = int(whole_text) 
decimal_text = float(decimal_text)

sum = whole_text + decimal_text
# TODO: turn the two lines of text into numbers and add them up

print(float(sum))   # the sum, as a decimal
print(int(sum))   # the same sum with the fraction chopped off toward zero
print(f"{whole_text} + {decimal_text} = {sum}")   # the report line


