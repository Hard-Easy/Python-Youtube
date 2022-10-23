# Exception Handling - Code Adhyayana
from exception.custome_exception import MyProjectException, SecondProjectException
from submodule.subprog import sub_function

try:
    try:
        sub_function()
        print("Process has been completed.")

    except Exception as e:
        exception_message = "Exception: " + str(e)
        print("Inner Exception block")
        print(exception_message)
        raise e
except Exception as e:
    print("Outer Exception block")
    print(e)


