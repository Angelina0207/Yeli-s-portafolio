import streamlit as st
from constants import info, embed_rss, endorsements
import base64

# -------------------- CONFIGURACIÓN GENERAL --------------------
st.set_page_config(
    page_title=f"Portafolio de {info['Nombre']}",
    page_icon="🌿",
    layout="wide"
)

# -------------------- ESTILOS --------------------
st.markdown("""
<style>
  body {
    background-color: #e8f5e9;
    font-family: 'Segoe UI', sans-serif;
  }
  .profile-wrapper {
    background: linear-gradient(135deg, #dcedc8, #c8e6c9);
    padding: 3rem 2rem;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 6px 20px rgba(0,0,0,0.1);
    margin-bottom: 2rem;
  }
  .profile-pic {
    border: 6px solid #4caf50;
    border-radius: 50%;
    width: 300px;
    height: 300px;
    object-fit: cover;
    transition: transform .3s, box-shadow .3s;
  }
  .profile-pic:hover {
    transform: scale(1.07);
    box-shadow: 0 8px 24px rgba(0,0,0,0.2);
  }
  .intro-text {
    font-size: 1.4rem;
    color: #2e7d32;
    margin-top: 1rem;
  }
  .section-box {
    background: #ffffff;
    border: 2px solid #a5d6a7;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
  }
  h1, h2, h3 {
    color: #2e7d32;
  }
  a {
    color: #1b5e20;
    text-decoration: none;
  }
  .tab-image {
    border-radius: 8px;
    transition: transform .2s;
  }
  .tab-image:hover {
    transform: scale(1.03);
  }
</style>
""", unsafe_allow_html=True)

# -------------------- PORTADA --------------------
st.title(f"🌿 Portafolio de {info['Nombre_Completo']}")

# Foto de perfil
try:
    st.image(info['Foto'], width=300, caption=None)
except:
    st.image(
        "https://via.placeholder.com/300?text=Sin+Foto",
        width=300,
        caption="Foto no disponible"
    )

# Introducción
st.markdown(f"<div class='intro-text'>✨ {info['Introducción']}</div>", unsafe_allow_html=True)

# -------------------- SOBRE MÍ --------------------
st.header("🌼 Sobre mí")
st.markdown(f"""
<div class="section-box">
  <b>Pronombre:</b> {info['Pronombre']}<br>
  <b>Ciudad:</b> {info['Ciudad']}<br>
  <b>Correo:</b> <a href="mailto:{info['Correo']}">{info['Correo']}</a><br>
  <b>Instagram:</b> <a href="{info['Instagram']}">@{info['Instagram'].split('/')[-1]}</a><br><br>
  {info['Acerca_de']}
</div>
""", unsafe_allow_html=True)

# -------------------- DESCARGA DE CV --------------------
st.header("📂 CV y contacto")
try:
    with open("CV_Angelina_Contreras.pdf", "rb") as f:
        pdf_bytes = f.read()
    b64 = base64.b64encode(pdf_bytes).decode()
    download_link = f"<a href='data:application/pdf;base64,{b64}' download='CV_Angelina_Contreras.pdf'>📄 Descargar mi CV</a>"
except FileNotFoundError:
    download_link = "<i>📄 CV no disponible temporalmente</i>"

st.markdown(f"""
<div class="section-box">
  {download_link}<br><br>
  📧 <a href="mailto:{info['Correo']}">{info['Correo']}</a><br>
  📸 <a href="{info['Instagram']}">@{info['Instagram'].split('/')[-1]}</a>
</div>
""", unsafe_allow_html=True)

# --- Estilos para galería compacta y hover ---
st.markdown("""
<style>
  .gallery-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.5rem;
    margin-bottom: 2rem;
  }
  .gallery-item {
    text-align: center;
    width: 150px;
  }
  .gallery-item img {
    border-radius: 8px;
    transition: transform .3s, box-shadow .3s;
    width: 150px;
    height: auto;
  }
  .gallery-item img:hover {
    transform: translateY(-8px) scale(1.08);
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  }
  .gallery-item p {
    font-size: 0.8rem;
    margin: 0.25rem 0 0;
    color: #2e7d32;
  }
</style>
""", unsafe_allow_html=True)

# ---------- GALERÍA VISUAL ----------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🖼️ Galería visual")

galeria = {
    "🎭 Expresión cultural": {
        "baile": "Participación en concursos culturales escolares que me conectaron con mis raíces.",
        "baile2": "Una forma de expresión que habita el escenario y transmite emociones.",
        "teatro": "Desde niña, el teatro me enseñó a comunicar con gestos y emociones."
    },
    "💚 Vida cotidiana": {
        "felicidad en amistades": "Momentos de conexión que inspiran mis narrativas visuales.",
        "felicidad en cinamon": "El cine y el café: espacios donde observo y reflexiono.",
        "felicidad en cremolada": "La ternura de lo simple: una cremolada y una sonrisa.",
        "gaseosa inka cola": "Ícono peruano que me conecta con lo popular y lo identitario."
    },
    "🎨 Creatividad visual": {
        "guitarrra": "Experimentar el ritmo y la armonía, también desde el sonido.",
        "medias": "Detalles únicos que expresan personalidad y juego visual.",
        "victor jara": "Inspiración constante: arte con mensaje y sensibilidad social."
    },
    "🍽️ Cultura y sabor": {
        "alegría en comida": "El acto de comer como espacio de identidad y disfrute.",
        "creación de kekes": "Trabajo familiar con amor, estética y sabor.",
        "comida": "Disfrutar lo cotidiano y observar cómo nos conecta."
    },
    "🎬 Referentes e íconos": {
        "star wars": "Mi lado geek y visual se inspira en universos narrativos potentes.",
        "pulp": "Contrastes visuales y culturas alternativas que me inspiran.",
        "pulp+smirnoff": "Juego gráfico, estética y humor combinados."
    },
    "🌟 Acción y comunidad": {
        "empoderate.pe": "Organización que promueve derechos, donde aporto desde la comunicación.",
        "actuar": "Habitar otros roles me ayuda a empatizar y observar el mundo."
    }
}

for titulo, imagenes in galeria.items():
    st.subheader(titulo)
    cols = st.columns(3)
    for idx, (clave, desc) in enumerate(imagenes.items()):
        with cols[idx % 3]:
            st.markdown("<div class='image-card'>", unsafe_allow_html=True)
            st.image(endorsements[clave], use_column_width=True)
            st.caption(desc)
            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# -------------------- BIOGRAFÍA PROFESIONAL --------------------
st.markdown("---")
st.header("📖 Biografía profesional")
with st.expander("👤 Perfil completo", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("💬 Quién soy")
        st.write("Comunicadora creativa e intuitiva, con vocación social y pasión por lo visual.")
        st.subheader("📘 Formación académica")
        st.write("""
        - C.E.P. Patrocinio de San José  
        - Cibertec (Excel, Word, Inkscape, Corel Draw)  
        - UNI – Ingeniería Mecánica (Corel Draw)  
        - PUCP – Publicidad y Comunicaciones (ITS)  
        - Estudios Generales Letras y Ciencias Sociales  
        - PUCP Idiomas – Inglés hasta Intermedio 4
        """)
        st.subheader("🛠️ Habilidades creativas")
        st.write("""
        - Edición de video (CapCut, Premiere Pro)  
        - Diseño gráfico (Canva, Illustrator)  
        - Storytelling visual e identidad de marca  
        - Escritura creativa y narrativa digital  
        - Curaduría estética de contenido
        """)
    with col2:
        st.subheader("💼 Experiencia")
        st.write("""
        - Community Manager en VMTeam SAC  
        - Voluntaria en Empoderate.Pe  
        - Creación de documentales, entrevistas y reels reflexivos  
        - Proyectos audiovisuales y gráficos académicos
        """)
        st.subheader("🎨 Pasiones")
        st.write("Baile, diseño editorial, teatro, música y arte cotidiano que narra historias.")
        st.subheader("🤝 Voluntariado")
        st.write("""
        - “Regálame una sonrisa”  
        - DOMUND  
        - Empoderate.Pe
        """)
    st.markdown("**📌 Referencias disponibles si se solicitan.**")
