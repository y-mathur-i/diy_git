"""Module containing commonly used utilities
"""
import os
import configparser


def repo_path(repo, *path):
    """Compute path under repo's git dir
    """
    return os.path.join(repo.gitdir, *path)


def repo_file(repo, *path, mkdir: bool = False):
    """Method creates the path is not there
    """
    if repo_dir(repo, *path[:-1], mkdir):
        return repo_path(repo, path)


def repo_dir(repo, *path, mkdir=False):
    """same as repo path but makes a dir
    """
    path = repo_path(repo, *path)
    if os.path.exists(path):
        if os.path.isdir(path):
            return path
        else:
            raise Exception("path not a directory")
    if mkdir:
        os.makedirs(path)
        return path


def repo_default_config():
    ret = configparser.ConfigParser()

    ret.add_section("core")
    ret.set("core", "repositoryformatversion", "0")
    ret.set("core", "filemode", "false")
    ret.set("core", "bare", "false")

    return ret
