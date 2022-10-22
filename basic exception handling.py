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
