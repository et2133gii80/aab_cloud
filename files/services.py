from files.models import Files, Folders


def get_files_by_folders(folders_id):
    folder = Folders.objects.get(id=folders_id)
    files = Files.objects.filter(folder=folder)
    return files


def get_favourites_files():
    return Files.objects.filter(favorite=True)


def recent_file_and_folders():
    files = Files.objects.order_by("-created_at")
    return files


# from django.contrib.auth import get_user_model
#
#
# def filter_users():
#     User = get_user_model()
#     return User.objects.filter(is_sub=True)
