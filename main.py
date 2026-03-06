import os

import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

SYSTEM_PROMPT = os.getenv(
    "SYSTEM_PROMPT",
    "Voce e um assistente prestativo que responde em portugues.",
)

st.set_page_config(page_title="Chat IA", page_icon="🤖", layout="centered")
st.title("Chatbot com IA")


@st.cache_resource
def inicializar_cliente_ia() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY", "")
    if not api_key:
        st.error("Defina OPENAI_API_KEY no arquivo .env")
        st.stop()
    return OpenAI(api_key=api_key)


if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

with st.sidebar:
    st.header("Configurações")
    modelo = st.text_input("Modelo", value=os.getenv("OPENAI_MODEL", "gpt-4o-mini"))
    temperatura = st.slider("Temperatura", 0.0, 2.0, 0.7, step=0.1)
    max_tokens = st.number_input("Max tokens", 256, 16384, 4096, step=256)
    st.divider()
    if st.button("Limpar conversa", use_container_width=True):
        st.session_state.mensagens = []
        st.rerun()


for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])


entrada_usuario = st.chat_input("Digite sua mensagem aqui...")

if entrada_usuario:
    st.chat_message("user").markdown(entrada_usuario)
    st.session_state.mensagens.append({"role": "user", "content": entrada_usuario})

    mensagens_api = [{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.mensagens

    try:
        cliente_ia = inicializar_cliente_ia()
        with st.chat_message("assistant"):
            stream = cliente_ia.chat.completions.create(
                model=modelo,
                messages=mensagens_api,
                temperature=temperatura,
                max_tokens=max_tokens,
                stream=True,
            )
            texto_resposta = st.write_stream(stream)

        st.session_state.mensagens.append(
            {"role": "assistant", "content": texto_resposta}
        )
    except Exception as erro:
        st.error(f"Erro ao chamar a IA: {erro}")


