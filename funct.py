from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    number = data['number']
    
    # Replace the following code with your own Python function
    # Modify this function to perform the desired calculations
    def your_python_function(input_number):
        # Example: Multiply the input number by 2
        return input_number * 2
    
    result = your_python_function(number)
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()
