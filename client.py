#!/usr/bin/env python
"""Dummy gRPC service client."""
import argparse
from itertools import repeat

import grpc
from google.protobuf.empty_pb2 import Empty

import service_pb2_grpc

parser = argparse.ArgumentParser(description="Dummy gRPC service client.")
parser.add_argument(
    "call",
    type=str,
    choices=["unary-unary", "unary-stream", "stream-unary", "stream-stream"],
    help="Call type.",
)
parser.add_argument(
    "--host",
    type=str,
    help="gRPC server host (default: server).",
    default="server",
)
parser.add_argument(
    "--port", type=int, help="gRPC server port (default: 6000).", default=6000
)

args = parser.parse_args()

with grpc.insecure_channel(f"{args.host}:{args.port}") as channel:
    stub = service_pb2_grpc.ServiceStub(channel)

    try:
        if args.call == "unary-unary":
            stub.UnaryUnary(Empty())
        elif args.call == "unary-stream":
            response_iterator = stub.UnaryStream(Empty())
            for _ in response_iterator:
                pass
        elif args.call == "stream-unary":
            stub.StreamUnary(repeat(Empty()))
        elif args.call == "stream-stream":
            response_iterator = stub.StreamStream(repeat(Empty()))
            for _ in response_iterator:
                pass
    except grpc.RpcError as ex:
        print("Received gRPC error:")
        # pylint: disable=no-member
        print("Status:\t\t%s" % ex.code())
        print("Details:\t%s" % ex.details())
