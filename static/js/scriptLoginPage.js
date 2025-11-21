// script.js

// O evento 'DOMContentLoaded' garante que o script só rode após o HTML estar completamente carregado
document.addEventListener('DOMContentLoaded', (event) => {
    console.log('Documento carregado e analisado.');
    // 1. Seleciona todos os elementos que têm a classe 'animar'
    const elementosAnimar = document.querySelectorAll('.animar');

    // 2. Itera sobre a lista de elementos selecionados
    elementosAnimar.forEach((elemento, index) => {
        /*
         * O 'setTimeout' é usado para aplicar a classe 'visivel' com um pequeno
         * atraso sequencial (opcional, mas recomendado) para que os elementos
         * apareçam um após o outro, o que cria um efeito mais dinâmico.
         */
        setTimeout(() => {
            // Adiciona a classe 'visivel', que inicia a animação CSS
            elemento.classList.add('visivel');
        }, index * 100); // 100ms de atraso sequencial entre cada elemento
    });
});