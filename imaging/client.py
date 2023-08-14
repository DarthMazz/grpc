import grpc
from api import imaging_pb2
from api import imaging_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:8000") as channel:
        stub = imaging_pb2_grpc.ImagingStub(channel)
        response = stub.GrayScale(imaging_pb2.GrayScaleRequest(name="Yamada"))
        print(f"RECV: {len(response.buffer)}bytes")
        with open("./grpc-receive.png", mode="wb") as f:
            f.write(response.buffer)


if __name__ == "__main__":
    run()
