import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="TAHA - رفيقك النفسي", page_icon="💬")

# Helper to retrieve or ask for API key

def get_api_key():
    if "GEMINI_API_KEY" in st.secrets:
        return st.secrets["GEMINI_API_KEY"]
    return st.text_input("أدخل مفتاح الـ API الخاص بك:", type="password")

API_KEY = get_api_key()

if API_KEY:
    try:
        genai.configure(api_key=API_KEY)
        # التأكد من وجود اسم النموذج الصحيح
        model = genai.GenerativeModel("gemini-pro")

        st.title("TAHA - رفيقك النفسي 💬")
        st.write("أنا هنا لأسمعك.. فضفض لي بما يجول في خاطرك.")

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        # Render previous messages
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        prompt = st.chat_input("كيف تشعر اليوم؟")
        if prompt:
            # append user message and display it
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Request a response from the model
            response = model.generate_content(
                f"أنت رفيق نفسي ودود اسمك طه: {prompt}"
            )
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.chat_history.append(
                {"role": "assistant", "content": response.text}
            )
    except Exception as e:
        st.error(f"حدث خطأ في الاتصال: {e}")
else:
    st.warning("يرجى إدخال المفتاح لبدء التطبيق.")
