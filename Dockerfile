FROM python:3.7
RUN mkdir /app
RUN pip install Flask 
RUN pip install Flask-WTF
COPY . /app
WORKDIR /app
CMD ["python", "app/api.py"]