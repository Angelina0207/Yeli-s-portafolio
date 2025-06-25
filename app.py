import streamlit as st
from constants import info, endorsements

# ---------- CONFIGURACIÓN GENERAL ----------
st.set_page_config(page_title=f" {info['Nombre']}", page_icon="🌿", layout="wide")

# ---------- ESTILO PERSONALIZADO ----------
st.markdown("""
<style>
body {
    background-color: #f3fdf6;
    font-family: 'Segoe UI', sans-serif;
}
h1, h2, h3 {
    color: #2e7d32;
}
.section {
    background-color: #ffffff;
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 2rem;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.05);
}
.image-card {
    background-color: #ffffff;
    padding: 1rem;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    text-align: center;
}
img {
    border-radius: 10px;
    transition: transform .2s;
}
img:hover {
    transform: scale(1.03);
}
a {
    color: #1b5e20;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------- PORTADA ----------
st.title(f"🌿 Portafolio de {info['Nombre_Completo']}")

st.markdown(f"""
<div style='text-align:center; margin: 2rem 0;'>
    <img src="{info['Foto']}" width="220" style="border: 5px solid #66bb6a; border-radius: 20px; box-shadow: 0 2px 12px rgba(0,0,0,0.15);">
    <h3 style='color:#388e3c; margin-top: 1rem;'>{info['Introducción']}</h3>
</div>
""", unsafe_allow_html=True)

# ---------- SOBRE MÍ ----------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🌸 Sobre mí")

st.markdown(f"""
**Pronombre:** {info['Pronombre']}  
**Ciudad:** {info['Ciudad']}  
**Correo:** [{info['Correo']}](mailto:{info['Correo']})  
**Instagram:** [@{info['Instagram'].split('/')[-1]}]({info['Instagram']})  

{info['Acerca_de']}
""")

st.markdown("</div>", unsafe_allow_html=True)

# ---------- GALERÍA VISUAL ----------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🖼️ Galería visual")

for seccion, items in {
    "🎭 Expresión cultural": ["baile", "baile2", "teatro"],
    "💚 Vida cotidiana": ["felicidad en amistades", "felicidad en cinamon", "felicidad en cremolada", "gaseosa inka cola"],
    "🎨 Creatividad visual": ["guitarrra", "medias", "victor jara"],
    "🍽️ Cultura y sabor": ["alegría en comida", "creación de kekes", "comida"],
    "🎬 Referentes e íconos": ["star wars", "pulp", "pulp+smirnoff"],
    "🌟 Acción y comunidad": ["empoderate.pe", "actuar"]
}.items():
    st.subheader(seccion)
    cols = st.columns(3)
    for i, clave in enumerate(items):
        with cols[i % 3]:
            st.markdown("<div class='image-card'>", unsafe_allow_html=True)
            st.image(endorsements[clave], use_column_width=True)
            st.caption(clave.capitalize())
            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------- BIO PROFESIONAL ----------
with st.expander("📖 Biografía profesional (ver más)", expanded=False):
    st.markdown("<div class='section'>", unsafe_allow_html=True)

    st.subheader("💬 Quién soy")
    st.markdown("Soy una joven creativa e intuitiva que encuentra en la comunicación una forma de expresión sensible, política y estética.")

    st.subheader("📘 Formación académica")
    st.markdown("""
- C.E.P. Patrocinio de San José  
- Cursos técnicos (Cibertec, UNI)  
- Estudiante en PUCP – Publicidad y Comunicación ITS  
- PUCP Idiomas – Inglés hasta Intermedio 4  
""")

    st.subheader("💼 Experiencia")
    st.markdown("""
- Community Manager en VMTeam SAC  
- Voluntaria activa en Empoderate.Pe  
- Proyectos audiovisuales y gráficos académicos
""")

    st.subheader("🛠️ Habilidades creativas")
    st.markdown("""
- Edición de video (CapCut, Premiere Pro)  
- Diseño gráfico (Canva, Illustrator)  
- Escritura creativa y storytelling visual
""")

    st.subheader("🌟 Enfoque personal")
    st.markdown("Creo en una comunicación empática y comprometida. Me gusta narrar lo cotidiano con sensibilidad y diseñar con intención.")

    st.subheader("📌 Proyectos")
    st.markdown("""
- Mini documental sobre cultura visual  
- Reel sobre salud mental adolescente  
- Publicaciones gráficas con enfoque social  
""")

    st.subheader("🤝 Voluntariado")
    st.markdown("""
- Regálame una sonrisa  
- DOMUND  
- Empoderate.Pe
""")

    st.subheader("📍 Referencias")
    st.markdown("Disponibles si se solicitan.")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- PIE DE PÁGINA ----------
st.markdown("""
<div style='text-align: center; padding: 1rem; font-size: 0.9rem; color: #888;'>
    Hecho con 💚 por Yeli | Streamlit
</div>
""", unsafe_allow_html=True)
