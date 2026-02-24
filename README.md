# TAHA - رفيقك النفسي (Streamlit + Gemini)

تطبيق ويب بسيط باستخدام **Streamlit** و **Google Gemini API** لرفيق نفسي عربي ودود باسم **"TAHA"**.

يوفّر:
- واجهة محادثة نظيفة بالعربية.
- شريط جانبي يتضمن تنبيهًا / إخلاء مسؤولية طبي واضح.
- شخصية ذكاء اصطناعي متعاطفة وغير حُكمية، تستخدم الاستماع الفعّال.
- تذكّر سجل المحادثة خلال جلسة المتصفح الواحدة.

## المتطلبات

```bash
pip install -r requirements.txt
```

## إعداد مفتاح Gemini API

للتشغيل، تحتاج إلى مفتاح من Google Gemini:

1. احصل على المفتاح من صفحة Google AI Studio.
2. إمّا أن:

- تضعه في متغير البيئة:

```bash
export GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

أو:

- تضعه في `~/.streamlit/secrets.toml`:

```toml
GEMINI_API_KEY = "YOUR_API_KEY_HERE"
```

## التشغيل

من داخل مجلد المشروع:

```bash
streamlit run app.py
```

ثم افتح الرابط الذي يظهر في الطرفية (عادة `http://localhost:8501`).

