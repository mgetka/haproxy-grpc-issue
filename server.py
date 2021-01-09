#!/usr/bin/env python
"""Dummy gRPC service server."""
from concurrent import futures

import grpc

import service_pb2_grpc


class Service(service_pb2_grpc.ServiceServicer):
    """gRPC server implementation."""

    def handler(self, _, context):
        """gRPC call handler that aborts the call immediately after its invocation."""
        context.abort(grpc.StatusCode.PERMISSION_DENIED, "Details sent by the server")

    UnaryUnary = handler
    StreamUnary = handler
    UnaryStream = handler
    StreamStream = handler


server = grpc.server(futures.ThreadPoolExecutor())
service_pb2_grpc.add_ServiceServicer_to_server(Service(), server)
server.add_insecure_port("0.0.0.0:6000")
server.start()
server.wait_for_termination()
