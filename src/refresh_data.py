import os
import git
import shutil
from fnmatch import fnmatch

def listdir(cwd: str, prefix: str) -> list:
    # List files in a directory
    matches = []
    for path, subdirs, files in os.walk(cwd):
        for name in files:
            if fnmatch(name, prefix):
                matches.append(os.path.join(path, name))
    return matches

def refresh_names() -> None:
    # Refresh data from git
    global unwanted_file_types
    unwanted_file_types = ['*.csv', '*.md', '*.idx']
    def remove_unwanted():
        global unwanted_file_types
        for file_type in unwanted_file_types:
            for file in listdir('data/names', file_type):
                os.remove(file)
    remove_unwanted()
    try:
        git.Repo.clone_from(
            'https://github.com/aruljohn/popular-baby-names.git',
            'data/names')
    except git.exc.GitCommandError:
        shutil.rmtree('data/names', ignore_errors=True)
        git.Repo.clone_from(
            'https://github.com/aruljohn/popular-baby-names.git',
            'data/names')
    remove_unwanted()
    

def refresh_data() -> None:
    refresh_names()

if __name__ == '__main__':
    refresh_data()