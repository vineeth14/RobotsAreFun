from flask import Flask, render_template,flash, send_from_directory, request
from forms import LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] ='1'

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route("/ctfsarefun")
def ctf():
	return render_template('flag.html')
@app.route("/login",methods=['GET','POST'])
def login():
	form= LoginForm()
	if form.validate_on_submit():
		flash(f'Successfullylogged in as  {form.username.data}!','success')
	return render_template('login.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)