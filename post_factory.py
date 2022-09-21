"""
PostFactory - generates fake forum posts

Example usage:
    PostFactory.generate(5)

Returns:
    A list of 5 fake posts
"""

from faker import Faker

class PostFactory():
    """Creates fake posts"""
    fake = Faker()
    counter = 0

    def __init__(self):
        """Constructor"""
        PostFactory.counter += 1
        self.id = PostFactory.counter
        self.name = self.fake.name()
        self.email = self.fake.email()
        self.body = self.fake.text()

    def serialize(self) -> dict:
        """Returns the instance as a dictionary"""
        return {
            "id": self.id,
            "postID": 1,
            "name": self.name,
            "email": self.email,
            "body": self.body
        }

    @staticmethod
    def generate(max: int = 1) -> list:
        results = []
        for _ in range(max):
            results.append(PostFactory().serialize())
        return results
