# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import psycopg2

db_params = {
    "host": "database",
    "database": "sreality",
    "user": "adam",
    "password": "123456",
}

class SrealityPipeline:
    def __init__(self, db_params):
        self.db_params = db_params

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        db_params = {
            "host": settings.get("POSTGRES_HOST", "localhost"),
            "port": settings.get("POSTGRES_PORT", 5432),
            "database": settings.get("POSTGRES_DB"),
            "user": settings.get("POSTGRES_USER"),
            "password": settings.get("POSTGRES_PASSWORD"),
        }
        return cls(db_params)
    
    def open_spider(self,spider):
        self.connection = psycopg2.connect(**self.db_params)
        self.cursor = self.connection.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS flats(id serial PRIMARY KEY, title text, image_url text);")
        # self.connection.commit()
        self.cursor.execute("DELETE FROM Flats;")
        self.connection.commit()

    def process_item(self, item, spider):

        insert_query = "INSERT INTO flats (title, image_url) VALUES (%s, %s)"
        data = (item['name'],item['img_url'])  
        try:
            self.cursor.execute(insert_query, data)
            self.connection.commit()
        except psycopg2.Error as e:
            self.connection.rollback()
            spider.logger.error(f"Error inserting data: {e}")
        return item
    
    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

    
    
    # def process_item(self, item, spider):
    #     with open('pipeline.json', "w") as json_file:
    #         json.dump(dict(item), json_file, indent=4)
    #     return item
