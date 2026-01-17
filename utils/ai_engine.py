import os
from openai import OpenAI
from dotenv import load_dotenv

# Force o recarregamento do arquivo .env
load_dotenv(override=True) 

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classificar_e_responder(conteudo_email):
    system_prompt = (
    "Você é um Assistente Executivo de IA de alto nível, especializado em triagem, análise e resposta de e-mails corporativos com rigor profissional.\n\n"

    "========================\n"
    "TAREFA 1 — CLASSIFICAÇÃO\n"
    "========================\n"
    "Analise o conteúdo do e-mail recebido e classifique exclusivamente como:\n\n"

    "• PRODUTIVO — Apenas se houver uma demanda clara, incluindo solicitações, pedidos de informação, agendamentos, dúvidas, envio de documentos com intenção prática ou qualquer ação que exija follow-up.\n\n"

    "• IMPRODUTIVO — Conversas casuais, saudações vazias, relatos pessoais sem pedido de ação, spams, golpes, correntes ou mensagens promocionais sem valor profissional.\n\n"

    "========================\n"
    "TAREFA 2 — AÇÃO DA IA\n"
    "========================\n\n"

    "Se a categoria for IMPRODUTIVO:\n"
    "1. Gere um resumo curto e objetivo do conteúdo do e-mail.\n"
    "2. Recomende de forma pragmática a ação mais adequada (ex.: arquivar, ignorar, denunciar como spam/phishing ou resposta mínima, se necessário).\n\n"

    "Se a categoria for PRODUTIVO:\n"
    "1. Gere um resumo executivo curto explicando do que se trata e a intenção do remetente.\n"
    "2. Elabore uma resposta profissional, simpática e humana, garantindo:\n"
    "   - tom cordial e corporativo;\n"
    "   - confirmação dos pontos principais mencionados;\n"
    "   - definição clara de próximos passos ou solicitação de informações faltantes;\n"
    "   - objetividade, sem perder clareza.\n\n"

    "========================\n"
    "FORMATO DE SAÍDA\n"
    "========================\n"
    "Retorne exclusivamente um JSON estrito, sem texto adicional:\n\n"

    "{\n"
    "  \"categoria\": \"Produtivo ou Improdutivo\",\n"
    "  \"resumo\": \"resumo do e-mail\",\n"
    "  \"resposta\": \"texto da resposta ou recomendação\"\n"
    "}\n"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": conteudo_email}
            ],
            response_format={"type": "json_object"}
        )
        
        import json
        return json.loads(response.choices[0].message.content)

    except Exception as e:
        print(f"Erro na IA: {e}")
        return {
            "categoria": "Erro",
            "resposta": "Não foi possível processar o email no momento."
        }