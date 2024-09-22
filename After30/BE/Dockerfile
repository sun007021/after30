FROM python:3.11-alpine3.18 as base

COPY ./ /home/BE/
WORKDIR /home/BE/

RUN apk update && \
    apk add --update --no-cache build-base libffi-dev && \
    pip install --upgrade pip && \
    mkdir -p /home/BE/wheels && \
    pip wheel --wheel-dir=/home/BE/wheels -r requirements.txt

FROM python:3.11-alpine3.18

COPY --from=base /home/BE/ /home/BE/
WORKDIR /home/BE/

RUN apk update && \
    apk add --update --no-cache bash curl && \
    mkdir /home/assets && \
    pip install --no-index --find-links=/home/BE/wheels -r requirements.txt && \
    rm -rf /home/BE/wheels && chmod +x /home/BE/imfast.sh

# Run alembic migrations


EXPOSE 80
CMD ["alembic upgrade head"]
CMD ["/home/BE/imfast.sh", "prod-run"]