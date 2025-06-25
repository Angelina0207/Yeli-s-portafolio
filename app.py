import streamlit as st
from constants import info, embed_rss, endorsements

# -------------------- CONFIGURACIÓN GENERAL --------------------
st.set_page_config(page_title=f"Portafolio de {info['Nombre']}", page_icon="🌿", layout="wide")

# -------------------- ESTILO PERSONALIZADO --------------------
st.markdown("""
<style>
    body {
        background-color: #e3f3ea;
        font-family: 'Arial', sans-serif;
    }
    .block-container {
        padding: 2rem 3rem;
    }
    h1, h2, h3 {
        color: #2e7d32;
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
    img {
        transition: transform .2s;
    }
    img:hover {
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

# -------------------- PORTADA --------------------
st.title(f"🌿 Portafolio de {info['Nombre_Completo']}")
st.markdown(f"### {info['Introducción']}")
st.image(info["Foto"], caption="Foto de perfil", width=220)
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

# -------------------- BIO PROFESIONAL --------------------
st.header("📖 Biografía profesional")
with st.expander("Ver más sobre mi trayectoria"):
    st.markdown("""
**💬 Quién soy**
Soy una joven creativa que encuentra en la comunicación una forma de expresión sensible, política y estética. Me gusta pensar visualmente, observar con empatía y actuar con propósito.

**💡 Experiencia**
- Community manager en VMTeam SAC.
- Voluntaria activa en Empoderate.Pe.
- Creadora de contenido social audiovisual.

**🎨 Intereses**
Baile, diseño, edición de videos, cultura visual, teatro y pequeños detalles que transforman.
    """)

st.markdown("---")

# -------------------- GALERÍA VISUAL --------------------
st.header("🖼️ Galería visual")

tabs = st.tabs(["🎭 Arte & Expresión", "🎶 Creatividad", "🍃 Cotidiano", "🍽️ Cultura", "🎬 Íconos", "🌟 Social"])

with tabs[0]:
    cols = st.columns(3)
    cols[0].image(endorsements["baile"], caption="Baile tradicional")
    cols[1].image(endorsements["baile2"], caption="Baile escénico")
    cols[2].image(endorsements["teatro"], caption="Teatro vivencial")

with tabs[1]:
    cols = st.columns(3)
    cols[0].image(endorsements["guitarrra"], caption="Guitarra reflexiva")
    cols[1].image(endorsements["medias"], caption="Estilo personal")
    cols[2].image(endorsements["victor jara"], caption="Inspiración musical")

with tabs[2]:
    cols = st.columns(3)
    cols[0].image(endorsements["felicidad en amistades"], caption="Amistades")
    cols[1].image(endorsements["felicidad en cinamon"], caption="Café y reflexión")
    cols[2].image(endorsements["felicidad en cremolada"], caption="Cremolada con memorias")

with tabs[3]:
    cols = st.columns(3)
    cols[0].image(endorsements["alegría en comida"], caption="Comida que abraza")
    cols[1].image(endorsements["gaseosa inka cola"], caption="Inka Kola & Perú")
    cols[2].image(endorsements["creación de kekes"], caption="Keke artesanal")

with tabs[4]:
    cols = st.columns(3)
    cols[0].image(endorsements["star wars"], caption="Star Wars")
    cols[1].image(endorsements["pulp"], caption="Estética pulp")
    cols[2].image(endorsements["pulp+smirnoff"], caption="Juego visual")

with tabs[5]:
    cols = st.columns(2)
    cols[0].image(endorsements["empoderate.pe"], caption="Empoderate.Pe")
    cols[1].image(endorsements["actuar"], caption="Actuación y expresión")

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
