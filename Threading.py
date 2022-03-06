import time
from threading import Thread, Lock


def square_numbers():
    for j in range(100):
        j * j


# if __name__ == "__main__":
#     threads = []
#     num_threads = 10
#
#     # create threads
#     for i in range(num_threads):
#         thread = Thread(target=square_numbers)
#         threads.append(thread)
#
#     # start threads
#     for thread in threads:
#         thread.start()
#
#     # join threads: wait for them to complete
#     for thread in threads:
#         thread.join()
#
#     print("End main")


# the following code creates a race condition between the two threads
# which results in the End Value being 1 instead of 2
# test_global_value = 0
#
#
# def increase():
#     global test_global_value
#
#     local_copy = test_global_value
#     local_copy += 1  # the two threads reach this point at the same time
#     time.sleep(0.1)
#     test_global_value = local_copy  # so when the threads get here local_copy == 1 for both threads
#
#
# if __name__ == "__main__":
#     print("Start value", test_global_value)
#
#     thread1 = Thread(target=increase)
#     thread2 = Thread(target=increase)
#
#     thread1.start()
#     thread2.start()
#
#     thread1.join()
#     thread2.join()
#
#     print("End value", test_global_value)
#
# # Start value 0
# # End value 1


test_global_value = 0


def increase(lock):
    global test_global_value
    lock.acquire()
    local_copy = test_global_value
    local_copy += 1
    time.sleep(0.1)
    test_global_value = local_copy
    lock.release()


# this increase method uses lock as a context manager
# eliminating the need for acquire and release statements
def increase_lock_context_manager(lock):
    global test_global_value
    with lock:
        local_copy = test_global_value
        local_copy += 1
        time.sleep(0.1)
        test_global_value = local_copy


if __name__ == "__main__":
    print("Start value", test_global_value)

    lock = Lock()
    thread1 = Thread(target=increase, args=(lock,))  # (lock,) is a tuple so requires the comma after lock
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("End value", test_global_value)


# Start value 0
# End value 2