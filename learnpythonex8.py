formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format(1.5,2.7,3.9,4.5))
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))

print(formatter.format(
    "Try yout",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"

))