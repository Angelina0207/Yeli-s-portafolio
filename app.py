import streamlit as st
from constants import info, embed_rss, endorsements
import base64

# -------------------- CONFIGURACIÓN GENERAL --------------------
st.set_page_config(
    page_title=f"Portafolio de {info['Nombre']}",
    page_icon="🌿",
    layout="wide"
)

# -------------------- ESTILO PERSONALIZADO --------------------
st.markdown("""
<style>
  body { background-color: #eafaf1; font-family: 'Segoe UI', sans-serif; }
  .block-container { padding: 2rem 3rem; }
  h1,h2,h3 { color: #2e7d32; }
  hr { border: 1px solid #a5d6a7; }
  .section-box {
    background: #fff;
    border: 2px solid #a5d6a7;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
  }
  .profile-wrapper {
    background: #c8e6c9;
    padding: 2rem;
    margin: 2rem 0;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  }
  .profile-pic-square {
    border: 5px solid #66bb6a;
    border-radius: 16px;
    width: 240px;
    object-fit: cover;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    margin-top: 1rem;
  }
  img { border-radius: 10px; transition: transform .2s; }
  img:hover { transform: scale(1.04); }
</style>
""", unsafe_allow_html=True)

# -------------------- PORTADA --------------------
st.title(f"🌿 Portafolio de {info['Nombre_Completo']}")
st.markdown(f"""
<div class='profile-wrapper'>
  <h2>✨ Comunicadora en formación creativa, visual y con vocación social</h2>
  <img src="{info['Foto']}" class="profile-pic-square"
       onerror="this.onerror=null;this.src='https://via.placeholder.com/240x240?text=Foto+no+disponible';">
</div>
""", unsafe_allow_html=True)

# -------------------- SOBRE MÍ --------------------
st.header("🌼 Sobre mí")
st.markdown(f"""
<div class='section-box'>
  <b>Pronombre:</b> {info['Pronombre']}<br>
  <b>Ciudad:</b> {info['Ciudad']}<br>
  <b>Correo:</b> <a href="mailto:{info['Correo']}">{info['Correo']}</a><br>
  <b>Instagram:</b> <a href="{info['Instagram']}">@{info['Instagram'].split('/')[-1]}</a><br><br>
  {info['Acerca_de']}
</div>
""", unsafe_allow_html=True)

# -------------------- DESCARGA DE CV --------------------
try:
    with open("CV_Angelina_Contreras.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    b64 = base64.b64encode(PDFbyte).decode()
    download_link = (
        f"<a href='data:application/octet-stream;base64,{b64}' "
        f"download='CV_Angelina_Contreras.pdf'>📄 Descargar mi CV</a>"
    )
except FileNotFoundError:
    download_link = "<i>📄 CV no disponible temporalmente</i>"

# -------------------- CONTACTO Y CIERRE --------------------
st.header("📬 Contacto y cierre")
st.markdown(f"""
<div class='section-box'>
  <h3>🌟 Gracias por visitar mi portafolio</h3>
  <p style='text-align: justify;'>
    Cada parte de este portafolio es una extensión de mi forma de ver, sentir y comunicar el mundo.
    Si te interesa colaborar, conocer más de mis proyectos o simplemente conversar sobre comunicación visual,
    puedes escribirme.
  </p>
  <ul>
    <li>📧 <b>Correo:</b> <a href="mailto:{info['Correo']}">{info['Correo']}</a></li>
    <li>📸 <b>Instagram:</b> <a href="{info['Instagram']}">{info['Instagram']}</a></li>
    <li>{download_link}</li>
  </ul>
  <p>✨ Sigo explorando, aprendiendo y creando cada día.</p>
</div>
""", unsafe_allow_html=True)

# -------------------- GALERÍA VISUAL --------------------
st.header("🖼️ Galería visual")
secciones = {
  "🎭 Expresión cultural": [
    ("baile", "Concursos culturales que conectan con mis raíces."),
    ("baile2", "El movimiento como forma de narrar."),
    ("teatro", "Comunicación a través del cuerpo y la voz.")
  ],
  "💚 Vida cotidiana": [
    ("felicidad en amistades", "Conexiones que inspiran mis relatos."),
    ("felicidad en cinamon", "Cine y café para reflexionar."),
    ("felicidad en cremolada", "Dulzura y calma en un bocado."),
    ("gaseosa inka cola", "Ícono popular y sentipensante.")
  ],
  "🎨 Creatividad visual": [
    ("guitarrra", "Armonía y ritmo en creación sonora."),
    ("medias", "Detalles que expresan personalidad."),
    ("victor jara", "Arte con consciencia social.")
  ],
  "🍽️ Cultura y sabor": [
    ("alegría en comida", "La comida como identidad y placer."),
    ("creación de kekes", "Estética y sabor familiar."),
    ("comida", "Observación de lo cotidiano en platos.")
  ],
  "🎬 Íconos": [
    ("star wars", "Narrativas épicas que inspiran."),
    ("pulp", "Estéticas alternativas y provocativas."),
    ("pulp+smirnoff", "Juego gráfico y humor visual.")
  ],
  "🌟 Comunidad": [
    ("empoderate.pe", "Comunicación para el empoderamiento juvenil."),
    ("actuar", "Empatía a través del rol y la expresión.")
  ]
}

for titulo, imagenes in secciones.items():
    with st.expander(titulo):
        filas = [imagenes[i : i+2] for i in range(0, len(imagenes), 2)]
        for fila in filas:
            cols = st.columns(len(fila))
            for col, (clave, descripcion) in zip(cols, fila):
                with col:
                    img_path = endorsements.get(clave)
                    if img_path:
                        st.image(
                            img_path,
                            use_container_width=True,
                            caption=descripcion
                        )
                    else:
                        st.warning(f"⚠️ Imagen no encontrada: {clave}")

# -------------------- BIOGRAFÍA PROFESIONAL --------------------
st.markdown("---")
st.header("📖 Biografía profesional")
with st.expander("👤 Todo sobre mí (perfil completo)", expanded=True):
    st.markdown("""
    <div class='section-box' style='text-align: justify; line-height: 1.6;'>
    """, unsafe_allow_html=True)
    st.subheader("💬 Quién soy")
    st.markdown("Soy una joven creativa e intuitiva que encuentra en la comunicación una forma de expresión sensible, política y estética.")
    st.subheader("📘 Formación académica")
    st.markdown("""
    - C.E.P. Patrocinio de San José  
    - Cibertec (Excel Expert, Word Expert, Inkscape y Corel Draw)  
    - UNI – Ingeniería Mecánica (Corel Draw)  
    - PUCP – Publicidad y Comunicaciones (ITS)  
    - Estudios Generales Letras y Ciencias Sociales  
    - PUCP Idiomas – Inglés hasta Intermedio 4
    """)
    st.subheader("💼 Experiencia profesional")
    st.markdown("""
    - Community manager en VMTeam SAC  
    - Voluntaria en Empoderate.Pe  
    - Proyectos audiovisuales y gráficos académicos  
    - Creación de documentales, entrevistas y reels reflexivos
    """)
    st.subheader("🛠️ Habilidades creativas")
    st.markdown("""
    - Edición de video (CapCut, Premiere Pro)  
    - Diseño gráfico (Canva, Illustrator)  
    - Storytelling visual e identidad de marca  
    - Escritura creativa y narrativa digital  
    - Curaduría estética de contenido
    """)
    st.subheader("🎨 Intereses visuales y personales")
    st.markdown("Me apasionan el baile, el diseño editorial, el teatro, la música y el arte cotidiano que cuenta historias.")
    st.subheader("🌟 Enfoque personal")
    st.markdown("Creo en una comunicación empática, cercana y comprometida con las realidades sociales.")
    st.subheader("🗂️ Proyectos personales")
    st.markdown("""
    - Mini documental sobre identidad y cultura visual  
    - Reel reflexivo sobre salud mental adolescente  
    - Diseño de publicaciones temáticas  
    """)
    st.subheader("🤝 Voluntariado")
    st.markdown("""
    - “Regálame una sonrisa”  
    - DOMUND  
    - Empoderate.Pe
    """)
    st.subheader("📌 Referencias")
    st.markdown("Disponibles si se solicitan.")
    st.markdown("</div>", unsafe_allow_html=True)
