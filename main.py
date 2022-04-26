from fastapi import FastAPI
import uvicorn
import math
from imdb import IMDb

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello folks!"}


@app.get("/movie/lion king")
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


# @app.get("/recommendation/movie")

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
