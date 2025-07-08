// Efeito de botão animado ao passar o mouse
document.addEventListener("DOMContentLoaded", () => {
    const botao = document.querySelector('.cta-botao');
    if (botao) {
        botao.addEventListener('mouseover', () => {
            botao.style.transition = 'transform 0.2s ease';
            botao.style.transform = 'scale(1.05)';
        });

        botao.addEventListener('mouseout', () => {
            botao.style.transform = 'scale(1)';
        });
    }
});
