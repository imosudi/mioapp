from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask import send_file
from flask import send_from_directory

from flask_bootstrap import Bootstrap
from flask_wtf import Form
from markupsafe import Markup # for the wtf form custom class
import pandas as pd
from cStringIO import StringIO
import StringIO
import io
import base64
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon


from cube2 import Cube
from logic import rubikOperation
from forms import rubikForm
from flaskapp import app



'''@app.route('/rubiksImage', methods = ['GET', 'POST'])
def fig2():
	num = rubikOperation()
	num = num.inputNbyNbyN()
	img = StringIO.StringIO()
	np.random.seed(42)
	fig = Cube(num, whiteplastic=True)
	#cubeName = "%dX%dX%d_Rubik's_Cubes.png" %(n, n, n)
	fig.render(flat=False).savefig(img, format='png')
	#fig.savefig(img, format='png')
	img.seek(0)
	plot_url = base64.b64encode(img.getvalue())
	#return send_file(img, mimetype='image/png')
	return render_template('rubiks_images.html', plot_url=plot_url, num=num)'''


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

