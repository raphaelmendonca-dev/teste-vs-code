function mostrarMensagem() {
    alert("Olá! Obrigado por visitar meu portfólio rodando na Vercel! 🚀");
}

// O comando abaixo busca o botão e fica "ouvindo" o clique
document.querySelector('.botao').addEventListener('click', function(event) {
    // Evita que o link abra uma nova aba (comportamento padrão) só para testarmos o JS
    event.preventDefault(); 
    mostrarMensagem();
});
