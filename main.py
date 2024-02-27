import psycopg2
def select(par=''):
    printing = f"""Select * FROM public.table_1 {par};"""
    cursor.execute(printing)
    data = cursor.fetchall()
    print(data)

def update(changes, par=''):
    updating = f"""UPDATE public.table_1 SET {changes} {par};"""
    cursor.execute(updating)
    con.commit()
def delete(par):
    deleting = f"""DELETE FROM public.table_1 WHERE {par};"""
    cursor.execute(deleting)
    con.commit()

def insert(par):
    inserting = f"""INSERT INTO public.table_1(login, password) VALUES ({par});"""
    cursor.execute(inserting)
    con.commit()


if __name__=="__main__":
    con = psycopg2.connect(dbname='test', user='postgres', password='Q1w2e3r4', host='localhost')
    cursor = con.cursor()
    a = int(input())
    if a == 1:
        select()
    elif a==2:
        update()
    elif a==3:
        delete()
    elif a==4:
        insert()