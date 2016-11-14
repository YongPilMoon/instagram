from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from photo.models import Photo


def photo_list(request):
    photos = Photo.objects.all()
    context = {
        'photos': photos,
    }
    return render(request, 'photo/photo_list.html', context)


class PhotoList(ListView):
    model = Photo
    paginate_by = 3
    context_object_name = 'photos'


@method_decorator(login_required, name='dispatch')
class PhotoAdd(CreateView):
    model = Photo
    fields = ['image', 'content']
    success_url = reverse_lazy('photo:photo_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PhotoAdd, self).form_valid(form)