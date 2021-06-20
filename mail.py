import smtplib  #import smtplib module necesar trimiterii mail-urilor
import sys
import Adafruit_DHT #import Adafruit_DHT module necesar citirii datelor cu ajutorul senzorului DHT11

#SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#conectarea la adresa de mail de pe care doresc sa trimit mail-urile
server.login("hellotemp98@gmail.com", "proiect98")

#citirea umiditatii si temperaturii cu ajutorul senzorului DHT11
umiditate, temperatura = Adafruit_DHT.read_retry(11,4)
#afisarea datelor la consola
print 'Temperatura: {0:0.1f} C, Umiditate: {1:0.1f} %'.format(temperatura, umiditate)

#crearea mesajului ce va fi trimis pe mail
message = "Temperatura din camera este " + str(temperatura) + "C si gradul de umiditate este de " + str(umiditate) + "%!"
#trimiterea mesajului la adresa de mail data
server.sendmail("hellotemp98@gmail.com", "ecaterina.mihalache98@gmail.com", message)
server.quit()
