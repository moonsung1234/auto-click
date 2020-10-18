from multiprocessing import Process

def hello() :
    print("hello")

if __name__ == "__main__" :
    Process1 = Process(target=hello)
    Process1.start()
    Process1.join()