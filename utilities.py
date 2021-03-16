import psycopg2
import bcrypt
from settings import *
from flask import make_response
# postgres functions 
def postgres_connetion(host,db_name,db_user,db_password):
    con = psycopg2.connect(" host={} dbname={} user={} password={}".format(host,db_name,db_user,db_password))
    
    print("You are connected ")
    return con

def post_resource(output,table_name,cur):
    columns = ""
    column=output.keys()    
    for i in range(len(column)):
        columns += "%s," 
    values=tuple(output.values())
    sql = f""" insert into {table_name}  values ({columns[:-1]})"""
    cur.execute(sql,values)

def post_resource_1(output,table_name,cur):
    column=output.keys()
    columns= '(%s)' % ', '.join(map(str, column))
    values=tuple(output.values())
    sql =f""" insert into {table_name} {columns} values {values}"""
    cur.execute(sql)


def get_resources_by_filter(table_name,filter_criteria,filter_criteria_value,cur):
    sql=(
        f"""select * from {table_name} where {filter_criteria}='{filter_criteria_value}'""")
    cur.execute(sql)
    record=cur.fetchall()
    return record


def check_existence(table_name,filter_criteria,filter_criteria_value,cur):
    sql = f"select exists(select 1 from {table_name} where {filter_criteria}= '{filter_criteria_value}')"
    print(sql)
    output = cur.execute(sql)
    return output

def get_resource(column_name,table_name,filter_criteria,filter_criteria_value,cur):
    sql=(
        f"""select {column_name} from {table_name} where {filter_criteria}='{filter_criteria_value}'""")
    cur.execute(sql)
    record=cur.fetchone()
    return record

def current_user(id):
    con=postgres_connetion(
        host,
        db_name,
        db_user,
        db_password)
    cur=con.cursor()
    psql=(
    f"""select user_id from users where user_id='{id}'""")
    cur.execute(psql)
    record=cur.fetchone()
    return record

def hash_string(password,pepper):
    password_peppred=(str(password)+pepper).encode("utf-8")
    hashed = bcrypt.hashpw(password_peppred, bcrypt.gensalt())
    return hashed

def check_password(password,hashed,pepper):
    if bcrypt.checkpw(str(password+pepper).encode("utf-8"), hashed.tobytes()):
        return True
    else:
        return False





    