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
The linter used for this project is flake8