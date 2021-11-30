FROM python:3.10-alpine
WORKDIR /workspace
COPY bot /workspace
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./silver472-bot.py"]