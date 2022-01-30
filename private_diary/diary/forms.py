from email import message
from django.core.mail import EmailMessage
from django import forms

from .models import Diary

# Not use model because no need to use database
class InquiryForm(forms.Form):
  name = forms.CharField(label='name', max_length=30)
  email = forms.EmailField(label='email')
  title = forms.CharField(label='title', max_length=30)
  message = forms.CharField(label='message', widget=forms.Textarea)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)


  # default function
  def send_email(self):
    # get data from form
    name = self.cleaned_data['name']
    email = self.cleaned_data['email']
    title = self.cleaned_data['title']
    message = self.cleaned_data['message']

    # make each args of EmailMessage
    subject = 'お問い合わせ'
    message = '送信者名: {0}\nメールアドレス: {1}\nメッセージ:\n{2}'.format(name,email,message)
    from_email = 'yutounwasese@gmail.com'
    to_list = [
      'geek.yuto@gmail.com'
    ]
    cc_list = [
      email
    ]
    message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
    message.send()

# use model because use database this time
class DiaryCreateForm(forms.ModelForm):
    class Meta:
        model = Diary
        # fields = ('title', 'content', 'photo1', 'photo2', 'photo3',)
        fields = '__all__'

    # this is how to apply Bootstrap form-control class to all field
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
