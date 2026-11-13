import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(
    page_title="Proyecto STA",
    page_icon="🎓",
    layout="centered"
)

# DISEÑO
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #e8f5dc, #ffffff);
}

h1, h2, h3, p, label, .stMarkdown {
    color: #244d24 !important;
}

.titulo {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #244d24;
}

.subtitulo {
    text-align: center;
    font-size: 20px;
    color: #476b43;
}

div.stButton > button,
div.stFormSubmitButton > button {
    background-color: #244d24;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# PRESENTACIÓN
st.markdown(
    '<div class="titulo">¡Bienvenidos a nuestro proyecto!</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">Proyecto de STA - Noveno año</div>',
    unsafe_allow_html=True
)

st.divider()

st.write("Estamos muy felices de que estés aquí.")
st.write("Para comenzar, dinos tu nombre.")

# FORMULARIO
with st.form("bienvenida"):
    nombre = st.text_input("Introduce tu nombre")
    enviar = st.form_submit_button("Entrar al proyecto")

if enviar:
    if nombre.strip():
        st.session_state["nombre"] = nombre.strip()
    else:
        st.warning("¡Introduce tu nombre!")

# BIENVENIDA
if "nombre" in st.session_state:

    st.success(
        f"¡Hola, {st.session_state['nombre']}! "
        "Nos alegra mucho tenerte aquí."
    )

    st.write("¡Prepárate para conocer nuestro proyecto!")

    st.divider()

    st.subheader("¡Nuestro colegio!")

with open("escudo.png", "rb") as archivo:
    imagen = base64.b64encode(
        archivo.read()
    ).decode()

        html = f"""
        <html>
        <head>
        <style>
        body {{
            margin: 0;
            overflow: hidden;
            font-family: Arial;
            background: transparent;
        }}

        .escudo {{
            width: 220px;
            display: block;
            margin: auto;
            animation: caer 2.5s cubic-bezier(.2,.8,.3,1) forwards;
        }}

        @keyframes caer {{
            0% {{
                transform: translateY(-420px) rotate(-25deg);
                opacity: 0;
            }}
            65% {{
                transform: translateY(130px) rotate(12deg);
                opacity: 1;
            }}
            78% {{
                transform: translateY(80px) rotate(-7deg);
            }}
            90% {{
                transform: translateY(125px) rotate(4deg);
            }}
            100% {{
                transform: translateY(110px) rotate(0deg);
                opacity: 1;
            }}
        }}

        .mensaje {{
            text-align: center;
            font-size: 25px;
            font-weight: bold;
            color: #244d24;
            margin-top: 125px;
            opacity: 0;
            animation: aparecer 1.5s ease forwards;
            animation-delay: 2.5s;
        }}

        @keyframes aparecer {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        </style>
        </head>

        <body>
            <img class="escudo"
            src="data:image/png;base64,{imagen}">

            <div class="mensaje">
                ¡Bienvenido a nuestro proyecto de STA!
            </div>
        </body>
        </html>
        """

        components.html(html, height=550)

        st.balloons()
        st.write("¡Gracias por pasarte a nuestro proyecto!")
