#streamlit run main.py to run
import streamlit as st
import google.generativeai as genai
import time
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🤖 AI Code Ethics Checker")

st.info("💡 Paste your code or describe your AI system (PL / EN supported)")

user_input = st.text_area("Input:")

if st.button("Analyze"):
    prompt = f"""
    Analyze the following code or system from an ethical perspective.

    IMPORTANT:
    - Respond in the same language as the user input (English or Polish).

    Structure your answer clearly using sections:
    1. List of Risks
    2. Explanation
    3. Recommendations
    4. Risk Level (Low/Medium/High)

    Focus on:
    - Bias
    - Privacy
    - Fairness
    - Transparency
    - Security

    Input:
    {user_input}
    """

    try:
        with st.spinner("🔍 Analyzing... please wait ⏳"):
            response = model.generate_content(prompt)

        result = response.text

        st.success("✅ Analysis ready")

        # 🔹 Вивід тексту
        st.markdown(result)

        # 🔥 Авто визначення рівня ризику
        text = result.lower()

        if "wysoki" in text or "high" in text:
            st.error("🔴 High Risk detected")
        elif "średni" in text or "medium" in text:
            st.warning("🟡 Medium Risk detected")
        elif "niski" in text or "low" in text:
            st.success("🟢 Low Risk detected")

    except Exception as e:
        if "429" in str(e):
            st.warning("⏳ Too many requests. Please wait...")
            time.sleep(15)
        else:
            st.error(f"Error: {e}")