from django.test import TestCase
from validations.models import ValidationTask


class ValidationTaskTest(TestCase):

    def test_task_default_completed(self):

        task = ValidationTask()

        self.assertFalse(task.completed)
