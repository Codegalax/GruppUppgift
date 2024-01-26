# Gruppuppgift
 LED control och temperatur monitor program med tester i python 

 # Mappbeskrivningar
- **LEDControl** : Den här mappen innehåller Arduino koden till LED control programmet och python koden som testar programmet.
- **tempHumidity**: Den här mappen innehåller Arduino koden till temperatur sensor programmet och testen i python.

# Användning

LEDControl :
-  Kompilera **LEDControl.ino** med Arduino IDE och ladda upp det till Arduino Uno. Dubbel kolla så serial monitor är stängd.
-  Kompilera python koden **LEDControlTest.py** och välj den port som är ansluten till Arduino. Med kommandon **ON/OFF** eller **EXIT** kan du styra hur LED tänds.
-  Python versionen som användes är 3.12.
 
tempHumidity :
-  Kompilera **tempHumidity.ino** med Arduino IDE och ladda upp det till Arduino Uno. Dubbel kolla så serial monitor är stängd.
-  Kompilera python koden **tempHumidityTest.py**. Med kommandon **Temp** eller **Humidity** kan få respektiv värde. Serial porten i den här exemplet är /dev/ttyACM0 men kan ändras i koden innan kompilering.
-  Python versionen som användes är 3.12.
# Licens

