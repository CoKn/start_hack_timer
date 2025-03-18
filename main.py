import streamlit as st
import time

st.set_page_config()

st.title("Epic Title 59:53")

# Center the timer text
st.markdown(
    """
    <style>
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh;
        font-size: 100px;
        font-family: Avenir Next;
        
    }
    </style>
    """,
    unsafe_allow_html=True
)

timer = st.empty()
N = 24*60*60
for secs in range(N, 0, -1):
    hh, rem = divmod(secs, 3600)
    mm, ss = divmod(rem, 60)
    timer.markdown(f'<div class="centered">{hh:02d}:{mm:02d}:{ss:02d}</div>', unsafe_allow_html=True)
    time.sleep(1)