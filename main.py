#
import openai
import streamlit as st


openai.api_key = "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"
st.title("SEO Article Generator")

def generate_article(keyword, style, word):
    result = ''
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages = [
            {"role": "user", "content": "Write a SEO optimized word article about " + keyword},
            {"role": "user", "content": f"This article has to be in {style} style "},
            {"role": "user", "content": f"The article must be {word} length"},
        ],
        temperature=0
    )
    for choice in response.choices:
        result += choice.message.content
    return result

if __name__ == '__main__':
    keyword = st.text_input("Enter a word")
    writing_style = st.selectbox("Select a Style", ['Funny', 'Sarcastic', 'Academic'])
    word_count = st.slider("Select word count", min_value=50, max_value=100, value=100)
    submit_button = st.button("Generate Article")

    if submit_button:
        message = st.empty()
        message.text("Generating ArticLe...")
        article = generate_article(keyword=keyword, style=writing_style, word=word_count)
        message.text("")
        st.write(article)
        st.download_button(label="Download Article", data=article, file_name="article.txt", mime='text/csv')


#!pip install pyngrok==4.1.1
#from pyngrok import ngrok
#!ngrok authtoken <PASTE YOUR API KEY>
#public_url = ngrok.connect(port='8501')
#print(public_url)