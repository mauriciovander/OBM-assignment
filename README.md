# OBM-assignment

# Create a virtual environment and install dependencies

```
python3 -m venv env
source env/bin/activate 
pip install --upgrade pip
pip install -r requirements.txt
```


## Install postgreSQL (MacOS)
`brew install postgres`

`pg_ctl -D /usr/local/var/postgres start`

## Create DB and user
```
createdb obm
createuser obm
```

`$ psql obm` 

```
alter user obm with encrypted password 'obm';
grant all privileges on database obm to obm ;
\q
```


## Install psycopg2 dependency (required for Postgres integration)
| postgress must be installed before
`pip install psycopg2`

Run DB Migration: 
`python manage.py migrate`

```
python manage.py makemigrations api
python manage.py migrate
```

## Create superuser

```
python manage.py createsuperuser --email admin@example.com --username admin
password: obmn2019
```

