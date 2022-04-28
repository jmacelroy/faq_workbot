from matplotlib.pyplot import getp
import pymongo, requests, urllib, getpass
import random


def db_connection():
    # password = getpass.getpass("Enter the password: ")    
    # client = pymongo.MongoClient("mongodb://workbotadmin:"+urllib.parse.quote_plus("workbotpass@22_")+"@0.0.0.0:27017")
    client = pymongo.MongoClient("mongodb://workbotadmin:workbotpass%4022_@mongodb_server:27017/?connectTimeoutMS=10000&authSource=admin")
    return client


# def add_document(email):
#     # client = db_connection()
#     client = pymongo.MongoClient("mongodb://workforce_bot_admin:"+urllib.parse.quote_plus("workbotpass@2022_")+"@127.0.0.1:27017")
#     db = client['employee_db']
#     collection = db['employee_emails']
#     dict = {
#         'employee_email': email,
#     }
#     try:
#         collection.insert_one(dict)
#         return True
#     except:
#         return False


# def show_documents():
#     client = pymongo.MongoClient("mongodb://workforce_bot_admin:"+urllib.parse.quote_plus("workbotpass@2022_")+"@127.0.0.1:27017")
#     db = client['employee_db']
#     collection = db['employee_emails']
#     result = collection.find()
#     try:
#         # for document in collection.find():
#         #     result += document["employee_email"] + "\n"
#         return result
#     except:
#         return False


def show_brain_teaser():
    client = pymongo.MongoClient("mongodb://workbotadmin:workbotpass%4022_@mongodb_server:27017/?connectTimeoutMS=10000&authSource=admin")
    # client = pymongo.MongoClient("mongodb://workbotadmin:"+urllib.parse.quote_plus("workbotpass@22_")+"@0.0.0.0:27017")
    db = client['brain_teasers']
    collection = db['questions']
    RandomNumber = random.randint(0, collection.count_documents({})-1)

    result = collection.find({},{'_id':0}).limit(-1).skip(RandomNumber).next()
    try:
        q_id = result['q_id']
        question = result['question']
        options = list(result['options'].keys())
        return {"q_id": q_id , "question": question, "options": options}
    except:
        return False


def brain_teaser_answer_check(q_id, answer):
    client = pymongo.MongoClient("mongodb://workbotadmin:workbotpass%4022_@mongodb_server:27017/?connectTimeoutMS=10000&authSource=admin")
    # client = pymongo.MongoClient("mongodb://workbotadmin:"+urllib.parse.quote_plus("workbotpass@22_")+"@0.0.0.0:27017")
    db = client['brain_teasers']
    collection = db['questions']
    result = collection.find_one({'q_id': q_id}, {'_id':0})
    print(result)
    try:
        if result['options'][answer]:
            return True
        else:
            return False
    except:
        return False


def show_project_list(project_name):
    client = pymongo.MongoClient("mongodb://workbotadmin:workbotpass%4022_@mongodb_server:27017/?connectTimeoutMS=10000&authSource=admin")
    # client = pymongo.MongoClient("mongodb://workbotadmin:"+urllib.parse.quote_plus("workbotpass@22_")+"@0.0.0.0:27017")
    db = client['projects']
    collection = db['project_lists']
    result = collection.find_one({'project_name': project_name}, {'_id':0})
    if result:
        return result
    else:
        return False


# if __name__ == '__main__':
#     # client = db_connection()
#     # print(client.list_database_names())
#     # result = show_brain_teaser()
#     # result = brain_teaser_answer_check('001', 'Delhi')

#     result = show_project_list(project_name="project arc")


#     print(result)
