#importing flask
from flask import Flask, render_template, request
import weather
#creating variable named app
app = Flask(__name__)


#creates page
@app.route("/")
#creates function called hello, returns hello world, change string to change web text
def index():
	address = request.values.get('address')
	forecast = None
	#will only pass through function if there is an address
	if address:
		forecast = weather.get_weather(address)
	return render_template('index.html', forecast=forecast)

@app.route("/about")
def about():
	return render_template('about.html')


#necessary to get application to run 
if __name__ == "__main__":
	app.run()