from sniffers.bwin_sniffer import start_extraction_from_bwin
from persistence.MongoDBConfig import MongoDBConfig

if __name__ == '__main__':
    # Open connection with MongoDB
    mongodb = MongoDBConfig()
    mongodb.get_instance().open_connection()

    # Start odds extraction
    bwin_data = start_extraction_from_bwin()

    # Get database
    db = mongodb.get_instance().get_database()

    # Save BWIN data
    bwin_collection = db['bwin_collection']
    bwin_collection.replace_one(bwin_data, bwin_data, upsert=True)
