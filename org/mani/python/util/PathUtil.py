import os

def get_root_path():
    """
    Returns the root path of the project.
    """
    return os.path.abspath(os.path.join(os.getcwd(), '../../../..'))