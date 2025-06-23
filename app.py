from flask import Flask, render_template
import requests
app = Flask(__name__)
@app.route('/')
def index():
    # Fetch data from the API
    response = requests.get('https://randomuser.me/api/?results=18')
    data = response.json()['results']
    print(data)
    # if response.status_code == 200 else {}
    # # Check if the data is empty
    # if not data or 'results' not in data:
    #     data = {'results': []}
    # data = data['results'] if 'results' in data else []
    # Render the template with the fetched data
    return render_template('index.html', data=data)
if __name__ == '__main__':
    app.run(debug=True)
