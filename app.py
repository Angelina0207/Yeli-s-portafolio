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

# -------------------- GALERÍA / ENDORSEMENTS --------------------
st.header("🖼️ Proyectos y trabajos destacados")
cols = st.columns(len(endorsements))
for i, (key, img_url) in enumerate(endorsements.items()):
    with cols[i]:
        st.image(img_url, caption=f"Trabajo {i+1}", use_column_width=True)

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
