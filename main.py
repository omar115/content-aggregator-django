import feedparser
feed = feedparser.parse('https://realpython.com/podcasts/rpp/feed')
podcast_title = feed.channel.title
print(podcast_title)
podcast_image = feed.channel.image['href']
print(podcast_image)