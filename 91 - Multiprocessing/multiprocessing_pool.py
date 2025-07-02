# -------------------------------------------------------------------
# 🔹 Multiprocessing with Pool in Python
# -------------------------------------------------------------------
# ✅ What is multiprocessing.Pool?
#    - A class that lets you parallelize function execution across multiple input values.
#    - Automatically manages worker processes behind the scenes.

# ✅ Why use Pool?
#    - Ideal for applying a function to a list of items using parallel workers.
#    - Easier syntax compared to manually managing multiple Process objects.

# ✅ Advantages:
#    - Simplifies code for parallel execution using map/apply functions.
#    - Automatically manages process creation and worker pool.
#    - Efficient for batch tasks (like multiple file downloads).

# ❌ Disadvantages:
#    - Less control over each individual process.
#    - Harder to debug than regular sequential code.
#    - Still uses more memory than multithreading.

# -------------------------------------------------------------------

import multiprocessing
import requests
import os

# 📥 Function to download an image (must be at the top level for Pool to work on Windows)
def download_file_pool(name):
    url = "https://picsum.photos/200/300"
    print(f"📥 Started downloading file{name}")
    response = requests.get(url)
    
    # Ensure directory exists
    os.makedirs("files", exist_ok=True)
    
    with open(f"files1/file{name}.jpg", "wb") as f:
        f.write(response.content)
    print(f"✅ Finished downloading file{name}")

# 🚀 Main function to setup and run Pool
if __name__ == "__main__":
    # 📌 Create a list of input values (file names or IDs)
    file_ids = [0, 1, 2, 3, 4]

    # 🧵 Create a Pool with number of worker processes (optional: default = CPU count)
    with multiprocessing.Pool(processes=5) as pool:
        # 🗂️ Map the function to input list → runs in parallel
        pool.map(download_file_pool, file_ids)

    print("🏁 All downloads completed using Pool.")
