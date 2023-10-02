from flask import Flask, render_template, request, url_for, redirect
import random

app = Flask(__name__)
# generta ranodm number
random_number = random.randint(0,100)
print("random number is",random_number)
# creating empty list to save all guess
guesses = []

@app.route("/", methods=["POST","GET"])
def home():
	if request.method == "POST" :
		if request.form["number"] != '':
			guess = int(request.form["number"])
		massage = guessNumberFunction(guess, random_number)
		guesses.append(massage)
		print(guesses)
	return render_template("index.html", title="Home Page", guessUser=reversed(guesses))

@app.route('/reset')
def reset():
	random_number = random.randint(0,100)
	guesses = []
	return redirect(url_for("home"))

def guessNumberFunction(guess_number, computer_number):
	"""
	for check the guess number for the user and random number
	"""
	if guess_number < computer_number:
		return f"{guess_number} is to low"
	elif guess_number > computer_number:
		return f"{guess_number} is to high"
	else:
		return f"{guess_number} is correct"


if __name__ == "__main__":
	app.run(port=10, debug=True)