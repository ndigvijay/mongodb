import pymongo


def display():
    docs=collection.find()
    for i in docs:
        print(i)
def insert_one():
    # user={}
    # key=input("enter a key")
    # value=input("enter a value")
    # user[key]=value
    email_entered=input("enter your email")
    password_entered=input("enter your password")
    user=dict(email=email_entered,pasword=password_entered)
    collection.insert_one(user)
    print("email and password inserted")
    # print(user)
def insert_many():
    n=int(input(""))




if __name__=="__main__":
    client=pymongo.MongoClient("mongodb://127.0.0.1:27017")
    print("mongodb connected")
    # databases=client.list_database_names()
    # print(databases)
    # input_database=input("please enter your database ")
    database=client["netflix"]
    collections=database.list_collection_names()
    # print(collections)
    # input_collection=input("please enter your collection ")
    collection=database["users1"]
    while(1):    
        print("1.display all documents \n 2.insert one document \n 3.insert many document \n 5.exit")
        choice=int(input("please enter your choice "))
        if choice==1:
            display()
        elif choice==2:
            insert_one()
        elif choice==3:
            insert_many()
        elif choice==5:
            break