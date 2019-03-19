FROM ubuntu:xenial

RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    libgconf2-4 libnss3-1d libxss1 \
    fonts-liberation libappindicator1 xdg-utils libasound2\
    software-properties-common \
    curl unzip wget \
    xvfb

# install chromedriver and google-chrome

RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    wget https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip -d /usr/bin
RUN chmod +x /usr/bin/chromedriver

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome*.deb
RUN apt-get install -y -f


VOLUME ["/allure-results"]


ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

ENV APP_HOME /usr/src/app
WORKDIR /$APP_HOME



COPY . $APP_HOME/

RUN pip3 install -r requirements.txt
#CMD tail -f /dev/null
CMD py.test example.py --alluredir=/allure-results
