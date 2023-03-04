# import sqlite3 as sq

# conn = sq.connect("SRD.db")
# print("Database created and Connected")

# curr = conn.cursor()

# # curr.execute("CREATE TABLE COMPANY( ID INTEGER PRIMARY KEY,NAME TEXT NOT NULL,AGE INTEGER NOT NULL,ADDRESS CHAR(50),SALARY REAL)")


# # print("Table created")

# # curr.execute('INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES(005,"ajay",20,"hsnbd",30000.800)');
# # curr.execute('INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES(006,"sujay",21,"balurghat",20000.800)');
# # print("Data updated")
# # rng = int(input("How many entry you want: "))

# # for i in range(rng):
# #     id1 = int(input("Enter uniqe id name"))
# #     name1 = input("Enter Your Name: ")
# #     age1 = int(input("Enter Your age: "))
# #     add1 = input("Enter your Address:n ")
# #     sal1 = int(input("Enter your salary: "))
# #     curr.execute('INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES(?,?,?,?,?)',(id1,name1,age1,add1,sal1))

# # curr.execute('DELETE FROM COMPANY WHERE ID=3')
# # print("Deleted succesfully")
# # conn.commit()


# # curr.execute("UPDATE COMPANY set ADDRESS='INDIA' where ID=2");
# # conn.commit()

# # data = conn.execute('SELECT * FROM COMPANY');
# # for col in data:
# #     print("ID=",col[0],end="")
# #     print("NAME=",col[1],end="")
# #     print("AGE=",col[2],end="")
# #     print("ADDRESS=",col[3],end="")
# #     print("SALARY=",col[4],end="")





# conn.commit()
# conn.close()

def solve(a, b):
       return b if a == 0 else solve(b % a, a)
print(solve(20, 50))