from database import Database
from config import resolve_db_config

if __name__ == "__main__":
    config_filename = 'database.ini'
    db_config_section = 'postgresql'

    db_config = resolve_db_config(config_filename, db_config_section)
    db = Database(db_config)
    result = db.get_data()
    print(result)
