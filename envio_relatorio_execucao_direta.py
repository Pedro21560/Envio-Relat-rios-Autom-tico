import smtplib
import os
import pandas as pd
from email.message import EmailMessage
from dotenv import load_dotenv
import glob

# Carregar variáveis de ambiente
load_dotenv()

EMAIL_REMETENTE = os.getenv('EMAIL_REMETENTE')
SENHA_APP = os.getenv('SENHA_APP')
EMAIL_DESTINATARIO = os.getenv('EMAIL_DESTINATARIO')

def encontrar_ultimo_relatorio():
    arquivos = glob.glob("relatorios/*.xlsx")
    if not arquivos:
        print("⚠️ Nenhum relatório encontrado na pasta 'relatorios'.")
        return None
    ultimo = max(arquivos, key=os.path.getctime)
    return ultimo

def enviar_relatorio():
    caminho_arquivo = encontrar_ultimo_relatorio()
    if not caminho_arquivo:
        return

    msg = EmailMessage()
    msg['Subject'] = 'Relatório Semanal'
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = EMAIL_DESTINATARIO
    msg.set_content('Olá! Segue em anexo o relatório semanal.')

    with open(caminho_arquivo, 'rb') as file:
        msg.add_attachment(file.read(), maintype='application',
                           subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                           filename=os.path.basename(caminho_arquivo))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_REMETENTE, SENHA_APP)
        smtp.send_message(msg)
    print(f"✅ Relatório '{os.path.basename(caminho_arquivo)}' enviado com sucesso!")

# Execução imediata única
if __name__ == "__main__":
    enviar_relatorio()
