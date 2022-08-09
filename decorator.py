def stars(func):
    def wrapper_func():
        print("***************")
        func()
        print("***************")
    return wrapper_func
