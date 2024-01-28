import 'package:flutter/material.dart';

// Your existing screen
import 'btn.dart'; // Import the new screen file
import 'checking.dart';

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

class MyHomePage extends StatefulWidget {
  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final String imageUrl =
      'https://i.pinimg.com/originals/2c/c8/4d/2cc84d20f5cf39cde7ae169aebf120c5.jpg'; 

      // Reemplaza con la URL de tu imagen
  String _formatTime(int totalSeconds) {
    int hours = totalSeconds ~/ 3600; // 3600 segundos en una hora
    int remainingSeconds = totalSeconds % 3600;
    int minutes = remainingSeconds ~/ 60; // El residuo después de las horas, dividido por 60
    int seconds = remainingSeconds % 60; // El residuo después de los minutos
    
    return '$hours:${_twoDigits(minutes)}:${_twoDigits(seconds)}';

    }

   String _twoDigits(int n) {
    if (n >= 10) return '$n';
    return '0$n';
  }

  int seg = 0;

  String get _t => _formatTime(seg);

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
                  Navigator.push(
                            context,
                            MaterialPageRoute(builder: (context) => Check()),
                          );
                },
              ),
              SizedBox(width: 50.0),
              Column(
                children: [
                  Text(
                    _t,
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
                  setState(() {
                            print('reset');
                            seg = 0;  
                          });;
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
                          setState(() {
                            print('$seg');
                            seg += 900;  
                          });
                          // Acción del primer botón
                          
                        },
                        child: Text('15 min'),
                      ),
                      SizedBox(height: 8.0), // Añade espacio entre los botones
                      ElevatedButton(
                        onPressed: () {
                         setState(() {
                            print('$seg');
                            seg += 1800;  
                          });
                          
                        },
                        child: Text('30 min'),
                      ),
                    ],
                  ),
                ),
                Expanded(
                  child: Column(
                    children: [
                      ElevatedButton(
                        onPressed: () {
                          setState(() {
                            print('$seg');
                            seg += 3600;  
                          });
                        },
                        child: Text('1 hora'),
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
                        child: Text('personalizada'),
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
