// Abre e fecha o menu nos celulares.
const botaoMenu = document.querySelector('.menu-button');
const menu = document.querySelector('.main-nav');
if (botaoMenu && menu) {
  botaoMenu.addEventListener('click', function () {
    const aberto = menu.classList.toggle('is-open');
    botaoMenu.setAttribute('aria-expanded', String(aberto));
    botaoMenu.setAttribute('aria-label', aberto ? 'Fechar menu' : 'Abrir menu');
  });
}
// Limita CPF e telefone a números e pontuação de formatação.
for (const nome of ['cpf', 'telefone']) {
  const campo = document.querySelector('[name="' + nome + '"]');
  if (campo) {
    campo.addEventListener('input', function () {
      campo.value = campo.value.replace(/[^\d().\-\s]/g, '');
    });
  }
}
// A validação do navegador ajuda o cliente; o Python valida tudo novamente.
