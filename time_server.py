from concurrent import futures
import grpc
import time_pb2
import time_pb2_grpc
from datetime import datetime

class TimeServiceServicer(time_pb2_grpc.TimeServiceServicer):
    def GetServerTime(self, request, context):
        current_time = datetime.now().isoformat()
        return time_pb2.TimeResponse(current_time=current_time)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    time_pb2_grpc.add_TimeServiceServicer_to_server(TimeServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("🟢 gRPC 서버가 포트 50051에서 실행 중입니다.")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()