from email.policy import default
import imp
from operator import ipow
from re import template
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
import logging
from .forms import InquiryForm, DiaryCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Diary
# logger setting
logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
  template_name = "index.html"

class InquiryView(generic.FormView):
  template_name = "inquiry.html"
  form_class = InquiryForm
  success_url = reverse_lazy('diary:inquiry')

  # run unless validation blocks form objects
  def form_valid(self, form):
    form.send_email()
    messages.success(self.request, 'Successfullly, an email has been sent:D')
    logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
    # call parent class's form_valid and send response to success_url
    return super().form_valid(form)

class DiaryListView(generic.ListView, LoginRequiredMixin):
  model = Diary
  template_name = 'diary_list.html'
  pagenate_by = 2

  # override get_queryset to filter queryset
  def get_queryset(self):
    diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
    return diaries

class DiaryDetailView(generic.DetailView, LoginRequiredMixin):
  model = Diary
  template_name = 'diary_detail.html'
  # chage variable from 'pk' to 'id'
  pk_url_kwarg = 'id'

class DiaryCreateView(generic.CreateView, LoginRequiredMixin):
  model = Diary
  template_name = 'diary_create.html'
  form_class = DiaryCreateForm
  success_url = reverse_lazy('diary:diary_list')

  # This method is called when valid form data has been posted.
  def form_valid(self,form):
    # Use function below if input valuse is not enough and store input values in variable
    diary = form.save(commit=False)
    # At this time, user object from request also must be included.
    diary.user = self.request.user
    # save diary in the database
    diary.save()
    messages.success(self.request, 'Successfully, you have posted new diary.')
    return super().form_valid(form)

  # This method is called when valid form data has failed to post.
  def form_invalid(self, form):
    messages.error(self.request, 'Unfortunately, you failed to post new diary.')