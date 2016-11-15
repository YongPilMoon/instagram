from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, FormView, DeleteView
from django.views.generic import ListView
from photo.models import Photo, PhotoComment
from django import forms

# def photo_list(request):
#     photos = Photo.objects.all()
#     context = {
#         'photos': photos,
#     }
#     return render(request, 'photo/photo_list.html', context)


class CommentInsertForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)


class PhotoDisplay(DetailView):
    model = Photo

    def get_context_data(self, **kwargs):
        context = super(PhotoDisplay, self).get_context_data(**kwargs)
        context['form'] = CommentInsertForm()
        return context


class CommentInsert(SingleObjectMixin, FormView):
    template_name = 'photo/photo_detail.html'
    form_class = PhotoComment
    model = Photo

    # form_valid는 is_valid이후에 실행
    def form_valid(self, form):
        self.object = self.get_object()
        content = form.cleand_data['content']
        PhotoComment.objects.create(
            photo=self.object,
            author=self.request.user,
            content=content
        )
        return super(CommentInsert, self).form_valid(form)

    def get_success_url(self):
        return reverse('photo:photo_detail', kwargs={'pk': self.object.pk})


class PhotoDetail(View):

    def get(self, request, *args, **kwargs):
        view = PhotoDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentInsert.as_view()
        return view(request, *args, **kwargs)


class PhotoList(ListView):
    model = Photo
    paginate_by = 3
    context_object_name = 'photos'
    queryset = Photo.objects.order_by('-created_date')


@method_decorator(login_required, name='dispatch')
class PhotoAdd(CreateView):
    model = Photo
    fields = ['image', 'content']
    success_url = reverse_lazy('photo:photo_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PhotoAdd, self).form_valid(form)


class PhotoDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('photo:photo_list')
