from tweepy import OAuthHandler
from tweepy import API
from datetime import datetime
from datetime import date
from datetime import timedelta

# KEYS DE LA CUENTA DEVELOPER DE TWITTER
API_KEY = ""
API_KEY_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""


class TwitterBot:

    @staticmethod
    def contenidoTweet():
        FECHA_INICIAL = date(2020, 1, 1)
        fechaActual = date.today()
        FECHA_FINAL = date(2020, 12, 31)
        TOTAL_DIAS = int((FECHA_FINAL - FECHA_INICIAL).days)
        TOTAL_BARRA = 26

        diasFaltantes = (FECHA_FINAL - fechaActual).days
        diasTranscurridos = int((fechaActual - FECHA_INICIAL).days)
        porcentajeDias = diasTranscurridos * 100 / TOTAL_DIAS

        porcentajeBarra = (TOTAL_BARRA / TOTAL_DIAS) * diasTranscurridos

        transcurridoBarra = int(porcentajeBarra)

        if fechaActual == FECHA_FINAL:
            mensaje = "Hoy se acaba año\n\n"
        else:
            mensaje = ("Todavia faltan {} días para terminar el año").format(str(diasFaltantes))

        return mensaje + 'Año: [' + ('|' * transcurridoBarra) + (' ' * (TOTAL_BARRA - transcurridoBarra)) + ']' \
               + str("{:.1f}".format(porcentajeDias)) + '%'
            


def main():
    auth = OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = API(auth)


    status = api.update_status(status=TwitterBot.contenidoTweet())



if __name__ == "__main__":
    main()