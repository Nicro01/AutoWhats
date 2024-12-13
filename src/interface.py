import customtkinter as tk
from tkinter import messagebox, PhotoImage
import time
import threading
import pyautogui as pg

from envio import Envio

class App:
    def __init__(self):
        self.debug = True
        
        self.campo_texto_x = 1048 if self.debug else None
        self.campo_texto_y = 968 if self.debug else None
        self.excel_entry = None
        self.operador_entry = None
        self.envio = Envio()
        self.root = tk.CTk()
        self.setup_window()
        self.create_widgets()
        

    def setup_window(self):
        img = PhotoImage(file='assets/icon.png')
        self.root.title("Envio Automático de Mensagens no WhatsApp")
        self.root.geometry("750x370")
        self.root.resizable(False, False)
        self.root.iconphoto(False, img)

    def create_widgets(self):
        self.create_input_frame()
        self.create_control_frame()
        self.create_log_frame()
        self.configure_grid()

    def create_input_frame(self):
        input_frame = tk.CTkFrame(self.root, bg_color="transparent")
        input_frame.grid(row=0, column=0, padx=10, pady=(10, 0), rowspan=3, columnspan=4, sticky='nsew')

        for i in range(4):
            input_frame.grid_columnconfigure(i, weight=1)

        tk.CTkLabel(input_frame, text="Selecione o arquivo Excel:").grid(row=0, column=0, padx=10, pady=(10, 0), sticky='w')
        
        #Input Excel
        self.excel_entry = tk.CTkEntry(input_frame) 
        self.excel_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=(10, 0), sticky='nsew')
        
        if self.debug:
            self.excel_entry.insert(0, "C:/Users/Nicro/Desktop/planilha.xlsx")
        
        self.excel_button = tk.CTkButton(input_frame, text="Selecionar Excel", command= lambda: self.envio.selecionar_excel(self.excel_entry), )
        self.excel_button.grid(row=0, column=3, padx=10, pady=(10, 0), sticky='nsew')

        tk.CTkLabel(input_frame, text="Nome do Operador:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
        
        #Input Operador
        self.operador_entry = tk.CTkEntry(input_frame)
        self.operador_entry.grid(row=1, column=1, columnspan=3, padx=10, pady=10, sticky='nsew')
        
        if self.debug:
            self.operador_entry.insert(0, "Operador")

    def create_control_frame(self):
        self.control_frame = tk.CTkFrame(self.root, fg_color="transparent", corner_radius=0)
        self.control_frame.grid(row=3, column=0, pady=10, columnspan=3, rowspan=1)

        tk.CTkButton(self.control_frame, text="Iniciar", command= lambda: self.envio.iniciar_envio(self.operador_entry.get(), self.campo_texto_x, self.campo_texto_y)).grid(row=0, column=0, padx=5)
        tk.CTkButton(self.control_frame, text="Pausar", command=self.envio.pausar_ou_continuar).grid(row=0, column=1, padx=5)
        tk.CTkButton(self.control_frame, text="Parar", command=self.envio.parar_envio).grid(row=0, column=2, padx=5)
        tk.CTkButton(self.control_frame, text="Configurar Posição", command=self.config_window).grid(row=0, column=3, padx=5)

    def create_log_frame(self):
        self.log_frame = tk.CTkFrame(self.root, corner_radius=0)
        self.log_frame.grid(row=4, column=0, columnspan=4, rowspan=4, sticky='nsew')

        self.log_textbox = tk.CTkTextbox(self.log_frame, state='disabled')
        self.log_textbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        self.send_log("Pronto para iniciar o envio de mensagens.")
        

    def configure_grid(self):
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure((2, 3), weight=0)
        self.root.grid_rowconfigure((0, 1, 2), weight=1)

    def send_log(self, message):
        self.log_textbox.configure(state='normal')
        self.log_textbox.insert(tk.END, f"{message}\n")
        self.log_textbox.configure(state='disabled')
        self.log_textbox.see(tk.END)
        
    def config_window(self):
        webbrowser.open("https://web.whatsapp.com/")
        self.count_window = tk.CTkToplevel(self.root)
        self.count_window.attributes('-fullscreen', True)
        self.count_window.attributes('-topmost', True)
        self.count_window.attributes('-alpha', 0.1)
        self.count_window.configure(background='black')

        label = tk.CTkLabel(self.count_window, text="Aguarde o carregamento da página", font=("Arial", 24))
        label.pack(expand=True)
        
        self.contador_label = tk.CTkLabel(self.count_window, text="", font=("Arial", 48))
        self.contador_label.pack(expand=True)

        threading.Thread(target=self.atualizar_contador, args=(self.contador_label, self.count_window, label), daemon=True).start()
        
    def configurar_posicao_click(self,event, window):
        self.campo_texto_x, self.campo_texto_y = event.x_root, event.y_root
        self.send_log(f"Posição configurada: ({self.campo_texto_x}, {self.campo_texto_y})")
        window.destroy()
        
    def atualizar_contador(self, label, window, text_label):
        global contador
        for contador in range(10, 0, -1):
            label.configure(text=str(contador))
            time.sleep(1)
            if contador == 1:
                for _ in range(18):
                    pg.hotkey("tab")
        
        label.configure(text="Selecione o campo de envio de mensagem")
        text_label.destroy()
        
        window.bind("<Button-1>", lambda e: self.configurar_posicao_click(e, window))

    def run(self):
        self.root.mainloop()
