📁 MusicStream/
├── 📁 instance/
│   └── 📄 musicstream.db        # Banco de dados SQLite local
├── 📁 static/
│   ├── 📁 css/
│   │   └── 📄 style.css         # Estilização da aplicação e layout responsivo
│   └── 📁 js/
│       └── 📄 script.js        # Lógica do front-end, DOM e controle do player
├── 📁 templates/
│   ├── 📄 base.html             # Template base (layout e player fixo)
│   ├── 📄 biblioteca.html       # Gerenciamento de playlists e biblioteca
│   ├── 📄 buscar.html           # Interface da busca global de faixas/artistas
│   ├── 📄 cadastro.html         # Tela de cadastro de novos usuários
│   ├── 📄 confirmacao.html      # Tela de confirmação/feedback
│   ├── 📄 home.html             # Feed "Garimpo" com novidades e tendências
│   ├── 📄 index.html            # Página inicial / Landing page
│   └── 📄 login.html            # Tela de autenticação
├── 📄 .env                      # Variáveis de ambiente
├── 📄 .gitignore                # Arquivos ignorados pelo Git
├── 📄 app.py                    # Ponto de entrada do servidor Flask
├── 📄 models.py                 # Definição das tabelas do banco de dados
├── 📄 README.md                 # Documentação do projeto
└── 📄 routes.py                 # Definição das rotas e endpoints do servidor