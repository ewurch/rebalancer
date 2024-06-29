FROM python:3.12

WORKDIR /app
COPY ./requirements.txt /app/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . /app/
RUN chmod +x entrypoint.sh

# Run the application on port 8000
ENTRYPOINT ["/app/entrypoint.sh"]
