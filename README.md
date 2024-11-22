# Envío de Correo con Tkinter y Gmail
Este proyecto permite enviar correos electrónicos utilizando la interfaz gráfica de Tkinter. El usuario puede introducir su correo de Gmail, destinatarios predefinidos, asunto, mensaje, y una contraseña de aplicación para realizar el envío.

# Requisitos
Python 3.x
Librerías:
tkinter (para la interfaz gráfica)
smtplib (para enviar correos a través de SMTP)
email.message (para estructurar el correo)
PIL (para manejar imágenes, como el logo)

# Funcionalidad
Campos de entrada:

Correo remitente: Introduce tu correo de Gmail.
Destinatario: Selecciona un destinatario predefinido o escribe uno manualmente.
Asunto: Escribe el asunto del correo.
Mensaje: Redacta el mensaje que deseas enviar.
Contraseña de aplicación: Introduce tu contraseña de aplicación generada en tu cuenta de Gmail.
Botón de envío:

Al hacer clic en "ENVIAR", el correo será enviado utilizando el servidor SMTP de Gmail (requiere habilitar el acceso a aplicaciones menos seguras en tu cuenta).
