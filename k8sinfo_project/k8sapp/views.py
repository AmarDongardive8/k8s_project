from django.shortcuts import render

def k8s_info_view(request):
    return render(request, 'k8sapp/k8s_info.html')
