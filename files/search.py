import os
import json

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_uri = os.path.join(SITE_ROOT,'newsdata.json')
json_dict_list = json.load(open(json_uri))


def searchFor(searchString):
     res_list =[]
     for dict in json_dict_list:
          value = dict.get("title")
          searchString = searchString.upper()
          value = value.upper()
          if searchString in value:
               # print(value)
               res_list.append(dict)
     return res_list               
     
# l = searchFor("KFC")
# print(len(l))
# for item in l:
#      print(item)