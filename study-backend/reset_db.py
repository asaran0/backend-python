from app.db.database import engine, Base
from app.db import models

# Drop all tables
Base.metadata.drop_all(bind=engine)
print("✅ Dropped all tables")

# Recreate tables
Base.metadata.create_all(bind=engine)
print("✅ Created all tables")