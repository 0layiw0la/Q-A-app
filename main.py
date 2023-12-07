import streamlit as st
from generator import answer,extract_text_from_txt,extract_text_from_docx,extract_text_from_pdf


def main():  
  st.title('Q & A app')
  ans = st.button("Generate Answer")
  col1,col2 = st.columns([1,1])
  with col2:
    user_input = st.text_area('Enter question here')
  with col1:
    user_context = st.text_area('Enter context here')
  uploaded_file = st.file_uploader("Choose a file", type=["txt", "docx", "pdf"])
  if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1]
    if file_extension == "txt":
      text = extract_text_from_txt(uploaded_file)
    elif file_extension == "docx":
      text = extract_text_from_docx(uploaded_file)
    elif file_extension == "pdf":
      text = extract_text_from_pdf(uploaded_file)
    
  if ans:
        if uploaded_file is not None:
            if user_input:
                an = answer(user_input,text)
                st.subheader('Answer')
                st.write(an)
        elif user_context:
          if user_input:
                an = answer(user_input,user_context)
                st.subheader('Answer')
                st.write(an)


if __name__ == '__main__':
    main()
