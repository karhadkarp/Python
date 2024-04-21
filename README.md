# Python
#Create virtaul environment
python -m venv .
# Activate the virtual environment (on Windows)
myenv\Scripts\activate

pip install -r ./requirements.txt


$ gcloud config list

[compute]
region = asia-south1
zone = asia-south1-b
[core]
account = dilsedigital007@gmail.com
project = starlit-zoo-420014


gcloud auth application-default login
curl -X POST -H "Content-Type: application/json" -d '{"customer_id": "15634602"}' http://35.244.22.147:8081/products

curl -X POST -H "Content-Type: application/json" -d '{"prompt": "can you prepare an e-mail for webinar on Generative AI on Sunday 10th April at 9 am. The target audience is anyone who is interested in learning Generative AI features. e-mail should contain text and images.", "temperature": "0.6"}' http://35.244.22.147:8081/send_data


curl -X POST -H "Content-Type: application/json" -d '{"customer_id": "15737888","product_id": "3", "temperature": "0.6","custom_prompt" : "This should be in html format"}' http://35.244.22.147:8081/send_customer_data
-------------------

ON GCP VM :
sudo apt-get update
sudo apt-get install python3-setuptools python3 build-essential pip3

set PATH=$PATH:/usr/bin
export PATH=$PATH:/usr/bin


sudo apt install python3.11-venv

dilsedigital007@instance-dilsedigital:~/GenerateContent$ pwd
/home/dilsedigital007/GenerateContent
dilsedigital007@instance-dilsedigital:~/GenerateContent$ python3 -m venv .

source ./bin/activate

pip3 install -r ./requirements.txt

curl -X POST -H "Content-Type: application/json" -d '{"prompt": "can you prepare an e-mail for webinar on Generative AI on Sunday 10th April at 9 am. The target audience is anyone who is interested in learning Generative AI features. e-mail should contain text and images.", "temperature": "0.6"}' http://35.244.22.147:5000/send_data

