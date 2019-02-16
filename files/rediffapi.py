from bs4 import BeautifulSoup 
import requests
import json

def getNewsUpdates():

    all_article_List =[]
    url = "https://realtime.rediff.com/getresult/all/influenza%20deaths/0?output=json"
    r= requests.get(url)
    json_data = json.loads(r.text)

    try:

        all_clusters = json_data.get("rediffnews").get("news").get("cluster")

        for cluster in all_clusters:
            # print(cluster.get('numarticles'))
            article_List = cluster.get('article')
            for article in article_List:

                # print (article.get('title'))
                title = article.get('title')
                descrip = article.get('description')
                article_url = article.get('url')
                imageurl = article.get('imageurl')
                source = article.get('source')
                imageheight = article.get('imageheight')
                imagewidth = article.get('imagewidth')
                article_date = article.get('harvesttime')

                data = {
                    'title':title,
                    'descrip':descrip,
                    'article_url':article_url,
                    'imageurl':imageurl,
                    'imageheight':imageheight,
                    'imagewidth':imagewidth,
                    'source':source,
                    'article_date':article_date
                }
                print(data)
                all_article_List.append(data)
    except:
        pass
    
    with open('newsdata.json','w')as outfile:
        json.dump(all_article_List,outfile)                
    # print(len(all_article_List))        



# getNewsUpdates()
