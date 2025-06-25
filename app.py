import streamlit as st
import pandas as pd
import plotly.express as px
import base64

# --- Datos de ejemplo (reemplaza con tus datos reales) ---
info = {
    "Nombre": "Yeli",
    "Nombre_Completo": "Yeli Kangie",
    "Foto": "https://i.imgur.com/yourphoto.jpg",  # reemplaza con tu url o ruta local
    "Introducción": "Soy publicista y comunicadora, apasionada por el diseño y el impacto social.",
    "Pronombre": "She/her",
    "Ciudad": "Lima, Perú",
    "Correo": "a20231270@pucp.edu.pe",
    "Instagram": "https://instagram.com/wwkangie",
    "Acerca_de": (
        "Soy Yeli, estudiante de Publicidad y Comunicaciones, nacida el 2 de julio. Me apasiona combinar "
        "el diseño, la narración y el pensamiento crítico para construir contenidos que generen impacto social. "
        "Soy parte activa de Empoderate.Pe, donde promuevo la participación juvenil y la equidad. También he trabajado "
        "como gestora de redes sociales para VMTeam SAC, una empresa emergente, y he realizado varios documentales, "
        "entrevistas y reels con enfoque reflexivo. Disfruto explorar lo visual, crear piezas gráficas y dar vida a ideas "
        "que conecten con las personas."
    )
}

# --- Configuración página ---
st.set_page_config(
    page_title=f"Portafolio de {info['Nombre']}",
    page_icon="🌿",
    layout="wide"
)

# --- Estilos CSS globales ---
st.markdown("""
<style>
  body {
    background-color: #121212;
    color: #e0f2f1;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  a {
    color: #80cbc4 !important;
    text-decoration: none;
  }
  a:hover {
    text-decoration: underline;
  }
  .profile-container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 3rem;
    margin-bottom: 3rem;
  }
  .profile-photo-container {
    background: linear-gradient(135deg, #43a047, #66bb6a);
    padding: 15px;
    border-radius: 16px;
    box-shadow: 0 10px 25px rgba(102,187,106,0.6);
    float: left;
  }
  .profile-photo {
    border-radius: 12px;
    width: 340px;
    height: 340px;
    object-fit: cover;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  .profile-photo:hover {
    transform: translateY(-10px) scale(1.05);
    box-shadow: 0 15px 40px rgba(102,187,106,0.9);
  }
  .title-portafolio {
    font-size: 3.2rem;
    font-weight: 700;
    color: #a5d6a7;
    text-shadow: 2px 2px 6px #1b5e20;
    margin: 0;
  }
  .intro-text {
    font-size: 1.5rem;
    max-width: 600px;
    line-height: 1.5;
    color: #b2dfdb;
    font-style: italic;
  }
  .section-box {
    background-color: #263238;
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 2rem;
    box-shadow: 0 8px 20px rgba(0,0,0,0.5);
  }
  h2, h3 {
    color: #80cbc4;
  }
  .contact-link {
    color: #80cbc4;
  }
</style>
""", unsafe_allow_html=True)

# -------------------- PORTADA --------------------
st.markdown("""
<style>
.profile-card {
    background: linear-gradient(135deg, #f1f8e9, #e0f2f1);
    padding: 3rem 2rem;
    border-radius: 20px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.1);
    margin-bottom: 3rem;
}
.title-text {
    font-size: 3.2rem;
    font-weight: 700;
    color: #1b5e20;
    margin-bottom: 1rem;
    font-family: 'Segoe UI', sans-serif;
}
.intro-text-large {
    font-size: 1.4rem;
    color: #4caf50;
    font-style: italic;
    margin-bottom: 1rem;
}
.profile-photo {
    border: 8px solid #66bb6a;
    border-radius: 50%;
    width: 350px;
    height: 350px;
    object-fit: cover;
    box-shadow: 0 8px 24px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# Contenedor tipo tarjeta
with st.container():
    st.markdown("<div class='profile-card'>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(f"<div class='title-text'>🌿 Portafolio de {info['Nombre_Completo']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='intro-text-large'>✨ {info['Introducción']}</div>", unsafe_allow_html=True)

    with col2:
        try:
            st.markdown(f"<img class='profile-photo' src='data:image/jpeg;base64,{base64.b64encode(open(info['Foto'], 'rb').read()).decode()}'/>", unsafe_allow_html=True)
        except:
            st.image("https://via.placeholder.com/350?text=Sin+Foto", width=350)

    st.markdown("</div>", unsafe_allow_html=True)
        
# -------------------- SOBRE MÍ --------------------
st.header("🌼 Sobre mí")

st.markdown("""
<style>
.about-container {
    background: linear-gradient(135deg, #ffffff, #f1f8e9);
    border-radius: 18px;
    padding: 2.5rem 2rem;
    box-shadow: 0 4px 16px rgba(0,0,0,0.05);
    margin-bottom: 2rem;
}
.about-left {
    font-size: 1.05rem;
    color: #2e7d32;
    padding-right: 2rem;
}
.about-left b {
    color: #1b5e20;
}
.about-line {
    margin-bottom: 0.6rem;
}
.about-line i {
    color: #43a047;
    margin-right: 0.5rem;
}
.about-right {
    font-size: 1.1rem;
    color: #4e342e;
    line-height: 1.6;
    text-align: justify;
}
</style>
""", unsafe_allow_html=True)

# Sección dividida en 2 columnas
with st.container():
    st.markdown('<div class="about-container">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown(f"""
        <div class="about-left">
            <div class="about-line"><i>🧍‍♀️</i><b>Pronombre:</b> {info['Pronombre']}</div>
            <div class="about-line"><i>📍</i><b>Ciudad:</b> {info['Ciudad']}</div>
            <div class="about-line"><i>📧</i><b>Correo:</b> <a href="mailto:{info['Correo']}">{info['Correo']}</a></div>
            <div class="about-line"><i>📸</i><b>Instagram:</b> <a href="{info['Instagram']}">@{info['Instagram'].split('/')[-1]}</a></div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="about-right">
        {info['Acerca_de']}
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

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
