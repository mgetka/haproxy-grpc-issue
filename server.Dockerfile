FROM python:3.9.1-alpine

COPY server.py service.proto requirements.txt /

RUN apk update && apk add --no-cache --virtual .build-deps build-base linux-headers && \
    apk add libstdc++                                                                           && \
    pip install -r requirements.txt                                                             && \
    apk --purge del .build-deps                                                                 && \
    rm -rf /var/lib/apt/lists/*                                                                 && \
    chmod +x server.py

ENTRYPOINT ["./server.py"]
