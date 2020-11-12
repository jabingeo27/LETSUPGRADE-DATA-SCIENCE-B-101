print("\n---------------Given the following jumbled word, OBANWRI guess the correct English word.-----------\n")
print("A. RANIBOW B. RAINBOW C. BOWRANI D. ROBWANI\n")
print("Answer - B . RAINBOW\n")


print("\n---------------PRINT LETS UPGRADE-----------------------------")

print("\nLETS UPGRADE\n")

print("\n--------------PROFIT / LOSS / NIETHER-----------------------")

CP = input("")
SP = input("")
c = int(CP) - int(SP)

if c < 0 :
    print("Profit")
elif c > 0 :
    print("Loss")
else :
    print("Neither")

print("\n-------------RUPEE TO EURO CONVERSION----------------------")

RUPEE = input("")
EURO = int(RUPEE)*80
print(EURO)
