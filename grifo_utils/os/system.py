import os

def _delete_file(path):
    try:
        """ Deletes file from filesystem. """
        if os.path.isfile(path):
            os.remove(path)
        return
    except Exception as e:
        return