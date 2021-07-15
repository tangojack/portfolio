from django.test import TestCase

# Create your tests here.
from projects.models import Projects

class ProjectsTest(TestCase):

    def test_project_creation(self):
        project = Project.objects.create(title="Transcription", description="My transcriptions")
