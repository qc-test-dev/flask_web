#!/usr/bin/python3
#from app import app
from flask import Flask
from flask import render_template
from flask import send_file
import glob,os
app=Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html',titulo="INICIO")

@app.route("/zte")
def zte():
	path="/home/usr_admin/flask_app/zte_repo/"
	mylist=os.listdir(path)
	#myfile="/home/usr_admin/flask_app/zte_repo1"
	for file in mylist:
		return '<a download="zte.txt" href="{path}/{file}">{file}</a>'.format(file=file,path=path)

@app.route("/repweb")
def repweb():
	path=("/home/usr_admin/flask_app/web_repo_auto/")
	repos=os.listdir(path)
	for file in repos:
		return '<a download="{file}" href="{path}/{file}">{file}</a>'.format(file=file,path=path)

def make_tree(path):
	tree = dict(name=os.path.basename(path), children=[])
	try: lst = os.listdir(path)
	except OSError:
		pass #ignore errors
	else:
		for name in lst:
			fn = os.path.join(path, name)
			if os.path.isdir(fn):
				tree['children'].append(make_tree(fn))
			else:
				tree['children'].append(dict(name=name))
	return tree

@app.route('/web_repo_auto')
def reportes():
	path=("/home/usr_admin/flask_app/web_repo_auto")
	return render_template('dirtree.html', tree=make_tree(path))

@app.route('/download')
def download():
	path=("/home/usr_admin/flask_app/web_repo_auto/prueba.txt")
	return send_file(path,as_attachment=True)
app.jinja_env.globals.update(download=download) 

if __name__=="__main__":
	app.run(host="0.0.0.0",debug=True)
