document.getElementById('emailForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    // Elementos da Interface (Input/Botão)
    const formData = new FormData(e.target);
    const btn = document.getElementById('btnProcessar');
    const btnText = document.getElementById('btnText');
    const btnSpinner = document.getElementById('btnSpinner');
    
    // Elementos de Status e Resultado
    const statusPlaceholder = document.getElementById('statusPlaceholder');
    const statusMessage = document.getElementById('statusMessage');
    const resultContent = document.getElementById('resultContent');
    const resultCard = document.getElementById('resultCard');
    
    // Elementos de Conteúdo do Resultado
    const labelClassificacao = document.getElementById('labelClassificacao');
    const textResposta = document.getElementById('textResposta');

    // 1. ESTADO DE CARREGAMENTO
    btn.disabled = true;
    btnText.innerText = "IA Analisando...";
    btnSpinner.classList.remove('d-none');
    
    // Mostra o placeholder de status e garante que o conteúdo antigo suma
    resultContent.classList.add('d-none');
    statusPlaceholder.classList.remove('d-none');
    statusMessage.innerText = "A OpenAI está processando seu email...";

    try {
        const response = await fetch('/classify', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (result.success) {
            // 2. SUCESSO: ESCONDER CARREGAMENTO E MOSTRAR RESULTADO
            statusPlaceholder.classList.add('d-none');
            resultContent.classList.remove('d-none');

            // Preenche os dados
            labelClassificacao.innerText = result.classification;
            textResposta.innerText = result.response;

            // 3. LÓGICA DE CORES DINÂMICAS (UX Sênior)
            if (result.classification === "Produtivo") {
                labelClassificacao.className = "badge bg-success mt-1";
                resultCard.classList.replace('border-primary', 'border-success');
                resultCard.classList.replace('border-warning', 'border-success');
            } else {
                labelClassificacao.className = "badge bg-warning text-dark mt-1";
                resultCard.classList.replace('border-primary', 'border-warning');
                resultCard.classList.replace('border-success', 'border-warning');
            }

        } else {
            alert("Erro: " + result.error);
            resetUI();
        }
    } catch (error) {
        console.error(error);
        alert("Erro de conexão com o servidor.");
        resetUI();
    } finally {
        // Restaura o botão original
        btn.disabled = false;
        btnText.innerText = "Processar Email";
        btnSpinner.classList.add('d-none');
    }
});


function copyToClipboard() {
    const text = document.getElementById('textResposta').innerText;
    const btnCopy = document.getElementById('btnCopy');
    
    navigator.clipboard.writeText(text).then(() => {
        const originalText = btnCopy.innerText;
        btnCopy.innerText = "Copiado!";
        btnCopy.classList.replace('btn-outline-primary', 'btn-success');
        
        setTimeout(() => {
            btnCopy.innerText = originalText;
            btnCopy.classList.replace('btn-success', 'btn-outline-primary');
        }, 2000);
    });
}

function resetUI() {
    document.getElementById('emailForm').reset();
    document.getElementById('resultContent').classList.add('d-none');
    document.getElementById('statusPlaceholder').classList.remove('d-none');
    document.getElementById('statusMessage').innerText = "Aguardando envio para análise...";
    
    const resultCard = document.getElementById('resultCard');
    resultCard.className = "card border-primary h-100 shadow-sm";
}