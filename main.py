import streamlit as st

from langchain_openai import ChatOpenAI
from database import create_new_chat
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