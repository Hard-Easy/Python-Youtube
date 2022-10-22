#Exception Handling - Code Adhyayana

try:
    with open('test.txt','r') as rfile:
        data = rfile.readlines()
        print(data)

except FileNotFoundError as e:
    print("Please check if file is available or not")
    print("sending email")

except Exception as e:
    print("Generic Exception")
    print(type(e).__name__)
    print(e)
else:
    print("sucess email")
finally:
    print("close data connection")




























"""
try:
    
    with open('abc.txt') as rfile:
        data = rfile.readlines()

except ZeroDivisionError as e:
    print("Divide by 0 exception: ", e)
except FileNotFoundError as e:
    print("Check if input file is available or not.")
    print("Sending email...")
except Exception as e:
    print(type(e).__name__)
    print("Exception : ",e)

    """