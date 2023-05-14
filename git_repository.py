"""Module with git repository object
"""
import os
import configparser
from repo_utils import repo_file, repo_dir, repo_default_config


class GitRepository:
    """Class to create repo object
        A git repo has two things 
        - work tree [files in version control live] # ?
        - git directory where git has it's own data
        # there are a lot more cases too
        -- as this is base
        the repo with hold two paths worktree and gitdir
    """
    worktree = None
    gitdir = None
    conf = None

    def __init__(self, path, force=False) -> None:
        self.worktree = path
        self.gitdir = os.path.join(paths=[path, ".git"])

        assert (force or os.path.isdir(self.gitdir)), "Path does not contain a repository"

        self.conf = configparser.ConfigParser()
        conf_file = repo_file(self, "config")

        if conf_file and os.path.exists(conf_file):
            self.conf.read([conf_file])
        elif not force:
            raise Exception("Config file missing fromr path")
    
        if not force:
            vers = int(self.conf.get("core", "repositoryformatversion"))
            assert not vers, ValueError(f"unsupported repositoryformatversion {vers}")
    

def create_repo(path) -> GitRepository:
    """Method to create git repo for a directory by creating dir if not there else checking for emptiness
        and creating the following paths
        .git is the git directory itself, which contains:
            .git/objects/ : the object store, which we’ll introduce in the next section.
            .git/refs/ the reference store, which we’ll discuss . It contains two subdirectories, heads and tags.
            .git/HEAD, a reference to the current HEAD (more on that later!)
            .git/config, the repository’s configuration file.
            .git/description, the repository’s description file.
    """
    repo = GitRepository(path, True)

    if os.path.exists(repo.worktree):
        assert os.path.isdir(repo.worktree), Exception(f"{repo.worktree} is not a directory")
        assert not os.listdir(repo.worktree), Exception(f"Dir is not empty")
    else:
        os.makedirs(repo.worktree)

    assert(repo_dir(repo, "branches", mkdir=True))
    assert(repo_dir(repo, "objects", mkdir=True))
    assert(repo_dir(repo, "refs", "tags", mkdir=True))
    assert(repo_dir(repo, "refs", "head", mkdir=True))

    with open(repo_file(repo, "description"), "w") as file:
        file.write("Unnamed repo; edit this file 'ddescription' to name the repo.\n")
    
    with open(repo_file(repo, "head"), "w") as file:
        file.write("ref: refs/heads/master\n")
    
    with open(repo_file(repo, "config"), "w") as file:
        config = repo_default_config()
        config.write(file)
    
    return repo
