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
            st.markdown(f"""
            <style>
            .floating-photo-wrapper {{
                width: 360px;
                height: 360px;
                background-color: #a5d6a7;
                border-radius: 20px;
                box-shadow: 0 12px 28px rgba(0,0,0,0.2);
                display: flex;
                align-items: center;
                justify-content: center;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                margin: auto;
            }}
            .floating-photo-wrapper:hover {{
                transform: translateY(-8px);
                box-shadow: 0 16px 32px rgba(0,0,0,0.25);
            }}
            .floating-photo {{
                width: 340px;
                height: 340px;
                object-fit: cover;
                border-radius: 12px;
                background-color: white;
            }}
            </style>

            <div class="floating-photo-wrapper">
                <img class="floating-photo" src="data:image/jpeg;base64,{base64.b64encode(open(info['Foto'], 'rb').read()).decode()}" />
            </div>
            """, unsafe_allow_html=True)
    except:
        st.image("https://via.placeholder.com/350?text=Sin+Foto", width=350)
        
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
