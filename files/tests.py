from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from files.models import Files, Folders
from users.models import User


class CloudTextCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="12345")
        self.files = Files.objects.create(
            file_name="test_file_name",
            uploaded_file="media/files/users_files/Пересдачи_за_зиму_2024_1_выпуск.xlsx",
            owner=self.user,
        )
        self.folders = Folders.objects.create(
            folders_name="test_folders_name", owner=self.user
        )

    def test_files_list(self):
        url = reverse("files:files_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_files(self):
        self.client.force_login(self.user)
        url = reverse("files:files_create")
        data = {
            "files_name": "files_name_1",
            "uploaded_file": "media/files/users_files/Пересдачи_за_зиму_2024_1_выпуск.xlsx",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_favourites_files(self):
        url = reverse("files:files_by_favourites")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_recent(self):
        url = reverse("files:recent_files_and_folders")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_files_delete(self):
        url = reverse("files:files_delete", args=(self.files.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_folders_list(self):
        url = reverse("files:folders_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_folders(self):
        self.client.force_login(self.user)
        url = reverse("files:folders_create")
        data = {
            "folders_name": "folders_name_1",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_files_by_folders(self):
        url = reverse("files:files_by_folders", args=(self.folders.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_folders_delete(self):
        url = reverse("files:folders_delete", args=(self.folders.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
