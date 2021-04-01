# Hexadecimal is used to avoid the errors gotten in dealing with binary and it usually called HEX (x) to base 16.
# Because 16 is an exact power of 2, converting between binary and hex is quick and easy.
# Hex is shorter and easier, e.g. 0 - 255 can be written in 2 hex digits and 0 - 65,535 in 4 hex digits.
# Working in base 16 means having digits of 0 - 15 like in bas 10 i.e 0 - 9 so the added symbols of A - F:
# Each hex digits repersents 4 digits called a nibble.  
for i in range(17):
  print("{0:>2} in hex is {0:>04x}".format(i))
# NOTE 16 to be 10 and from 10 - 15 0a...0f respectively.
# Also note the diiference betwenn this and binary. 
x = 0x20
y = 0x0a

print(x)
print(y)
print(x * y)

print(0b101010) # or print(0b00101010)

# addiction and sbtraction can be done in hex but rear
# 
# 
# OCTAL unlike hexdeciml, Octal is base 8 and uses the digits 037. 
z = 450
print("{0:>04o}".format(z))