# Test file for testing the modules in flask

from app import flask_app

# test function 01
def test_01():
	print("This is the test function in the src module")
	print("-------- Exiting from here ---------- ")

def test_02():
	print("Printing config from the config.py file")
	# debug_option = app.config["CLIENTSECRETS_LOCATION"]

	print(flask_app.config)

	path = flask_app.instance_path
	print(path)
	print("---------Debugging report here------------")

	print(flask_app.config["DEBUG"])

	debug_option = flask_app.config["CLIENTSECRETS_LOCATION"]
	print(debug_option)
	print("-------- Exiting from test02 function ---------- ")
