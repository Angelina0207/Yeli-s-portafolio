import streamlit as st
from constants import info, embed_rss, endorsements
import base64

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
        color: #2e7d32;
    }
    hr {
        border: 1px solid #a5d6a7;
    }
    .section-box {
        background-color: #ffffff;
        border: 2px solid #a5d6a7;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    }
    .profile-wrapper {
        background-color: #c8e6c9;
        padding: 2rem;
        margin-top: 1rem;
        margin-bottom: 2rem;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .profile-pic-square {
        border: 5px solid #66bb6a;
        border-radius: 16px;
        width: 240px;
        height: auto;
        object-fit: cover;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        margin-top: 1rem;
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
st.markdown(f"""
<div class='profile-wrapper'>
    <h2 style='color:#2e7d32;'>✨ Comunicadora en formación creativa, visual y con vocación social</h2>
    <img src="{info['Foto']}" class="profile-pic-square"
    onerror="this.onerror=null; this.src='https://via.placeholder.com/240x240?text=Foto+no+disponible';">
</div>
""", unsafe_allow_html=True)

# -------------------- SOBRE MÍ --------------------
st.header("🌼 Sobre mí")
st.markdown(f"""
<div class='section-box'>
<b>Pronombre:</b> {info['Pronombre']}  <br>
<b>Ciudad:</b> {info['Ciudad']}  <br>
<b>Correo:</b> <a href='mailto:{info['Correo']}'>{info['Correo']}</a>  <br>
<b>Instagram:</b> <a href='{info['Instagram']}'>@{info['Instagram'].split('/')[-1]}</a>  <br><br>
{info['Acerca_de']}
</div>
""", unsafe_allow_html=True)

# -------------------- DESCARGA DE CV --------------------
try:
    with open("CV_Angelina_Contreras.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
        b64 = base64.b64encode(PDFbyte).decode()
        download_link = f"<a href='data:application/octet-stream;base64,{b64}' download='CV_Angelina_Contreras.pdf'>📄 Descargar mi CV</a>"
except:
    download_link = "<i>📄 CV no disponible temporalmente</i>"

# -------------------- CONTACTO Y CIERRE --------------------
st.header("📬 Contacto y cierre")
st.markdown(f"""
<div class='section-box'>
<h3 style='color:#2e7d32;'>🌟 Gracias por visitar mi portafolio</h3>
<p style='text-align: justify;'>
Cada parte de este portafolio es una extensión de mi forma de ver, sentir y comunicar el mundo.
Si te interesa colaborar, conocer más de mis proyectos o simplemente conversar sobre comunicación visual, puedes escribirme.
</p>
<ul>
    <li>📧 <b>Correo:</b> <a href='mailto:{info['Correo']}'>{info['Correo']}</a></li>
    <li>📸 <b>Instagram:</b> <a href='{info['Instagram']}'>{info['Instagram']}</a></li>
    <li>{download_link}</li>
</ul>
<p>✨ Sigo explorando, aprendiendo y creando cada día.</p>
</div>
""", unsafe_allow_html=True)

# -------------------- GALERÍA VISUAL --------------------
st.header("🖼️ Galería visual")

secciones = {
    "🎭 Expresión cultural": [
        ("baile", "Participación en concursos culturales escolares que me conectaron con mis raíces y mi cuerpo."),
        ("baile2", "Una forma de expresión que habita el escenario y transmite emociones."),
        ("teatro", "Desde niña, el teatro me enseñó a comunicar con gestos y emociones.")
    ],
    "💚 Vida cotidiana": [
        ("felicidad en amistades", "Momentos de conexión que inspiran mis narrativas visuales."),
        ("felicidad en cinamon", "El cine y el café: espacios donde observo y reflexiono."),
        ("felicidad en cremolada", "La ternura de lo simple: una cremolada y una sonrisa."),
        ("gaseosa inka cola", "Ícono peruano que me conecta con lo popular y lo identitario.")
    ],
    "🎨 Creatividad visual": [
        ("guitarrra", "Experimentar el ritmo y la armonía, también desde el sonido."),
        ("medias", "Detalles únicos que expresan personalidad y juego visual."),
        ("victor jara", "Inspiración constante: arte con mensaje y sensibilidad social.")
    ],
    "🍽️ Cultura y sabor": [
        ("alegría en comida", "El acto de comer como espacio de identidad y disfrute."),
        ("creación de kekes", "Trabajo familiar con amor, estética y sabor."),
        ("comida", "Disfrutar lo cotidiano y observar cómo nos conecta.")
    ],
    "🎬 Íconos": [
        ("star wars", "Mi lado geek y visual se inspira en universos narrativos potentes."),
        ("pulp", "Contrastes visuales y culturas alternativas que me inspiran."),
        ("pulp+smirnoff", "Juego gráfico, estética y humor combinados.")
    ],
    "🌟 Comunidad": [
        ("empoderate.pe", "Organización que promueve derechos, donde aporto desde la comunicación."),
        ("actuar", "Habitar otros roles me ayuda a empatizar y observar el mundo.")
    ]
}

for titulo, imagenes in secciones.items():
    with st.expander(titulo):
        filas = [imagenes[i:i+2] for i in range(0, len(imagenes), 2)]
        for fila in filas:
            cols = st.columns(len(fila))
            for col, (clave, descripcion) in zip(cols, fila):
                with col:
                    img_path = endorsements.get(clave)
                    if img_path:
                        st.image(img_path, use_container_width=True, caption=descripcion)
                    else:
                        st.warning(f"⚠️ Imagen '{clave}' no encontrada.")
