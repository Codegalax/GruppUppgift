# Gruppuppgift
 LED control och temperatur monitor program med tester i python 

 # Mappbeskrivningar
- **LEDControl** : Den här mappen innehåller Arduino koden till LED control programmet och python koden som testar programmet.
- **tempHumidity**: Den här mappen innehåller Arduino koden till temperatur sensor programmet och testen i python.

# Användning

- **LEDControl** :
- 1. Inkludera **My_stm32f4_uart_lib.h** i din programkod.
2. Anropa **LIB_UART_Init-funktionen** för att initiera UART med önskad kommunikationstyp och baud rate.
3. Använd **LIB_UART_Write-funktionen** för att skicka tecken över UART.
4. Använd **LIB_UART_Read-funktionen** för att ta emot tecken.

# Licens

Det här projektet är licensierat under **_MIT-licensen_**.
