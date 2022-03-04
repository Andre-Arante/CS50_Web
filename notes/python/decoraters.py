def announce(f):
    def wrapper():
        print("About to run funcion...")
        f()
        print("Done with function...")
    return wrapper

def hello():
    print("Hello world")