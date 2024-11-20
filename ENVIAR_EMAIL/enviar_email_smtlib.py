from email.message import EmailMessage
import smtplib
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

# Interfaz Tkinter
ventana = Tk()
ventana.title("Outlook")
ventana.geometry("425x425")
ventana.resizable(0, 0)
ventana.config(bd=10)

Label(ventana, text="Microsoft Outlook", fg="black", font=("Arial", 15, "bold"), padx=5, pady=5).grid(row=0, column=0, columnspan=2)

# Imagen
imagen_gmail = Image.open("logo.png")
nueva_imagen = imagen_gmail.resize((90, 90))
render = ImageTk.PhotoImage(nueva_imagen)
label_imagen = Label(ventana, image=render)
label_imagen.image = render
label_imagen.grid(row=1, column=0, columnspan=2)

# Variables
remitente = StringVar(ventana)
destinatario = StringVar(ventana)
asunto = StringVar(ventana)
CDA = StringVar(ventana)

# Lista de correos predefinidos
lista_correos = ["fjcoronati@gmail.com", "programacionsabattini@gmail.com", "lafortaleza246@gmail.com"]

Label(ventana, text="Tu Gmail:", fg="black", font=("Arial", 10, "bold"), padx=5, pady=5).grid(row=2, column=0)
Entry(ventana, textvariable=remitente, width=34).grid(row=2, column=1)

Label(ventana, text="Destinatario:", fg="black", font=("Arial", 10, "bold"), padx=5, pady=5).grid(row=3, column=0)
combo_destinatario = ttk.Combobox(ventana, textvariable=destinatario, values=lista_correos, width=31)
combo_destinatario.grid(row=3, column=1)
combo_destinatario.set("Seleccionar o escribir")

Label(ventana, text="Asunto:", fg="black", font=("Arial", 10, "bold"), padx=5, pady=5).grid(row=4, column=0)
Entry(ventana, textvariable=asunto, width=34).grid(row=4, column=1)

Label(ventana, text="Mensaje:", fg="black", font=("Arial", 10, "bold"), padx=5, pady=5).grid(row=5, column=0)
mensaje = Text(ventana, height=5, width=28, padx=5, pady=5)
mensaje.grid(row=5, column=1)
mensaje.config(font=("Arial", 9), padx=5, pady=5)

# Cuadro de texto para contraseña
Label(ventana, text="Contraseña de aplicación:", fg="black", font=("Arial", 10, "bold"), padx=5, pady=5).grid(row=6, column=0)
Entry(ventana, textvariable=CDA, width=34, show="*").grid(row=6, column=1)

# Enviar correo
def enviar_email():
    remitente_email = remitente.get()
    destinatario_seleccionado = destinatario.get()
    if remitente_email == "":
        messagebox.showerror("Error", "Por favor, introduce tu correo Gmail.")
        return
    if destinatario_seleccionado == "" or destinatario_seleccionado == "Seleccionar o escribir":
        messagebox.showerror("Error", "Por favor, introduce un destinatario válido.")
        return
    
    # Estructura de email
    email = EmailMessage()
    email["From"] = remitente_email
    email["To"] = destinatario_seleccionado
    email["Subject"] = asunto.get()
    email.set_content(str(mensaje.get(1.0, 'end')))
    
    try:
        # Conexión SMTP
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        
        # Login con la contraseña proporcionada
        smtp.login(remitente_email, CDA.get())
        
        # Enviar el correo
        smtp.sendmail(remitente_email, destinatario_seleccionado, email.as_string())
        
        # Mostrar mensaje de éxito
        messagebox.showinfo("MENSAJERIA", "Mensaje enviado correctamente")
        
        # Cerrar la conexión SMTP
        smtp.quit()
        
    except Exception as e:
        # Mostrar mensaje de error en caso de fallo
        messagebox.showerror("Error", f"No se pudo enviar el correo: {e}")

# Botón de envío
Button(ventana, text="ENVIAR", command=enviar_email, height=2, width=10, bg="black", fg="white", font=("Arial", 10, "bold")).grid(row=7, column=0, columnspan=2, padx=5, pady=10)

ventana.mainloop()
