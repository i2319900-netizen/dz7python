import requests

# Задание 1: первые 5 постов из публичного API JSONPlaceholder
response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()

for post in posts[:5]:
    print(post["title"])
    print(post["body"])
    print("-" * 40)
