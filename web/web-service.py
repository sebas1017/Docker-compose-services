import logging
from flask import Flask, render_template, request, redirect

import requests
import json
import logging
app =  Flask(__name__)

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)



@app.route("/")
def home():
    try:
        url = f"http://api-service:{81}/"
        res = requests.get(url).json()
        return render_template("table-with-pagination.html", profiles=res)
    except requests.exceptions.HTTPError as err:
        app.logger.debug(err)
        raise SystemExit(err)
    
@app.route("/admin")
def admin():
    return render_template("admin.html",context={})

@app.route('/home_page', methods=['GET'])
def shortenurl():
    if request.method == 'GET':
        return redirect('/')


@app.route("/admin/delete_records")
def delete_records():
    try:
        url = f"http://api-service:{81}/admin/borrar_registros"
        res = requests.get(url).json()
        return redirect("/admin")
    except Exception:
        return {"message":"registros eliminados correctamente"}

@app.route("/admin/create_records")
def create_records():
    url = f"http://api-service:{81}/admin/crear_registros"
    res = requests.get(url).json()
    return redirect("/admin")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=82, debug=True)