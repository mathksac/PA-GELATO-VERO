// URL do backend Flask. Depois de publicar o backend, coloque aqui o endereço dele.
const API_URL = "https://SEU-BACKEND-FLASK.onrender.com";

const menuBotao = document.getElementById("menuBotao");
const menu = document.getElementById("menu");
menuBotao.addEventListener("click", () => menu.classList.toggle("aberto"));
menu.querySelectorAll("a").forEach(link => link.addEventListener("click", () => menu.classList.remove("aberto")));

document.getElementById("formCadastro").addEventListener("submit", async (event) => {
  event.preventDefault();
  const mensagem = document.getElementById("mensagem");
  const dados = {
    nome: document.getElementById("nome").value.trim(),
    email: document.getElementById("email").value.trim(),
    telefone: document.getElementById("telefone").value.trim()
  };

  if (!dados.nome || !dados.email) {
    mensagem.textContent = "Preencha seu nome e e-mail.";
    return;
  }

  if (API_URL.includes("SEU-BACKEND")) {
    mensagem.textContent = "O formulário está pronto. Falta publicar e conectar o servidor Python.";
    return;
  }

  mensagem.textContent = "Enviando cadastro...";
  try {
    const resposta = await fetch(API_URL + "/cadastro", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(dados)
    });
    const resultado = await resposta.json();
    if (!resposta.ok) throw new Error(resultado.erro || "Não foi possível cadastrar.");
    mensagem.textContent = "Cadastro realizado com sucesso! 💗";
    event.target.reset();
  } catch (erro) {
    mensagem.textContent = erro.message || "Erro ao enviar. Tente novamente.";
  }
});