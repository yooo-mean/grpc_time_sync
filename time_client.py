import grpc
import time_pb2
import time_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = time_pb2_grpc.TimeServiceStub(channel)
        response = stub.GetServerTime(time_pb2.TimeRequest())
        print(f"서버 시간: {response.current_time}")

if __name__ == '__main__':
    run()