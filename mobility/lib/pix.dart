import 'dart:async';
import 'package:flutter/material.dart';
import 'main.dart';
import 'package:http/http.dart'

Function a(){

  var url = ('localhost:5000', 'api/data');
  print('Response status: ${url}');

};
class CountdownTimer extends StatefulWidget {
  @override
  Pix createState() => Pix();
}

class Pix extends State<CountdownTimer> {
  late Timer _timer;
  int _secondsRemaining = 10; // Tiempo total en segundos
  var data = await getData('http://10.0.2.2:5000/api/data');
  var decodedData = jsonDecode(data);
  print(decodedData['query'])
  final String imageUrl =
      'https://i.pinimg.com/originals/2c/c8/4d/2cc84d20f5cf39cde7ae169aebf120c5.jpg'; 

  @override
  void initState() {
    super.initState();
    _startTimer();
  }

  void _startTimer() {
    _timer = Timer.periodic(Duration(seconds: 1), (timer) {
      setState(() {
        if (_secondsRemaining > 0) {
          _secondsRemaining--;
        } else {
          _timer.cancel(); // Detener el temporizador cuando llega a cero
          
          // Redirigir a la página de inicio
          Navigator.of(context).pushReplacement(
            MaterialPageRoute(builder: (context) => MyHomePage()), // Cambiado a MyHomePage
          );
        }
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    String minutes = (_secondsRemaining ~/ 60).toString().padLeft(2, '0');
    String seconds = (_secondsRemaining % 60).toString().padLeft(2, '0');

    return Scaffold(
      appBar: AppBar(
        title: Text('Temporizador de Cuenta Regresiva'),
        centerTitle: true,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              '$minutes:$seconds',
              style: TextStyle(fontSize: 48, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 20),
            Container(
              width: double.infinity,
              height: 400.0, // Establece la altura deseada
              padding: EdgeInsets.all(20.0), // Añade padding alrededor de la imagen
              child: Image.network(
                imageUrl,
                fit: BoxFit.contain,
              ),
            ),
            SizedBox(height: 16.0),
            ElevatedButton(
              onPressed: () {
                // Puedes reiniciar el temporizador si lo deseas
                setState(() {
                  _secondsRemaining = 10; // Establece el tiempo deseado al reiniciar
                });
                _startTimer();
                a()
              },
              child: Text('Reiniciar'),
            ),
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    _timer.cancel(); // Asegúrate de detener el temporizador al salir de la pantalla
    super.dispose();
  }
}
