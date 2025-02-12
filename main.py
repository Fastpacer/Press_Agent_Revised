import streamlit as st
from backend.data_fetch import fetch_supplementary_data
from backend.content_gen import generate_press_release
from backend.review_agent import review_press_kit


st.title("PressAgent: AI-Generated Press Kit")

company_name = st.text_input("Company Name:")
press_topic = st.text_area("Press Kit Topic:")

if st.button("Generate Press Kit"):
    with st.spinner("Fetching supplementary data..."):
        supplementary_data = fetch_supplementary_data(company_name)
    
    with st.spinner("Generating press release..."):
        press_kit_text = generate_press_release(company_name, press_topic, supplementary_data)

    with st.spinner("Reviewing press kit..."):
        review = review_press_kit(press_kit_text)

    st.subheader("Generated Press Kit")
    st.write(press_kit_text)

    st.subheader("Quality Review")
    st.json(review)

    
