import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

def escolher_pasta_destino():
    pasta_destino = filedialog.askdirectory()
    entry_destino.delete(0, tk.END)
    entry_destino.insert(0, pasta_destino)

def baixar_video():
    url = entry_url.get()
    yt = YouTube(url)
    
    if var_formato.get() == "mp4":
        video_stream = yt.streams.filter(file_extension='mp4', progressive=True).first()
    else:
        video_stream = yt.streams.filter(only_audio=True).first()

    destino = entry_destino.get() if entry_destino.get() else "."
    video_stream.download(output_path=destino)
    label_status.config(text="Download concluído!")

# Criar a interface gráfica
app = tk.Tk()
app.title("Baixador de Vídeos do YouTube")

# Componentes da interface
label_url = tk.Label(app, text="URL do vídeo:")
entry_url = tk.Entry(app, width=40)
label_destino = tk.Label(app, text="Diretório de destino:")
entry_destino = tk.Entry(app, width=30)
button_selecionar_destino = tk.Button(app, text="Selecionar Pasta", command=escolher_pasta_destino)
label_formato = tk.Label(app, text="Formato:")
var_formato = tk.StringVar()
radio_mp4 = tk.Radiobutton(app, text="MP4", variable=var_formato, value="mp4")
radio_mp3 = tk.Radiobutton(app, text="MP3", variable=var_formato, value="mp3")
button_baixar = tk.Button(app, text="Baixar", command=baixar_video)
label_status = tk.Label(app, text="Status: Aguardando download...")

# Posicionamento dos componentes
label_url.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
entry_url.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky=tk.W)
label_destino.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
entry_destino.grid(row=1, column=1, padx=5, pady=10, sticky=tk.W)
button_selecionar_destino.grid(row=1, column=2, pady=10, sticky=tk.W)
label_formato.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
radio_mp4.grid(row=2, column=1, padx=5, pady=10, sticky=tk.W)
radio_mp3.grid(row=2, column=2, padx=5, pady=10, sticky=tk.W)
button_baixar.grid(row=3, column=0, columnspan=3, pady=10)
label_status.grid(row=4, column=0, columnspan=3, pady=10)

# Iniciar o loop da aplicação
app.mainloop()
