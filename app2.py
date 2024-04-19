from flask import Flask, request, jsonify
from flask_cors import CORS
import email1
import RMDemo_GenAI_V3.1.2

app = Flask(__name__)
CORS(app)

@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.json    
    # Do something with the received data
    print("Received data:", data)
    prompt=''
    temperature=''
    # Print only the values
    for key,value in data.items():
        if key == "prompt" : 
            prompt = value
        if key == "temperature":
            temperature = value
        print("Prompt is: ", prompt)
        print("Temperature is: ", temperature)   
    content=email1.multiturn_generate_content(prompt,temperature)     
    print(content)
    return content


@app.route('/send_customer_data', methods=['POST'])
def send_customer_data():
    data = request.json    
    # Do something with the received data
    print("Received data:", data)
    customPrompt=''
    customerId=''
    temperature=''
    # Print only the values
    for key,value in data.items():
        if key == "prompt" : 
            customPrompt = value
        if key == "customerId":
            customerId = value
        if key == "temperature":
            temperature = value
        print("Temperature is: ", temperature)
    prompt = RMDemo_GenAI_V3.1.2.getPrompt(customerId, productId, customPrompt)
    content=email1.multiturn_generate_content(prompt,temperature)     
    print(content)
    return content   


if __name__ == '__main__':
    app.run(debug=True)

