# O Lobinho <img alt="html" src="https://img.shields.io/badge/Html-blue?style=for-the-badge&logo=html&logoColor=white" /> <img alt="css" src="https://img.shields.io/badge/Css-orange?style=for-the-badge&logo=css&logoColor=white" /> <img alt="python" src="https://img.shields.io/badge/Python-green?style=for-the-badge&logo=python&logoColor=white" /> <img alt="MIT" src="https://img.shields.io/badge/MIT-red?style=for-the-badge&logo=mit&logoColor=white" />
### Site com Gemini API que detecta se uma notícia, de acordo com o título, é falsa ou não

## Tabela de conteúdos
- [Concepção do site](#concepção-do-site)
- [Páginas](#páginas)
- [Como utilizar](#como-utilizar)
  

# Concepção do site
Esse site foi criado com o propósito de mostrar que a IA também pode minimizar o problema das falsas notícias. O teste Lobinho tem como entrada o título de uma notícia, e essa notícia passa por uma verificação do Gemini para responder as seguintes três perguntas: veracidade da notícia, risco da notícia e a justificativa que comprove a classificação da notícia.

As classificações do risco da notícia foram baseadas na pirâmide de risco do AI Act, como forma de estabelecer uma base mais profunda no prompt do Gemini.

Ademais, para o fronted foi utilizado o Css e o HTML, enquanto no backend foi utilizado o Python e o Flask para permitir a conexão entre o backend e o frontend.

# Páginas
O site Lobinho possui 3 páginas:
- Página inicial
- Páginia de verificação da notícia
- Página Sobre

<img width="1918" height="2904" alt="paginas" src="https://github.com/user-attachments/assets/d88baee4-649c-4d14-a9b2-cba5eae309bf" />


#### O visual do site foi criado tendo em vista o critério de fazer com que ele fosse utilizado por qualquer pessoa, ou seja, algo que pudesse ser utilizado publicamente. Então, foi preferível cores destacadas, fontes legíveis e textos auto explicatíveis. O lobo foi utilizado como metáfora para a mentira, uma vez que o lobsomem precisar convencer as pessoas (através da mentira e manipulação) de que não é um lobsomem.

# Como utilizar

Para ter acesso ao site, recomendo que baixe o repositório, abra com o Visual Code e dê run no arquivo main.py, que é exatamente onde fica o Flask.
