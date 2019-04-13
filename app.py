from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')
	
@app.route("/downloads")
def downloads():
	return render_template('downloads.html')

@app.route("/darkweblinks")
def darkweblinks():
	return render_template('darkweblinks.html')

@app.route("/about")
def about():
	return render_template('about.html')
	 
@app.route("/destroypc")
def destroypc():
	return render_template('destroypc.html')

@app.route("/explosiverecipes")
def explosiverecipes():
	return render_template('explosiverecipes.html')
	
@app.route("/hateschool")
def hateschool():
	return render_template('hateschool.html')

if __name__ == "__main__":
		app.run(debug=True, host="0.0.0.0", port=80)