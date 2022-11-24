import psycopg2


conn = psycopg2.connect(
   host="localhost",
   database="dictionary",
   user="postgres",
   password="continuousimpliesintegrable"
)

def read_dict(C):
    """reads the dictionary from the database"""
    cur = C.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_word(C, word, translation):
    """adds a word and its translation to the dictionary"""
    cur = C.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
def delete_word(C, ID):
    """deletes an entry from the dictionary"""
    cur = C.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
def save_dict(C):
    """commits all changes to the database"""
    cur = C.cursor()
    cur.execute("COMMIT;")
    cur.close()

print("Available commandes are list, add, delete and quit")
while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")
    if cmd == "list":
        print(read_dict(conn))
    elif cmd == "add":
        name = input("  Word: ")
        phone = input("  Translation: ")
        add_word(conn, name, phone)
        print(f'Added word {name}')
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
        print(f'Deleted word {name}')
    elif cmd == "quit":
        save_dict(conn)
        print('Goodbye!')
        exit()
