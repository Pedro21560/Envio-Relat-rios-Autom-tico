# 🚀 Robô de Envio de Relatórios Semanais por E-mail

Automatize o envio de relatórios `.xlsx` via e-mail toda segunda-feira às 08:00 com este robô Python simples e eficaz.  
Ideal para freelancers, pequenos negócios ou quem quer aprender automação com Python.

---

## 🖼️ Demonstração

<img src="https://user-images.githubusercontent.com/00000000/email-demo.png" width="600" alt="Demonstração do envio por e-mail" />

---

## ✨ Funcionalidades

✅ Busca automática do último arquivo `.xlsx` na pasta `relatorios/`  
✅ Envio por e-mail com autenticação segura  
✅ Agendamento automático via `schedule`  
✅ Personalizável para diferentes horários, relatórios ou múltiplos destinatários

---

## 📂 Estrutura do Projeto

```
📦 seu_projeto/
├── envio_relatorio_automatico.py
├── .env
├── relatorios/
│   └── relatorio_teste.xlsx
├── README.md
├── TUTORIAL_USO.md
```

---

## 🛠️ Como Usar

📘 Acesse o tutorial completo aqui:  
[TUTORIAL_USO.md](./TUTORIAL_USO.md)

Ou veja abaixo um resumo rápido:

```bash
# Instale as dependências
pip install pandas python-dotenv schedule

# Execute o robô
python envio_relatorio_automatico.py
```

---

## ⚙️ Variáveis de Ambiente (.env)

```env
EMAIL_REMETENTE=seuemail@gmail.com
SENHA_APP=sua_senha_de_aplicativo
EMAIL_DESTINATARIO=cliente@exemplo.com
```

> A senha de aplicativo deve ser gerada no Gmail (veja o tutorial)

---

## ⏰ Personalizar horário de envio

Abra o script e edite a linha:
```python
schedule.every().monday.at("08:00").do(enviar_relatorio)
```

---

## 💡 Para Melhorar

- [ ] Múltiplos destinatários
- [ ] Registro de logs
- [ ] Validação do conteúdo do relatório
- [ ] Deploy em servidor com execução contínua

---

## 📣 Compartilhe!

Se este projeto te ajudou ou inspirou, marque no LinkedIn, contribua com melhorias ou envie uma ⭐ no GitHub!

---

## 👤 Autor

**Seu Nome**  
🔗 [LinkedIn](https://linkedin.com/in/seunome) | 🐙 [GitHub](https://github.com/seunome)
