# firebase, firestore 관련 소스 코드(분리 예정)
import firebase_admin
from firebase_admin import credentials, firestore, storage

# Firebase 서비스 계정 키
cred = credentials.Certificate("hs-gpt-b4da9-firebase-adminsdk-jhqn3-13e1e5b847.json")

# Firebase 초기화 (Storage 버킷 이름 포함)
firebase_admin.initialize_app(cred, {
    'storageBucket': 'hs-gpt-b4da9.appspot.com'  # Firebase Storage 버킷 이름 설정
})

# Firestore 클라이언트 초기화
db = firestore.client()

# Firebase Storage 사용을 위한 bucket 초기화
bucket = storage.bucket()  # Firebase Storage 기본 버킷을 가져오기

# 새로운 채팅 만드는 함수
def create_new_chat(user_id):
    chat_ref = db.collection("users").document(user_id).collection("chats").document()
    chat_ref.set({"created_at": firestore.SERVER_TIMESTAMP})
    return chat_ref.id