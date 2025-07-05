import grpc
import time_pb2
import time_pb2_grpc

def run():
    timezone = input("원하는 타임존을 입력하세요 (예 : Asia/Seoul, UTC): ")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = time_pb2_grpc.TimeServiceStub(channel)
        response = stub.GetServerTime(time_pb2.TimeRequest(timezone=timezone))
        print(f"서버 시간: {response.current_time}")

if __name__ == '__main__':
    run()