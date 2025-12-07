function mostrarMensagem() {
alert("Uma vez Flamengo, Flamengo até Morrer 🚀");
}

// O comando abaixo busca o botão e fica "ouvindo" o clique
document.querySelector('.botao').addEventListener('click', function(event) {
    // Evita que o link abra uma nova aba (comportamento padrão) só para testarmos o JS
    event.preventDefault(); 
    mostrarMensagem();
});