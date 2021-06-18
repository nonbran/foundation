from constant.names import drive
from constant.names import home
from constant.names import project
from constant.names import projects
from constant.names import root
from constant.names import script
from pathlib import Path
import os

# initialize the core paths
path_to_running_script = Path(os.getcwd())
path_to_project = path_to_running_script.parent
path_to_projects = path_to_project.parent
path_to_home = path_to_projects.parent

# build the path dictionary
paths = {
    script:         path_to_running_script,
    project:        path_to_project,
    projects:       path_to_projects,
    home:           path_to_home,
    root:           path_to_home.root,
    drive:          path_to_home.parts[0]
}

# verify the core paths exist
for path_name, path in paths.items():
    if not os.path.exists(path):
        print(f'path does not exist at {path}')
        exit()

pass

