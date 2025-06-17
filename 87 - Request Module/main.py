# ----------------------------------------------------------
# 🌐 Python requests Module - Beginner Guide
# ----------------------------------------------------------

# What is it?
# ➤ Used to send HTTP requests like GET, POST, PUT, DELETE.
# ➤ Great for web APIs, scraping, automation, testing, etc.


import requests  # Import the requests module

# ----------------------------------------------------------
# ✅ 1. Sending a GET Request
# ----------------------------------------------------------

print("🔹 Sending a GET request to https://jsonplaceholder.typicode.com/posts")

response = requests.get("https://jsonplaceholder.typicode.com/posts")

# Check status code
print("Status Code:", response.status_code)

# Print first 2 items from JSON response
if response.status_code == 200:
    data = response.json()  # Convert response to JSON
    print("First two posts:")
    for post in data[:2]:
        print(f"ID: {post['id']} | Title: {post['title']}")
else:
    print("Failed to fetch data")

# ----------------------------------------------------------
# ✅ 2. Sending a POST Request (create new resource)
# ----------------------------------------------------------

print("\n🔹 Sending a POST request...")

post_data = {
    "title": "Hello API",
    "body": "This is a test post.",
    "userId": 1
}

post_response = requests.post("https://jsonplaceholder.typicode.com/posts", json=post_data)
print("Status Code:", post_response.status_code)
print("Response JSON:", post_response.json())

# ----------------------------------------------------------
# ✅ 3. Sending a PUT Request (update a resource)
# ----------------------------------------------------------

print("\n🔹 Sending a PUT request (update post ID 1)...")

put_data = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated body content.",
    "userId": 1
}

put_response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=put_data)
print("Status Code:", put_response.status_code)
print("Updated Resource:", put_response.json())

# ----------------------------------------------------------
# ✅ 4. Sending a DELETE Request
# ----------------------------------------------------------

print("\n🔹 Sending a DELETE request for post ID 1...")

delete_response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print("Status Code:", delete_response.status_code)
if delete_response.status_code == 200 or delete_response.status_code == 204:
    print("✅ Post deleted successfully.")
else:
    print("❌ Failed to delete post.")

# ----------------------------------------------------------
# 📝 Summary:
# GET    → requests.get(url)
# POST   → requests.post(url, json=data)
# PUT    → requests.put(url, json=data)
# DELETE → requests.delete(url)
# ----------------------------------------------------------

print("\n✅ All requests completed.")
