import 'package:flutter/material.dart';
import '../api_service.dart';
import '../widgets/project_list_item.dart';

class ProjectListScreen extends StatefulWidget {
  const ProjectListScreen({Key? key}) : super(key: key);

  @override
  _ProjectListScreenState createState() => _ProjectListScreenState();
}

class _ProjectListScreenState extends State<ProjectListScreen> {
  final ApiService apiService = ApiService();
  late Future<List<dynamic>> projects;

  @override
  void initState() {
    super.initState();
    projects = apiService.fetchProjects();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Projects'),
      ),
      body: FutureBuilder<List<dynamic>>(
        future: projects,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          } else {
            return ListView.builder(
              itemCount: snapshot.data?.length ?? 0,
              itemBuilder: (context, index) {
                var project = snapshot.data?[index];
                return ProjectListItem(project: project);
              },
            );
          }
        },
      ),
    );
  }
}

