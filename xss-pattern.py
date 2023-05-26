import sys

def filter_urls(urls, patterns):
    vulnerable_urls = []

    for index, url in enumerate(urls, start=1):
        for pattern in patterns:
            if pattern in url:
                vulnerable_urls.append(url)
                break
        
        # Print progress message
        print(f"Processed URL {index}/{len(urls)}")

    return vulnerable_urls

# Read URLs from standard input
urls = [line.strip() for line in sys.stdin.readlines()]

patterns = [
    "q=",
    "s=",
    "search=",
    "lang=",
    "keyword=",
    "query=",
    "page=",
    "keywords=",
    "year=",
    "view=",
    "email=",
    "type=",
    "name=",
    "p=",
    "callback=",
    "jsonp=",
    "api_key=",
    "api=",
    "password=",
    "email=",
    "emailto=",
    "token=",
    "username=",
    "csrf_token=",
    "unsubscribe_token=",
    "id=",
    "item=",
    "page_id=",
    "month=",
    "immagine=",
    "list_type=",
    "url=",
    "terms=",
    "categoryid=",
    "key=",
    "l=",
    "begindate=",
    "enddate="
]

filtered_urls = filter_urls(urls, patterns)

for url in filtered_urls:
    print(url)
