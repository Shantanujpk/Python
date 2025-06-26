# what is multi threading \
# why to use
# adv
# disadv 

import threading
import time
def sleeptime(n):
    print(f"The function will sleep for {n} seconds")
    t = time.sleep(n)
    return t

# sleeptime(4)
# sleeptime(5)
# sleeptime(10)
print("done !!")

#print(time.perf_counter())
print("Threading Stated")
thread1 = threading.Thread(target=sleeptime, args=[4])
thread2 = threading.Thread(target=sleeptime, args=[15])
thread3 = threading.Thread(target=sleeptime, args=[19])

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
