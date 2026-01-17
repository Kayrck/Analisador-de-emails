document.getElementById('emailForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);
    const btn = document.getElementById('btnProcessar');
    const btnText = document.getElementById('btnText');
    const btnSpinner = document.getElementById('btnSpinner');
    const statusMessage = document.getElementById('statusMessage');

    // Estado de Carregamento
    btn.disabled = true;
    btnText.innerText = "IA Analisando...";
    btnSpinner.classList.remove('d-none');
    statusMessage.innerText = "A IA está lendo o conteúdo e classificando...";

    try {
        const response = await fetch('/classify', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (result.success) {
            window.location.href = result.redirect;
        } else {
            alert("Erro: " + result.error);
            resetBtn();
        }
    } catch (error) {
        alert("Erro de conexão com o servidor.");
        resetBtn();
    }
});

function resetBtn() {
    document.getElementById('btnProcessar').disabled = false;
    document.getElementById('btnText').innerText = "Processar Email";
    document.getElementById('btnSpinner').classList.add('d-none');
}