from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter


def main():
    load_dotenv()
    st.set_page_config(page_title="Document ")
    st.header("Ask your PDF")
    st.subheader("This is a GPT powered webapp to ask queries to your documents built using Langchain backend and Streamlit")    
    #upload file
    pdf = st.file_uploader("Upload your PDF here", type="pdf")
    
    #extract the text
    if pdf:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

         #split into chunks
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size = 1000,
            chunk_overlap = 200,
            length_function = len
         )
        chunks = text_splitter.split_text(text)

        st.write(chunks)

if __name__ == "__main__":
    main()