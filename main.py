import time
def decorator(func):
    def innerFun(*args):
        start=time.perf_counter()
        func(*args)
        end=time.perf_counter()-start
        print(f"It took {end} to run {func.__name__}")
    
    return innerFun

@decorator
def arithmetic(one:int,two:int):
    print(one**two+two**one)

arithmetic(10,20)


