# Projeto: Coleta de Dados Financeiros (Yahoo Finance)

Este desafio tem como objetivo coletar dados financeiros do Yahoo Finance utilizando duas abordagens distintas:
1. **Web Scraping**: Utilizando `BeautifulSoup` para extrair dados diretamente do site do Yahoo Finance.
2. **API (yfinance)**: Obtendo dados de ações através da API do Yahoo Finance (`yfinance`).

Os dados são armazenados em arquivos CSV para fácil análise e processamento posterior.

---

## 📁 Estrutura do Projeto
```
PROJETO_COLETA_DADOS/
│── api/
│   ├── application/
│   │   ├── data_formatter.py  # Formatação dos dados da API
│   ├── infra/
│   │   ├── yahoo_api.py       # Requisições à API do Yahoo Finance
│   ├── persistence/
│   │   ├── csv_exporter.py    # Exportação de dados em CSV
│   ├── utils/
│   │   ├── logger.py          # Logger para API
│
│── scraping/
│   ├── application/
│   │   ├── data_formatter.py  # Formatação dos dados do Scraping
│   ├── infra/
│   │   ├── yahoo_scraper.py   # Web Scraping do Yahoo Finance
│   ├── persistence/
│   │   ├── csv_exporter.py    # Exportação de dados em CSV
│   ├── utils/
│   │   ├── logger.py          # Logger para Scraping
│
│── data/                      # Diretório contendo os arquivos CSV gerados
│   ├── dados_yahoo_api.csv
│   ├── dados_yahoo_scraping.csv
│
│── logs/                      # Diretório contendo logs das execuções
│   ├── api_fetcher.log
│   ├── scraping.log
│
│── env/                       # Diretório reservado para variáveis de ambiente
│── main_api.py                 # Script principal para execução da coleta via API
│── main_scraping.py            # Script principal para execução do Web Scraping
│── requirements.txt            # Arquivo com as dependências do projeto
│── README.md                   # Documentação do projeto
```

---

## 🚀 Instalação e Configuração
### 1️⃣ Pré-requisitos
- Python 3.8+
- `pip` instalado

### 2️⃣ Instalar dependências
Execute o seguinte comando para instalar todas as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

---

## 🔄 Execução dos Scripts
### 📊 Web Scraping
Para executar o script de Web Scraping, utilize o comando:
```bash
python main_scraping.py
```
Isso coletará os dados das ações mais ativas no Yahoo Finance e salvará o arquivo `dados_yahoo_scraping.csv` na pasta `data/`.

### 🔍 Coleta via API
Para coletar os dados através da API do Yahoo Finance, execute:
```bash
python main_api.py
```
O resultado será salvo no arquivo `dados_yahoo_api.csv` dentro da pasta `data/`.

---

## 📌 Arquivos CSV Gerados
Os arquivos CSV contêm as seguintes colunas:
- **Symbol**: Código da ação
- **Price**: Último preço registrado
- **Change**: Variação no preço (Web Scraping)
- **Percentage**: Percentual de variação (Web Scraping)

---

## 🏗 Arquitetura
O projeto segue o padrão **MVC (Model-View-Controller)**:
- **Model**: Representação dos dados extraídos.
- **View**: Responsável por exportação dos dados em CSV.
- **Controller**: Orquestra a coleta e o processamento dos dados.

---

## 📌 Considerações Finais
- O Web Scraping pode falhar caso o site do Yahoo Finance altere sua estrutura.
- Para evitar bloqueios, há um sistema de logging e manipulação de erros.
- Melhorias futuras incluem suporte a múltiplas fontes de dados e otimização do scraping.

---

## 📝 Autor
- Desenvolvido por **Vinícius Franco**

🚀 Projeto criado para fins de estudo e automação da coleta de dados financeiros!

