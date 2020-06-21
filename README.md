# BotTwitter

Bot de Twitter utilizando Selenium que twittea la diferencia entre la fecha actual y una establecida previamente,
además, calcula el porcentaje que ha transcurrido entre la fecha actual y la incial. El tweet tiene el siguiente
formato:
```
  /////////////////////////////////////////////////////
  |  Aún faltan 193 días para que se acabe el año.    |
  |                                                   |
  |  Año: [||||||||||||               ] 47.1%         |
  |                                                   |
  /////////////////////////////////////////////////////
```

# Requisitos

- Instalar Selenium para la correspondiente versión de Python. `pip install selenium` o `pip3 install selenium`
- Firefox versión 60 o mayor.
- Intalar el webdriver para Firefox. `https://github.com/mozilla/geckodriver/releases`
