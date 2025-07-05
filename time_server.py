from concurrent import futures
import grpc
import time_pb2
import time_pb2_grpc
from datetime import datetime
import pytz  # 전체 모듈 import (중요)

class TimeServiceServicer(time_pb2_grpc.TimeServiceServicer):
    def GetServerTime(self, request, context):
        requested_tz = request.timezone or "UTC"
        try:
            tz_info = pytz.timezone(requested_tz)  # ❗ 여기서 'pytz.timezone' 사용해야 함
        except pytz.UnknownTimeZoneError:
            context.set_details(f"Unknown timezone: {requested_tz}")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return time_pb2.TimeResponse(current_time="")

        current_time = datetime.now(tz_info).isoformat()
        return time_pb2.TimeResponse(current_time=current_time)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    time_pb2_grpc.add_TimeServiceServicer_to_server(TimeServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("🟢 서버가 실행 중입니다 (포트: 50051)")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
