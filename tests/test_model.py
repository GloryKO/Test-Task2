from django.test import TestCase
from api import models

class ModelTest(TestCase):
    def test_tag_model_str(self):
        task=models.Task.objects.create(
            task_name = "Assignment One",
            task_description ="Get Assignment One Done by 12",
            task_iscompleted = False
        )
        self.assertEqual(str(task),task.task_name)