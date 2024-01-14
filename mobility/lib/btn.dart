// new_screen.dart
import 'package:flutter/material.dart';

class NewScreen extends StatelessWidget {
 
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('4 Columnas x 3 Filas'),
      ),
      body: Center(
      child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Text(
                labeltime().currentTime,
                style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
              ),
              ],
            ),
            SizedBox(height: 100.0),

            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                NumberButton(number: 1),
                NumberButton(number: 2),
                NumberButton(number: 3),
              ],
            ),
            SizedBox(height: 18.0),

            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                NumberButton(number: 4),
                NumberButton(number: 5),
                NumberButton(number: 6),
              ],
            ),
            SizedBox(height: 18.0),

            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                NumberButton(number: 7),
                NumberButton(number: 8),
                NumberButton(number: 9),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

class labeltime {
  // Singleton instance
  static final labeltime _instance = labeltime._internal();

  // Valor global
  String currentTime = '00:00:00';

  // Getter para acceder a la instancia de la clase
  factory labeltime() {
    return _instance;
  }

  // Constructor privado
  labeltime._internal();
}

// Uso de la variable global

class NumberButton extends StatelessWidget {
 final int number;

  NumberButton({required this.number});

  @override
  Widget build(BuildContext context) {
    labeltime().currentTime = '12:34:56';
    
    return Container(
      width: 60.0, // Ajusta el ancho del botón
      height: 50.0, // Ajusta la altura del botón
      decoration: BoxDecoration(
        shape: BoxShape.circle, // Hace que el contorno del botón sea circular
        color: Colors.blue, // Cambia el color del botón
      ),
      child: ElevatedButton(
        onPressed: () {
          // Acción cuando se presiona el botón
          print('Botón $number presionado');
        },
        style: ElevatedButton.styleFrom(
          primary: Colors.transparent, // Hace que el fondo del botón sea transparente
          onPrimary: Colors.white, // Cambia el color del texto del botón
        ),
        child: Text(
          '$number',
          style: TextStyle(fontSize: 20.0), // Ajusta el tamaño del texto del botón
        ),
      ),
    );
  }
}

