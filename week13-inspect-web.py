#!/usr/bin/env python3
import bs4

notPurple = open('my_web_fie.html')
purpleSoup = bs4.BeautifulSoup(notPurple, 'html.parser')
#Print out the title page:

print(f"\nTitle of the document:\n")
print(purpleSoup.find("title"))

#Retrieving the links: (a) tags
links = purpleSoup.select('a')
print("\nThese are the links on the page:")
print(f"\n{links}\n")

links2 = str(links)
print(links2[10:17:1])
print(links2[40:50:1])
