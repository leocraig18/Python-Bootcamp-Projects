import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/list/ls068718974/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="lister-item-header")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles

with open("/Users/User101/PycharmProjects/45-100-movies/movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}")

