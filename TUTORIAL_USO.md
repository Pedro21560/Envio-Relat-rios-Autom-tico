# 📘 Tutorial de Uso – Robô de Envio de Relatórios por E-mail (Python)

Este robô envia automaticamente um relatório `.xlsx` por e-mail toda segunda-feira às 08:00. Ideal para quem deseja automatizar o envio de planilhas com Python.

---

## ⚙️ Requisitos

- Python 3 instalado
- Conta Gmail com **verificação em duas etapas ativada**
- Senha de aplicativo gerada no Google
- Biblioteca Python:
  ```bash
  pip install pandas python-dotenv schedule
  ```

---

## 📁 Estrutura Esperada

```
📦 seu_projeto/
├── envio_relatorio_automatico.py
├── .env
├── relatorios/
│   └── relatorio_teste.xlsx
```

---

## 🛠️ Configuração Passo a Passo

### 1. Gere a senha de aplicativo no Gmail

1. Acesse: https://myaccount.google.com/security
2. Ative a **verificação em duas etapas**
3. Vá para: https://myaccount.google.com/apppasswords
4. Crie uma senha de aplicativo:
   - Aplicativo: Outro → `RelatorioPython`
   - Copie a senha gerada (16 caracteres)

---

### 2. Edite o arquivo `.env`

Crie um arquivo `.env` com este conteúdo:

```
EMAIL_REMETENTE=seuemail@gmail.com
SENHA_APP=sua_senha_de_aplicativo
EMAIL_DESTINATARIO=destinatario@exemplo.com
```

🔒 Este arquivo **não deve ser versionado no GitHub** (adicione no `.gitignore`)

---

### 3. Prepare a pasta `relatorios/`

Coloque seus arquivos `.xlsx` dentro da pasta `relatorios/`.

📌 O robô irá pegar o arquivo mais recente automaticamente.

---

### 4. Configure o horário de envio (opcional)

No arquivo `envio_relatorio_automatico.py`, altere esta linha para definir o dia e horário:

```python
schedule.every().monday.at("08:00").do(enviar_relatorio)
```

Exemplos:
- `monday.at("07:30")` – Segunda às 07:30
- `friday.at("18:00")` – Sexta às 18:00

---

### 5. Execute o robô

```bash
python envio_relatorio_automatico.py
```

> O script ficará rodando em segundo plano, verificando o horário para envio.

---

## 🧪 Teste Local

Para testar antes de enviar de verdade:
- Use o arquivo `relatorio_teste.xlsx` incluído
- Rode o script e observe os logs
- Comente a parte do `SMTP` se quiser rodar apenas localmente

---

## 🧠 Dica

Para rodar o robô automaticamente sem precisar abrir manualmente:
- Use o **Agendador de Tarefas do Windows**
- Ou crie um serviço `cron` no Linux/macOS

---

## 🙋 Dúvidas Frequentes

### Posso usar outro provedor que não seja Gmail?
Sim, desde que você conheça as configurações de SMTP do provedor (host, porta, login e senha).

### O cliente precisa interagir com o robô?
Não. Basta ele salvar o relatório na pasta `relatorios/`.

---

## 👨‍💻 Autor

Desenvolvido por Pedro Pedreira de Cerqueira
Linkedin: https://www.linkedin.com/in/pedro-pedreira-de-cerqueira-78b340330/

