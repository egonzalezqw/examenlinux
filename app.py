import streamlit as st

st.set_page_config(page_title="Examen Bash Cisco", layout="centered")

st.title("🧪 Examen Práctico – Linux Bash & Shell Scripting")
st.subheader("Cisco Linux Fundamentals - Chapters 1 & 2")

score = 0

# =========================
# 1 - 10: Shell Features
# =========================

st.markdown("## 📘 Advanced Shell Features")

q1 = st.radio("1. ¿Qué hace `>`?", [
    "Concatena comandos",
    "Redirige salida sobrescribiendo archivo",
    "Elimina archivos",
    "Ejecuta procesos"
])
if q1 == "Redirige salida sobrescribiendo archivo": score += 1

q2 = st.radio("2. ¿Qué hace `|`?", [
    "Conecta comandos",
    "Elimina archivos",
    "Copia texto",
    "Muestra usuarios"
])
if q2 == "Conecta comandos": score += 1

q3 = st.radio("3. ¿Qué hace `grep`?", [
    "Busca texto",
    "Ordena archivos",
    "Elimina procesos",
    "Crea directorios"
])
if q3 == "Busca texto": score += 1

q4 = st.radio("4. ¿Qué hace `head`?", [
    "Últimas líneas",
    "Primeras líneas",
    "Ordena datos",
    "Borra datos"
])
if q4 == "Primeras líneas": score += 1

q5 = st.radio("5. ¿Qué hace `tail`?", [
    "Primeras líneas",
    "Últimas líneas",
    "Crea archivos",
    "Edita scripts"
])
if q5 == "Últimas líneas": score += 1

q6 = st.radio("6. ¿Qué hace `cat`?", [
    "Muestra contenido",
    "Elimina archivos",
    "Crea usuarios",
    "Muestra procesos"
])
if q6 == "Muestra contenido": score += 1

q7 = st.radio("7. ¿Qué hace `wc`?", [
    "Cuenta líneas/palabras",
    "Busca texto",
    "Ordena archivos",
    "Copia archivos"
])
if q7 == "Cuenta líneas/palabras": score += 1

q8 = st.radio("8. ¿Qué hace `sort`?", [
    "Ordena datos",
    "Elimina duplicados",
    "Ejecuta scripts",
    "Muestra logs"
])
if q8 == "Ordena datos": score += 1

q9 = st.radio("9. ¿Qué hace `uniq`?", [
    "Elimina duplicados",
    "Ordena archivos",
    "Crea procesos",
    "Ejecuta comandos"
])
if q9 == "Elimina duplicados": score += 1

q10 = st.radio("10. ¿Qué hace `chmod +x`?", [
    "Borra archivo",
    "Da permisos de ejecución",
    "Copia archivo",
    "Edita archivo"
])
if q10 == "Da permisos de ejecución": score += 1


# =========================
# 11 - 15: Script Analysis (NUEVO)
# =========================

st.markdown("## 🧠 Análisis de Scripts (Bash)")

st.markdown("### Script 1")
st.code("""
#!/bin/bash
echo "Inicio"
echo "Fin"
""")

q11 = st.radio("11. ¿Qué hace este script?", [
    "No hace nada",
    "Imprime Inicio y Fin",
    "Elimina archivos",
    "Crea usuarios"
])
if q11 == "Imprime Inicio y Fin": score += 1


st.markdown("### Script 2")
st.code("""
#!/bin/bash
name="Ana"
echo "Hola $name"
""")

q12 = st.radio("12. ¿Qué salida genera?", [
    "Hola $name",
    "Hola Ana",
    "Error",
    "Nada"
])
if q12 == "Hola Ana": score += 1


st.markdown("### Script 3")
st.code("""
#!/bin/bash
for i in 1 2 3
do
  echo $i
done
""")

q13 = st.radio("13. ¿Qué imprime?", [
    "1 2 3 en una línea",
    "1 2 3 en líneas separadas",
    "Error",
    "Nada"
])
if q13 == "1 2 3 en líneas separadas": score += 1


st.markdown("### Script 4")
st.code("""
#!/bin/bash
if [ 5 -gt 3 ]
then
  echo "Mayor"
fi
""")

q14 = st.radio("14. ¿Qué imprime?", [
    "Menor",
    "Mayor",
    "Error",
    "Nada"
])
if q14 == "Mayor": score += 1


st.markdown("### Script 5")
st.code("""
#!/bin/bash
ls /noexiste
""")

q15 = st.radio("15. ¿Qué ocurre?", [
    "Lista archivos",
    "Error de directorio",
    "Crea carpeta",
    "Elimina archivos"
])
if q15 == "Error de directorio": score += 1


# =========================
# 16 - 24: Scripting
# =========================

st.markdown("## 📙 Shell Scripting")

q16 = st.radio("16. ¿Qué significa #!/bin/bash?", [
    "Comentario",
    "Intérprete del script",
    "Variable",
    "Error"
])
if q16 == "Intérprete del script": score += 1

q17 = st.radio("17. ¿Qué hace read?", [
    "Lee archivos",
    "Entrada usuario",
    "Elimina variables",
    "Imprime logs"
])
if q17 == "Entrada usuario": score += 1

q18 = st.radio("18. ¿Cómo defines variable?", [
    "var = 10",
    "var==10",
    "var=10",
    "set var"
])
if q18 == "var=10": score += 1

q19 = st.radio("19. ¿Cómo imprimes variable?", [
    "echo $var",
    "print var",
    "cat var",
    "show var"
])
if q19 == "echo $var": score += 1

q20 = st.radio("20. ¿Qué hace exit?", [
    "Inicia script",
    "Finaliza script",
    "Copia script",
    "Edita script"
])
if q20 == "Finaliza script": score += 1


# =========================
# 21 - 24: Linux básico
# =========================

q21 = st.radio("21. ¿Qué hace ls?", [
    "Lista archivos",
    "Cambia directorio",
    "Elimina archivos",
    "Muestra ruta"
])
if q21 == "Lista archivos": score += 1

q22 = st.radio("22. ¿Qué hace cd?", [
    "Lista archivos",
    "Cambia directorio",
    "Crea archivos",
    "Borra archivos"
])
if q22 == "Cambia directorio": score += 1

q23 = st.radio("23. ¿Qué hace pwd?", [
    "Ruta actual",
    "Lista archivos",
    "Borra archivos",
    "Crea scripts"
])
if q23 == "Ruta actual": score += 1

q24 = st.radio("24. ¿Qué hace touch?", [
    "Crea archivo",
    "Borra archivo",
    "Edita archivo",
    "Ejecuta script"
])
if q24 == "Crea archivo": score += 1


# =========================
# 25: Pregunta abierta
# =========================

st.markdown("## ✍️ Pregunta final")

q25 = st.text_input("25. Escribe el comando para mostrar archivos en formato detallado")

if q25.strip() in ["ls -l", "ls -la"]:
    score += 1


# =========================
# RESULTADO
# =========================

st.markdown("---")

if st.button("📊 Calcular nota"):
    st.success(f"Puntuación final: {score} / 25")

    if score == 25:
        st.balloons()
        st.write("🔥 Nivel experto")
    elif score >= 18:
        st.write("👍 Buen dominio")
    elif score >= 12:
        st.write("⚠️ Nivel básico-intermedio")
    else:
        st.write("📚 Necesita reforzar fundamentos")
