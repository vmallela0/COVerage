def searcher(county, category):
    from googlesearch import search
    query = county + " covid-19 " + category + " news"
    urls = []
    for url in search(
        query,
        tld="com",
        num=5,
        stop=5,
        pause=2
    ):
        urls.append(url)
    return urls

searcher("Santa Clara County", "Economy")
