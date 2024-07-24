import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  final String baseUrl = 'http://127.0.0.1:8000/api';  // Update this to your Django server's address if it's different

  Future<List<dynamic>> fetchProjects() async {
    final response = await http.get(Uri.parse('$baseUrl/projects/'));
    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to load projects');
    }
  }
}
