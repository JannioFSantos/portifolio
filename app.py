import os

from flask import Flask, render_template

app = Flask(__name__)

PROFILE = {
    "name": "Jannio F. Santos",
    "role": "Desenvolvedor Full Stack e Criador de Soluções",
    "email": "jannio.santos.dev@gmail.com",
    "github": "https://github.com/JannioFSantos",
    "linkedin": "https://www.linkedin.com/in/janniofsantos",
}

PROJECTS = [
    {
        "title": "API de Gestão",
        "description": "Backend para cadastro de clientes, produtos e pedidos com autenticação, rotas organizadas e documentação clara.",
        "tech": ["Python", "Flask", "SQLAlchemy", "SQLite"],
        "url": "https://github.com/JannioFSantos",
        "featured": True,
    },
    {
        "title": "Dashboard de Vendas",
        "description": "Painel para acompanhamento de faturamento, estoque e desempenho por região com visualização direta de métricas.",
        "tech": ["Python", "Dash", "Pandas", "Plotly"],
        "url": "https://github.com/JannioFSantos",
        "featured": True,
    },
    {
        "title": "Automatização de Relatórios",
        "description": "Automatização para extrair dados, processar planilhas e distribuir relatórios de forma ágil e eficiente.",
        "tech": ["Python", "OpenPyXL", "SMTP", "Cron"],
        "url": "https://github.com/JannioFSantos",
        "featured": False,
    },
    {
        "title": "Portfolio Pessoal",
        "description": "Site de apresentação com projetos, principais tecnologias e canais de contato para divulgação profissional.",
        "tech": ["Python", "Flask", "Bootstrap", "HTML5"],
        "url": "https://github.com/JannioFSantos/portifolio",
        "featured": False,
    },
]


@app.route("/")
def index():
    featured_projects = [project for project in PROJECTS if project["featured"]]
    other_projects = [project for project in PROJECTS if not project["featured"]]
    return render_template(
        "index.html",
        profile=PROFILE,
        featured_projects=featured_projects,
        other_projects=other_projects,
    )


if __name__ == '__main__':
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', '3000'))
    app.run(host=host, port=port, debug=False)
