FROM kennethreitz/pipenv

WORKDIR mkdir /var/app

WORKDIR /var/app

RUN pipenv install

ENTRYPOINT ["python", "main.py"]