from bs4 import BeautifulSoup 
import requests
import json

def parse_page():

    res_list = []
    url = "https://singpromos.com/bydate/ontoday/"

    
    while url :

    
        r= requests.get(url)
        # print(r.status_code)

        s = BeautifulSoup(r.content,features="lxml")

        # deals = s.select(".tabs1Content .mh-loop-item")
        deals = s.select(".tabs1Content .mh-loop-title a")
        #iterate over Blocks
        for deal in deals:


            try:

                #get image
                # deal_images = deal.select(".mh-loop-thumb")
                # deal_image = deal_images[0].find('img')['src']

                
            #     #get Title
                # deal_excerpt = deal.select('.mh-excerpt')
                # deal_title_text = deal_excerpt[0].text

            #     #get start date
            #     # meta = deal.select(".mh-meta mh-loop-meta")
            #     # print(len(meta))

                #get link
                # deal_data = deal.select('.tabs1Content a')
                # deal_data_url = deal_data[0]['href']
                deal_data_url = deal['href']
                #scrape data from deal_data_url
                secondr = requests.get(deal_data_url)
                ss = BeautifulSoup(secondr.content,'lxml')
                deal_start_date = ss.select('tr:nth-child(1) td:nth-child(2)')[0].text
                deal_end_date = ss.select('tr:nth-child(1) td~ td')[0].text 
                deal_title_text =  ss.select('.entry-title')[0].text
                deal_image  = ss.select('.entry-thumbnail img')[0]['src']
                deal_tags = ss.select('.entry-meta-categories a')[0].text
                data = {
                    'thumb_img': deal_image,
                    'Title':deal_title_text,
                    'start_date':deal_start_date,
                    'end_date':deal_end_date,
                    'tags':deal_tags
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

# parse_page()