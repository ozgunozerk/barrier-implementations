######
''' 
let's try to fix our code for loops
the barrier should be set to its initial value after each iteration of the loop
so that the next iteration can happen safely
----
but again there is a problem, look at the end for the problem description
'''

import threading

barrier = threading.Semaphore(0)  # global semaphore
mutex = threading.Lock()  # global mutex
count = 0  # global variable for count
thread_amount = 5
critical_value = 0

def gameTime():
    
    global count 
    global critical_value

    for turn in range(100):
        print(f"Turn: {turn}, I'm {threading.get_ident()}")
        #sleep(0.01)

        mutex.acquire()
        count = count + 1
        mutex.release()

        if count == thread_amount:
            #print(f"I'm {threading.get_ident()}, I'm gonna increment the counter!")
            barrier.release()
        
        barrier.acquire()
        barrier.release()  # ONLY DIFFERENCE IS THIS LINE

        critical_value += 1
        #print(f"I'm {threading.get_ident()}, I reached to the critical region!")


        mutex.acquire()
        count -= 1
        mutex.release()

        if count == 0:
            barrier.acquire()


    
    
t1 = threading.Thread(target = gameTime)
t2 = threading.Thread(target = gameTime)
t3 = threading.Thread(target = gameTime)
t4 = threading.Thread(target = gameTime)
t5 = threading.Thread(target = gameTime)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()


'''
line 32 and line 47 are problematic
assume we have n threads
say n-1th thread is interrupted just before eecuting line 32
and then nth thread is scheduled, it passes through the first mutex
now, both threads find that count==n
and both threads will release the barrier 
---
Similar problem might happen at line 47


Note: this problem was there all along in the previous versions
'''