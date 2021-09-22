import os

from lib.seeder import PopulateData
from lib.generate_data import GenerateRandomData

def main():
    db_user = os.environ.get("DB_USER", "postgres")
    db_password = os.environ.get("DB_PASSWORD", "password")
    db_database = os.environ.get("DB_DATABASE", "nestjsrealworld")
    db_host =  os.environ.get("DB_HOST", "localhost")

    seed_counter = int(os.environ.get("SEED_COUNTER", 1000))

    datagen = GenerateRandomData(count=seed_counter)

    seeder = PopulateData(user=db_user, password=db_password, database=db_database, host=db_host)

    seeder.insert_users(datagen.user_data())
    seeder.insert_articles(datagen.article_data())
    seeder.insert_favorites_article(datagen.favorite_articles_data())
    seeder.insert_comments(datagen.comment_data())
    seeder.insert_tags(datagen.tag_data())
    seeder.insert_follows(datagen.follow_data())



if __name__ == "__main__":
    main()

