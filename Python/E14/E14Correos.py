from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import smtplib
import getpass
import ssl

asunto = input("Ingrese el asunto del correo: ")
ian = input("Ingrese nombre completo: ")
cuerpo = input("Ingrese el cuerpo del correo: ")
mensaje = (cuerpo + " " + ian)
receptor = input("Ingrese el correo receptor: ")
usuario = input("Ingrese su correo: ")
contraseña = getpass.getpass()

email_msg = MIMEMultipart("alternative")
email_msg["From"] = usuario
email_msg["To"] = receptor
email_msg["Subject"] = asunto

email_msg.attach(MIMEText(mensaje, "plain"))

filename = input("Ingrese el archivo que se mandará: ")
with open(filename, "rb") as attachment:
    
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
 
encoders.encode_base64(part)


part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)


email_msg.attach(part)


context = ssl.create_default_context()
with smtplib.SMTP("smtp.office365.com", 587) as server:
    server.ehlo()
    server.starttls(context=context)
    server.login(usuario, contraseña)
    server.sendmail(
        usuario, receptor, email_msg.as_string()
    )
print("successfully sent email to %s" % (receptor))
