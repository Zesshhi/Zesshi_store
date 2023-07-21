FROM python:3.10

RUN mkdir -p /home/ps_store

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV HOME=/home/ps_store
ENV APP_HOME=/home/ps_store/web

RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME

# устанавливаем зависимости
RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# копируем содержимое текущей папки в контейнер
COPY . .