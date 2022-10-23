def sub_function():
    try:
        1/0
    except Exception as e:
        message = "Exception from sub program: " + str(e)
        raise Exception(message)
