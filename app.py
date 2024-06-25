import streamlit as st
import joblib
model = joblib.load("sentiment-model.pkl")
sentiment_labels = {'1': 'Positiv', '0' : 'Negative'}
st.title("Sentiment Analysis")
user_input = st.text_area('Enter your text here:')
if st.button('Predict'):

    predicted_sentiment = model.predict([user_input])[0]
    predicted_sentiment_label = sentiment_labels[str(predicted_sentiment)]
    st.info(f"Predicted Sentiment: {predicted_sentiment_label}")