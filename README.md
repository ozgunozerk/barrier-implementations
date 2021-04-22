# Barrier implementations with Semaphores

Semaphores are available in nearly every popular programming language.

In parallel/concurrent programming, barriers hold significant importance. 

In this repository, different approaches to barrier implementations of semaphores will be demonstrated. Alongside with the implementation itself, the corresponding errors are explained in detail.

For each code, there is a next version, trying to solve the previous error. Order of the trials are as follows:

1. version1.py  (most straight-forward barrier implementation trial)
2. version2.py  (solving the deadlock in version1)
3. version2-problem.py  (version2 works, but not in loops)
4. reusable-1.py  (trying create loop-friendly barriers)
5. reusable-2.py  (fixing the interrupt related problem in all previous versions)
6. solution (fixes the issue of one thread may advance in iterations without waiting for others) 


All errors are explained in detail as comments in the python files.



### Reference: 
The algorithms for above implementations are taken from the book: \
*The Little Book of Semaphores Allen B. Downey Version 2.2.1* [https://www.cse.iitb.ac.in/~mythili/os/references/LittleBookOfSemaphores.pdf]\

