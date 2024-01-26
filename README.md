# Gruppuppgift
 LED control och temperatur monitor program med tester i python 

 # Filbeskrivningar
- **LEDControl.ino** : Den här filen inneh
- **My_stm32f4_uart_lib.h**: Den här filen ärver från **My_stm32f4_uart_driver.h** och deklarerar två uppräkningskonstanter: **UART_ComType** och **UART_BaudrateType**. Den inkluderar också tre funktionsdeklarationer:
    - _LIB_UART_Write_: Tar emot ett tecken som input och skickar det över UART.
    - _LIB_UART_Read_: Tar emot ett tecken och skriver ut det.
    - _LIB_UART_Init_: Tar emot uppräkningskonstanterna för att initiera UART.
- **My_stm32f4_uart_lib.c** : Den här filen börjar med att definiera olika variabler som behövs för funktionerna. Den sätter _baud rate_, _aktiverar_ och _inaktiverar_ UART och TX, _definierar stoppbiten_ och _konfigurerar flödeskontroll_. Sedan går den vidare till att fullständigt definiera funktionerna som deklarerats i *My_stm32f4_uart_lib.h*.
- **main.c**: Den här filen visar exekveringen av applikationen. Den inkluderar *My_stm32f4_uart_lib.h* och initierar UART för att möjliggöra kommunikation. Inne i en while-loop använder den UART-skriverfunktionen för att kontinuerligt skicka tecken över UART.

# Användning

1. Inkludera **My_stm32f4_uart_lib.h** i din programkod.
2. Anropa **LIB_UART_Init-funktionen** för att initiera UART med önskad kommunikationstyp och baud rate.
3. Använd **LIB_UART_Write-funktionen** för att skicka tecken över UART.
4. Använd **LIB_UART_Read-funktionen** för att ta emot tecken.

# Licens

Det här projektet är licensierat under **_MIT-licensen_**.
