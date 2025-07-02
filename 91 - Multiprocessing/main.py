# -------------------------------------------------------------------
# 🔹 Multiprocessing in Python
# -------------------------------------------------------------------
# ✅ What is it?
#    - A Python module that allows parallel execution of code using multiple CPU cores.
#    - It bypasses the Global Interpreter Lock (GIL), making it ideal for CPU-bound tasks.

# ✅ Why use it?
#    - To run CPU-intensive tasks in true parallelism (not just concurrency like threads).
#    - For heavy computation or downloading/uploading tasks that can run independently.

# ✅ Advantages:
#    - Uses multiple CPU cores → true parallel execution.
#    - Can significantly reduce execution time for CPU-bound tasks.
#    - Avoids GIL limitation (unlike threading).

# ❌ Disadvantages:
#    - Processes consume more memory than threads.
#    - Inter-process communication is more complex than multithreading.
#    - Starting a new process has more overhead than starting a thread.

# -------------------------------------------------------------------

import multiprocessing  # Used for spawning independent processes
import requests         # Used to make HTTP requests

# 📥 Function to download an image from a URL
def download_file(url, name):
    print(f"📥 Started downloading {name}")
    response = requests.get(url)  # Sends GET request to download image
    open(f"files/file{name}.jpg", "wb").write(response.content)  # Writes image to disk
    print(f"✅ Finished downloading {name}")

# 🚀 Main program entry point
if __name__ == "__main__":
    url = "https://picsum.photos/200/300"  # Sample image API (generates random image)
    processes = []  # List to keep track of all spawned processes

    # 🔁 Create and start 5 separate processes for downloading
    for i in range(5):
        p = multiprocessing.Process(target=download_file, args=[url, i])
        p.start()          # Starts the process (runs in parallel)
        processes.append(p)  # Store for later joining

    # ⏳ Wait for all processes to finish
    for p in processes:
        p.join()

    print("🏁 All downloads completed.")
