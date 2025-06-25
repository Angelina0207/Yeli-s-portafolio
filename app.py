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


# --- Galería visual mejorada ---
st.header("🖼️ Galería visual")

secciones = {
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
}

# Creamos pestañas por categoría
tabs = st.tabs(list(secciones.keys()))
for tab, categoria in zip(tabs, secciones):
    with tab:
        st.markdown("<div class='gallery-grid'>", unsafe_allow_html=True)
        for key, desc in secciones[categoria]:
            img_path = endorsements.get(key)
            if img_path:
                st.markdown(f"""
                  <div class='gallery-item'>
                    <img src='{img_path}' alt='{key}'>
                    <p>{desc}</p>
                  </div>
                """, unsafe_allow_html=True)
            else:
                st.warning(f"⚠️ Imagen no encontrada: {key}")
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
