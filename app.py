import streamlit as st

st.set_page_config(page_title="Examen Bash Cisco", layout="centered")

st.title("🧪 Examen Práctico – Linux Bash & Shell Scripting")
st.subheader("Cisco Linux Fundamentals - Chapters 1 & 2")

st.write("Responde las siguientes preguntas. Al final obtendrás tu puntaje.")

score = 0

# -------------------------
# PREGUNTA 1
# -------------------------
st.markdown("### 1. ¿Qué hace el operador `>` en Linux?")

q1 = st.radio(
    "Selecciona una opción:",
    [
        "Concatena comandos",
        "Redirige salida sobrescribiendo un archivo",
        "Muestra ayuda del sistema",
        "Ejecuta un script en segundo plano"
    ]
)

if q1 == "Redirige salida sobrescribiendo un archivo":
    score += 1

# -------------------------
# PREGUNTA 2
# -------------------------
st.markdown("### 2. ¿Qué hace un pipe `|`?")

q2 = st.radio(
    "Selecciona una opción:",
    [
        "Guarda un archivo",
        "Conecta la salida de un comando con otro",
        "Elimina procesos",
        "Muestra usuarios conectados"
    ]
)

if q2 == "Conecta la salida de un comando con otro":
    score += 1

# -------------------------
# PREGUNTA 3
# -------------------------
st.markdown("### 3. ¿Qué comando muestra las primeras líneas de un archivo?")

q3 = st.radio(
    "Selecciona una opción:",
    ["tail", "head", "cat", "grep"]
)

if q3 == "head":
    score += 1

# -------------------------
# PREGUNTA 4
# -------------------------
st.markdown("### 4. ¿Qué significa `chmod +x script.sh`?")

q4 = st.radio(
    "Selecciona una opción:",
    [
        "Borra el script",
        "Ejecuta el script automáticamente",
        "Da permisos de ejecución al archivo",
        "Copia el archivo"
    ]
)

if q4 == "Da permisos de ejecución al archivo":
    score += 1

# -------------------------
# PREGUNTA 5
# -------------------------
st.markdown("### 5. ¿Qué hace `read` en un script Bash?")

q5 = st.radio(
    "Selecciona una opción:",
    [
        "Lee archivos del sistema",
        "Permite entrada del usuario",
        "Elimina variables",
        "Ejecuta comandos ocultos"
    ]
)

if q5 == "Permite entrada del usuario":
    score += 1

# -------------------------
# PREGUNTA 6 (CORTA)
# -------------------------
st.markdown("### 6. Escribe el comando para listar archivos del directorio actual")

q6 = st.text_input("Escribe tu respuesta:")

if q6.strip() == "ls" or q6.strip() == "ls -l":
    score += 1

# -------------------------
# RESULTADO
# -------------------------
st.markdown("---")

if st.button("📊 Calcular nota"):
    st.success(f"Tu puntuación final es: {score} / 6")

    if score == 6:
        st.balloons()
        st.write("🔥 Excelente trabajo")
    elif score >= 4:
        st.write("👍 Buen trabajo, pero puedes mejorar")
    else:
        st.write("📚 Necesitas repasar los conceptos básicos")
