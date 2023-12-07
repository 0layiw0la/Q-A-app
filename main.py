import streamlit as st
from textly import answer,extract_text_from_txt,extract_text_from_docx,extract_text_from_pdf


def main():  
  st.title('Text Summarizer App')
  ans = st.button("Generate Answer")
        
  user_input = st.text_area('Enter text here')
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
                st.write(an)


if __name__ == '__main__':
    main()
