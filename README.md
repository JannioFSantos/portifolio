# Portfólio Pessoal em Flask

Este projeto é um portfólio profissional criado com Python e Flask para apresentar minhas habilidades, projetos e formas de contato.

## Sobre o projeto

A aplicação foi desenvolvida para funcionar como uma landing page moderna de apresentação pessoal, com:

- seção de apresentação profissional
- destaque para projetos em destaque
- lista de tecnologias e stack
- links para GitHub, LinkedIn e contato
- layout responsivo para desktop e mobile

## Stack utilizada

- Python
- Flask
- HTML5
- CSS3
- Git / GitHub

## Estrutura do projeto

```bash
portfolio-flask/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── static/
│   └── css/
│       └── style.css
└── templates/
    └── index.html
```

## Como executar localmente

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

A aplicação ficará disponível em:

```text
http://localhost:5000
```

## Deploy no Coolify

Para usar em um ambiente de produção no Coolify, o projeto já foi ajustado para ler a porta via variável de ambiente `PORT`.

Exemplo de configuração no painel do Coolify:

- Build command: `pip install -r requirements.txt`
- Start command: `python app.py`
- Porta: `5000` ou use a variável `PORT` do ambiente

## Personalização

Você pode alterar facilmente:

- nome, bio e links de contato em `templates/index.html`
- dados dos projetos em `app.py`
- estilo visual em `static/css/style.css`

## Autor

Jannio F. Santos

## Licença

Este projeto é destinado a uso pessoal e profissional.
