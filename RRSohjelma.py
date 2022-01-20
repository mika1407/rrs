# Yle pääuutiset RSS ohjelma.
# Tee komento (pip install feedparser), datetime kuuluu Pythoniin. 
# Tämä komento toimi itsellä: C:\Users\konea\AppData\Local\Programs\Python\Python310\Scripts>pip install feedparser
# Värillisiin tulosteisiin: pip install termcolor

from calendar import weekday
import feedparser
import datetime
from termcolor import colored

# lokin kirjoitus
def kirjoita_lokia(parametri):
    aikaleima = datetime.datetime.today()
   
    tiedosto = open("yleuutiset.txt", "a")
    rivi = str(aikaleima) + " " + parametri
   
    tiedosto.write(rivi + "\r")
    tiedosto.close()

url = "https://feeds.yle.fi/uutiset/v1/majorHeadlines/YLE_UUTISET.rss"
feed = feedparser.parse(url)

day2 = datetime.datetime.today()
day = datetime.datetime.today().weekday()

weekday = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]
print('\n')
print(colored('YLE pääuutiset', 'yellow'))
print(f'Tänään on {weekday[day]}')
print(day2)
print('\n')

print(colored(feed.feed.title , "yellow"))

feed_entries = feed.entries

for entry in feed.entries:

    article_title = entry.title
    article_link = entry.link
    article_published_at = entry.published # Unicode string
    article_published_at_parsed = entry.published_parsed # Time object
    content = entry.summary

    print ("{}[{}]".format(article_title, article_link))
    print ("Julkaistu: {}".format(article_published_at)) 
    print(colored("Sisältö: {}".format(content), "cyan"))


uutinen = feed.entries[day].summary_detail.value
#print(uutinen)
kirjoita_lokia(f"Tänään uutisena : {uutinen} ")

