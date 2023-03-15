from flask import Flask, render_template, redirect, session, request
from perguntas import perguntas
import wikipedia
wikipedia.set_lang('pt')

app = Flask(__name__)
app.secret_key = 'secret_key'

questao = 1

@app.route('/', methods=['GET', 'POST'])
def index():
    global questao
    pergunta1 = perguntas[f"{questao}"][0]
    pergunta2 = perguntas[f"{questao}"][1]
    return render_template('teste.html', pergunta1=pergunta1, pergunta2=pergunta2)

@app.route('/resposta', methods=["POST"])
def resposta():
    global questao
    global ordem   
    selected_option = request.form.get("flexRadioDefault")
    match questao:
        case 1:
            if selected_option == "pergunta1":
                questao = 2
            if selected_option == "pergunta2":
                questao = 10

        case 2:
            if selected_option == "pergunta1":
                    questao = 9
            if selected_option == "pergunta2":
                    questao = 3

        case 3:
            if selected_option == "pergunta1":
                    ordem = 'Dermaptera'
                    questao = 28
            if selected_option == "pergunta2":
                    questao = 4

        case 4:

            if selected_option == "pergunta1":
                ordem = 'Hemiptera'
                questao = 28
            if selected_option == "pergunta2":
                questao = 5

        case 5:
            if selected_option == "pergunta1":
                    ordem = 'Coleoptera'
                    questao = 28
            if selected_option == "pergunta2":
                    questao = 6

        case 6:
            if selected_option == "pergunta1":
                    ordem = 'Orthoptera'
                    questao = 28
            if selected_option == "pergunta2":
                    questao = 7

        case 7:
            if selected_option == "pergunta1":
                    ordem = 'Mantodea'
                    questao = 28
            if selected_option == "pergunta2":
                    questao = 8

        case 8:
            if selected_option == "pergunta1":
                    ordem = 'Phasmatodea'
                    questao = 28
            if selected_option == "pergunta2":
                    ordem = 'Blattodea'
                    questao = 28

        case 9:
            if selected_option == "pergunta1":
                    ordem = 'Orthoptera'
                    questao = 28
            if selected_option == "pergunta2":
                    ordem = 'Strepsiptera'
                    questao = 28

        case 10:
            if selected_option == "pergunta1":
                    questao = 11
            if selected_option == "pergunta2":
                    questao = 13

        case 11:
            if selected_option == "pergunta1":
                    questao = 12
            if selected_option == "pergunta2":
                    ordem = 'Diptera'
                    questao = 28

        case 12:
            if selected_option == "pergunta1":
                    ordem = 'Hemiptera'
                    questao = 28
            if selected_option == "pergunta2":
                    ordem = 'Ephemeroptera'
                    questao = 28

        case 13:
            if selected_option == "pergunta1":
                    questao = 21
            if selected_option == "pergunta2":
                    questao = 14

        case 14:
            if selected_option == "pergunta1":
                    questao = 15
            if selected_option == "pergunta2":
                    questao = 22

        case 15:
            if selected_option == "pergunta1":
                    ordem = 'Hemiptera'
                    questao = 28
            if selected_option == "pergunta2":
                    questao = 16

        case 16:
            if selected_option == "pergunta1":
                    ordem = 'Embiidina'
                    questao = 28
            if selected_option == "pergunta2":
                    questao = 17

        case 17:
            if selected_option == "pergunta1":
                    ordem = 'Odonata'
                    questao = 28
            if selected_option == "pergunta2":
                    questao = 18

        case 18:
            if selected_option == "pergunta1":
                    ordem = 'Isoptera'
                    questao = 28
            if selected_option == "pergunta2":
                    questao = 19

        case 19:
            if selected_option == "pergunta1":
                    ordem = 'Zoraptera'
                    questao = 28
            if selected_option == "pergunta2":
                    questao = 20

        case 20:
            if selected_option == "pergunta1":
                    ordem = 'Thysanopetera'
                    questao = 28
            if selected_option == "pergunta2":
                    ordem = 'Pscopetera'
                    questao = 28

        case 21:
            if selected_option == "pergunta1":
                    ordem = 'Plecoptera'
                    questao = 28
            if selected_option == "pergunta2":
                    ordem = 'Ephemeroptera'
                    questao = 28

        case 22:
            if selected_option == "pergunta1":
                    questao = 23
            if selected_option == "pergunta2":
                    questao = 24

        case 23:
            if selected_option == "pergunta1":
                    ordem = 'Lepidoptera'
                    questao = 28
            if selected_option == "pergunta2":
                    ordem = 'Trichoptera'
                    questao = 28

        case 24:
            if selected_option == "pergunta1":
                    ordem = 'Hymenoptera'
                    questao = 28
            if selected_option == "pergunta2":
                    questao = 25

        case 25:
            if selected_option == "pergunta1":
                    questao = 26
            if selected_option == "pergunta2":
                    ordem = 'Mecoptera'
                    questao = 28

        case 26:
            if selected_option == "pergunta1":
                    questao = 27
            if selected_option == "pergunta2":
                    ordem = 'Neuropetera'
                    questao = 28

        case 27:
            if selected_option == "pergunta1":
                    ordem = 'Megaloptera'
                    questao = 28
            if selected_option == "pergunta2":
                    ordem = 'Raphidoptera'
                    questao = 28
    if questao == 28:
        return redirect('ordem_inseto')
    else:
        return redirect('/')

@app.route('/zerar', methods=["POST","GET"])
def zerar():
    global questao
    questao = 1
    return redirect('/')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/ordem_inseto')
def ordem_inseto():
    global ordem
    def returnimage(pagina_inseto):
        check = True
        cont = 0
        while(check):
            if(('jpg' in str(pagina_inseto.images[cont]) or 'png' in str(pagina_inseto.images[cont]))):
                check = False
            else:
                cont = cont + 1
        return pagina_inseto.images[cont]
    pagina_inseto = wikipedia.page(ordem)
    imagem_inseto = returnimage(pagina_inseto)
    descricao_inseto = wikipedia.summary(ordem)
    return render_template('ordem.html', descricao_inseto=descricao_inseto, ordem = ordem, imagem_inseto = imagem_inseto)

if __name__ == "__main__":
    app.run(debug=True)

#teste
#teste2