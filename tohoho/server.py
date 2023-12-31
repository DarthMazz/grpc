from concurrent import futures
import grpc
import hello_pb2
import hello_pb2_grpc


class HelloWorld(hello_pb2_grpc.HelloWorldServicer):
    def SayHello(self, request, context):
        print("RECV: %s" % request.name)
        message = "Hello, %s!" % request.name
        print("SEND: %s" % message)
        return hello_pb2.HelloReply(message=message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloWorldServicer_to_server(HelloWorld(), server)
    server.add_insecure_port("[::]:8000")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
