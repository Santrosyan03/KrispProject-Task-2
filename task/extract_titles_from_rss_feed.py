############
#
# Extract Titles from RSS feed
#
# Implement get_headlines() function. It should take a url of an RSS feed
# and return a list of strings representing article titles.
#
############

import feedparser


google_news_url = "https://news.google.com/news/rss"


def get_headlines(rss_url):
    """
    @returns a list of titles from the rss feed located at `rss_url`
    """
    feed = feedparser.parse(rss_url)
    titles = []
    for entry in feed.entries:
        titles.append(entry.title)

    return titles


if __name__ == "__main__":
    print(get_headlines(google_news_url))
