Use official Python image
FROM python:3.10-slim

Set working directory
WORKDIR /app

Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

Copy bot script
COPY bot.py .

Run the bot
CMD ["python", "bot.py"]
