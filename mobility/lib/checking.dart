// checking.dart
import 'package:flutter/material.dart';
import 'pix.dart'; 


class Check extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(''),
      ),
      body: Align(
        alignment: Alignment.topCenter,
        child: Column(
          children: [
            SizedBox(height: 16.0), // Añade espacio entre la imagen y los botones

            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Column(
                  children: [
                SizedBox(height: 152.0),

                    Text(
                      'Precio: \tR\$ 12.22 \n'
                      'tiempo: 00:00:00',
                      style: TextStyle(fontSize: 20.0),
                      textAlign: TextAlign.center, // Puedes ajustar la alineación según tus necesidades
                      maxLines: null, // null significa que puede tener un número ilimitado de líneas
                    ),
                    SizedBox(height: 80.0),
                    // Puedes agregar aquí más elementos si es necesario
                  ],
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
                          print('15 min');
                          // Acción del primer botón
                          Navigator.push(
                             context,
                             MaterialPageRoute(builder: (context) => CountdownTimer()),
                           );
                        },
                        child: Text('pix '),
                      ),
                      SizedBox(height: 8.0), // Añade espacio entre los botones
                      
                    ],
                  ),
                ),
                Expanded(
                  child: Column(
                    children: [
                      ElevatedButton(
                        onPressed: () {
                          print('1 hora');
                          // Acción del tercer botón
                        },
                        child: Text('carto covenio'),
                      ),
                      SizedBox(height: 8.0), // Añade espacio entre los botones
                      
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
