from multiprocessing import Process
from interface import Interface

inface = Interface()

if(inface.setClickMode() == "beta") :
    if __name__ == "__main__" :
            inface.setClickOrder(2)
            inface.init()

            Process1 = Process(target=inface.check)
            Process1.daemon = True
            Process1.start()

            while True :
                inface.move()
                inface.exit()

else :
    inface.setClickOrder(2)
    inface.start()

