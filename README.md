Bate-papo IA
Chatbot interativo com streaming de respostas, construído com Streamlit e OpenAI .

Python Streamlit

Funcionalidades
Chat em tempo real com streaming de respostas
Modelo, temperatura e max tokens configuráveis ​​pela barra lateral
Prompt do sistema personalizável via.env
Botão para limpar conversa
Pré-requisitos
Python 3.10+
Uma chave de API da OpenAI

# Crie e ative um ambiente virtual
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install streamlit openai python-dotenv
Configuração
Copie o arquivo de exemplo e preencha com sua chave:

cp .env.example .env
Edite o .env:

OPENAI_API_KEY=sk-sua-chave-aqui
OPENAI_MODEL=gpt-4o-mini
SYSTEM_PROMPT=Voce e um assistente prestativo que responde em portugues.
Variável	Descrição	padrão
OPENAI_API_KEY	Chave da API OpenAI (obrigatória)	—
OPENAI_MODEL	Modelo a ser usado	gpt-4o-mini
SYSTEM_PROMPT	Alerta do sistema do assistente	Assistente em português
Uso
streamlit run main.py
Acesse http://localhost:8501no navegador.

Estrutura
chatAI/
├── main.py          # Aplicação principal
├── .env             # Variáveis de ambiente (não versionado)
├── .env.example     # Template de configuração
├── .gitignore       # Arquivos ignorados pelo git
└── README.md        # Este arquivo
licença
