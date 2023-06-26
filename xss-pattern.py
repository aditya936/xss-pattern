import sys

def filter_urls(urls, patterns):
    vulnerable_urls = []

    for url in urls:
        for pattern in patterns:
            if pattern in url:
                vulnerable_urls.append(url)
                break

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
    "msg=",
    "error=",
    "categoryid=",
    "key=",
    "l=",
    "begindate=",
    "enddate="
]

filtered_urls = filter_urls(urls, patterns)

# Print the filtered URLs
for url in filtered_urls:
    print(url)
