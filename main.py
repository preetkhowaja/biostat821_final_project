from fastapi import FastAPI
import uvicorn
import math
from imdb import IMDb
from bs4 import BeautifulSoup as SOUP
import re
import requests
import asyncio

app = FastAPI()


@app.get("/")
async def root():
    return {
        "Hello folks! In order to use the recommendation engine, type one of the following:"
        " Sad, Angr, Anticipating, Horror, Content, Motivated, or Bollywood"
    }


@app.get("/movie/string1")
async def movie(string1: str):
    ia = IMDb()
    name = string1
    emp_list = []
    search = ia.search_movie(name)
    for i in search:
        emp_list.append(i["title"])
    return emp_list


@app.get("/genre/string2")
async def genre(string2: str):
    ia = IMDb()
    info = ia.search_movie(string2)
    ID = info[0].movieID
    movie = ia.get_movie(ID)
    for genre in movie["genres"]:
        return genre


@app.get("/recommendation/emotion")
async def recommendation(emotion: str):

    if emotion == "Sad":
        urlhere = "https://www.imdb.com/list/ls002121036/, asc"

    # Angry -> Drama
    elif emotion == "Angry":
        urlhere = "https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc, asc"

    # Content ->
    elif emotion == "Content":
        urlhere = "http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc"

    # Anticipation/ Thriller
    elif emotion == "Anticipating":
        urlhere = "http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc"

    # Motivated
    elif emotion == "Motivated":
        urlhere = "http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc"

    # Horror
    elif emotion == "Horror":
        urlhere = "http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc"

    # Bollywood
    elif emotion == "Bollywood":
        urlhere = "https://www.imdb.com/list/ls009997493/, asc"

    # HTTP request to get the data
    response = requests.get(urlhere)
    data = response.text

    # Parsing the data using BeautifulSoup
    soup = SOUP(data, "lxml")

    # Extract movie titles from the data using regex
    title = soup.find("a", attrs={"href": re.compile(r"\/title\/")})
    
    a = title.text.strip()
    return a


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
