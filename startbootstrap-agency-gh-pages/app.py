from flask import *
from flask import render_template
import json
import requests
from flask import request
from database import *
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hompage():
	all_my_stories = query_all()
	return render_template("index.html",all_my_stories=all_my_stories)

@app.route('/adventure',methods=['GET', 'POST'])
def adventure():
	if request.method == 'POST':
		name = request.form['firstname']
		story1 = request.form['story']
		story(name,story1)
		return redirect(url_for('hompage'))

	return render_template("story.html")

@app.route('/study', methods = ['POST','GET'])
def study():
    print('is this working')
    image_url = request.form['picture']
    headers = {'Authorization': 'Key f1516afefe384e3ea7ac095cfb9eccdc'}
    api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"
    data ={"inputs": [
      {
        "data": {
          "image": {
            "url": image_url
          }
        }
      }
    ]}

    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    response_dict = json.loads(response.content)
    responses = response_dict["outputs"][0]["data"]["concepts"]

    return render_template('index.html', results=responses)


if __name__ == '__main__':
    app.run(debug=True,port=3000)