
class negativeError(Exception):
    pass

def getmoney():
    while True:
        try:
            
            Amount = int (input("ENTER AMOUNT "))
            if Amount>0:
                break
            else :
                raise negativeError("Cant have negative money blud ")
            
        except ValueError:
            print("Only Integer Numbers ")

        except negativeError as e:
            print(e)

    return Amount


Amount = getmoney()
print (f"the money is {Amount}")


print(Amount)
