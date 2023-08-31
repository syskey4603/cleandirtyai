import geocoder
g = geocoder.ip('me')
print("http://www.google.com/maps/place/" + str(g.latlng[0]) + "," + str(g.latlng[1]))