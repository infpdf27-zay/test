import time
import streamlit as st

st.title("ساعة رقمية حية على الويب 🕒")

# مكان مخصص لتحديث الوقت
placeholder = st.empty()

# حلقة لتحديث الوقت كل ثانية
for i in range(100):
  current_time = time.strftime("%H:%M:%S")
  placeholder.markdown(f"### الوقت الحالي هو: {current_time}")
  time.sleep(1)
