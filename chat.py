import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="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")

# titulo
st.write("# ChatBot")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# input do chat
texto_usuario = st.chat_input("Digite sua mensagem")

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if texto_usuario:
    # mostrar a mensagem que o usuário enviou no chat
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario) 

    # ia responde
    resposta_ia = modelo_ia.chat.completions.create(messages=st.session_state["lista_mensagens"], model="gpt-4o")
    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("ai").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)