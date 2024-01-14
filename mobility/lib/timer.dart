import 'dart:async';

import 'package:flutter/material.dart';

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
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  late Stopwatch _stopwatch;
  late Timer _timer;
  bool _isRunning = false;

  @override
  void initState() {
    super.initState();
    _stopwatch = Stopwatch();
    _timer = Timer.periodic(Duration(milliseconds: 700), _updateTimer);
  }

  void _startStop() {
    setState(() {
      if (_isRunning) {
        _stopwatch.stop();
      } else {
        _stopwatch.start();
      }
      _isRunning = !_isRunning;
    });
  }

  void _reset() {
    setState(() {
      _stopwatch.reset();
      _isRunning = false;
    });
  }

  void _updateTimer(Timer timer) {
    if (_isRunning) {
      setState(() {});
    }
  }

   void _showNewView() {
    _stopwatch.stop();
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => NewView()),
    );
  }


  String _formatTime() {
    int hours   = _stopwatch.elapsed.inHours;
    int minutes = (_stopwatch.elapsed.inMinutes % 60);
    int seconds = (_stopwatch.elapsed.inSeconds % 60);
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
        title: Text('Cronómetro'),
        centerTitle: true,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              'Tiempo transcurrido:',
              style: TextStyle(fontSize: 18),
            ),
            Text(
              _formatTime(),
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 20),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                ElevatedButton(
                  onPressed: _startStop,
                  child: Text(_isRunning ? 'Detener' : 'Iniciar'),
                ),
                SizedBox(width: 20),
                ElevatedButton(
                  onPressed: _reset,
                  child: Text('Reiniciar'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    _timer.cancel();
    super.dispose();
  }
}


class NewView extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Nueva Vista'),
        centerTitle: true,
      ),
      body: Center(
        child: Text(
          '¡Ha pasado un minuto!',
          style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
        ),
      ),
    );
  }
}