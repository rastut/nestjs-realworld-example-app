from typing import Any, Dict, Iterator
import psycopg2.extras
import logging

# Class for insert data in PG. Include different methods to cover 
# all the tables from the DB
#
class PopulateData:
    def __init__(self, user: str, password: str, database: str, host: str) -> None:
        self.user = user
        self.password = password
        self.database = database
        self.host = host

        self._pgconnection()
        # Temporal, probably I should create a logging class but not enough time
        logging.basicConfig(level=logging.DEBUG)

    # Insert_users: inserts fake data for the user table. 
    # Input iterator for users.
    #
    def insert_users(self, users: Iterator[Dict[str, Any]]) -> None:
        
        try:

            with self.connection.cursor() as cursor:

                users = ({**user} for user in users)

                psycopg2.extras.execute_batch(cursor, """
                    INSERT INTO public.user VALUES (
                        %(id)s,
                        %(username)s,
                        %(email)s,
                        %(bio)s,
                        %(image)s,
                        %(password)s
                    );
                """, users)
            
            logging.info("User table seed completed!")
        
        except Exception as e:
            logging.error(f"Something has gone wrong inserting data for user: {e}")

    # Insert_tags: inserts fake data for the tags table. 
    # Input: tags iterator.
    #
    def insert_tags(self, tags: Iterator[Dict[str, Any]]) -> None:
        
        try:

            with self.connection.cursor() as cursor:

                tags = ({**tag} for tag in tags)

                psycopg2.extras.execute_batch(cursor, """
                    INSERT INTO tag VALUES (
                        %(id)s,
                        %(tag)s
                    );
                """, tags)
            
            logging.info("Tags table seed completed!")

        except Exception as e:
            logging.error(f"Something has gone wrong inserting data for tags: {e}")
    
    # Insert_follows: inserts fake data for the follows table. 
    # Input follows iterator.
    #
    def insert_follows(self, follows: Iterator[Dict[str, Any]]) -> None:
        
        try:

            with self.connection.cursor() as cursor:

                follows = ({**follow} for follow in follows)

                psycopg2.extras.execute_batch(cursor, """
                    INSERT INTO follows VALUES (
                        %(id)s,
                        %(followerId)s,
                        %(followingId)s
                    );
                """, follows)
            
            logging.info("Follow table seed completed!")

        except Exception as e:
            logging.error(f"Something has gone wrong inserting data for follows: {e}")       

    # Insert_comments: inserts fake data for the comments table. 
    # Input comments iterator.
    #
    def insert_comments(self, comments: Iterator[Dict[str, Any]]) -> None:
        
        try:

            with self.connection.cursor() as cursor:

                comments = ({**comment} for comment in comments)

                psycopg2.extras.execute_batch(cursor, """
                    INSERT INTO comment VALUES (
                        %(id)s,
                        %(body)s,
                        %(articleId)s
                    );
                """, comments)

            logging.info("Comment table seed completed!")

        except Exception as e:
            logging.error(f"Something has gone wrong inserting data for comments: {e}")

    # Insert_articles: inserts fake data for the articles table. 
    # Input articles iterator.
    #
    def insert_articles(self, articles: Iterator[Dict[str, Any]]) -> None:
        
        try:

            with self.connection.cursor() as cursor:

                articles = ({**article} for article in articles)

                psycopg2.extras.execute_batch(cursor, """
                    INSERT INTO article VALUES (
                        %(id)s,
                        %(slug)s,
                        %(title)s,
                        %(description)s,
                        %(body)s,
                        %(created)s,
                        %(updated)s,
                        %(tagList)s,
                        %(favoriteCount)s,
                        %(authorId)s
                    );
                """, articles)

            logging.info("Article table seed completed!")

        except Exception as e:
            logging.error(f"Something has gone wrong inserting data for articles: {e}")
    
    # Insert_favorites__articles: inserts fake data for the favorites_articles table. 
    # Input favorites_articles iterator.
    #
    def insert_favorites_article(self, favorites_articles: Iterator[Dict[str, Any]]) -> None:
        try:
            with self.connection.cursor() as cursor:

                favorites_articles = ({**favorite_article} for favorite_article in favorites_articles)

                psycopg2.extras.execute_batch(cursor, """
                    INSERT INTO user_favorites_article VALUES (
                        %(userId)s,
                        %(articleId)s
                    );
                """, favorites_articles)

            logging.info("Favorites_article table seed completed!")

        except Exception as e:
            logging.error(f"Something has gone wrong inserting data for favorites_article: {e}")
    
    # _pgconnection: Creates an authenticated client for PG.
    #
    def _pgconnection(self):
        self.connection = psycopg2.connect(
            user=self.user,
            password=self.password,
            database=self.database,
            host=self.host
        )
    
        self.connection.autocommit = True