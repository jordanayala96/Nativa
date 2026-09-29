# Nativa — versión para Streamlit

Esta versión conserva el diseño HTML, CSS y JavaScript de Nativa, pero incorpora un archivo principal de Python para publicarla en Streamlit Community Cloud.

## Ejecutarla en Visual Studio Code

Abre esta carpeta en Visual Studio Code y ejecuta en el terminal:

```powershell
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Streamlit abrirá automáticamente la página. Si no ocurre, entra en:

```text
http://localhost:8501
```

Para detenerla, presiona `Ctrl + C` en el terminal.

## Publicarla en Streamlit Community Cloud

1. Sube esta carpeta completa a un repositorio de GitHub.
2. Entra en `https://share.streamlit.io` e inicia sesión con GitHub.
3. Selecciona **Create app** o **New app**.
4. Escoge el repositorio y la rama `main`.
5. En **Main file path**, escribe `streamlit_app.py`.
6. Elige el subdominio deseado y presiona **Deploy**.

## Archivos principales

- `streamlit_app.py`: prepara y muestra el sitio dentro de Streamlit.
- `index.html`: textos y estructura visual.
- `styles.css`: paleta, diseño y adaptación a celulares.
- `script.js`: menú, filtros, galería, modal y conexión con WhatsApp.
- `assets/`: fotografías optimizadas.
- `requirements.txt`: dependencia necesaria para el despliegue.

## WhatsApp configurado

Los botones abren el número `+593 98 481 3531`. El valor técnico se encuentra en `script.js` como `593984813531`.

## Paleta de colores

Las variables están al inicio de `styles.css`, dentro de `:root`. Puedes cambiar la identidad completa modificando `--color-ink`, `--color-paper`, `--color-surface`, `--color-accent`, `--color-accent-strong`, `--color-gold`, `--color-rose` y `--color-muted`.
