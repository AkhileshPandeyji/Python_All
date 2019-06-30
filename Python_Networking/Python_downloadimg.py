import urllib.request
import urllib.error

url = "https://upload.wikimedia.org/wikipedia/commons/7/7b/Deepwater_Horizon_oil_spill_-_May_24%2C_2010_-_with_locator.jpg "

try:
    urllib.request.urlretrieve(url,"myimage.jpeg")
except urllib.error.HTTPError:
    print("Such url does not exist")

