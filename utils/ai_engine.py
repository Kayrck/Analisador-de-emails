import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classificar_e_responder(conteudo_email):
    """
    Usa a API da OpenAI para classificar o email e sugerir uma resposta.
    """
    # Definimos o comportamento da IA (System Prompt)
    system_prompt = (
        "Você é um assistente de produtividade. Sua tarefa é analisar emails.\n"
        "1. Classifique o email como 'Produtivo' (se contiver ações, tarefas ou informações úteis) "
        "ou 'Improdutivo' (se for spam, informativo irrelevante ou sem ação necessária).\n"
        "2. Se for 'Produtivo', escreva uma sugestão de resposta profissional e concisa.\n"
        "3. Se for 'Improdutivo', sugira uma resposta curta de arquivamento ou ignore.\n"
        "Responda EXATAMENTE neste formato JSON:\n"
        '{"categoria": "Produtivo/Improdutivo", "resposta": "texto da resposta"}'
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": conteudo_email}
            ],
            response_format={"type": "json_object"} # Força a saída em JSON
        )
        
        # O retorno é uma string que transformamos em dicionário Python
        import json
        return json.loads(response.choices[0].message.content)

    except Exception as e:
        print(f"Erro na IA: {e}")
        return {
            "categoria": "Erro",
            "resposta": "Não foi possível processar o email no momento."
        }