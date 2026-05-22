import psycopg2

class DBClient:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            database="crm_db",
            user="postgres",
            password="password"
        )

    def get_customer_by_id(self, customer_id):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT id, name, tenant_id FROM customers WHERE id = %s",
            (customer_id,)
        )
        result = cursor.fetchone()
        cursor.close()
        return result