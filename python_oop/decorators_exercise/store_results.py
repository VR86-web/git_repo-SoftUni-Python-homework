def store_results(func):
    _FILE_NAME = "files/log.txt"

    def wrapper(*args, **kwargs):
        with open(_FILE_NAME, "a") as log_file:
            log_file.write(f"Function {func.__name__} was called. Result: {func(*args, **kwargs)}\n")

    return wrapper


class store_result:

    _FILE_NAME = "files/log.txt"

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with open(self._FILE_NAME, "a") as log_file:
            log_file.write(f"Function {self.func.__name__} was called. Result: {self.func(*args, **kwargs)}\n")


class store_results_in_file_name():

    _DIR = "files"

    def __init__(self, file_name):
        self.file_name = file_name

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with open(f"{self._DIR}/{self.file_name}", "a") as log_file:
                log_file.write(f"Function {func.__name__} was called. Result: {func(*args, **kwargs)}\n")

        return wrapper


@store_results_in_file_name("result.txt")
def sum_numbers(a, b):
    return a + b


sum_numbers(2, 10)
