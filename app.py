import streamlit as st
import google.generativeai as genai

# إعدادات واجهة التطبيق
st.set_page_config(page_title="TAHA - رفيقك النفسي", page_icon="💬")

# Gestion de la clé API : récupération depuis secrets.toml ou demande à l'utilisateur
if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    GEMINI_API_KEY = st.text_input("Veuillez entrer votre GEMINI_API_KEY :", type="password")
    if not GEMINI_API_KEY:
        st.warning("Veuillez fournir une clé GEMINI_API_KEY pour utiliser l'application.")
        st.stop()

# إعداد نموذج جوجل
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("TAHA - رفيقك النفسي 💬")
st.write("أنا هنا لأسمعك.. فضفض لي بما يجول في خاطرك.")

# ذاكرة المحادثة
if "chat_history" not in st.session_state:
	st.session_state.chat_history = []

# عرض الرسائل السابقة
for msg in st.session_state.chat_history:
	with st.chat_message(msg["role"]):
		st.markdown(msg["content"])

# صندوق المحادثة

if prompt := st.chat_input("كيف تشعر اليوم؟"):
	# إضافة رسالة المستخدم وعرضها
	st.session_state.chat_history.append({"role": "user", "content": prompt})
	with st.chat_message("user"):
		st.markdown(prompt)

	# جلب رد الذكاء الاصطناعي
	system_instruction = "أنت رفيق نفسي ودود اسمك طه، استمع بإنصات وتحدث بالعربية الدافئة."
	response = model.generate_content(f"{system_instruction}\nالمستخدم: {prompt}")
	# إضافة رد البوت وعرضه
	with st.chat_message("assistant"):
		st.markdown(response.text)
	st.session_state.chat_history.append({"role": "assistant", "content": response.text})
	# إضافة رد البوت وعرضه
	with st.chat_message("assistant"):
		st.markdown(response.text)
	st.session_state.chat_history.append({"role": "assistant", "content": response.text})
