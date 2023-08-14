import grpc
import hello_pb2
import hello_pb2_grpc
import performance


@profile
def run():
    with grpc.insecure_channel("localhost:8000") as channel:
        stub = hello_pb2_grpc.HelloWorldStub(channel)
        with performance.Performance(message="stub.SayHello", verbose=True):
            response = stub.SayHello(hello_pb2.HelloRequest(name="Yamada"))
    print(f"RECV: {len(response.message)}bytes")
    with open("./grpc-receive.png", mode="wb") as f:
        f.write(response.message)


if __name__ == "__main__":
    run()
