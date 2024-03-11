FROM python:3.10-slim

RUN pip install Flask

RUN pip install Flask-Cors

RUN pip install SQLAlchemy==1.4.17

RUN pip install pymysql

WORKDIR /home/app

CMD ["python" , "routes.py"]