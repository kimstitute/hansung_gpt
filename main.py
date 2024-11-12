import streamlit as st

from langchain_openai import ChatOpenAI
#from database import create_new_chat
chat_model = ChatOpenAI()

st.set_page_config(page_title="Hansung-GPT", page_icon="https://pbs.twimg.com/profile_images/1212031261297930241/p6kIo01N_400x400.jpg", layout="centered")
st.title("Hansung-GPT")
subject = st.text_input("원하는 주제를 입력해 주세요.")
st.write(f"시의 주제: {subject}")


if st.button("시 작성"):
    with st.spinner("시 작성 중..."):
        result = chat_model.invoke(f"{subject}에 대한 시를 윤동주가 쓴 것처럼 써줘")
        st.write(result.content)

AVAILABLE_MODELS = [
    "gpt-4o",
    "gpt-4o-mini",
    "gpt-4-turbo",
    "gpt-4",
    "gpt-3.5-turbo-0125",
]
########################################
# firebase, firestore 관련 소스 코드(분리 예정)
import firebase_admin
from firebase_admin import credentials, firestore, storage

# Firebase 서비스 계정 키
cred = credentials.Certificate("AIzaSyC5iGjh0cK-GLkTcvChf7CST7BL2CfnqVk")

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
########################################
# 메인 함수
def main():
    with st.sidebar:
        st.title("Hansung-GPT Chat")

        model = st.selectbox(
            "사용할 언어 모델 선택",
            AVAILABLE_MODELS,
            index=0, # 기본 값은 0번 모델
        )

        # streamlit의 session_state 딕셔너리에 사용 중인 모델 저장
        st.session_state["model"] = model

        # 새 채팅 시작하는 버튼
        if st.button("새 채팅", key="new_chat_button", use_container_width=True):
            new_chat_id = create_new_chat(st.session_state["user"])
            st.session_state["selected_chat"] = new_chat_id
            st.rerun()

        '''
        if "selected_chat" in st.session_state and st.session_state["selected_chat"]:
            chat.render(st.session_state["selected_chat"], st.session_state["model"])
        else:
            new_chat_id = create_new_chat(st.session_state["user"])
            st.session_state["selected_chat"] = new_chat_id
            st.rerun()
        '''

if __name__ == "__main__":
    main()