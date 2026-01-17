📧 Analisador de E-mails

Uma solução Full Stack orientada por IA, desenvolvida para elevar a eficiência operacional por meio da triagem inteligente e resposta automatizada de e-mails. Com OpenAI GPT-4o-mini no core, o sistema entrega uma jornada de produtividade end-to-end, segregando demandas reais de ruídos operacionais com assertividade estratégica.

🌐 Demonstração Online

O deploy está ativo na Render e pronto para operação: 
👉 https://analisador-de-emails-1.onrender.com/ 

Observação: Instâncias gratuitas da Render podem levar ~50 segundos para inicialização (cold start).

✨ Principais Capacidades

🔹 Classificação Inteligente (IA OpenAI)
Segmentação automática entre:

Produtivo: demandas, solicitações, dúvidas, agendamentos

Improdutivo: conversas triviais, spam, irrelevâncias

🔹 Respostas Profissionais Automáticas
Geração de rascunhos claros, cordiais e orientados a desfecho para e-mails classificados como produtivos.

🔹 Arquitetura SPA
Front-end responsivo com experiência fluida, processando dados via Fetch API sem recarregamento de página.

🔹 Extração Multi-formato
Processamento direto de:

Texto colado

Arquivos .txt

Arquivos .pdf via pypdf

🔹 Segurança e Robustez

Limite de upload (16MB)

Gerenciamento seguro de variáveis de ambiente

Proteção de sessão e boas práticas Flask

🛠️ Stack Tecnológico

Linguagem: Python 3.13.7
Backend: Flask + Gunicorn
IA: OpenAI API (GPT-4o-mini)
Frontend: HTML5, CSS3 (Bootstrap 5), JavaScript assíncrono
Bibliotecas Core: pypdf, python-dotenv, openai

🚀 Como Rodar Localmente
1. Preparar Ambiente
git clone https://github.com/Kayrck/Analisador-de-emails.git
cd Analisador-de-emails
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

2. Configurar Variáveis

Crie um arquivo .env na raiz:

OPENAI_API_KEY=sua_chave_aqui
SECRET_KEY=sua_chave_secreta_flask

3. Iniciar Aplicação
python app.py

📝 Estrutura da Solução
Arquivo / Pasta	Descrição
app.py	Core do servidor e endpoints da API
utils/ai_engine.py	Engenharia de prompt e integração com OpenAI
utils/processors.py	Pipeline de extração e tratamento de arquivos
static/js/main.js	Lógica dinâmica e experiência do usuário
📄 Licença

Distribuído sob a licença MIT.

👩‍💻 Autoria

Desenvolvido por Kaylanne Nogueira da Silva
Transformando IA em vantagem competitiva por meio de soluções escaláveis e centradas em performance.