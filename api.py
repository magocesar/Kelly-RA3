from flask import Flask, request, jsonify, render_template
from Py_Aux.CheckListCreator import CheckListCreator

app = Flask(__name__, template_folder='TemplatesHtml')

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/handle_radio_data", methods=['POST'])
def handle_ratio_data():

    request_data = request.get_json()
    
    cc = CheckListCreator(request_data['perguntas'], request_data['respostas'])

    cc.start()

    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)