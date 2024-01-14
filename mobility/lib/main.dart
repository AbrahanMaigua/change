import 'package:flutter/material.dart';

// Your existing screen
import 'btn.dart'; // Import the new screen file


void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  final String imageUrl =
      'https://i.pinimg.com/originals/2c/c8/4d/2cc84d20f5cf39cde7ae169aebf120c5.jpg'; 
      // Reemplaza con la URL de tu imagen

  String _formatTime() {
    int hours   = 00;
    int minutes = (0 % 60);
    int seconds = (0 % 60);
    return '$hours:${_twoDigits(minutes)}:${_twoDigits(seconds)}';
  }

   String _twoDigits(int n) {
    if (n >= 10) return '$n';
    return '0$n';
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Imagen desde URL con Botones'),
      ),
      body: Align(
        alignment: Alignment.topCenter,
        child: Column(
          children: [
            Container(
              width: double.infinity,
              height: 400.0, // Establece la altura deseada
              padding: EdgeInsets.all(20.0), // Añade padding alrededor de la imagen
              child: Image.network(
                imageUrl,
                fit: BoxFit.contain,
              ),
            ),
            SizedBox(height: 16.0), // Añade espacio entre la imagen y los botones
            Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              IconButton(
                icon: Icon(Icons.arrow_back),
                onPressed: () {
                  // Acción del botón izquierdo
                  print('Botón izquierdo presionado');
                },
              ),
              SizedBox(width: 50.0),
              Column(
                children: [
                  Text(
                    _formatTime(),
                    style: TextStyle(fontSize: 20.0),
                  ),
                  SizedBox(height: 8.0),
                 
                ],
              ),
              SizedBox(width: 50.0),
              IconButton(
                icon: Icon(Icons.arrow_forward),
                onPressed: () {
                  // Acción del botón derecho
                  print('Botón derecho presionado');
                },
              ),
            ],
          ),
            SizedBox(height: 30.0), // Añade espacio entre la imagen y los botones

            Row(
              children: [
                Expanded(
                  child: Column(
                    children: [
                      ElevatedButton(
                        onPressed: () {
                          // Acción del primer botón
                          print('Botón 1 presionado');
                        },
                        child: Text('Botón 1'),
                      ),
                      SizedBox(height: 8.0), // Añade espacio entre los botones
                      ElevatedButton(
                        onPressed: () {
                          // Navigate to the new screen
                          Navigator.push(
                            context,
                            MaterialPageRoute(builder: (context) => NewScreen()),
                          );
                        },
                        child: Text('Botón 2'),
                      ),
                    ],
                  ),
                ),
                Expanded(
                  child: Column(
                    children: [
                      ElevatedButton(
                        onPressed: () {
                          // Acción del tercer botón
                          print('Botón 3 presionado');
                        },
                        child: Text('Botón 3'),
                      ),
                      SizedBox(height: 8.0), // Añade espacio entre los botones
                      ElevatedButton(
                        onPressed: () {
                          // Acción del tercer botón
                          print('Botón 3 presionado');
                        },
                        child: Text('Botón 3'),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
