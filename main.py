# Program accesses website content and searches through HTML tags to find data for the program. Program then creates a Python dataframe out of a list of dictionaries. More specifically, with each iteration of the boat_data function, key values are added to a dictionary, so, in this program, there will be 4 key-value pairs added in one iteration. For example, {"price": "189,000", "location": "San Diego", etc}. Each listing will have its own dictionary. The dictionaries will then be stored in a list.

from bs4 import BeautifulSoup
import requests
#import textwrap
#import pandas


def main():
    """Accesses the website content. Note that search parameters on yachtfinder.com were set to include boats from 1999 to present, and only those on the west side of the US and HI"""

    requested_website = requests.get("https://www.yachtworld.com/core/listing/cache/searchResults.jsp?cit=true&slim=quick&ybw=&sm=3&searchtype=homepage&Ntk=boatsEN&Ntt=&is=&man=&hmid=0&ftid=0&enid=0&type=%28Sail%29&fromLength=32&toLength=36&fromYear=1999&toYear=2019&fromPrice=0&toPrice=&luom=126&currencyid=100&city=&rid=107&rid=108&pbsint=&boatsAddedSelected=-1")

    search_page = requested_website.content
    search_page_readable = BeautifulSoup(search_page, "html.parser")
    boats_found = search_page_readable.find_all("div",{"class":"information"})

    boat_data(boats_found)


def boat_data(boats_found):
    """Searches through HTML tags to find data for the program"""

    #### Finding Individual Elements
    # price
    #print(boats_found[5].find("div",{"class": "price"}).text.replace("\n","").replace("*","").replace(" ",""))

    # make and model and length
    #print(boats_found[5].find("div",{"class": "make-model"}).text.strip().replace(" ", ""))
    #########################

    for boat in boats_found:
        # Price
        print(boat.find("div",{"class": "price"}).text.replace("\n","").replace("*","").replace(" ",""))

        # length, make and model
        print(boat.find("div",{"class": "make-model"}).text.strip().replace(" ", "").replace("\n", " "))

        # Length only
        #print(boat.find("div",{"class": "make-model"}).find("span").text.strip())

        # location
        print(boat.find("div",{"class": "location"}).text.strip().replace("  ", "").replace("\n", " "))

        # Broker
        print(boat.find("div",{"class": "broker"}).text.strip())

        print("---")
main()



# use extract() to remove unwanted tag before you get the text, so I can have boat type and length as separate variables - just not sure how to do this yet - https://www.crummy.com/software/BeautifulSoup/bs4/doc/
        #print(boat.find("span",{"class": "length feet"}).text.replace("\n","").replace(" ",""))

        #boat_length = boat.find("a").text
        #unwanted = boat.find("span",{"class": "length feet"})
        #print(boat_length)




'''
l=[]
base_url="https://www.yachtworld.com/core/listing/cache/searchResults.jsp?sm=3&searchtype=homepage&Ntk=boatsEN&ftid=0&Ns=PBoat_sortByPriceAsc%7C0&enid=0&toYear=2018&hmid=0&type=%28Sail%29&boatsAddedSelected=-1&slim=quick&currencyid=100&fromPrice=0&luom=126&rid=107&rid=108&toLength=45&fromLength=32&cit=true&fromYear=1990&ps=50&No="

for page in range(0,200,50):
    print(base_url+str(page))
    r=requests.get(base_url+str(page))
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"information"})

    for item in all:
        d={}
        d["Sailboat"]=textwrap.shorten(item.find("div",{"class":"make-model"}).text,width=50)
        if item.find("div",{"class":"price"}).text.replace("\n","").replace("*","").replace(" ","") == 'Call$(".currNote").hide()':
            d["Price"]=("Call for current price")
        else:
            d["Price"]=item.find("div",{"class":"price"}).text.replace("\n","").replace("*","").replace(" ","")
        d["Location"]=textwrap.shorten(item.find("div",{"class":"location"}).text,width=50)
        d["Broker"]=textwrap.shorten(item.find("div",{"class":"broker"}).text,width=50)
        l.append(d)

df=pandas.DataFrame(l)
df.to_csv("West Coast Sailboats for Sale From Yacht Finder.csv")
'''
