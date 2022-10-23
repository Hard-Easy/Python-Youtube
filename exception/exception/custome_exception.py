class SecondProjectException(Exception):
    """this is placeholder for custome Exception"""

class MyProjectException(Exception):
    start_value = 0
    end_value = 8

    def __init__(self, data):
        super().__init__()
        self.data = data

    def __str__(self) -> str:
        return f'value {self.data} is not proper value it should be in between {self.start_value} and {self.end_value}'

