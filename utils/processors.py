import io
from pypdf import PdfReader

def extract_text_from_txt(file_stream) -> str:
    """Extrai texto de um arquivo TXT enviado via formulário Flask."""
    try:
        content = file_stream.read()
        # Se for um objeto de arquivo do Flask, precisamos resetar o ponteiro se lido antes
        if hasattr(file_stream, 'seek'):
            file_stream.seek(0)
        return content.decode("utf-8", errors="ignore").strip()
    except Exception as e:
        raise ValueError(f"Erro ao ler arquivo TXT: {str(e)}")

def extract_text_from_pdf(file_stream) -> str:
    """Extrai texto de um arquivo PDF usando pypdf."""
    try:
        reader = PdfReader(file_stream)
        text = ""
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
        return text.strip()
    except Exception as e:
        raise ValueError(f"Erro ao extrair texto do PDF: {str(e)}")