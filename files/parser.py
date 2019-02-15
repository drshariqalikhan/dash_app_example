from bs4 import BeautifulSoup 
import requests
import json

def parse_page():

    res_list = []
    url = "https://singpromos.com/bydate/ontoday/"

    
    while url :

        # print(url)
    
        r= requests.get(url)
        s = BeautifulSoup(r.content,features="lxml")

        deals = s.select(".tabs1Content .mh-loop-item")
        #iterate over Blocks
        for deal in deals:

            try:
                #get image
                deal_images = deal.select(".mh-loop-thumb")
                deal_image = deal_images[0].find('img')['src']

                
            #     #get Title
                deal_excerpt = deal.select('.mh-excerpt')
                deal_title_text = deal_excerpt[0].text

            #     #get start date
            #     # meta = deal.select(".mh-meta mh-loop-meta")
            #     # print(len(meta))

            #     #get link
            #     # deal_title = deal.select(".mh-loop-title a")
            #     # deal_title_url = deal_title[0]['href']
            #     # headline_url = headline["href"]
            #     # headline_url = url+headline_url
            
                data = {
                    'thumb_img': deal_image,
                    'Title':deal_title_text,
            #         # 'Link':deal_title_url
                }

                # print (data)
                res_list.append(data)
                
                
            except:
                pass    

        if s.select('.next'):
            url = s.select('.next')[0]['href']
            # print(url)
        else:
            with open('apidata.json','w')as outfile:
                json.dump(res_list,outfile)
            break    
            # return res_list
