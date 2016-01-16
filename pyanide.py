import requests
from bs4 import BeautifulSoup
import urllib.request
import random
import sys
# Importing required libraries
def main():
    print("Welcome to the Cyanide and Happiness comic downloader")
    print("Enter number to download a specific comic")
    print("Enter random to download a random comic")
    print("Enter latest to download the latest comic")
    print("Enter anything else to exit")

    # Asking the user what action they want to perform

    user_input = input(">>>").lower()
    if user_input == "number":
        comic_no = input("Enter comic number")
    elif user_input == "random":
        comic_no = str(random.randint(1,4180))
    elif user_input == "latest":

        comic_no = "latest"
    else:
        print("Enter proper input. (random/latest/number)")
        sys.exit()

    # Getting the comic denoted by the comic_no

    url = "http://explosm.net/comics/" + comic_no + "/"

    request = requests.get(url)

    # Checking if the URL exists, and downloading it if it does. If it doesn't, the program displays an error message

    if request.status_code == 200:
        request = request.content
        soup = BeautifulSoup(request,"html.parser")

        #Finding all tags with the id main-comic and getting the value of their src attribute.

        a = soup.find(id="main-comic")

        src = a["src"]
        src = "http://" + src[2:]
        print("Saving image.....")
        urllib.request.urlretrieve(src,comic_no+ ".png")
    else:
        print("Please enter proper comic numbers. (Latest comic is 4180)")
if __name__ =="__main__":
    main()
