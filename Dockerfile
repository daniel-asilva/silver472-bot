FROM python:3.7.4-alpine
COPY bot .
RUN pip install -r requirements.txt
CMD python silver472-bot.py
