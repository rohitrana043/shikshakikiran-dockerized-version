import requests
from django.shortcuts import render
from .models import Subject, Topic, Video
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class EducationSubjectList(ListView):
	model = Subject
	template_name = 'education/education.html'

class EducationTopicList(ListView):
	model = Topic
	def get_queryset(self):
		s=Subject.objects.get(subject_name=self.kwargs['subject'])
		return Topic.objects.filter(subject=s)


class EducationVideoList(LoginRequiredMixin, ListView):
	model = Video
	def get_queryset(self):
		t=Topic.objects.get(topic_name=self.kwargs['topic'])
		return Video.objects.filter(topic=t)

# def education(request):
# 	topic_tree_url = 'https://www.khanacademy.org/api/v1/topictree?kind=topic'
# 	main_data = requests.get(topic_tree_url).json()

# 	#Fetch Topic Nodes
# 	topic_nodes = main_data['children']

# 	#Fetch Topic Names where render_type is Domain
# 	topic_nodes = list(filter(lambda x:x['render_type']=='Domain',topic_nodes))

# 	for topic in topic_nodes:
# 		topic['topic_subjects'] = list(filter(lambda x:x['curriculum_key']=='', topic['children']))

# 	context={
# 		'topic_nodes': topic_nodes,
# 	}

# 	return render(request, 'education/education.html', context)