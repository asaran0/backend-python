from app.db.database import SessionLocal, engine, Base
from app.db.models import Category, Question, User
from app.utils.jwt_handler import hash_password

# Create tables if not exist
Base.metadata.create_all(bind=engine)

# Get DB session
db = SessionLocal()

# Clear existing data (optional)
db.query(Question).delete()
db.query(Category).delete()
db.query(User).delete()

# Add categories
categories_data = [
    {"name": "Python"},
    {"name": "Java"},
    {"name": "Data Structures"},
    {"name": "Operating Systems"},
    {"name": "Computer Networks"},
]

categories = []
for cat_data in categories_data:
    cat = Category(**cat_data)
    db.add(cat)
    db.flush()
    categories.append(cat)

db.commit()

# Add questions
questions_data = [
    {
        "category_id": categories[0].id,  # Python
        "question": "What is a list in Python?",
        "answer": "A list is a mutable, ordered collection of items in Python."
    },
    {
        "category_id": categories[0].id,  # Python
        "question": "What is the difference between list and tuple?",
        "answer": "Lists are mutable (can be changed) while tuples are immutable (cannot be changed)."
    },
    {
        "category_id": categories[1].id,  # Java
        "question": "What is JVM?",
        "answer": "JVM (Java Virtual Machine) is an abstract computing machine that enables a computer to run Java programs."
    },
    {
        "category_id": categories[1].id,  # Java
        "question": "What is the difference between JDK and JRE?",
        "answer": "JDK is Java Development Kit (includes compiler and tools), JRE is Java Runtime Environment (only runtime)."
    },
    {
        "category_id": categories[2].id,  # Data Structures
        "question": "What is a binary tree?",
        "answer": "A binary tree is a tree data structure where each node has at most two children (left and right)."
    },
    {
        "category_id": categories[2].id,  # Data Structures
        "question": "What is the time complexity of binary search?",
        "answer": "The time complexity of binary search is O(log n)."
    },
    {
        "category_id": categories[3].id,  # Operating Systems
        "question": "What is a process?",
        "answer": "A process is an instance of a program that is being executed by the operating system."
    },
    {
        "category_id": categories[4].id,  # Computer Networks
        "question": "What is TCP/IP?",
        "answer": "TCP/IP is a suite of protocols used for communication over the internet (Transmission Control Protocol / Internet Protocol)."
    },
]

for q_data in questions_data:
    q = Question(**q_data)
    db.add(q)

db.commit()

print("✅ Database seeded successfully!")
print(f"✅ Added {len(categories)} categories")
print(f"✅ Added {len(questions_data)} questions")

# Adding User Data
test_user = User(
    username="amar1",
    email="amargpt17@gmail.com",
    fullname="Amar Deep Gupta",
    mobile_no="",
    hashed_pwd=hash_password("pass"),
)
db.add(test_user)

test_user2 = User(
    username="amar2",
    email="ved@gmail.com",
    fullname="Ved",
    mobile_no="",
    hashed_pwd=hash_password("pass"),
)
db.add(test_user2)

db.commit()
print("✅ Added 2 users")
print(f"✅ Total users in DB: {db.query(User).count()}")

db.close()