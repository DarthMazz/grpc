from concurrent import futures
from io import BytesIO

import cv2
from api import imaging_pb2, imaging_pb2_grpc

import grpc


class Imaging(imaging_pb2_grpc.ImagingServicer):
    def GrayScale(self, request, context):
        print("RECV: %s" % request.name)
        path = "./grpc-logo.png"
        # with open(path, mode="rb") as f:
        #     message = f.read()
        #     print(f"SEND: {len(message)}bytes")
        #     return imaging_pb2.GrayScaleResponse(buffer=message)
        img = cv2.imread(path)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, num_bytes = cv2.imencode(".jpeg", img_gray)
        num_bytes = num_bytes.tobytes()
        return imaging_pb2.GrayScaleResponse(buffer=num_bytes)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    imaging_pb2_grpc.add_ImagingServicer_to_server(Imaging(), server)
    server.add_insecure_port("[::]:8000")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
