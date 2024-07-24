import 'package:flutter/material.dart';

class ProjectListItem extends StatelessWidget {
  final Map<String, dynamic> project;

  const ProjectListItem({Key? key, required this.project}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ListTile(
      title: Text(project['title']),
      subtitle: Text(project['description']),
      onTap: () {
        // Handle item tap
      },
    );
  }
}
