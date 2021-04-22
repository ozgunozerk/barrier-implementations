######
''' 
let's try to fix the problem in reusable1
in both cases, the barrier operations are inside the mutex,
so practically, threads are immune to interrupts for barrier operations
but there is still a problem present, look at the end for the explanation of this error
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
        if count == thread_amount:
            #print(f"I'm {threading.get_ident()}, I'm gonna increment the counter!")
            barrier.release()
        ## we simply moved the barrier operations inside the mutex
        mutex.release()
        
        barrier.acquire()
        barrier.release()  # ONLY DIFFERENCE IS THIS LINE

        critical_value += 1
        #print(f"I'm {threading.get_ident()}, I reached to the critical region!")


        mutex.acquire()
        count -= 1
        if count == 0:
            barrier.acquire()
        ## we simply moved the barrier operations inside the mutex
        mutex.release()

        


    
    
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
This code allows a precocious thread to finish its iteration (expected behaviour),
but additionally allows the same thread to skip to the next iteration 
and pass through the second mutex in that next iteration,
effectively getting ahead of the other threads by a lap

Here is the scenario:
thread amount = 5
say we are on the first iteraton,
all threads passed the barrier,
count = 5
at the moment, only the first thread reached to the second mutex
it decreased count by 1 ->  (5 - 1 = 4)
does not go into if statement in line 44
gets out of mutex,
still no interrupt happens
goes to the next iteration
increases count by 1 ->  (4 + 1 = 5)
signals the barrier
gets out of mutex
can pass the barrier now
gets to critical point
gets to the second mutex

NOW first thread is at the second iteration's second mutex,
yet others are in the first iteraton's second mutex
first thread is ahead of others by a lap, this can happen endlessly



'''