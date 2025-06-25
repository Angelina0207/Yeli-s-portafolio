import streamlit as st
from constants import info, embed_rss, endorsements

# -------------------- CONFIGURACIÓN GENERAL --------------------
st.set_page_config(page_title=f"Portafolio de {info['Nombre']}", page_icon="🌿", layout="wide")

# -------------------- ESTILO PERSONALIZADO --------------------
st.markdown("""
<style>
    body {
        background-color: #ecf7f5;
    }
    .block-container {
        padding: 2rem 3rem;
    }
    h1, h2, h3 {
        color: #00695c;
    }
    hr {
        border: 1px solid #a5d6a7;
    }
    .card {
        border-radius: 12px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.1);
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        background-color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

# -------------------- PORTADA --------------------
st.title(f"🌿 Portafolio de {info['Nombre_Completo']}")
st.markdown(f"### {info['Introducción']}")
st.image(info["Foto"], caption="Foto de perfil", width=200)
st.markdown("---")

# -------------------- SOBRE MÍ --------------------
st.header("🌼 Sobre mí")
with st.container():
    st.markdown(f"""
    **Pronombre:** {info['Pronombre']}  
    **Ciudad:** {info['Ciudad']}  
    **Correo:** [{info['Correo']}](mailto:{info['Correo']})  
    **Instagram:** [@{info['Instagram'].split('/')[-1]}]({info['Instagram']})  
    
    {info['Acerca_de']}
    """)

st.markdown("---")

# -------------------- GALERÍA VISUAL --------------------
st.header("🖼️ Galería visual de identidad")

st.subheader("🎭 Expresiones artísticas")
cols1 = st.columns(3)
with cols1[0]:
    st.image(endorsements["baile"], caption="Baile tradicional")
with cols1[1]:
    st.image(endorsements["baile2"], caption="Baile escénico")
with cols1[2]:
    st.image(endorsements["teatro"], caption="Teatro vivencial")

st.subheader("🎶 Momentos de creatividad personal")
cols2 = st.columns(3)
with cols2[0]:
    st.image(endorsements["guitarrra"], caption="Tocando guitarra")
with cols2[1]:
    st.image(endorsements["medias"], caption="Detalles que inspiran")
with cols2[2]:
    st.image(endorsements["victor jara"], caption="Inspiración musical")

st.subheader("🍃 Alegrías cotidianas")
cols3 = st.columns(3)
with cols3[0]:
    st.image(endorsements["felicidad en amistades"], caption="Amistades")
with cols3[1]:
    st.image(endorsements["felicidad en cinamon"], caption="Momentos dulces")
with cols3[2]:
    st.image(endorsements["felicidad en cremolada"], caption="Compartir una cremolada")

st.subheader("🍽️ Cultura y sabor")
cols4 = st.columns(3)
with cols4[0]:
    st.image(endorsements["alegría en comida"], caption="Riqueza culinaria")
with cols4[1]:
    st.image(endorsements["gaseosa inka cola"], caption="Inka Kola y tradición")
with cols4[2]:
    st.image(endorsements["creación de kekes"], caption="Creación casera")

st.subheader("🎬 Referencias e íconos")
cols5 = st.columns(3)
with cols5[0]:
    st.image(endorsements["star wars"], caption="Star Wars y narrativa")
with cols5[1]:
    st.image(endorsements["pulp"], caption="Estética pulp")
with cols5[2]:
    st.image(endorsements["pulp+smirnoff"], caption="Juego visual y contraste")

st.subheader("🌟 Participación social")
cols6 = st.columns(2)
with cols6[0]:
    st.image(endorsements["empoderate.pe"], caption="Voluntariado en Empoderate.Pe")
with cols6[1]:
    st.image(endorsements["actuar"], caption="Compromiso expresivo")

st.markdown("---")

# -------------------- PUBLICACIONES --------------------
st.header("📚 Publicaciones o blog")
st.components.v1.html(embed_rss['rss'], height=550)

st.markdown("---")

# -------------------- CIERRE --------------------
st.markdown("""
🌱 Gracias por visitar este espacio. 
Estoy creciendo, explorando y aprendiendo constantemente 💚
""")
