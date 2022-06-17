**Proyecto Flask QC**
"""sitio web desarrollado en flask,jinja2,gunicorn3(webapp), server nginx"""
-Flask v2
-Pip3
-gunicorn3(sudo gunicorn3 app:app --daemon)
-nginx(puerto:8000)

*ver requirements.txt



**templates folder**
"""Guardar aqui los archivos  .html, agregar ruta html en app.py"""

**app.py**
"""Aplicación python, corriendo flask, aqui añadir rutas @app.route para nodos web"""

**@app.routes()**
-home(index)-web QC Home
-zte_repo-repositorio versiones ZTE


**git ignore files**
"""siempre omitir folder bk,static y flaskenv""
"""añadir archivos o directorios para no ser agregados a repo git"""

**static folder**
"""archivos estaticos, js,descargas""



**git branches**
-main
-dev(siempre usar dev)
