from bs4 import BeautifulSoup
import requests
import mysql.connector

from priceInfo import PriceInfo

urlToId = {
    "https://www.iga.net/en/search?k=": PriceInfo("id", "body_0_main_1_GrocerySearch_TemplateResult_SearchResultListView_MansoryPanel", "item-product", "price text--strong", "span", "string", "js-ga-productimage", "https://www.iga.net"), # %20 for spaces
    #"https://www.maxi.ca/search?search-bar=": PriceLocation(), # %20 for spaces
    "https://www.superc.ca/en/search?filter=": PriceInfo("class", "products-tiles-list", "products-tile-list__tile", "pi--main-price", "div", "data-main-price", "product-details-link", "https://www.superc.ca") # %20 for spaces
}

db = mysql.connector.connect(
    #change these parameters later
    host="localhost",
    user="root",
    password="",
    database="conuhackathon"
)

cursor = db.cursor()

cursor.execute("SELECT fruit FROM fruitsandvegetables")

fruitAndVegetableList = cursor.fetchall()

for i in range(len(fruitAndVegetableList)):
    fruitAndVegetableList[i] = fruitAndVegetableList[i][0]

fruitAndVegetableSet = set(fruitAndVegetableList)

print(fruitAndVegetableList)

def toURL(fruit):
    return fruit.replace(" ", "%20")


for fruit in fruitAndVegetableList:

    bestPrice = 0
    bestPriceUrl = None

    for url in urlToId.keys():
        res = requests.get(url+toURL(fruit))
        print(url+toURL(fruit))

        doc = BeautifulSoup(res.text, "html.parser")

        priceLoc = urlToId.get(url)

        print(priceLoc.itemListClass)

        itemList = doc.find_all("div", class_=priceLoc.itemClass)

        print("SFDDSFA "+ str(len(itemList)))

        priceTags = doc.find_all("div", class_=priceLoc.priceLocationClass)
        priceLinks = doc.find_all("a", class_=priceLoc.linkLocationClass)


        #rn for super c only one item in itemList (should be all on page)
        #print(len(itemList))

        for item in itemList:
            curPriceTag = item.find(priceLoc.priceTag, class_=priceLoc.priceLocationClass)

            if priceLoc.priceAttribute == "span":
                curPrice = curPriceTag.text
            else:
                curPrice = curPriceTag[priceLoc.priceAttribute]

            #print(curPrice)

            if bestPrice == 0 or float(curPrice) < float(bestPrice):
                bestPrice = curPrice
                #print(priceLoc.baseLink + priceLinks[priceTags.index(curPriceTag)]['href'])
                #bestPriceUrl = priceLoc.baseLink + priceLinks[priceTags.index(curPriceTag)]['href']
                bestPriceUrl = priceLoc.baseLink + item.find("a", class_=priceLoc.linkLocationClass)['href']

    print(bestPrice)
    print(bestPriceUrl)

    cursor.execute("UPDATE fruitsandvegetables SET bestPrice=%s, bestPriceUrl=%s WHERE fruit=%s", (bestPrice, bestPriceUrl, fruit))
    db.commit()

