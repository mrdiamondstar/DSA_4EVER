import time

def logger(funct):
    def timmings():
        start=time.time()
        funct()
        end=time.time()
        print(f"Time taken for the execution of the function {end-start}")
    return timmings

@logger
def display():
    print("Hello brother")
    time.sleep(2)
    print("Its me Dstar")
display()