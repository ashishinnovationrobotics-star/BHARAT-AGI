import streamlit as st
from core.bharat_core import BharatCore
from perception.llm_wrapper import PerceptionEngine
from memory.chunked_memory import ChunkedMemory
from rakshak.shield import RakshakShield

st.set_page_config(page_title="BHARAT-AGI", page_icon="🇮🇳", layout="wide")
st.title("🇮🇳 BHARAT-AGI v0.1 | First AI of India - 3026 Mindset")

query = st.text_area("Ask BHARAT-AGI:", "Design a safer mine monitoring system for Jharkhand using RAKSHAK")
if st.button("🧠 Think - 3026 Mode"):
    memory = ChunkedMemory()
    perception = PerceptionEngine()
    shield = RakshakShield()
    core = BharatCore(memory, perception, shield)
    ethical = shield.ethical_check(query)
    if ethical['allowed']:
        response = core.think(query)
        st.success("Dharma Shield Passed")
        st.markdown(response)
    else:
        st.error(ethical['reason'])
