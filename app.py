import os
import logging
from flask import Flask, render_template, request, jsonify, session, url_for, redirect
from dotenv import load_dotenv

# Nossas ferramentas criadas nas fases anteriores
from utils.processors import extract_text_from_txt, extract_text_from_pdf
from utils.ai_engine import classificar_e_responder

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "chave-secreta-padrao")
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # Limite de 16MB

# Configuração de Logs básica
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/")
def index():
    """Renderiza a interface inicial."""
    return render_template("index.html")

@app.route("/classify", methods=["POST"])
def classify():
    """Rota principal de processamento."""
    try:
        conteudo = ""
        
        # 1. Tenta pegar texto direto
        texto_direto = request.form.get("email_text", "").strip()
        
        if texto_direto:
            conteudo = texto_direto
        # 2. Se não houver texto, tenta processar arquivo
        elif "email_file" in request.files:
            arquivo = request.files["email_file"]
            if arquivo.filename != "":
                nome = arquivo.filename.lower()
                if nome.endswith(".txt"):
                    conteudo = extract_text_from_txt(arquivo)
                elif nome.endswith(".pdf"):
                    conteudo = extract_text_from_pdf(arquivo)
                else:
                    return jsonify({"error": "Formato de arquivo não suportado."}), 400
        
        if not conteudo:
            return jsonify({"error": "Nenhum conteúdo enviado."}), 400

        # 3. Envia para a OpenAI
        resultado = classificar_e_responder(conteudo)
        
        # 4. Salva na sessão para exibir na página de resultado
        session["result"] = {
            "original_content": conteudo[:1000] + ("..." if len(conteudo) > 1000 else ""),
            "classification": resultado.get("categoria"),
            "response": resultado.get("resposta")
        }
        
        return jsonify({
            "success": True, 
            "classification": resultado.get("categoria"),
            "response": resultado.get("resposta")
        })

    except Exception as e:
        logger.error(f"Erro no processamento: {e}")
        return jsonify({"error": "Erro interno no servidor."}), 500

@app.route("/result")
def result():
    """Exibe o resultado armazenado na sessão."""
    data = session.get("result")
    if not data:
        return redirect(url_for("index"))
    
    return render_template(
        "result.html",
        classification=data["classification"],
        response=data["response"],
        original_content=data["original_content"]
    )

if __name__ == "__main__":
    app.run(debug=True)