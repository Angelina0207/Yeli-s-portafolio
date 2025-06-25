import streamlit as st
from constants import info, embed_rss, endorsements

# -------------------- CONFIGURACIÓN GENERAL --------------------
st.set_page_config(page_title=f"Portafolio de {info['Nombre']}", page_icon="🌿", layout="wide")

# -------------------- ESTILO PERSONALIZADO --------------------
st.markdown("""
<style>
    body {
        background-color: #eafaf1;
        font-family: 'Segoe UI', sans-serif;
    }
    .block-container {
        padding: 2rem 3rem;
    }
    h1, h2, h3 {
        color: #1b5e20;
    }
    hr {
        border: 1px solid #a5d6a7;
    }
    .section-box {
        background-color: #ffffff;
        border: 2px solid #c8e6c9;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    }
    .profile-pic {
        border: 4px solid #66bb6a;
        border-radius: 50%;
        width: 220px;
        height: 220px;
        object-fit: cover;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        margin-bottom: 0.5rem;
    }
    img {
        border-radius: 10px;
        transition: transform .2s;
    }
    img:hover {
        transform: scale(1.04);
    }
</style>
""", unsafe_allow_html=True)

# -------------------- PORTADA --------------------
st.title(f"🌿 Portafolio de {info['Nombre_Completo']}")
st.markdown(f"### {info['Introducción']}")
st.markdown(f"""<img src='{info['Foto']}' class='profile-pic'>""", unsafe_allow_html=True)
st.markdown("---")

# -------------------- SOBRE MÍ --------------------
st.header("🌼 Sobre mí")
with st.container():
    st.markdown(f"""
    <div class='section-box'>
    <b>Pronombre:</b> {info['Pronombre']}  <br>
    <b>Ciudad:</b> {info['Ciudad']}  <br>
    <b>Correo:</b> <a href='mailto:{info['Correo']}'>{info['Correo']}</a>  <br>
    <b>Instagram:</b> <a href='{info['Instagram']}'>@{info['Instagram'].split('/')[-1]}</a>  <br><br>
    {info['Acerca_de']}
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -------------------- BIO PROFESIONAL --------------------
st.header("📖 Biografía profesional")
with st.expander("Ver más sobre mi trayectoria"):
    st.markdown("""
<div class='section-box'>
<b>💬 Quién soy</b><br>
Soy una joven creativa que encuentra en la comunicación una forma de expresión sensible, política y estética. Me gusta pensar visualmente, observar con empatía y actuar con propósito.
<br><br>
<b>📘 Formación</b><br>
- C.E.P. Patrocinio de San José  
- Cibertec (Excel Expert, Word Expert, Inkscape y Corel Draw)  
- Universidad Nacional de Ingeniería – Facultad de Ingeniería Mecánica (Corel Draw)  
- Estudiante de Publicidad y Comunicaciones en la Pontificia Universidad Católica del Perú (PUCP), modalidad ITS.  
- Cursos en Estudios Generales Letras y Ciencias Sociales  
- PUCP Idiomas – Inglés: desde nivel básico hasta intermedio 2
<br><br>
<b>💡 Experiencia</b><br>
- Community manager en VMTeam SAC.  
- Voluntaria activa en Empoderate.Pe.  
- Creadora de contenido social audiovisual.  
- Participación en concursos culturales de danza tradicional y teatro escolar.  
- Proyectos académicos y personales en narrativa digital.
<br><br>
<b>🛠️ Habilidades</b><br>
- Edición de video (CapCut, Premiere Pro)  
- Diseño gráfico (Canva, Illustrator)  
- Gestión de redes sociales con enfoque crítico  
- Escritura creativa y storytelling visual  
- Trabajo en equipo y liderazgo  
- Aprendizaje autónomo y rápido  
- Manejo de herramientas tecnológicas y plataformas digitales
<br><br>
<b>🎨 Intereses</b><br>
Baile, diseño, edición de videos, cultura visual, teatro, deportes y observación cotidiana.
<br><br>
<b>🌟 Enfoque personal</b><br>
Creo en una comunicación empática, cercana y comprometida con las realidades sociales. Me gusta narrar lo cotidiano con sensibilidad y diseñar con intención.
<br><br>
<b>🗂️ Proyectos personales</b><br>
- Mini documental sobre identidad y cultura visual (en desarrollo)  
- Reel reflexivo sobre salud mental adolescente  
- Diseño de publicaciones personalizadas para campañas temáticas
<br><br>
<b>🤝 Voluntariado</b><br>
- “Regálame una sonrisa”  
- DOMUND  
- Empoderate.Pe
<br><br>
<b>📌 Referencias</b><br>
Disponibles si se solicitan.
</div>
    """, unsafe_allow_html=True)

st.markdown("---")
