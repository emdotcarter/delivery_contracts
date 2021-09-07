FROM python:3-buster

ENV APP_HOME=/home/app
WORKDIR ${APP_HOME}

RUN git clone https://github.com/katamarija/delivery_contracts.git
RUN pip install pipenv
WORKDIR ${APP_HOME}/delivery_contracts
RUN scripts/setup
ENTRYPOINT ["scripts/server"]
