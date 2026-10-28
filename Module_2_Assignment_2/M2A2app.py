from flask import Flask, request, jsonify

app = Flask(__name__)

# GET endpoint
@app.get("/hello")

def hello():
	return jsonify({
	"message": "Welcome to my API!",
	"status": "success"
})

# POST endpoint
# This POST endpoint takes integers in a JSON format and outputs the sum of those integers
@app.post("/sum")
def calculateSum():
	
	data = request.get_json() # This line will take the JSON sent by the user
	
	if not isinstance(data, dict): # This checks that the input really is in JSON format
		return jsonify({"error": "Send a JSON argument"}), 400
	
	numbers = data.get("numbers", []) # This line looks for the list labeled with a "numbers" key in the JSON
	
	if not isinstance(numbers, list) or not numbers: # This line checks that numbers actually populate the JSON file
		return jsonify({"error": "Provide a list of numbers"}), 400
	
	total = sum(numbers) # Add the numbers in the JSON
    
	if not data:
		return jsonify({
        "error": "No JSON data provided"
        }), 400
	return jsonify({
"numbers": numbers,
"sum": total
})

if __name__ == "__main__":
	app.run(debug=True)