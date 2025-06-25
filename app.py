import streamlit as st
from constants import info, embed_rss, endorsements

# -------------------- CONFIGURACIÓN GENERAL --------------------
st.set_page_config(page_title=f"Portafolio de {info['Nombre']}", page_icon="🌿", layout="wide")

# -------------------- ESTILO PERSONALIZADO --------------------
st.markdown("""
<style>
    body {
        background-color: #eafaf1;
        font-family: 'Segoe UI', sans-serif;
    }
    .block-container {
        padding: 2rem 3rem;
    }
    h1, h2, h3 {
        color: #1b5e20;
    }
    hr {
        border: 1px solid #a5d6a7;
    }
    .section-box {
        background-color: #ffffff;
        border: 2px solid #c8e6c9;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    }
    img {
        border-radius: 10px;
        transition: transform .2s;
    }
    img:hover {
        transform: scale(1.04);
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
    <div class='section-box'>
    <b>Pronombre:</b> {info['Pronombre']}  
    <b>Ciudad:</b> {info['Ciudad']}  
    <b>Correo:</b> <a href='mailto:{info['Correo']}'>{info['Correo']}</a>  
    <b>Instagram:</b> <a href='{info['Instagram']}'>@{info['Instagram'].split('/')[-1]}</a>  
    <br><br>
    {info['Acerca_de']}
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -------------------- BIO PROFESIONAL --------------------
st.header("📖 Biografía profesional")
with st.expander("Ver más sobre mi trayectoria"):
    st.markdown("""
<div class='section-box'>
<b>💬 Quién soy</b><br>
Soy una joven creativa que encuentra en la comunicación una forma de expresión sensible, política y estética. Me gusta pensar visualmente, observar con empatía y actuar con propósito.
<br><br>
<b>💡 Experiencia</b><br>
- Community manager en VMTeam SAC.<br>
- Voluntaria activa en Empoderate.Pe.<br>
- Creadora de contenido social audiovisual.
<br><br>
<b>🎨 Intereses</b><br>
Baile, diseño, edición de videos, cultura visual, teatro y pequeños detalles que transforman.
</div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -------------------- GALERÍA VISUAL --------------------
st.header("🖼️ Galería visual")

secciones = {
    "🎭 Arte & Expresión": ["baile", "baile2", "teatro"],
    "🎶 Creatividad": ["guitarrra", "medias", "victor jara"],
    "🍃 Cotidiano": ["felicidad en amistades", "felicidad en cinamon", "felicidad en cremolada"],
    "🍽️ Cultura": ["alegría en comida", "gaseosa inka cola", "creación de kekes"],
    "🎬 Íconos": ["star wars", "pulp", "pulp+smirnoff"],
    "🌟 Social": ["empoderate.pe", "actuar"]
}

for titulo, claves in secciones.items():
    st.subheader(titulo)
    cols = st.columns(len(claves))
    for i, key in enumerate(claves):
        with cols[i]:
            st.image(endorsements[key], caption=key.capitalize())
    st.markdown("<br>", unsafe_allow_html=True)

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
