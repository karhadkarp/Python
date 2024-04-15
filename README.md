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

curl -X POST -H "Content-Type: application/json" -d '{"prompt": "can you prepare an e-mail for webinar on Generative AI on Sunday 10th April at 9 am. The target audience is anyone who is interested in learning Generative AI features. e-mail should contain text and images.", "temperature": "0.6"}' http://127.0.0.1:5000/send_data
