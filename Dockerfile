FROM python:3.10
WORKDIR /app

COPY . .
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

EXPOSE 5050
CMD ["python", "bot/main.py"]
