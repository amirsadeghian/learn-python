
import urllib.request
url='https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A34.15028278757794%2C%22south%22%3A31.402703015751616%2C%22east%22%3A-94.93765252343749%2C%22west%22%3A-99.25527947656249%7D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A150000%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A763%7D%2C%22lot%22%3A%7B%22min%22%3A217800%2C%22max%22%3Anull%2C%22units%22%3Anull%7D%7D%2C%22isListVisible%22%3Atrue%2C%22category%22%3A%22cat1%22%2C%22mapZoom%22%3A8%7D'
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"
urllib._urlopener = AppURLopener()
response = urllib._urlopener.open(url)