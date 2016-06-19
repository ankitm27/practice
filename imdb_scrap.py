import requests
from bs4 import BeautifulSoup
import re
var = 0
link = 1
check = 1
while check:
    #url = "http://www.imdb.com/search/title?sort=year&start=link&title_type=feature&year=2011,2011"
    try:
        url = "http://www.imdb.com/search/title?sort=year&start="+str(link)+"&title_type=feature&year=2011,2015"
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text)
        main = soup.find("div",{"id":"main"})
        result =  main.find("table",{"class":"results"})
        container = result.find_all("tr",{"class":"odd detailed"})
        for items in container:
            print "MOVIE "+str(var)
            description = items.find("td",{"class":"title"})
            print "movie name -" +description.find("a").string
            print "movie year -"+description.find("span",{"class":"year_type"}).string
            print "movie ratings -"+description.find("div",{"class":"user_rating"}).find("div",{"class":"rating rating-list"})["title"].split(' ')[3].split('/')[0]
            genres = description.find("span",{"class":"genre"}).find_all("a")
            list = []
            for genre in genres:
                genre = str(genre.string)
                list.append(genre)
            print "Genre - "+str(list)
            var = var +1
    
        container = result.find_all("tr",{"class":"even detailed"})
        for items in container:
            print "MOVIE "+str(var)
            description = items.find("td",{"class":"title"})
            print "movie name -" +description.find("a").string
            print "movie year -"+description.find("span",{"class":"year_type"}).string
            print "movie ratings -"+description.find("div",{"class":"user_rating"}).find("div",{"class":"rating rating-list"})["title"].split(' ')[3].split('/')[0]
            genres = description.find("span",{"class":"genre"}).find_all("a")
            list = []
            for genre in genres:
                genre = str(genre.string)
                list.append(genre)
            print "Genre - "+str(list)
            var = var +1



    except:
        pass     
    try:
        fetch_link = main.find("span",{"class":"pagination"}).find_all("a")
        list = []
        for next in fetch_link:
            next = re.sub(r'[^\x00-\x7F]',' ', next.string)
            next = next.strip()
            list.append(next)
        if len(list) == 1:
            list.append("dumpy_data")
        if list[0] == "Next" or list[1] == "Next":
            link = link + 50
        else:
            check = 0    
  

    except:
        link = link +50
