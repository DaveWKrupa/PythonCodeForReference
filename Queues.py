import time
from threading import Thread, Lock, current_thread
from queue import Queue

# if __name__ == "__main__":
#
#     q = Queue()
#
#     q.put(111)
#     q.put(222)
#     q.put(333)
#
#     if not q.empty():
#         first = q.get()  # get removes the item from the q
#         q.task_done()  # tells the queue processing is complete with this object and can continue
#         print(first)
#         second = q.get()
#         q.task_done()
#         print(second)
#         third = q.get()
#         q.task_done()
#         print(third)
#
#         q.join()  # blocks the processing until all the queued items have been processed
#         print(q.empty())
#
#     print("End main")

# 111
# 222
# 333
# True
# End main


def my_function(q, lock):
    while True:  # infinite loop will stop when main thread exits, see daemon thread comment below
        value = q.get()  # if q has no items this line will block until items are added to the queue
        with lock:  # make sure multiple threads do not try to print at the same time
            print(f"{current_thread().name} got {value}")
        q.task_done()


if __name__ == "__main__":

    q = Queue()

    lock = Lock()

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=my_function, args=(q, lock))
        # daemon thread is a background thread that will die when the main thread dies
        # this allows the infinite loop in my_function to exit as the thread running the loop is killed
        thread.daemon = True  # daemon is false by default
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

    print("End main")

#
# Thread-2 (my_function) got 1
# Thread-3 (my_function) got 2
# Thread-4 (my_function) got 3
# Thread-6 (my_function) got 4
# Thread-1 (my_function) got 5
# Thread-7 (my_function) got 6
# Thread-7 (my_function) got 16
# Thread-8 (my_function) got 7
# Thread-8 (my_function) got 18
# Thread-8 (my_function) got 19
# Thread-8 (my_function) got 20
# Thread-3 (my_function) got 12
# Thread-4 (my_function) got 13
# Thread-6 (my_function) got 14
# Thread-1 (my_function) got 15
# Thread-10 (my_function) got 8
# Thread-7 (my_function) got 17
# Thread-2 (my_function) got 10
# Thread-5 (my_function) got 11
# Thread-9 (my_function) got 9
# End main
#

