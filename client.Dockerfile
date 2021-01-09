FROM python:3.9.1-alpine

COPY client.py service.proto requirements.txt /

RUN apk update && apk add --no-cache --virtual .build-deps build-base linux-headers && \
    apk add libstdc++                                                                           && \
    pip install -r requirements.txt                                                             && \
    apk --purge del .build-deps                                                                 && \
    rm -rf /var/lib/apt/lists/*                                                                 && \
    python -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. service.proto && \
    chmod +x client.py

ENTRYPOINT ["./client.py"]
CMD ["-h"]
