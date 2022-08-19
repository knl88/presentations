FROM python:3.8-slim as base

RUN pip install emoji

WORKDIR /app

COPY hello-docker.py ./

RUN useradd -u 999 non-root-user
USER non-root-user

ENTRYPOINT ["python"]
CMD ["hello-docker.py"]