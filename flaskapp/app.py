from flask import Flask, render_template
import os

app = Flask(__name__)

template_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Weblap'))

app.template_folder = template_path

@app.route('/')
def hello():
    return render_template('adminlog.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
