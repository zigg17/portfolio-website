from newsapi import NewsApiClient
import os

api_key = os.getenv('NEWS_API_KEY')

if not api_key:
    print("API Key not found! Make sure it's set in your environment variables.")
    exit(1)

newsapi = NewsApiClient(api_key=api_key)

top_headlines = newsapi.get_top_headlines(language='en', page_size=6, category='science')

if top_headlines['status'] == 'ok':
    articles = top_headlines['articles']
    for i, article in enumerate(articles, start=1):
        title = article['title']
        description = article['description'] if article['description'] else "No description available."

        truncated_description = description[:50]
        if len(description) > 50:
            truncated_description += '...'

        print(f"Headline {i}: {title}")
        print(f"URL: {article['url']}")
        print(f"Image URL: {article['urlToImage']}")
        print(f"Published At: {article['publishedAt']}")
else:
    print("Failed to retrieve headlines.")