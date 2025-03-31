FROM python:3.9
WORKDIR app/
COPY app/ .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 9090
CMD ["python", "app.py"]
# leogloriainfnet/flask-acme:1.0