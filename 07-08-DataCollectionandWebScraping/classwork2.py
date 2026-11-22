import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url, timeout=15)
response.raise_for_status()   # Check if the request was successful

posts = response.json()  # Parse the JSON response
for post in posts[:5]:  # Print the first 5 posts
    print(f"Post ID: {post['id']}, Title: {post['title']}")