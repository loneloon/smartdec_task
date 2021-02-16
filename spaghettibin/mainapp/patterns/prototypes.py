from .utils import *
from django.shortcuts import render
import copy


class PrototypeMixin:
    def clone(self):
        return copy.deepcopy(self)


class ModelMixin:

    def get_attrs(self):
        return dict((key, self.__getattribute__(key)) for key in self.__slots__ if self.__getattribute__(key) is not None)

    @classmethod
    def init_and_get_attrs(cls, *args, **kwargs):
        return cls(*args, **kwargs).get_attrs()


class BaseView:
    __slots__ = 'title', 'content', 'template'

    @classmethod
    def view(cls, request, **kwargs):

        if request.method == 'GET':
            return cls().get(request, **kwargs)
        else:
            return cls().post(request, **kwargs)

    def response(self, request, appendix=None):
        object_list = {'title': self.title,
                       'content': self.content,
                       'path': request.path}

        if appendix is not None:
            object_list.update(appendix)

        # if request.next:
        #     if request.path == signin_link:
        #         object_list['next'], request.next = request.next, ""
        #     elif request.next == signin_link:
        #         return redirect_302(f"{request.pop('next')}?next={request['path']}")
        #     else:
        #         return redirect_302(f"{request.pop('next')}")

        return render(request, self.template, object_list)

    def get(self, request, **kwargs):
        return self.response(request)

    def post(self, request, **kwargs):
        return self.get(request, **kwargs)
