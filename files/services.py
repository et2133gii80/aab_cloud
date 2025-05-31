from files.models import Files
from files.models import Folders


def get_files_by_folders(folders_id):
    folder = Folders.objects.get(id=folders_id)
    files = Files.objects.filter(folder=folder)
    return files

def get_favourites_files():
    return Files.objects.filter(favorite= True)