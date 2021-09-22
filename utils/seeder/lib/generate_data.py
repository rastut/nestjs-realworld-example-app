from datetime import datetime
from faker import Faker
from typing import Iterator, List, Dict, Any

# Class GenerateRandomData: The class includes diferent methods to generate fake data for
# the db. Supports all the entities.
#
class GenerateRandomData:
    
    def __init__(self, count: int) -> None:
        self.count = count
        self.fake = Faker()
    
    # Generate fake data for article 
    #
    def article_data(self) -> Iterator[Dict[str, Any]]:

        for i in range(1, self.count + 1):
            article_dict = [{
                "id": i,
                "slug": self.fake.unique.bothify(text="????"),
                "title": self.fake.sentence(nb_words=6),
                "description": self.fake.paragraph(nb_sentences=3),
                "body":  self.fake.paragraph(nb_sentences=5),
                "created": self.fake.date_between_dates(date_start=datetime(2021,1,1), date_end=datetime(2021,4,1)), 
                "updated": self.fake.date_between_dates(date_start=datetime(2021,5,1), date_end=datetime(2021,8,1)),
                "tagList": self._generate_taglist(),
                "favoriteCount": self.fake.random_int(min=0, max=30),
                "authorId": self.fake.random_int(min=1, max=1000)

            }]

            yield from article_dict
        

    # Generate fake data for user 
    #
    def user_data(self) -> Iterator[Dict[str, Any]]:


        for i in range(1, self.count + 1):
            user_dict = [{
                "id": i,
                "username": self.fake.unique.user_name(),
                "email": self.fake.unique.email(),
                "bio": self.fake.sentence(nb_words=6),
                "image":  f"http://s3.amazonaws.com/fakebucket/{self.fake.file_name(category='image')}",
                "password": self.fake.md5()      
            }]

            yield from user_dict
        

    # Generate fake data for tag 
    #    
    def tag_data(self) -> Iterator[Dict[str, Any]]:


        for i in range(1, self.count + 1):
            tag_dict = [{
                "id": i,
                "tag": self.fake.word(),
            }]

            yield from tag_dict
  
    # Generate fake data for follow 
    # 
    def follow_data(self) -> Iterator[Dict[str, Any]]:


        for i in range(1, self.count + 1):
            follow_dict = [{
                "id": i,
                "followerId": self.fake.random_int(min=1, max=1000),
                "followingId": self.fake.random_int(min=1, max=1000),
            }]
            yield from follow_dict    

    # Generate fake data for comment 
    # 
    def comment_data(self) -> Iterator[Dict[str, Any]]:


        for i in range(1, self.count + 1):
            comment_dict = [{
                "id": i,
                "body": self.fake.sentence(nb_words=1),
                "articleId": self.fake.random_int(min=1, max=1000),
            }]

            yield from comment_dict

    # Generate fake data for favorite_article table
    # 
    def favorite_articles_data(self) -> Iterator[Dict[str, Any]]:
        # I wanted to use fake.unique.random_int(min=1, max=1000) but getting some duplicates
        # just adding 1to1 mapping
        #
        for i in range(1, self.count + 1):
            favorite_article_dict = [{
                "userId": i,
                "articleId": i,
            }]

            yield from favorite_article_dict

    # _generate_taglist: Helper for generate taglist for user profile
    #
    def _generate_taglist(self) -> List:
        self.tags = []

        for _ in range(5):
            self.tags.append(self.fake.word())
        
        return self.tags



