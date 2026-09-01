import threading
import time
import asyncio

def task(n, args = None):
    o = 1 + 3
    print(f'task: {n}')
    print(f'args {args}')
    print(o)



def main():
    print('sequential...')
    start = time.time()
    print(start)
    task('01')
    end = time.time()

    print(f'time: {(end - start):.5f}')

    print('async with threading')
    thread = threading.Thread(target=task, args=('01',))
    thread.start()


    print(f'')



main()


