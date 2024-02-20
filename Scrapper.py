import threading
import time

def print_message(message):
    for _ in range(5):
     time.sleep(1)
     print(message)

thread1 = threading.Thread(target=print_message, args=("vlakno 1 bezi",))
thread2 = threading.Thread(target=print_message, args=("vlakno 2 bezi",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Vlakna skoncili vykonavanie.")
