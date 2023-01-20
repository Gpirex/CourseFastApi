import databases
import sqlalchemy
from decouple import config

# DATABASE_URL = f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@localhost:5434/complaints"
DATABASE_URL = f"postgresql://postgres:postgres@localhost:5434/complaint"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
