import webbrowser

def google_search(query):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(url)
    return f"Searching Google for: {query}"
