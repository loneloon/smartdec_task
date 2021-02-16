from django.shortcuts import render
from .patterns.prototypes import BaseView
from api.views import get_list


class IndexView(BaseView):
    def __init__(self):
        self.title = "Home"
        self.content = "New posted notes will be displayed here..."
        self.template = "../templates/mainapp/index.html"

    def get(self, request, **kwargs):
        # initial_list = get_list(request).data

        # objects = {"script_list": initial_list}
        return self.response(request)
