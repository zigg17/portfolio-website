import json
from newsapi import NewsApiClient
import os

# Set up NewsAPI client
api_key = os.getenv('NEWS_API_KEY')

if not api_key:
    print("API Key not found! Make sure it's set in your environment variables.")
    exit(1)

newsapi = NewsApiClient(api_key=api_key)

# Fetch top headlines from the 'science' category
top_headlines = newsapi.get_top_headlines(language='en', page_size=6, category='science')

if top_headlines['status'] == 'ok':
    articles = top_headlines['articles']
    
    # Create a list of articles to store in JSON
    articles_list = []
    
    for i, article in enumerate(articles, start=1):
        # Gather relevant data
        title = article['title']
        url = article['url']
        published_at = article['publishedAt']
        author = article['author'] if article['author'] else "Unknown author"
        
        # Create an article dictionary
        article_dict = {
            'title': title,
            'url': url,
            'published_at': published_at,
            'author': author
        }
        
        # Append to the articles list
        articles_list.append(article_dict)

    # Save the list to a JSON file
    with open('txt-files/headlines.json', 'w') as json_file:
        json.dump(articles_list, json_file, indent=4)

    print("JSON file created: headlines.json")
else:
    print("Failed to retrieve headlines.")

