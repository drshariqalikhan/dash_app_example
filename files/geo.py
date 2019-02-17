
from geopy.geocoders import Nominatim

def getCity(lat,lon):

    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.reverse("%s , %s"%(lat,lon))
    data = location.raw
    city = data.get('address').get('city')

    if city is None:
        print("search...")
        lat = lat - 0.5
        location = geolocator.reverse("%s , %s"%(lat,lon))
        data = location.raw
        city = data.get('address').get('city')
        if city is None:
            lat = lat + 1.5
            location = geolocator.reverse("%s , %s"%(lat,lon))
            data = location.raw
            city = data.get('address').get('city')
            if city is None:
                pass
            else:
                return city.split(' ')[0]
                print(city.split(' ')[0])
                print("front: %s"% city)
        else:
            return city.split(' ')[0]
            print(city.split(' ')[0])
            print("back: %s" % city)            
    else:
        return city.split(' ')[0]
        print(city.split(' ')[0])
        print("orig: %s" % city)




print(getCity(26.9,75.7))

# getCity(28.64,77.21)
