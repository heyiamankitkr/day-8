try:
    x=int(input("enter a number"))
    ans=10/x
except ZeroDivisionError:
    print("enter a number other than 0")
except ValueError:
    print("enter a number instead of string")
else:
     print(f"ans is {ans}")    
finally:
    print("end of program")