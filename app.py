import streamlit as st
from constants import info, endorsements
import base64

# --- Configuración general ---
st.set_page_config(
    page_title=f"Portafolio de {info['Nombre']}",
    page_icon="🌿",
    layout="wide"
)

# --- Estilos personalizados (añade al bloque de CSS existente) ---
st.markdown("""
<style>
  /* Perfil */
  .profile-wrapper {
    background: linear-gradient(135deg, #d0f2d0, #c8e6c9);
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
    transition: transform .3s;
  }
  .profile-pic:hover {
    transform: scale(1.07);
    box-shadow: 0 8px 24px rgba(0,0,0,.2);
  }
  .intro-text {
    font-size: 1.4rem;
    color: #2e7d32;
    margin-top: 1rem;
  }
</style>
""", unsafe_allow_html=True)

# --- Portada con foto grande y fondo degradado ---
st.markdown(f"""
<div class="profile-wrapper">
  <!-- Foto de perfil -->
  <img
    src="{info['Foto']}"
    class="profile-pic"
    onerror="this.onerror=null;this.src='https://via.placeholder.com/300?text=Sin+Foto';"
  >
  <!-- Introducción -->
  <div class="intro-text">
    ✨ {info['Introducción']}
  </div>
</div>
""", unsafe_allow_html=True)

# --- Sobre mí breve ---
st.markdown(f"""
<div class="section-box">
  <b>Pronombre:</b> {info['Pronombre']}<br>
  <b>Ciudad:</b> {info['Ciudad']}<br>
  <b>Correo:</b> <a href="mailto:{info['Correo']}">{info['Correo']}</a><br>
  <b>Instagram:</b> <a href="{info['Instagram']}">@{info['Instagram'].split('/')[-1]}</a><br><br>
  {info['Acerca_de']}
</div>
""", unsafe_allow_html=True)

# --- Galería interactiva en pestañas, 2 imágenes por fila ---
st.header("🖼️ Galería visual")
secciones = {
  "🎭 Expresión cultural": ["baile","baile2","teatro"],
  "💚 Vida cotidiana": ["felicidad en amistades","felicidad en cinamon","felicidad en cremolada","gaseosa inka cola"],
  "🎨 Creatividad visual": ["guitarrra","medias","victor jara"],
  "🍽️ Cultura y sabor": ["alegría en comida","creación de kekes","comida"],
  "🎬 Íconos": ["star wars","pulp","pulp+smirnoff"],
  "🌟 Comunidad": ["empoderate.pe","actuar"]
}
tabs = st.tabs(list(secciones.keys()))
for tab, categoria in zip(tabs, secciones):
    with tab:
        imgs = secciones[categoria]
        for i in range(0, len(imgs), 2):
            cols = st.columns(2)
            for col, key in zip(cols, imgs[i:i+2]):
                img = endorsements.get(key)
                if img:
                    col.image(img, use_container_width=True, caption=key.replace("_"," ").capitalize())
                else:
                    col.warning(f"⚠️ Imagen no encontrada: {key}")
                    
# --- Biografía profesional ---
st.header("📖 Biografía profesional")
with st.expander("👤 Perfil completo", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("💬 Quién soy")
        st.write("Comunicadora creativa, intuitiva y sensible, con vocación social y pasión por lo visual.")
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
        st.subheader("💼 Experiencia profesional")
        st.write("""
        - Community Manager en VMTeam SAC  
        - Voluntaria en Empoderate.Pe  
        - Creación de documentales, entrevistas y reels reflexivos  
        - Proyectos audiovisuales y gráficos académicos
        """)
        st.subheader("🎨 Intereses y pasiones")
        st.write("Baile, diseño editorial, teatro, música y arte cotidiano que narra historias.")
        st.subheader("🤝 Voluntariado")
        st.write("""
        - “Regálame una sonrisa”  
        - DOMUND  
        - Empoderate.Pe
        """)
    st.markdown("**📌 Referencias disponibles si se solicitan.**")
