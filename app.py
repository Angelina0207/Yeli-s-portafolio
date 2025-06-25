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
import base64

# Leer la foto y codificarla en base64 para usarla como fondo inline
try:
    with open(info['Foto'], "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode()
except Exception:
    img_base64 = None

st.markdown(f"""
<style>
.header-container {{
    position: relative;
    width: 100%;
    height: 400px;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    margin-bottom: 3rem;
    background-image: url("data:image/jpeg;base64,{img_base64 if img_base64 else ''}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

.header-overlay {{
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-color: rgba(0,0,0,0.45); /* oscurece para que el texto blanco resalte */
    border-radius: 20px;
}}

.header-text {{
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    font-family: 'Segoe UI', sans-serif;
    font-size: 3.5rem;
    font-weight: 700;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
    text-align: center;
    white-space: nowrap;
}}
</style>

<div class="header-container">
  <div class="header-overlay"></div>
  <div class="header-text">🌿 Portafolio de {info['Nombre_Completo']}</div>
</div>
""", unsafe_allow_html=True)
        
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
