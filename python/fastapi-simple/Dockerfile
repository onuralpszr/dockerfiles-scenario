FROM python:3.10

# Code directory
WORKDIR /code

# Copy requirements.txt
COPY ./requirements.txt /code/requirements.txt

# Install requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy app directory
COPY ./app /code/app

# Run FastAPI server with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]