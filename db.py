import sqlite3

con = sqlite3.connect("teleg_database.db")
cur = con.cursor()
lst=[]

def delete_inf(id_chat):
    cur.execute(f"DELETE FROM users WHERE id_chat={id_chat}")
    cur.execute(f"DELETE FROM users_mess WHERE id_chat={id_chat}")
    con.commit()

def send_may(id_chat):
    result=cur.execute(f"SELECT message from users_mess WHERE id_chat={id_chat}")  
    return "".join(result.fetchall()[0])+" мяу"  

def date_base(id_chat,surname,message):
    if id_chat not in lst:

        name="пукич"
        message=str(message)
        lst.append(id_chat)
        cur.execute(f"INSERT INTO users (id_chat,surname,name) VALUES({id_chat},\"{surname}\",\"{name}\")")
        cur.execute(f"INSERT INTO users_mess (id_chat,message) VALUES({id_chat},\"{message}\")")
    else:    
        cur.execute(f"UPDATE users_mess SET message=\"{message}\" WHERE users_mess.id_chat={id_chat}")
    
    
    
    con.commit()
    return send_may(id_chat)