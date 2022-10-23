from submodule.subprog import sub_function
from exception.custome_exception import MyProjectException, SecondProjectException

try:
    try:
        input_num = 9
        assert input_num == 9 , "Number should be 9"
        0/1
        sub_function()
        raise SecondProjectException("This is 2nd Exception")
        raise MyProjectException("Z")
    except Exception as e:
        print("Inner: " + str(e))
        raise Exception(e)
    else:
        print("Inner: Didn't get the Exception.")
    finally:
        print("Inner: Process Ended in Finally")

except Exception as e:
    print("Outer: " + str(e))
else:
    print("Outer: Didn't get the Exception.")
finally:
    print("Outer: Process Ended in Finally")
