#!/usr/bin/python3
#from app import app
from flask import Flask
from flask import render_template
from flask import send_file
from flask import url_for
import glob,os
app=Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template('home.html',titulo="INICIO")

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

@app.route('/zte_repo')
def zte_repo():
	path=("/home/usr_admin/flask_app/static/zte_repo")
	return render_template('dirtree.html', tree=make_tree(path))

@app.route('/auto_reportes')
def auto_reportes():
        path=("/home/usr_admin/flask_app/static/auto_reportes")
        return render_template('reportes_dirtree.html', tree=make_tree(path))

if __name__=="__main__":
	app.run(host="0.0.0.0",debug=True)
