// Função que busca dados na API Python
async function buscarDadosDoPython() {
    try {
        // O JavaScript vai lá na url /api/tempo buscar os dados
        const resposta = await fetch('/api/tempo');
        
        // Ele converte o texto estranho (JSON) para um objeto legível
        const dados = await resposta.json();
        
        // Agora pegamos o elemento da tela e trocamos o texto
        const elemento = document.getElementById('mensagem-python');
        elemento.innerText = `🐍 ${dados.saudacao} Hora certa: ${dados.hora_servidor}`;
        
    } catch (erro) {
        console.error("Erro ao buscar dados:", erro);
    }
}

// Quando clicar no botão, chama a função acima
document.querySelector('.botao').addEventListener('click', function(event) {
    event.preventDefault(); // Não deixa mudar de página
    buscarDadosDoPython();  // Chama o Python
});