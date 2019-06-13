FROM python

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

# RUN chmod +x /app/migrate.sh

WORKDIR /app

EXPOSE 8000

CMD python manage.py runserver