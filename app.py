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
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');

  body {
    background-color: #fff8e1; /* Fondo crema claro */
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #2e7d32; /* Verde oscuro para textos */
    margin: 0;
    padding: 0 1rem;
  }

  /* Letra moderna y grande para el título inicial */
  .profile-header {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 3.5rem;
    color: #1b5e20;
    margin-top: 1rem;
    margin-bottom: 0.3rem;
  }

  /* Mini descripción con letra más pequeña pero formal */
  .profile-subtitle {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 1.5rem;
    color: #388e3c;
    margin-top: 0;
  }

  .profile-wrapper {
    background: linear-gradient(135deg, #dcedc8, #c8e6c9);
    padding: 3rem 2rem;
    border-radius: 20px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.1);
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
  }

  .profile-pic-container {
    background-color: #a5d6a7; /* Verde suave para el cuadrado */
    padding: 10px;
    border-radius: 16px;
    width: 320px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.1);
    transition: box-shadow 0.3s ease;
    flex-shrink: 0;
  }

  .profile-pic-container:hover {
    box-shadow: 0 12px 32px rgba(0,0,0,0.2);
  }

  .profile-pic {
    border-radius: 12px;
    width: 300px;
    height: 300px;
    object-fit: cover;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .profile-pic:hover {
    transform: scale(1.07);
    box-shadow: 0 8px 24px rgba(0,0,0,0.25);
  }

  .intro-text {
    margin-left: 2rem;
    max-width: 600px;
  }

  .section-box {
    background: #fff;
    border: 2px solid #a5d6a7;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 2rem 0;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    color: #2e7d32;
  }

  h1, h2, h3 {
    color: #2e7d32;
  }

  a {
    color: #1b5e20;
    text-decoration: none;
  }

  a:hover {
    text-decoration: underline;
  }

  /* Sobre mí */
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

  /* Galería */
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

  /* Galería hover */
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

# -------------------- PORTADA --------------------
st.markdown(f"""
<div class="profile-wrapper">
    <div class="profile-pic-container">
        <img src="{info['Foto']}" alt="Foto de perfil" class="profile-pic">
    </div>
    <div class="intro-text">
        <h1 class="profile-header">🌿 {info['Nombre_Completo']}</h1>
        <p class="profile-subtitle">✨ {info['Introducción']}</p>
    </div>
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

with st.container():
    st.markdown('<div class="about-container">', unsafe_allow_html=True)
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
  📸 <a href="{info['Instagram']}" target="_blank">@{info['Instagram'].split('/')[-1]}</a>
</div>
""", unsafe_allow_html=True)

# -------------------- GALERÍA VISUAL --------------------
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
        for i in range(0, len(items), 4):
            cols = st.columns(4)
            for col, (clave, desc) in zip(cols, items[i:i+4]):
                img_path = endorsements.get(clave)
                if img_path:
                    col.image(img_path, caption=desc, use_container_width=False)
                else:
                    col.warning(f"⚠️⚠️ Imagen no encontrada: {clave}")
        st.markdown("</div>", unsafe_allow_html=True)

# -------------------- EMBED RSS --------------------
st.header("📰 Blog y artículos")
st.markdown(embed_rss["rss"], unsafe_allow_html=True)

# -------------------- CONSULTA PERSONALIZADA --------------------
st.markdown("---")
st.header("🔍 Consulta personalizada")

opciones_consulta = [
    "Selecciona un tema",
    "Experiencia profesional",
    "Habilidades creativas",
    "Proyectos destacados",
    "Contacto"
]

seleccion = st.selectbox("¿Sobre qué quieres saber más?", opciones_consulta)

if seleccion == "Experiencia profesional":
    st.write("""
    - Community Manager en VMTeam SAC  
    - Voluntaria en Empoderate.Pe  
    - Creación de documentales, entrevistas y reels reflexivos  
    - Proyectos audiovisuales y gráficos académicos
    """)
elif seleccion == "Habilidades creativas":
    st.write("""
    - Edición de video (CapCut, Premiere Pro)  
    - Diseño gráfico (Canva, Illustrator)  
    - Storytelling visual e identidad de marca  
    - Escritura creativa y narrativa digital  
    - Curaduría estética de contenido
    """)
elif seleccion == "Proyectos destacados":
    st.write("""
    Aquí puedes destacar algunos proyectos importantes, como:  
    - Documental sobre participación juvenil  
    - Campañas visuales para Empoderate.Pe  
    - Gestión creativa de redes sociales para VMTeam SAC  
    - Series de reels con mensajes reflexivos
    """)
elif seleccion == "Contacto":
    st.markdown(f"""
    📧 Correo: <a href="mailto:{info['Correo']}">{info['Correo']}</a><br>
    📸 Instagram: <a href="{info['Instagram']}" target="_blank">@{info['Instagram'].split('/')[-1]}</a>
    """, unsafe_allow_html=True)




