#!/usr/bin/python3
import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)

        print(got_dj["name"])

        for chr_book in got_dj["books"]:
            ## display the booksof character
            print(f"Book Name: {chr_book}")

	for chr_algnc in got_dj["allegiances"]:
            ## display the allegiances of character
            print(f"Book Name: {chr_algnc}")
                        

if __name__ == "__main__":
        main()
