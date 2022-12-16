from threading import Thread
from time import sleep, perf_counter


def task(id):
    plik1 = open('../dane/t1.txt', 'w')
    plik1.write(str(id))
    sleep(1)

def task2(id):
    plik2 = open('../dane/t2.txt', 'w')
    plik2.write(str(id))
    sleep(1)


# task(1)
start_time = perf_counter()

t1 = Thread(target=task, args=(1,))
t2 = Thread(target=task2, args=(2,))

t1.start()
t2.start()

t1.join()
t2.join()

end_time = perf_counter()

print(f'To zajęło {end_time - start_time:0.2f} sek')
