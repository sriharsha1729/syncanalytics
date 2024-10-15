import streamlit as st
from wordcloud import WordCloud
from textblob import TextBlob
import matplotlib.pyplot as plt

def textual_analysis(df):
    st.subheader("Text Analysis")
    text_column = st.selectbox("Select Text Column for Analysis", df.select_dtypes(include='object').columns)
    if text_column:
        generate_wordcloud(df[text_column])
        perform_sentiment_analysis(df, text_column)

def generate_wordcloud(text_series):
    text = ' '.join(text_series.dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)

def perform_sentiment_analysis(df, column):
    st.subheader("Sentiment Analysis")
    df['Sentiment'] = df[column].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    st.bar_chart(df['Sentiment'])
