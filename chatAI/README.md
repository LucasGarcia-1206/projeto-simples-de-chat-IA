# 🤖 Chat IA

Chatbot interativo com streaming de respostas, construído com **Streamlit** e **OpenAI**.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red)

## Funcionalidades

- 💬 Chat em tempo real com streaming de respostas
- ⚙️ Modelo, temperatura e max tokens configuráveis pela sidebar
- 🧠 System prompt personalizável via `.env`
- 🗑️ Botão para limpar conversa

## Pré-requisitos

- Python 3.10+
- Uma chave de API da [OpenAI](https://platform.openai.com/api-keys)

## Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/chatAI.git
cd chatAI

# Crie e ative um ambiente virtual
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install streamlit openai python-dotenv
```

## Configuração

Copie o arquivo de exemplo e preencha com sua chave:

```bash
cp .env.example .env
```

Edite o `.env`:

```env
OPENAI_API_KEY=sk-sua-chave-aqui
OPENAI_MODEL=gpt-4o-mini
SYSTEM_PROMPT=Voce e um assistente prestativo que responde em portugues.
```

| Variável | Descrição | Padrão |
|---|---|---|
| `OPENAI_API_KEY` | Chave da API OpenAI **(obrigatória)** | — |
| `OPENAI_MODEL` | Modelo a ser usado | `gpt-4o-mini` |
| `SYSTEM_PROMPT` | Prompt de sistema do assistente | Assistente em português |

## Uso

```bash
streamlit run main.py
```

Acesse `http://localhost:8501` no navegador.

## Estrutura

```
chatAI/
├── main.py          # Aplicação principal
├── .env             # Variáveis de ambiente (não versionado)
├── .env.example     # Template de configuração
├── .gitignore       # Arquivos ignorados pelo git
└── README.md        # Este arquivo
```

## Licença

MIT
