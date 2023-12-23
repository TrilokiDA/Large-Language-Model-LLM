import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


# function for getting response from llama llm
def getLlamaResponse(input_text, no_words, blog_style):

    # add llama model in model path
    llm = CTransformers(model='model/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens':256,
                                'temperature':0.01
                                })

    # Prompt template
    template = """
    Write a blog for {blog_style} job profile for topics {input_text} within {no_words} words.
    """
    prompt = PromptTemplate(input_variables=['blog_style','input_text','no_words'],
                            template=template)

    # Response from llm
    response = llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response

# streamlit configuration
st.set_page_config(
    page_title='Generate Blogs',
    page_icon="",
    layout='centered',
    initial_sidebar_state='collapsed'
)

# streamkit header
st.header("Generate Blogs")

# input box
input_text = st.text_input("Enter The Blog Topics")

# define clo1 amd col2 input text box
col1, col2 = st.columns([5,5])
with col1:
    no_words = st.text_input("No. of words")
with col2:
    blog_style = st.selectbox("Writing the blog for", ("Student", "Researcher", "Data Scientist", "Engineer"), index=0)

# submit button
submit = st.button("Generate")

if submit:
    st.write(getLlamaResponse(input_text, no_words, blog_style))