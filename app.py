import streamlit as st
from constants import info, endorsements
import base64

# ---------- CONFIGURACIÓN DE LA PÁGINA ----------
st.set_page_config(
    page_title=f"Portafolio de {info['Nombre']}",
    page_icon="🌿",
    layout="wide",
)

# ---------- ESTILOS GENERALES ----------
st.markdown("""
<style>
    /* Fondo crema y fuente */
    body {
        background-color: #fff8e1;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #2e7d32;
        margin: 0;
        padding: 1rem 3rem;
    }

    /* Contenedor general con sombra suave y borde redondeado */
    .container {
        background: #f9fbe7;
        border-radius: 20px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        padding: 3rem;
        margin-bottom: 3rem;
    }

    /* Contenedor de foto con fondo verde suave y sombra */
    .photo-container {
        background-color: #a5d6a7;
        border-radius: 20px;
        padding: 12px;
        max-width: 320px;
        box-shadow: 0 12px 32px rgba(0,0,0,0.12);
        transition: box-shadow 0.3s ease;
        float: left;
        margin-right: 3rem;
    }
    .photo-container:hover {
        box-shadow: 0 16px 40px rgba(0,0,0,0.2);
    }
    .photo-container img {
        border-radius: 16px;
        width: 300px;
        height: 300px;
        object-fit: cover;
        transition: transform 0.3s ease;
    }
    .photo-container img:hover {
        transform: scale(1.07);
    }

    /* Texto introductorio */
    .intro-text h1 {
        font-weight: 700;
        font-size: 2.8rem;
        margin-bottom: 0.4rem;
        color: #1b5e20;
    }
    .intro-text p {
        font-size: 1.4rem;
        line-height: 1.5;
        max-width: 700px;
        color: #33691e;
        margin-top: 0;
    }

    /* Sección "Sobre mí" */
    .about-section {
        background: linear-gradient(135deg, #dcedc8, #c8e6c9);
        border-radius: 20px;
        padding: 2rem 3rem;
        box-shadow: 0 6px 24px rgba(0,0,0,0.07);
        color: #2e7d32;
        margin-bottom: 3rem;
    }
    .about-left {
        font-size: 1.1rem;
        line-height: 1.4;
        padding-right: 2rem;
    }
    .about-left b {
        color: #1b5e20;
    }
    .about-left a {
        color: #33691e;
        text-decoration: none;
    }
    .about-left a:hover {
        text-decoration: underline;
    }
    .about-line {
        margin-bottom: 1rem;
    }
    .about-line i {
        color: #43a047;
        margin-right: 0.6rem;
    }
    .about-right {
        font-size: 1.15rem;
        line-height: 1.7;
        color: #4e342e;
        text-align: justify;
    }

    /* CV y contacto */
    .cv-contact {
        background: #fff;
        border: 2px solid #a5d6a7;
        border-radius: 20px;
        padding: 2rem 3rem;
        box-shadow: 0 6px 24px rgba(0,0,0,0.06);
        color: #2e7d32;
        margin-bottom: 3rem;
        font-size: 1.1rem;
    }
    .cv-contact a {
        color: #1b5e20;
        font-weight: 600;
        text-decoration: none;
    }
    .cv-contact a:hover {
        text-decoration: underline;
    }

    /* Galería */
    .gallery-section {
        margin-bottom: 3rem;
    }
    .gallery-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        justify-content: center;
    }
    .gallery-item {
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 24px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer;
        width: 150px;
    }
    .gallery-item:hover {
        transform: translateY(-6px) scale(1.05);
        box-shadow: 0 12px 36px rgba(0,0,0,0.18);
    }
    .gallery-item img {
        width: 150px;
        height: 150px;
        object-fit: cover;
        display: block;
    }
    .gallery-item p {
        margin: 0.5rem 0 0;
        font-size: 0.85rem;
        text-align: center;
        color: #2e7d32;
    }

    /* Biografía profesional */
    .bio-container {
        margin-top: 3rem;
    }
    .bio-subsection h3 {
        color: #1b5e20;
    }
    .bio-subsection p, .bio-subsection ul {
        font-size: 1.1rem;
        line-height: 1.6;
        color: #4e342e;
        margin-top: 0.3rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------- PORTADA ----------
st.markdown('<div class="container">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 2])
with col1:
    st.markdown('<div class="photo-container">', unsafe_allow_html=True)
    st.image(info['Foto'], width=700)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="intro-text">
        <h1>🌿 Portafolio de {info['Nombre_Completo']}</h1>
        <p>✨ {info['Introducción']}</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# ---------- SOBRE MÍ ----------
st.markdown('<div class="about-section">', unsafe_allow_html=True)
st.header("🌼 Sobre mí")

col1, col2 = st.columns([1, 2])
with col1:
    st.markdown(f"""
    <div class="about-left">
        <div class="about-line"><i>🧍‍♀️</i><b>Pronombre:</b> {info['Pronombre']}</div>
        <div class="about-line"><i>📍</i><b>Ciudad:</b> {info['Ciudad']}</div>
        <div class="about-line"><i>📧</i><b>Correo:</b> <a href="mailto:{info['Correo']}">{info['Correo']}</a></div>
        <div class="about-line"><i>📸</i><b>Instagram:</b> <a href="{info['Instagram']}" target="_blank">@{info['Instagram'].split('/')[-1]}</a></div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="about-right">
        {info['Acerca_de']}
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- DESCARGA DE CV Y CONTACTO ----------
st.header("📂 CV y contacto")
try:
    with open("CV_Angelina_Contreras.pdf", "rb") as f:
        pdf_bytes = f.read()
    b64 = base64.b64encode(pdf_bytes).decode()
    download_link = f"""<a href="data:application/pdf;base64,{b64}" download="CV_Angelina_Contreras.pdf" target="_blank">📄 Descargar mi CV</a>"""
except FileNotFoundError:
    download_link = "<i>📄 CV no disponible temporalmente</i>"

st.markdown(f"""
<div class="cv-contact">
    {download_link}<br><br>
    📧 <a href="mailto:{info['Correo']}">{info['Correo']}</a><br>
    📸 <a href="{info['Instagram']}" target="_blank">@{info['Instagram'].split('/')[-1]}</a>
</div>
""", unsafe_allow_html=True)

# --- GALERÍA COMPACTA CON st.image Y HOVER ZOOM ---
# CSS para zoom y sombras en las imágenes de la galería
st.markdown("""
<style>
  /* Solo afecta las imágenes dentro de la galería */
  .gallery-section .stImage img {
    border-radius: 8px;
    transition: transform .3s, box-shadow .3s;
    width: 150px !important;
  }
  .gallery-section .stImage img:hover {
    transform: translateY(-5px) scale(1.05);
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  }
</style>
""", unsafe_allow_html=True)

# Definimos la sección de la galería
st.header("🖼️ Galería visual")
for categoria, items in {
    "🎭 Expresión cultural": [
        ("baile", "Concursos culturales que conectan mis raíces."),
        ("baile2", "Movimiento que narra emoción."),
        ("teatro", "Comunicación con cuerpo y voz.")
    ],
    "💚 Vida cotidiana": [
        ("felicidad en amistades", "Conexión e inspiración diaria."),
        ("felicidad en cinamon", "Reflexión entre cine y café."),
        ("felicidad en cremolada", "La ternura de lo simple."),
        ("gaseosa inka cola", "Ícono popular y creativo.")
    ],
    "🎨 Creatividad visual": [
        ("guitarrra", "Armonía y ritmo creativo."),
        ("medias", "Detalles que cuentan historias."),
        ("victor jara", "Arte con mensaje social.")
    ],
    "🍽️ Cultura y sabor": [
        ("alegría en comida", "Identidad y disfrute en un bocado."),
        ("creación de kekes", "Estética y sabor familiar."),
        ("comida", "Observación de lo cotidiano.")
    ],
    "🎬 Íconos": [
        ("star wars", "Universos narrativos épicos."),
        ("pulp", "Estéticas alternativas e impactantes."),
        ("pulp+smirnoff", "Juego gráfico y humor.")
    ],
    "🌟 Comunidad": [
        ("empoderate.pe", "Comunicación para el empoderamiento."),
        ("actuar", "Empatía y exploración de roles.")
    ]
}.items():
    with st.expander(categoria, expanded=False):
        st.markdown("<div class='gallery-section'>", unsafe_allow_html=True)
        # Mostramos en filas de 4
        for i in range(0, len(items), 4):
            cols = st.columns(4)
            for col, (clave, desc) in zip(cols, items[i:i+4]):
                img_path = endorsements.get(clave)
                if img_path:
                    col.image(img_path, caption=desc, use_container_width=False)
                else:
                    col.warning(f"⚠️ Imagen no encontrada: {clave}")
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

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

