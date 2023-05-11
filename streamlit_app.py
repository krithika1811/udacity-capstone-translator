import pandas as pd
import streamlit as st
from utils.get_quotes import get_random_quote
from utils.translator import quote_translate
import os

"""
# Udacity Universal Quotes Generator

This App generates a quote based on an emotion that you specify
and it can also translate into another language
of your choice.

Have fun playing!
"""



df = pd.DataFrame({
    'language': ["English", "Hindi", "French", "Japanese", "German"],
    'emotion': ["Success", "Inspirational", "Knowledge", "Humor", "Love"]
    })

mood_option = st.selectbox(
    'What is your mood right now?',
     df['emotion'])
    
language_option = st.selectbox(
    'in what language you want to express your mood?',
    df['language']
)

f'You are in **{mood_option}** state and you want to express that in **{language_option}**'

"""
# Are you ready ?
"""
quote = get_random_quote(token=os.environ['TOKEN'],category=mood_option)
quote_translation = quote_translate(quote, to_language=language_option)

f'your quote for **{mood_option}** is **{quote}**'
f'It can be expressed in **{language_option}** as **{quote_translation}**'

