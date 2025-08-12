# RecetasApp (Flask + PWA)

## Ejecutar local
1. Crear virtualenv y activar:
   - `python -m venv venv`  
   - Windows: `venv\Scripts\activate`  
   - mac/linux: `source venv/bin/activate`
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar: `python app.py`
4. Abrir en el navegador: `http://127.0.0.1:5000`

> Para probar PWA en local usa HTTPS o abre Chrome con flag que permita service workers en HTTP (no recomendado). Es mejor desplegar en Render/Heroku/PythonAnywhere para probar en móvil.

## Despliegue rápido (Render)
1. Subir este repositorio a GitHub.
2. Crear cuenta en Render y conectar el repo.
3. Crear un "Web Service" que ejecuta `python app.py` y exponga el puerto `5000`.
4. Render proveerá HTTPS automáticamente — ahora las funciones PWA y SW funcionarán en móvil.

## Despliegue en PythonAnywhere (opción sin Docker)
1. Crear cuenta en PythonAnywhere (free tiene limitaciones).  
2. Subir archivos (o conectar con GitHub).  
3. Configurar web app desde el panel, apuntando a `app.py`.
4. PythonAnywhere ya sirve con HTTPS para cuentas con pago. En free puede haber limitaciones con HTTPS — por eso recomiendo Render para PWA completa.