from django.shortcuts import render
from projects.models import Projects


def index(request):
    project_data = Projects.objects.all()


    return render(request,"index.html",{'project_data':project_data})

def portfolio(request):
    project_data = Projects.objects.all()
    return render(request,"portfolio.html",{'project_data':project_data})

def project_detail_view(request, project_id):
    project = Projects.objects.filter(project_id=project_id)
    for data in project:
        project_name = data.project_name
        project_description = data.project_description
        project_Sills = data.project_Sills
        project_live_link = data.project_live_link
        project_github_link = data.project_github_link
        project_image_1 = data.image_1
        project_image_2 = data.image_2

    project = {'project_name': project_name,'project_description':project_description,'project_Skills':project_Sills,'project_live_link':project_live_link,'project_github_link':project_github_link,'project_image_1':project_image_1,'project_image_2':project_image_2}

    return render(request, 'project_page.html', project)
