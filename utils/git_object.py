"""Module implementing a git object
"""


class GitObject:
    repo = None

    def __init__(self, repo = None, data = None) -> None:
        self.repo = repo
        if data is not None:
            self.deserialize(data)
        
    def serialize(self) -> None:
        """Method to serialize the data
        """
        raise NotImplementedError
    
    def deserialize(self) -> None:
        """Method to deserialize the data
        """
        raise NotImplementedError
    