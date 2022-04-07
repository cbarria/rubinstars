FROM makuk66/pygithub

ADD . /app

RUN pip install PyGithub

RUN pip install pyyaml 

WORKDIR /app

CMD ["python","rubinstars.py"]

