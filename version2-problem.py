######
''' 
assume threads need to perform their operations in a loop
so we need a reusable barrier
in version2, the barrier was left open in the end
causing problems in loops
'''

import threading
#from time import sleep

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

