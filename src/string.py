parrot = "Norwegian Blue"
print(len(parrot))
print(parrot.upper())
print(parrot.lower())
pi = 3.14
print(str(pi))
print("Spam "+"and "+"eggs")

string_1 = "Camelot"
string_2 = "place"

print("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))
print('C:\some\name')
print('C:\some\\name')
print(r'C:\some\name')

# use '\' to eliminate print of the first line
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print("hello")
exit()
name = input("What is your name?")
quest = input("What is your quest?")
color = input("What is your favorite color?")

print("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))
