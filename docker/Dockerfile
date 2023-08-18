FROM python:3.11 as base

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY hello.py ./
COPY app.py ./app.py

RUN useradd -u 999 non-root-user
USER non-root-user

ARG niva-arg=I_SHOULD_NOT_BE_A_SECRET

ENTRYPOINT ["python", "hello.py"]
CMD [ "docker" ]