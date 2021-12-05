# Welcome to Rick and Morty API!

This API allow us to manipulate **Episodes**, **Characters** and **Comments** data.

## Requirements
- python (3.9+)
- postgresql
- Create a new database

## Setup
- Create a new directory, e.g api_workspace and move into it
- Create a new python environment
```
python -m venv rmapi-env
```
- Activate it
```
source rmapi-env/bin/activate
```
- Clone this repository and navigate into it
- Install requirements
```
pip install -r requirements.txt
```
- Create a new file named **.env**, to put your database connection parameters
```
DATABASE_USER=<your_database_user>
DATABASE_PASSWORD=<your_database_password>
DATABASE_HOST=<your_database_host>
DATABASE_PORT=<your_database_port>
DATABASE_NAME=<your_database_name>
```
- Run uvicorn server
```
uvicorn app.main:app --reload
```
- Load data to your database by running the script
```
python script/load.py
```

## How to use it
Open the navigator and access to this URL: http://0.0.0.0:8000/docs, you will find all the APIs available

## Misc
- The linter used for this project is flake8
- Pytest is user for testing

## API Documentation
**Users**
- POST --> /user/: to create a new user
    - Return the new created user
- GET --> /user/{user_id}: to read a user
    - Return the requested user
    - Return 404 not found status if the user does not exist
- PUT --> /user/{user_id}: to update a user
    - Return the updated user
    - Return 404 not found status if the user does not exist
- DELETE --> /user/{user_id}: to delete a user
    - Return 404 not found status if the user does not exist

**Comment**
- GET --> /comment/: to read comments
    - Return comments based on limit and offset query parameters
- GET --> /comment/{comment_id}: to read a comment
    - Return the requested comment
    - Return 404 not found status if the comment does not exist
- PUT --> /comment/{comment_id}: to update a comment
    - Return the updated comment
    - Return 404 not found status if the comment does not exist
- DELETE --> /comment/{comment_id}: to delete a comment
    - Return 404 not found status if the comment does not exist

**Episode**
- GET --> /episode/: to read episodes
    - Return all the episodes
- POST --> /episode/{episode_id}/comment: to create a new comment for the episode passed in the path parameter
    - Return the new created comment
    - Return 404 not found status if the episode does not exist

**Character**
- GET --> /character/: to read character
    - Return characters based on limit and offset query parameters, we can also filtering by name, status and gender
- POST --> /character/{character_id}/comment: to create a new comment for the character passed in the path parameter
    - Return the new created comment
    - Return 404 not found status if the character does not exist