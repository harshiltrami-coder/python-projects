import requests

query = input("What type of news are you interested in today: ")

api = "My-api-key"

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-10-01&sortBy=publishedAt&apiKey={api}"

r = requests.get(url)
data = r.json()

if data.get("status") != "ok":
    print("API Error:", data.get("message"))
else:
    articles = data["articles"]

    for index, article in enumerate(articles):
        print(index + 1, article["title"], article["url"])
        print("\n*****************************************\n")