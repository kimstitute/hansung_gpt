import streamlit as st

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

st.set_page_config(page_title="Hansung-GPT", page_icon="https://pbs.twimg.com/profile_images/1212031261297930241/p6kIo01N_400x400.jpg", layout="centered")
#st.title("인공지능 시인 Created by Minsang")
subject = st.text_input("시의 주제를 입력해주세요.")
st.write(f"시의 주제: {subject}")


if st.button("시 작성"):
    with st.spinner("시 작성 중..."):
        result = chat_model.invoke(f"{subject}에 대한 시를 윤동주가 쓴 것처럼 써줘")
        st.write(result.content)

# 메인 함수
#def main():


#if __name__ == "__main__":
#    main()
