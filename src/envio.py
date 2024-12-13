from tkinter import filedialog, messagebox
import threading
import customtkinter as tk
import pandas as pd
import random
import webbrowser
import time
import pyperclip
import pyautogui as pg

class Envio:
    def __init__(self):
        self.envio_ativo = True
        self.pausar_envio = False
        self.file_path = None
        self.campo_texto_x = None
        self.campo_texto_y = None

    def focus_input_field(self):
        if self.campo_texto_x and self.campo_texto_y:
            pg.click(self.campo_texto_x, self.campo_texto_y)
            time.sleep(1)

    def selecionar_mensagem(self,nome, operador):
        mensagens = [
            f"Olá *{nome}*, boa tarde! Sou {operador}, consultora da Editora Caras, tudo bem ?\n\nFinal de ano chegou! 🤩\n\nRenove agora e aproveite:\n\nOpções de Plano\n1. 1 ano: 8x de R$155,48\n2. 2 anos: 12x de R$207,31\n\nIncluso BRINDE : Colar decorado com cristal Swarovisk.\n\nFormas de Pagamento\n- Boleto à vista\n- Cartão de crédito (primeiro pagamento no próximo vencimento)\n\nQual opção fica melhor para você?"
        ]
        return random.choice(mensagens)

    def verificar_navegador_aberto(self,numero):
        url = webbrowser.open(f"https://web.whatsapp.com/send?phone={numero}")
        return url == True

    def selecionar_excel(self, excel_entry):
        self.file_path = filedialog.askopenfilename(title="Selecione o arquivo Excel", filetypes=[("Excel files", "*.xlsx;*.xls")])
        if self.file_path:
            excel_entry.delete(0, tk.END)
            excel_entry.insert(0, self.file_path)

    def iniciar_envio(self, operador_entry, campo_texto_x, campo_texto_y):
        self.campo_texto_x = campo_texto_x
        self.campo_texto_y = campo_texto_y
        if not self.file_path:
            messagebox.showwarning("Erro", "Por favor, selecione o arquivo Excel e a imagem antes de iniciar.")
            return
        if not campo_texto_x or not campo_texto_y:
            messagebox.showwarning("Erro", "Por favor, configure a posição do campo de texto antes de iniciar.")
            return
        threading.Thread(target=self.enviar_mensagens, args=(self.file_path, operador_entry), daemon=True).start()
        print("Envio iniciado...")

    def pausar_ou_continuar(self):
        self.pausar_envio = not self.pausar_envio
        self.pause_button.configure(text="Continuar" if self.pausar_envio else "Pausar")

    def parar_envio(self):
        self.envio_ativo = False

    def enviar_mensagens(self,file_path, operador):    
        
        df = pd.read_excel(file_path)

        for index, row in df.iterrows():
            
            if not self.envio_ativo:
                return

            while self.pausar_envio:
                time.sleep(1)

            nome = row['Nome']
            
            numero = str(row['Telefone']).replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
            
            numero_formatado = '+55' + numero
                
            if not self.verificar_navegador_aberto(numero_formatado):
                continue

            time.sleep(random.uniform(25, 30))
            
            mensagem = self.selecionar_mensagem(nome, operador)

            pyperclip.copy(mensagem)
            
            self.focus_input_field()
            
            pg.hotkey('ctrl', 'v')
            
            time.sleep(random.uniform(3, 5))
            
            pg.press('enter')
            
            time.sleep(random.uniform(3, 5))
            
            pg.hotkey('ctrl', 'w')
            
            time.sleep(random.uniform(40, 90))