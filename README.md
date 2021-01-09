The repository contains a minimal example for the purpose of the Stack Overflow question. Example
consist of a simple python gRPC server and client application that are ran inside of docker
containers. Provided `docker-compose` file launches the server and configured HAProxy instance.

------------

## Running the server

```
$ docker-compose up
```

_NOTE_: This call will invoke docker container build. During the build, grpc-core is being compiled
 and this may take a while.

## Building the client

```
$ docker build . -f client.Dockerfile -t client
$ docker run client
usage: client.py [-h] [--host HOST] [--port PORT]
                 {unary-unary,unary-stream,stream-unary,stream-stream}

Dummy gRPC service client.

positional arguments:
  {unary-unary,unary-stream,stream-unary,stream-stream}
                        Call type.

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           gRPC server host (default: server).
  --port PORT           gRPC server port (default: 6000).
```

### Direct call

```
$ docker run -it --rm --network haproxy_grpc_issue client --host server stream-stream
Received gRPC error:
Status:		StatusCode.PERMISSION_DENIED
Details:	Details sent by the server
```

### Call through the proxy

```
$ docker run -it --rm --network haproxy_grpc_issue client --host proxy stream-stream
Received gRPC error:
Status:		StatusCode.CANCELLED
Details:	Received RST_STREAM with error code 8
```
