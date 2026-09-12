import os

from flask import Flask, render_template

app = Flask(__name__)

PROFILE = {
    "name": "Jannio F. Santos",
    "role": "Desenvolvedor Full Stack · Python · Automação · Sistemas Web",
    "email": "jannio.santos.dev@gmail.com",
    "github": "https://github.com/JannioFSantos",
    "linkedin": "https://www.linkedin.com/in/janniofsantos",
}

PROJECTS = [
    {
        "title": "Gestão Contábil",
        "description": "Plataforma web para escritórios contábeis, com gestão de clientes, documentos, mensagens, avisos e portal do cliente.",
        "tech": ["Next.js", "TypeScript", "Prisma", "PostgreSQL", "NextAuth"],
        "url": "https://github.com/JannioFSantos/gest-oClienteContabil",
        "featured": True,
    },
    {
        "title": "Gerador de Etiquetas de Preço",
        "description": "Aplicação web para transformar planilhas Excel em etiquetas prontas para impressão, com pré-visualização, personalização e exportação para PDF.",
        "tech": ["React", "TypeScript", "Tailwind CSS", "SheetJS", "jsPDF"],
        "url": "https://github.com/JannioFSantos/geradorEtiquetas",
        "featured": True,
    },
    {
        "title": "Consulta de Preços",
        "description": "Sistema Flask otimizado para dispositivos móveis que consulta preços por código ou descrição diretamente a partir de uma planilha Excel.",
        "tech": ["Python", "Flask", "OpenPyXL", "HTML/CSS"],
        "url": "https://github.com/JannioFSantos/apppreco",
        "featured": True,
    },
    {
        "title": "Consulta NCM por GTIN",
        "description": "Aplicação web para consulta de produtos por GTIN, exibindo informações como descrição, NCM, CEST, marca, embalagem e foto.",
        "tech": ["Python", "Flask", "REST API", "HTML/CSS"],
        "url": "https://github.com/JannioFSantos/consultaNCMporGTIN",
        "featured": True,
    },
    {
        "title": "Conversor de CF-e para Excel",
        "description": "Ferramenta de automação para converter dados de arquivos XML de CF-e em planilhas Excel, facilitando análise e tratamento das informações.",
        "tech": ["Python", "XML", "Excel", "Automação"],
        "url": "https://github.com/JannioFSantos/conversorxml",
        "featured": False,
    },
    {
        "title": "Downloader de NF-e",
        "description": "Automação com Selenium para realizar consultas e baixar arquivos XML de NF-e, com interface gráfica e acompanhamento do processamento.",
        "tech": ["Python", "Selenium", "Automação", "GUI"],
        "url": "https://github.com/JannioFSantos/DownloadXMLNf-e",
        "featured": False,
    },
    {
        "title": "CRM com Django",
        "description": "Projeto de CRM desenvolvido com Django, incluindo autenticação, banco de dados, área administrativa e estrutura para gerenciamento de informações.",
        "tech": ["Python", "Django", "SQLite", "HTML/CSS"],
        "url": "https://github.com/JannioFSantos/CRM-basico-com-Django",
        "featured": False,
    },
    {
        "title": "Automação de Documentos Word",
        "description": "Ferramenta para geração e atualização em lote de documentos Word a partir de modelos e campos variáveis.",
        "tech": ["Python", "Automação", "Microsoft Word"],
        "url": "https://github.com/JannioFSantos/alteraWordEmLote",
        "featured": False,
    },
]

PRIVATE_PROJECTS_NOTE = {
    "title": "Projetos privados",
    "description": "Também desenvolvo soluções proprietárias e projetos de uso interno. Por questões de confidencialidade, detalhes, código e repositórios privados não são publicados.",
}


@app.route("/")
def index():
    featured_projects = [project for project in PROJECTS if project["featured"]]
    other_projects = [project for project in PROJECTS if not project["featured"]]
    return render_template(
        "index.html",
        profile=PROFILE,
        featured_projects=featured_projects,
        other_projects=other_projects,
        private_projects_note=PRIVATE_PROJECTS_NOTE,
    )


if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "3000"))
    app.run(host=host, port=port, debug=False)
