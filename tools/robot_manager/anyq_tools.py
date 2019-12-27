import requests
import json

def ask(question, robot_id, host="localhost", port=8999):
    url = "http://{}:{}/anyq?question={}&robot_id={}".format(host, port, question, robot_id)
    response = requests.get(url)
    data = json.loads(response.text)
    return data


