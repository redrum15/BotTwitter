from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time


class TwitterBot:
    def __init__(self, email, contrasena):
        self.email = email
        self.contrasena = contrasena
        self.bot = webdriver.Firefox()
        self.contenido = ""

    def ingresar(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(5)
        email = bot.find_element_by_name("session[username_or_email]") # Encuentra la casilla para el correo
        email.send_keys(self.email) # Copia el correo
        contrasena = bot.find_element_by_name("session[password]") # Encuentra la casilla para la contraseña
        contrasena.send_keys(self.contrasena) # Copia la contraseña
        contrasena.send_keys(Keys.RETURN) # Da enter luego de ingresar la contraseña

    def contenidoTweet(self):
        FECHA_INICIAL = datetime.date(2020, 1, 1)
        fecha_actual = datetime.date.today()
        FECHA_FINAL = datetime.date(2020, 12, 1) # Año, mes, dia
        TOTAL_DIAS = int((FECHA_FINAL - FECHA_INICIAL).days)
        TOTAL_BARRA = 25 # Tamaño de la barra, se puede cambiar dependiendo de las demas palabras que hayan en el mismo renglón

        dias_faltantes = (FECHA_FINAL - fecha_actual).days
        dias_transcurridos = int((fecha_actual - FECHA_INICIAL).days)
        porcentaje_dias = dias_transcurridos * 100 / TOTAL_DIAS

        porcentaje_barra = (TOTAL_BARRA / TOTAL_DIAS) * dias_transcurridos

        transcurrido_barra = int(porcentaje_barra)

        if fecha_actual == FECHA_FINAL:
            mensaje = "Hoy es la fecha\n\n"
        else:
            mensaje = "Todavia faltan " + str(dias_faltantes) + " días para la fecha.\n\n"

        return mensaje + 'Transcurrido: [' + ('|' * transcurrido_barra) + (' ' * (TOTAL_BARRA - transcurrido_barra)) + ']' \
               + str("{:.1f}".format(porcentaje_dias)) + '%'

    def twittear(self, contenido):
        bot = self.bot
        self.contenido = contenido
        time.sleep(5)
        bot.get('https://twitter.com/compose/tweet')
        time.sleep(5)
        twittear = bot.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div"
                                             "/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div"
                                             "/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div")
        twittear.send_keys(self.contenido) # Copia el texto a twittear
        bot.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/"
                                  "div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/"
                                  "div[4]/div/div/div[2]/div[4]").click() # Da click en el botón tweet
        time.sleep(5)
        bot.close() # Cierra el navegador


cuenta = TwitterBot("ejemplo@gmail.com", "ejemplo")
cuenta.ingresar()
contenido = cuenta.contenidoTweet()
cuenta.twittear(contenido)
