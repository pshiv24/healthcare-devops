FROM python:3.8 
ENV PYTHONUNBUFFERED 1
WORKDIR /healthcare-devops/backend
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
RUN python manage.py migrate
EXPOSE 8000
CMD [ "gunicorn", "backend.wsgi", "--bind", "0.0.0.0:8000" ]
