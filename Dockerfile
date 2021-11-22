FROM python:3.7.4-alpine
WORKDIR /workspace
COPY bot /workspace
RUN pip install -r requirements.txt
CMD python silver472-bot.py