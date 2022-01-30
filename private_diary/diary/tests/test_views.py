from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from ..models import Diary

class LoggedInTestCase(TestCase):
	"""Original TestCase which override common advance process each Test Classes use """

	def setUp(self):
		"""advance settings before running Test methods"""

		# set password for Test user
		self.password = 'starving_guy'

		# create test user used on each instance methods 
		# and store that in Instance variable
		self.test_user = get_user_model().objects.create_user(
			username = 'yuto',
			email = 'geek.yuto@gmail.com',
			password = 'self.password'
		)

		# Login using test user
		self.client.login(email=self.test_user.email, password=self.password)

# By using LoggedInTestCase, loggedIn process is executed before each Test methods
class TestDiaryCreateView(LoggedInTestCase):
	def test_create_diary_success(self):
		"""Check if Create Diary works"""

		# POST param
		params = {
		'title': 'this is test title',
		'content': 'this is test content',
		'photo1':'',
		'photo2':'',
		'photo3':'',
		}

		# Execute Create Diary
		# With self.client, simulate only GET and POST requests.
		response = self.client.post(reverse_lazy('diary:diary_create'), params)

		# check if redirect to diary-list page works
		self.assertRedirects(response, reverse_lazy('diary:diary_list'))

		# check if diary data is saved in the DB
		self.assertEqual(Diary.objects.filter(title='this is test title').count(),1)

	def test_create_diary_failure(self):
		"""Check if Create Diary View fail without param"""
		
		# Execute Create Diary
		response = self.client.post(reverse_lazy('diary:diary_create'))
		# Check if error shows without input on required form field
		self.assertFormError(response, 'form', 'title', 'このフィールドは必須です。')

class TestDiaryUpdateView(LoggedInTestCase):
	"""TestCase for DuaryUpdateView"""

	def test_update_diary_success(self):
		"""Check if Update Diary works"""

		# Create test Diary data
		diary = Diary.objects.create(user=self.test_user, title='before updating title')

		# POST param
		params = {'title': 'After Updating title'}

		# Execute Update
		response = self.client.post(reverse_lazy('diary:diary_update', kwargs={'pk': diary.pk}), params)

		# check if redirect to diary-detail works
		self.assertRedirects(response, reverse_lazy('diary:diary_detail', kwargs={'pk':diary.pk}))

		# check if diary data is saved in the DB
		self.assertEqual(Diary.objects.filter(title='After Updating title').count(),1)

	def test_update_diary_failure(self):
		"""Check if Update Diary View fail with pk which does not exist"""
		
		# Execute Update Diary
		# pk = 9213 does not exist on DB
		response = self.client.post(reverse_lazy('diary:diary_update'), kwargs={'pk': 9213})
		# Check if response is 404 when records associated with 9213 does not exist
		self.assertEqual(response.status_code, 404)

	

class TestDiaryDeleteView(LoggedInTestCase):
	"""TestCase for DiaryDeleteView"""

	def test_delete_diary_success(self):
		"""Check if Delete Diary works"""

		# Create test Diary data
		diary = Diary.objects.create(user=self.test_user, title='title')

		# Execute delete
		response = self.client.post(reverse_lazy('diary:diary_delete', kwargs={'pk': diary.pk}))

		# check if redirect to diary-list works
		self.assertRedirects(response, reverse_lazy('diary:diary_list'))

		# check if diary data is deleted
		self.assertEqual(Diary.objects.filter(pk = diary.pk).count(),0)

	def test_delete_binary_failure(self):
		"""Check if Delete Diary View fail with pk which does not exist"""
		
		# Execute delete Diary
		# pk = 9213 does not exist on DB
		response = self.client.post(reverse_lazy('diary:diary_delete'), kwargs={'pk': 9213})
		# Check if response is 404 when records associated with 9213 which does not exist
		self.assertEqual(response.status_code, 404)