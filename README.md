# FastAPI Movie Catalog API

A simple RESTful API built using **FastAPI** for managing a movie catalog. Supports operations like creating, retrieving, updating, and deleting movie records using both path and query parameters.

## Features

- Get all movies
- Get movie by title or ID
- Get movies by genre or director
- Create a new movie
- Update an existing movie
- Delete a movie

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

##  Installation 

```bash
# Clone the repo
git clone https://github.com/ironcopper/FastCrud.git
cd FastCrud

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload
```