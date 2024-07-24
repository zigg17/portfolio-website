import 'package:flutter/material.dart';
import 'screens/project_list_screen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Web App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: ProjectListScreen(),
    );
  }
}

