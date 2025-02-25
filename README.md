# 📚 Raspagem de Notícias

> <i>NewsScraping</i> é um projeto acadêmico criado para colocar em prática o conteúdo teórico das matérias com proposito de fixação de conteúdo utilizando um ecossistema vasto de tecnologias e possibilidades.

## 🚀 Tecnologias Utilizadas

Este projeto foi desenvolvido com uso das seguintes tecnologias direta ou indiretamente:

- Python
    - Requests
    - Beautifulsoup4
    - textwrap
- Docker
- git
- github
- markdown
- html
- css

## 📌 Funcionalidades

- ✅ Extrai Principais notícias de um site e exibe os resultados no terminal


## 📂 Estrutura do Projeto

```bash
📂 NewsScraping
    ├── 📁 app  
        ├── 📁 services 
            ├── 📄 scraper.py
        ├── 📁 utils
            ├── 📄 display.py
            ├── 📄 formatter.py
        ├── 📄 main.py
    ├── 📁 docker
        ├── 📄 .dockerignore
    ├── 📄 .gitignore 
    ├── 📄 Dockerfile  
    ├── 📄 LICENSE
    ├── 📄 README.md 
    ├── 📄 requirements.txt
```

## 🛠️ Como Executar o Projeto

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:

- Docker

### Instalação e Execução

```bash
# Construir a imagem:
docker build -t news_scraping .

# Rodar o projeto
docker run -p 5000:5000 news_scraping

- A aplicação esta direcionada a um endereco especifico. Para realizar mudanças deve alterar os paramentros, e ter conhecimentos de html e css.
```
📝 Licença
Este projeto está sob Unlicense, uma licença de software de domínio público. Ao utilizar a Unlicense, o autor do software renuncia a todos os direitos autorais e dedica o código à domínio público, permitindo que qualquer pessoa use, modifique e distribua o software sem restrições.

👨‍💻 Desenvolvido por Francisco Cleiton   
📌 Entre em contato: franciscocleitondev@gmail.com
