
from geopy.geocoders import Nominatim

def getCity(lat,lon):
    dat = {}
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.reverse("%s , %s"%(lat,lon))
    data = location.raw
    city = data.get('address').get('city')
    city = splitcity(city)
    state = data.get('address').get('state')
    # country = data.get('address').get('city')
    # print(data.get('address'))
    if(city != None):

        dat['city'] = city
        
    if(state != None):
        dat['state']= state
        
    # if(country != None):
    #     dat['country']= country

    # print(dat)
    return dat

#     if city is None:
#         # print("search...")
#         lat = str(float(lat) - 0.2)
#         location = geolocator.reverse("%s , %s"%(lat,lon))
#         data = location.raw
#         city = data.get('address').get('city')
#         if city is None:
#             lat = str(float(lat) + 0.4)
#             location = geolocator.reverse("%s , %s"%(lat,lon))
#             data = location.raw
#             city = data.get('address').get('city')
#             if city is None:
#                 return "no data"
#             else:
#                 return splitcity(city)
#                 # print(splitcity(city))
#                 # print("front: %s"% city)
#         else:
#             return splitcity(city)
#             # print(splitcity(city))
#             # print("back: %s" % city)            
#     else:
#         return splitcity(city)
#         # print(splitcity(city))
#         # print("orig: %s" % city)


def splitcity(city):
    if len(city.split(' ')) >  2:
        return city.split(' ')[0]
    else:
        return city    




# print(getCity(26.9,75.7))

# getCity(1.4927,103.7414)
