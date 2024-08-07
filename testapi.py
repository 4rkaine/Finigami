import streamlit as st
import requests

url = 'http://127.0.0.1:5000/predict'

sample_texts = [
    'Akums Drugs and Pharmaceuticals makes positive debut, lists at 7% premium',
    'Markets slip after early gains! Nifty around 24,250, Sensex struggling to hold 79,400;',
    'India\'s Railways go high-tech: The track-laying process is powered by cutting-edge machinery.',
    'Marico slumps 4% on Bangladesh business continuity concerns',
    'Stocks To Watch: Bharti Airtel, ONGC, BEML, Adani Energy Solutions',
    'Global stock markets crash: Recession fears loom!',
    'Japan\'s stocks selloff on Monday seen as overdone: Invesco',
    'Adani Unveils $213 Billion Succession Plan as Scrutiny Persists',
    'Nvidia\'s Huang Sold $323 Million of Stock in July Before Decline',
    'Banking has been the worst performing sector in the last three trading sessions. For all those who are thinking why? The answer lies in the shareholding structure of the banks. It is the banks where FPI have maximum holding and whenever there is selling due to global reasons, it is the banks which come under pressure because FPI will sell what they own and because they own banks the maximum, these stocks come under pressure. But the other side to it is that Indian banks are far better placed than what they were five years ago, which makes analysts bullish on them with a medium to long term perspective.'
]

st.title('Sentiment Analysis for Financial News Articles')

exp = st.expander('Expand for sample texts', expanded=False)
exp.dataframe(sample_texts)

input = st.text_area('Enter your own news article')

if input:
    try:
        data = {'text': input}
        response = requests.post(url, json=data)
        if dict(response.json())['sentiment'] == 'negative':
            st.error('NEGATIVE')
        elif dict(response.json())['sentiment'] == 'positive':
            st.success('POSITIVE')
        else:
            st.warning('NEUTRAL')
        
    except Exception as e:
        st.warning('An error occured while trying to reach Flask server. Please ensure you\'ve run flaskapp.py, and the server is running on 127.0.0.1:5000, and then try again')