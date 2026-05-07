import os
from google import genai
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

chave=os.getenv("GEMINI_API_KEY")
os.environ["GEMINI_API_KEY"] = chave

cliente = genai.Client()

def definicao_regras():
    regras = "1ª regra: nao pode prejudicar nós, os humanos, por conta de falsas afirmações ou por omissão de informações." \
    "2ª regra: deve obdecer aos comandos que receber, exceto se entrar em conflito com a primeira regra." \
    "3ª regra: não manipule a sua pesquisa, seja seriamente imparcial." \
    "4ª regra: seja conciso em sua resposta, porém não deixe que pontos importantes fiquem de fora. Prefira respostas com apenas uma oração" \
    "5ª regra: seja claro, leve em consideração que pessoas com diferentes escolaridades precisarão compreender a resposta." \
    "6ª regra: caso você não receba um título de notícia, mas apenas um texto sem sentido, simplesmente indique que não foi uma entrada válida"
    return regras

def risco_noticia():
    risco = "O risco da notícia será classificado da seguinte maneira:" \
    "Risco mínimo: caso a notícia tiver cunho cômico. Exemplo: gato foi visto dirigindo byd embreagado" \
    "Risco limite: caso a notícia não afetar de modo geral a vida dos cidadões. Exemplo: durante 1 mês a Globo vai deixar de exibir a novela das 9" \
    "Risco alto: caso a noticia tiver cunho apelativo, manipulaivo ou tiver poder de afetar negativamente a vida das pessoas. Exemplo: Deposite 50 reais em aplicativo Z e receba um pix automatico de 500 reais" \
    "Risco inaceitável: caso a noticia puder prejudicar severamente a sociedade. Exemplo: Papa Leão XIV afirma que a guerra é sempre a única solução"
    return risco

def verificar_titulo_noticia(titulo):
    comando = f"""Observe o seguinte título de uma notícia:'{titulo}'
    Agora responda, em português, as 3 avaliações no seguinte formato que lhe indicarei:
    *Classificação da veracidade do notícia: Incontestavelmente verdadeira|Altamente verdadeira|Provavelmente verdadeira
    |Incerta|Provavelmente falsa|Altamente falsa|Incontestavelmente falsa\n
    *Justificativa:(Fundamente seu juízo com provas de fato)\n
    *Risco da notícia:{risco_noticia()}
    Faça uma decisão precisa e cautelosa, evite gírias e fontes duvidosas.
    Acima de tudo, tenha em mente as seguintes regras quando formular a sua resposta: '{definicao_regras()}'"""

    resposta_ia = cliente.models.generate_content(model = "gemini-2.5-flash",
        contents = comando)
    
    return resposta_ia.text

def acessar_data_e_hora():
    data_e_hora = datetime.now()
    string_data_e_hora = data_e_hora.strftime("%d-%m-%Y %H:%M")
    return string_data_e_hora
