import sqlite3
import os

usersdb = None
is_closed = False
status = None
msg = None

def connect_database():
    global usersdb
    if usersdb is None:
        curpath = os.path.abspath(os.path.curdir)
        usersdb = sqlite3.connect(curpath + "\usersdb.db")

def commit_and_close():
    global usersdb
    global is_closed
    usersdb.commit()
    usersdb.close()
    is_closed = True
    usersdb = None

def add_user(user):
    create_table_if_not_exists()

    if user_exists(user) == True:
        status = 0
        msg ="User already exists!"
        print msg
    else:
        stmt = "INSERT INTO users VALUES(?,?,?)"
        usersdb.execute(stmt,(user.username,user.password,user.nickname))
        #On adding successfully
        status = 1
        msg = "User added successfully!"
        print msg

    commit_and_close()
    return status,msg

def user_exists(user):
    global usersdb
    query = "SELECT count(*) FROM users WHERE username='"+user.username+"';"
    print query
    cursor = usersdb.execute(str(query))
    num_records=cursor.next()[0]
    if num_records > 0:
        return True
    else:
        print "Doesn't Exist"
        return False

def create_table_if_not_exists():
    # Create or open db
    global usersdb
    connect_database()
    print "Database opened successfully!"

    # Create table if not exists
    usersdb.execute(
        "CREATE TABLE IF NOT EXISTS users (username varchar(15) PRIMARY KEY NOT NULL, password varchar(30),nickname varchar(20));")
    print "Table accessed successfully!"


def get_all_users():
    create_table_if_not_exists()
    users_list = []
    global usersdb
    print "In get users"
    connect_database()
    from users.User import User
    cursor = usersdb.execute("SELECT * FROM users;")

    for user in cursor:
        username = user[0]
        password = user[1]
        nickname = user[2]
        newuser = User(username,password,nickname)
        users_list.append(newuser)

    commit_and_close()
    if len(users_list) == 0:
        return None
    return users_list

def delete_user(user):
    global usersdb
    connect_database()
    if not user_exists(user):
        status = 0
        msg = "User doesn't exist in the database!"
        print msg
    else:
        usersdb.execute("DELETE FROM users WHERE username='"+user.username+"'")
        usersdb.commit()
        status = 1
        msg = "User deleted successfully!"
        print msg

    commit_and_close()
    return status,msg

def get_user(username):
    from users import User
    connect_database()
    query = "SELECT * FROM users WHERE username='"+username+"';"
    cursor = usersdb.execute(str(query))
    user = cursor.next()
    return User.User(username=user[0],password=user[1],nickname=user[2])

def update_user(user):
    global usersdb
    connect_database()
    print user.info()
    print user.nickname
    query = "UPDATE users SET username=?,password=?,nickname=? WHERE username=? "
    print query
    usersdb.execute(query,(user.username,user.password,user.nickname,user.username))
    print "User info updated successfully"
    commit_and_close()


if __name__ == '__main__':
    from users.User import User
    user = User("Shivam","shivam@A","Shivam Wifi")
    add_user(user)
    print get_all_users()
    delete_user(user)
    print get_all_users()