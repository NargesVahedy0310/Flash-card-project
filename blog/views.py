import socket
from .models import Article, ViewSite
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404

class BlogMe(APIView):

    def get(self, request):
        ip_address = ViewSite.objects.all().values()
        count = len(ip_address)
        all_ip = []
        for num in range(count):
            ip_ad = ViewSite.objects.all().values()[::-1][num]
            ip = ip_ad['ip_address']
            all_ip.append(ip)
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        if not ip_address in all_ip:
            ip = ViewSite.objects.create(hostname=hostname, ip_address=ip_address)

        article = Article.objects.get(id=2)
        article.views = len(all_ip)
        article.save()

        Articles = Article.objects.all()
        context = {'data': Articles}
        return render(request, 'blogs.html', context)