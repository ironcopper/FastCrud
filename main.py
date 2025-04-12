from fastapi import FastAPI, Body

app = FastAPI()


movies_db = [
    {
        "id": 1,
        "director": "Christopher Nolan",
        "movie_title": "Inception",
        "genre": "Sci-Fi"
    },
    {
        "id": 2,
        "director": "Steven Spielberg",
        "movie_title": "Jurassic Park",
        "genre": "Adventure"
    },
    {
        "id": 3,
        "director": "James Cameron",
        "movie_title": "Avatar",
        "genre": "Sci-Fi"
    }
]

@app.get("/")
async def hello():
    return {"msg": "Welcome to the Movie Catalog API"}

@app.get("/movies")
async def get_all_movies():
    return movies_db

# Search by movie title (path parameter)
@app.get("/movies/{movie_title}")
async def get_movie_by_title(movie_title: str):
    for movie in movies_db:
        if movie.get('movie_title').casefold() == movie_title.casefold():
            return movie

# This route would clash with the above
@app.get("/movies/{movie_id}")
async def get_movie(movie_id):
    for movie in movies_db:
        if movie.get('id') == movie_id:
            return movie

# so we use a different path
@app.get("/movies/byid/{movie_id}")
async def get_movie_by_id(movie_id: int):
    for movie in movies_db:
        if movie.get('id') == movie_id:
            return movie

# Search by genre (query parameter)
@app.get("/movies/")
async def get_movies_by_genre(genre: str):
    movies_to_return = []
    for movie in movies_db:
        if movie.get('genre').casefold() == genre.casefold():
            movies_to_return.append(movie)
    return movies_to_return

# Search by director and genre (path + query)
@app.get("/movies/{director}/")
async def get_movies_by_director_and_genre(director: str, genre: str):
    return [
        movie for movie in movies_db
        if movie.get('director').casefold() == director.casefold() and movie.get('genre').casefold() == genre.casefold()
    ]

# Create a new movie (POST)
@app.post("/movies/create_movie")
async def create_movie(new_movie=Body()):
    movies_db.append(new_movie)

# Update an existing movie (PUT)
@app.put("/movies/update_movie")
async def update_movie(updated_movie=Body()):
    for index in range(len(movies_db)):
        if movies_db[index].get('id') == updated_movie.get('id'):
            movies_db[index] = updated_movie

# Delete a movie (DELETE)
@app.delete("/movies/delete_movie/{movie_id}")
async def delete_movie(movie_id: int):
    for index in range(len(movies_db)):
        if movies_db[index].get('id') == movie_id:
            movies_db.pop(index)
            break
