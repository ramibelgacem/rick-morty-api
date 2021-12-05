# rick-morty-api

# Requirement
python3.9+
postgresql
a new database

# ENv variables for postgresql connection
Create a file .env under rick-morty-api directory and put these variables with your values
DATABASE_USER=<your_database_user>
DATABASE_PASSWORD=<your_database_password>
DATABASE_HOST=<your_database_host>
DATABASE_PORT=<your_database_port>
DATABASE_NAME=<your_database_name>

pip install -r requirements.txt

uvicorn app.main:app --reload

python script/load.py



flake8