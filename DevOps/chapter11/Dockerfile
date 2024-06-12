FROM python:3.7.3-alpine

ENV APP_HOME /app
WORKDIR ${APP_HOME}

COPY . .

RUN pip install -r requirements.txt
EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD [ "ex01.py" ]