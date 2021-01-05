FROM python:3.7
RUN mkdir /app
RUN pip install Flask
WORKDIR /app
CMD ["python", "api.py"]