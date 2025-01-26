

try:
    a = int(input("Enter A values: "))
    b = int(input("Enter B values"))

    print(a/b)
except Exception as e:
    print("Some thing went wrong ....")

finally:
    print("Final block executed")        


