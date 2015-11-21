
from googlemaps import Client as GoogleMaps
gmaps = GoogleMaps(api_key="YOUR KEY")
address = 'Constitution Ave NW & 10th St NW, Washington, DC'
lat, lng = gmaps.address_to_latlng(address)
print lat, lng