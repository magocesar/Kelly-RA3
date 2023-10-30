from flask import Flask, request, jsonify, render_template
from Py_Aux.CheckListCreator import CheckListCreator
from Py_Aux.CreateNc import CreateNc
from Py_Aux.EmailNc import EmailNc
import os

app = Flask(__name__, template_folder='TemplatesHtml')

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/handle_radio_data", methods=['POST'])
def handle_ratio_data():

    request_data = request.get_json()
    
    cc = CheckListCreator(request_data['perguntas'], request_data['respostas'], request_data['nome_projeto'])

    nc = CreateNc(request_data['perguntas'], request_data['respostas'], request_data['justificativas'], request_data['gravidades'], request_data['nome_projeto'], request_data['responsavel_projeto'], request_data['rqa_projeto'], request_data['acoes'], request_data["responsavel_escalonamento"])

    dir_nc, len_nc = nc.start()

    if dir_nc == False or len_nc == False:
        print("dir_nc or len_nc == False")
        return jsonify({'status': 'Error', 'message': "Verifique se algum arquivo .xlsx está aberto."})

    dir_cc = cc.start()

    if dir_cc == False:
        print("dir_cc == False")
        for file in os.listdir(dir_nc):
            os.remove(f"{dir_nc}/{file}")
        os.rmdir(dir_nc)
        return jsonify({'status': 'Error', 'message': "Verifique se algum arquivo .xlsx está aberto."})
    

    if(len_nc > 0):
        print("Precisa mandar email")
        email = EmailNc(request_data['nome_projeto'], request_data['responsavel_projeto'], request_data['rqa_projeto'], dir_nc, len_nc, request_data['email_nc'])
        if(request_data['precisa_escalonar'] == False):
            email.mandarEmail()
            return jsonify({'status': 'Success', 'message': "Arquivos criados com sucesso e email enviado.", 'dir_nc': dir_nc, 'len_nc': len_nc, 'dir_cc': dir_cc})
        else:
            email.mandarNcEscalonada(request_data['responsavel_escalonamento'], request_data['email_nc_escalonamento'])
            return jsonify({'status': 'Success', 'message': "Arquivos criados com sucesso e email enviado ao Supervisor.", 'dir_nc': dir_nc, 'len_nc': len_nc, 'dir_cc': dir_cc})

    else:
        return jsonify({'status': 'Success', 'message': "Arquivos criados com sucesso, nenhuma NC.", 'dir_nc': dir_nc, 'len_nc': len_nc, 'dir_cc': dir_cc})



if __name__ == "__main__":
    app.run(debug=True)