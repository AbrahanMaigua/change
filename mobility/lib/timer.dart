import 'dart:async';

import 'package:flutter/material.dart';

Function Temporizador() {
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
  void dispose() {
    _timer.cancel();
    super.dispose();
  }
}

