import streamlit as st
from constants import info, endorsements
import base64

# --- Configuración general ---
st.set_page_config(
    page_title=f"Portafolio de {info['Nombre']}",
    page_icon="🌿",
    layout="wide"
)

# --- Estilos personalizados ---
st.markdown("""
<style>
  body { background-color: #eafaf1; font-family: 'Segoe UI', sans-serif; }
  .profile-wrapper { 
    text-align: center; 
    padding: 2rem; 
    background: #c8e6c9; 
    border-radius: 16px; 
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 2rem;
  }
  .profile-pic { 
    border: 5px solid #66bb6a; 
    border-radius: 16px; 
    width: 200px; 
    height: 200px;
    object-fit: cover;
    transition: transform .2s;
  }
  .profile-pic:hover { transform: scale(1.05); }
  .section-box { 
    background: #ffffff; 
    border: 2px solid #a5d6a7; 
    border-radius: 12px; 
    padding: 1.5rem; 
    margin: 1.5rem 0; 
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
  }
  h1, h2, h3 { color: #2e7d32; }
  a { color: #1b5e20; text-decoration: none; }
  .tab-image {
    border-radius: 8px;
    transition: transform .2s;
  }
  .tab-image:hover { transform: scale(1.03); }
</style>
""", unsafe_allow_html=True)

# --- Portada con foto corregida ---
st.title(f"🌿 Portafolio de {info['Nombre_Completo']}")
st.markdown(f"""
<div class="profile-wrapper">
  <h2 style="color:#2e7d32;">✨ {info['Introducción']}</h2>
  <img
    src="{info['Foto']}"
    class="profile-pic"
    onerror="this.onerror=null;this.src='https://via.placeholder.com/200?text=Sin+Foto';"
  >
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
