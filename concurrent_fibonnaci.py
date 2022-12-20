"""
Task: Implement a program that generates and prints the Fibonacci sequence up to a given number, using concurrent execution. The program should accept a number as an input and should print the Fibonacci sequence up to that number.

Constraints:

The program should use concurrent execution to generate and print the Fibonacci sequence.
The program should use at least two concurrent threads.
Example:
Input: 10
Output: 0 1 1 2 3 5 8

To solve this task, you can use Python's threading module. Here is some pseudocode to get you started:


```
def generate_fibonacci(n):
  # generate the Fibonacci sequence up to n
  # ...

def print_fibonacci(n):
  # print the Fibonacci sequence up to n
  # ...

def main():
  # read n from the command line
  # create a thread to generate the Fibonacci sequence
  # create a thread to print the Fibonacci sequence
  # start both threads
  # ...

if __name__ == '__main__':
  main()

```

To use the threading module, you will need to import it and create a Thread object, passing a function as the target. Then, you can start the thread using the start() method.
"""
from concurrent.futures import ThreadPoolExecutor
from queue import Queue, Empty
from threading import Thread


def generate_fibonacci(n, queue: Queue):
    prev = None
    prev_prev = None
    for i in range(n):
        if i == 0:
            queue.put(1)

        elif i == 1:
            queue.put(1)
            prev_prev = 1
            prev = 1

        elif i > 2:
            current = prev + prev_prev
            queue.put(current)
            prev_prev = prev
            prev = current


def print_fibonacci(queue: Queue):
    # print the Fibonacci sequence up to n
    while True:
        try:
            v = queue.get(timeout=1)
            print(v)

        except Empty:
            break

def main():
    # read n from the command line
    text = input("prompt")
    n = int(text)
    # n = 10
    queue = Queue()
    with ThreadPoolExecutor(max_workers=2) as pool:
        # create a thread to generate the Fibonacci sequence
        fut1 = pool.submit(generate_fibonacci, n, queue)
        # create a thread to print the Fibonacci sequence
        fut2 = pool.submit(print_fibonacci, queue)

        # fut1.result()
        # fut2.result()



if __name__ == '__main__':
    main()
