import streamlit as st
# from dotenv import load_dotenv
# load_dotenv()

from langchain.chat_models import ChatOpenAI
#from langchain_openai import ChatOpenAI
# from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()

# subject = "AI"
# result = chat_model.invoke(f"{subject}에 대한 시를 써줘")
# print(result.content)

st.title("인공지능 시인 Created by Minsang")
subject = st.text_input("시의 주제를 입력해주세요.")
st.write(f"시의 주제: {subject}")

if st.button("시 작성"):
    with st.spinner("시 작성 중..."):
        result = chat_model.invoke(f"{subject}에 대한 시를 윤동주가 쓴 것처럼 써줘")
        st.write(result.content)

