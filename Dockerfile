FROM python:3

WORKDIR /app

ADD main.py .

RUN python -m pip install --upgrade pip
RUN pip install requests
RUN pip install flask
EXPOSE 5000

CMD ["python", "main.py"]