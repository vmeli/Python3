import threading
import time

class Demo_thread(threading.Thread):
    def run(self):
        print('{} Inicio'.format(self.getName()))
        time.sleep(1)
        print('{} Terminado'.format(self.getName()))

if __name__ == '__main__':
    for x in range(9):
        th = Demo_thread(name='Hilo - {}'.format(x + 1)) #inicializando el hilo
        th.start() #ejecutando hilo
        time.sleep(.5)

'''h = Demo_thread()
h.run()'''