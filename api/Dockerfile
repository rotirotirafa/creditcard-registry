FROM python:3.11.1

ENV PYTHONUNBUFFERED 1

EXPOSE 8001

WORKDIR /app

# this copy requirements from host, to docker container in /app
COPY ./requirements.txt .
# this copy everything from ./src directory to /app in the container
COPY ./src .

RUN pip install -r requirements.txt # Install the dependencies
# lets run the application in the port 8000
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8001", "src.main:app"]