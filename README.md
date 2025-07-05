# ⏱️ Python gRPC - 시간 동기화 예제

gRPC를 사용해 서버의 현재 시간을 클라이언트가 요청하여 받아오는 간단한 예제입니다.  
Python 환경에서 gRPC 구조를 연습하고, 클라이언트-서버 데이터 흐름을 이해하는 데 목적이 있습니다.

---

## 📦 사용 기술

- Python 3.7+
- gRPC (`grpcio`, `grpcio-tools`)
- Protocol Buffers

---
## 🧱 프로젝트 구조

grpc_time_sync/
├── time.proto # gRPC 서비스 및 메시지 정의
├── time_server.py # gRPC 서버
├── time_client.py # gRPC 클라이언트
├── time_pb2.py # .proto → Python 변환 결과
└── time_pb2_grpc.py # .proto → Stub/Servicer 생성 코드


---

## 🚀 실행 방법

### 1. 패키지 설치

bash
pip install grpcio grpcio-tools

### 1. .proto 파일 컴파일
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. time.proto

### 2. 서버 실행
python time_server.py

### 1. 클라이언트 실행 (새 터미널)
python time_client.py

## 서버 구조
[클라이언트] ─── gRPC 채널 연결 → 서버에 시간 요청
     ↓
[Stub] ─────── 요청 메시지 직렬화 및 전송
     ↓
[서버] ←────── HTTP/2 수신 후 현재 시간 생성
     ↓
[서버] ────── 응답 메시지 직렬화 후 전송
     ↓
[클라이언트] ← 시간 출력

## 출력 예시
서버 시간: 2025-07-05T14:02:13.123456