# 🎧 MusicStream

O **MusicStream** é um web app de streaming e garimpo de música voltado para o "Ouvinte Explorador". O projeto foca em uma interface minimalista, rápida e sem anúncios, permitindo aos usuários descobrir faixas *indie*, *remixes* e edições da comunidade.

Este projeto foi concebido utilizando a metodologia de **Design Thinking** e construído com uma arquitetura web leve e eficiente.

---

## 🎯 Escopo do Projeto

- **Player Fixo e Contínuo:** Player no rodapé (*persistent player*) em HTML5/JS para navegação sem interrupções.
- **Feed "Garimpo" (Home):** Exibição de músicas em alta e novidades independentes consumidas em tempo real.
- **Busca Global:** Pesquisa integrada por músicas e artistas via API.
- **Playlists e Biblioteca:** Autenticação de usuários, criação e gerenciamento de playlists customizadas salvas em banco de dados local.
- **Compartilhamento:** Links diretos e integrados para compartilhar faixas com outros ouvintes.

---

## 🛠️ Tecnologias Utilizadas

### Front-end
- **HTML5:** Estruturação semântica da interface.
- **CSS3:** Estilização moderna e layout responsivo (3 colunas em Desktop).
- **JavaScript (Vanilla):** Manipulação de DOM, consumo de APIs (Fetch API) e controle do Player de Áudio.

### Back-end
- **Python:** Linguagem principal do servidor.
- **Flask:** Micro-framework para criação de rotas, renderização de templates e controle de sessão/autenticação.

### Banco de Dados & APIs
- **SQLite3:** Banco de dados relacional leve para armazenar usuários, playlists e curtidas.
- **Audius REST API:** Provedor de dados e streaming de áudio do catálogo *indie* e comunidade.

---
