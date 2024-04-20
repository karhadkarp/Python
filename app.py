from flask import Flask, request, jsonify
from flask_cors import CORS
import email1
import customer_prompt

app = Flask(__name__)
CORS(app)


@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.json
    # Do something with the received data
    print("Received data:", data)
    prompt = ''
    temperature = ''
    # Print only the values
    for key, value in data.items():
        if key == "prompt":
            prompt = value
        if key == "temperature":
            temperature = value
        print("Prompt is: ", prompt)
        print("Temperature is: ", temperature)
    content = email1.multiturn_generate_content(prompt, temperature)
    print(content)
    return content


@app.route('/send_customer_data', methods=['POST'])
def send_customer_data():
    data = request.json
    # Do something with the received data
    print("Received data:", data)
    custom_prompt = ''
    customer_id = ''
    product_id = ''
    temperature = ''
    # Print only the values
    for key, value in data.items():
        if key == "product_id":
            product_id = value
        if key == "custom_prompt":
            custom_prompt = value
        if key == "customerId":
            customer_id = value
        if key == "temperature":
            temperature = value
        print("Temperature is: ", temperature)
    prompt = customer_prompt.getPrompt(customer_id, product_id, custom_prompt)
    content = email1.multiturn_generate_content(prompt, temperature)
    print(content)
    return content

@app.route('/products', methods=['POST'])
def get_products():
    data = request.json
    # Do something with the received data
    print("Received data:", data)
    customer_id = ''
    # Print only the values
    for key, value in data.items():
        if key == "customer_id":
            customer_id = value
    cust_name, sug_products = customer_prompt.get_customer_info(customer_id)
    print(cust_name)
    print(sug_products)
    return cust_name, sug_products

if __name__ == '__main__':
    app.run(debug=True)
