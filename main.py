import os
from flask import Flask, render_template, request
import teste_lobinho as lobinho
from dotenv import set_key, load_dotenv
app = Flask(__name__)
load_dotenv()


@app.route('/')
def home():
    return render_template('index.html', teste_lobinho_mais_recente=os.getenv("TESTE_MAIS_RECENTE"))

@app.route('/verificacao')
def verificacao():
    return render_template('verificacao.html')

@app.route('/verificar', methods=['POST'])
def acessar_titulo_noticia():
    titulo_noticia=request.form.get("noticia")
    print("O titulo da notícia é",titulo_noticia)
    return é_lobinho(titulo_noticia)

@app.route('/resultado')
def é_lobinho(titulo_noticia):
    ultimo_teste = titulo_noticia," | ",lobinho.acessar_data_e_hora()
    set_key(".env","TESTE_MAIS_RECENTE",str(ultimo_teste))
    resultado=lobinho.verificar_titulo_noticia(titulo_noticia)
    return render_template("resultado.html",resultado_lobinho=resultado)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run(debug=True)