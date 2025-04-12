import requests
from bs4 import BeautifulSoup
import csv 

# source = requests.get("https://books.toscrape.com/").text
source = requests.get("https://books.toscrape.com/catalogue/category/books/travel_2/index.html").text
# print(source)
soup = BeautifulSoup(source,'lxml')
# print(soup.prettify())

csv_file = open("TravelBook_Scraper.csv",'w',newline="", encoding="utf-8")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','product_link','price'])

for article in  soup.find_all("article", class_="product_pod"):
    # print(article.h3.text)
    title = article.h3.a['title']
    # print(title) # to extract the attribute 
    url = article.h3.a['href']
    product_url = "https://books.toscrape.com/"+url
    # print(product_url) # https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
    price = article.find("p", class_ = "price_color").text
    print(price)
    # print()

    csv_writer.writerow([title, product_url, price])

csv_file.close() # as we haven't used the context manager

# ---------to extract the youtube video id from the iframe embedded link and to create a youtube link via video_id.-----------------
iframe_vid_src = "https://www.youtube.com/embed/K8L6KVGG-7o?version=3&amp;rel=1&amp;fs=l&amp;autohide=2&amp;showsearch=0&amp;showinfo=l&amp;iv_load_policy=1&amp;wmode=transparent"
vid_id = iframe_vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
# print(vid_id)
yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)

# #--------- if some details are missing in the web page then our scaper might break so need to add a try except block  -------------
# iframe_vid_src = "https://www.youtube.com/embed/K8L6KVGG-7o?version=3&amp;rel=1&amp;fs=l&amp;autohide=2&amp;showsearch=0&amp;showinfo=l&amp;iv_load_policy=1&amp;wmode=transparent"
# for article in  soup.find_all("article", class_="product_pod"):
#     try: # if url is missing in the website for some product it might break our scaper so adding try catch block can prevent that
#         # print(article.h3.text)
#         vid_id = iframe_vid_src.split('/')[4]
#         vid_id = vid_id.split('?')[0]
#         # print(vid_id)
#         yt_link = f'https://youtube.com/watch?v={vid_id}' # youtube link is set only if it is available 
#     except Exception as e:
#         yt_link = None # esle it will set as None 
#     print(yt_link)