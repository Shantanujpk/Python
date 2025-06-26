# -------------------------------------------------------------------
# 🔹 concurrent.futures Module in Python
# -------------------------------------------------------------------
# ✅ What is it?
#    - A high-level interface for asynchronously executing function calls.
#    - Supports both threads (ThreadPoolExecutor) and processes (ProcessPoolExecutor).
#
# ✅ Why Use It?
#    - To run tasks in parallel to speed up I/O-bound or CPU-bound operations.
#
# ✅ Use Cases:
#    - I/O-bound tasks like API requests, file reading/writing, web scraping.
#    - CPU-bound tasks like image processing, heavy calculations using ProcessPoolExecutor.
#
# ✅ Advantages:
#    - Simple syntax with map() and submit().
#    - Avoids manual thread/process management.
#    - Automatically manages the pool size.
#
# ❌ Disadvantages:
#    - Overhead for simple tasks may not be worth it.
#    - Limited control over low-level thread/process behavior.
#    - ThreadPoolExecutor is still bound by Python's GIL (for CPU-bound tasks).
# -------------------------------------------------------------------

import concurrent.futures  # 🔁 Used for running concurrent code
import time  # ⏱️ To simulate delay and measure execution time

# 🔧 Function to simulate a task (like fetching from an API)
def fetch_data(name):
    print(f"📡 Fetching data for {name}...")  # Show which task is running
    time.sleep(2)  # Simulates a delay
    return f"✅ Data fetched for {name}"  # Returns result

# Sample data to run tasks in parallel
names = ['Alice', 'Bob', 'Charlie', 'David', 'Dan','Adam']

def main():
    start = time.time()  # ⏳ Start timer

    # 🔁 Create thread pool and run fetch_data for each name concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Use map() to apply fetch_data to all items in names in parallel
        results = executor.map(fetch_data, names)

        # 🔍 Print the results as they are completed
        for result in results:
            print(result)

    end = time.time()  # 🕒 End timer
    print(f"\n⏱️ Total Time Taken: {round(end - start, 2)} seconds")

# 🔰 Ensures the code only runs if executed directly
if __name__ == "__main__":
    main()
