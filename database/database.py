import psycopg2

class Database:
    def __init__(self, db_config):
        self.host = db_config["host"]
        self.port = db_config["port"]
        self.user = db_config["user"]
        self.dbname = db_config["dbname"]

    def get_data(self):
        print("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(host=self.host,
                                port=self.port,
                                user=self.user,
                                dbname=self.dbname)

        data = None
        with conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM address;")    
                data = cur.fetchall()

        if conn is not None:
            conn.close()
            print("Database connection closed.")
        
        return data