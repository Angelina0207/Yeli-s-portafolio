import streamlit as st
from constants import info, endorsements
import base64

# --- Configuración general ---
st.set_page_config(
    page_title=f"Portafolio de {info['Nombre']}",
    page_icon="🌿",
    layout="wide"
)

# --- Estilos ---
st.markdown("""
<style>
  body { background-color: #eafaf1; font-family: 'Segoe UI', sans-serif; }
  .profile-wrapper { text-align: center; padding: 2rem; background: #c8e6c9; border-radius:16px; }
  .profile-pic { border:5px solid #66bb6a; border-radius:16px; width:240px; }
  .section-box { background:#fff; border:2px solid #a5d6a7; border-radius:12px; padding:1.5rem; margin:1.5rem 0; }
</style>
""", unsafe_allow_html=True)

# --- Portada con foto ---
st.title(f"🌿 Portafolio de {info['Nombre_Completo']}")
st.markdown(f"""
<div class="profile-wrapper">
  <h2 style="color:#2e7d32;">✨ {info['Introducción']}</h2>
  <img src="{info['Foto']}" class="profile-pic"
       onerror="this.onerror=null;this.src='https://via.placeholder.com/240?text=Foto+no+disponible';">
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

# -------------------- GALERÍA VISUAL INTERACTIVA --------------------
st.header("🖼️ Galería visual interactiva")
secciones = {
    "🎭 Expresión cultural": [
        ("baile", "Participación en concursos culturales escolares que me conectaron con mis raíces y mi cuerpo."),
        ("baile2", "El movimiento como forma de narrar emociones."),
        ("teatro", "El teatro me enseñó a comunicar con cuerpo y voz.")
    ],
    "💚 Vida cotidiana": [
        ("felicidad en amistades", "Conexión y alegría compartida con amigas."),
        ("felicidad en cinamon", "Cine y café: mis momentos de reflexión."),
        ("felicidad en cremolada", "La suavidad de lo simple en una cremolada."),
        ("gaseosa inka cola", "Un icono peruano que inspira creatividad popular.")
    ],
    # ... (resto de secciones igual)
}

for titulo, imagenes in secciones.items():
    with st.expander(titulo, expanded=False):
        filas = [imagenes[i : i+2] for i in range(0, len(imagenes), 2)]
        for fila in filas:
            cols = st.columns(len(fila))
            for col, (clave, descripcion) in zip(cols, fila):
                with col:
                    img_path = endorsements.get(clave)
                    if img_path:
                        with st.expander(f"🔍 {clave.capitalize()}", expanded=False):
                            st.image(
                                img_path,
                                width=200,
                                caption=""  # quitamos caption aquí
                            )
                            st.write(descripcion)
                    else:
                        st.warning(f"⚠️ Imagen no encontrada: {clave}")

st.markdown("---")

# -------------------- BIOGRAFÍA PROFESIONAL ORGANIZADA --------------------
st.header("📖 Biografía profesional")
with st.expander("👤 Todo sobre mí (perfil completo)", expanded=False):
    # Creamos dos columnas para dividir la info
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("💬 Quién soy")
        st.write("Soy una joven creativa e intuitiva que encuentra en la comunicación una forma de expresión sensible, política y estética.")
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
        st.write("Me apasionan el baile, el diseño editorial, el teatro, la música y el arte cotidiano que cuenta historias.")
        st.subheader("🤝 Voluntariado")
        st.write("""
        - “Regálame una sonrisa”  
        - DOMUND  
        - Empoderate.Pe
        """)
    # Opcional: referencias al final
    st.markdown("**📌 Referencias disponibles si se solicitan.**")
