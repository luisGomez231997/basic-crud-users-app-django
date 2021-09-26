#image base:
FROM python:3.8
# active the python buffer console:
ENV PYTHONUNBUFFERED 1
# create a directory with the project folder dir.
RUN mkdir /app
WORKDIR /app
# create a volume with the required files and dependencies.
COPY ./kly_main_app /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# run the server app in the continer.
CMD python manage.py runserver 0.0.0.0:8000