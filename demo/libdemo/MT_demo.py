from threading import Thread
import threading


def print_numbers():
    for i in range(1, 11):
        print(i)


mt = threading.current_thread()
print(mt.name)

t = Thread(target=print_numbers)
t.start()

print(threading.active_count())

# Wait for t to terminate
t.join()

for i in range(1, 11):
    print(f'Main : {i}')