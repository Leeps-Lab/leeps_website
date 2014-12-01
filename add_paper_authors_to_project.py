for paper in Paper.objects.all():
    projects = paper.project_set.all()
    if len(projects) != 0:
        project = projects[0]
        paper_authors = set(paper.authors.all())
        project_people = set(project.people.all())
        if not paper_authors.issubset(project_people):
            for author in paper_authors.difference(project_people):
                project.people.add(author)
                project.save()
