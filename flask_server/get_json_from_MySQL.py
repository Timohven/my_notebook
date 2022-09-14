import pandas as pd
from sqlalchemy import create_engine

def get_all():
    # MySQL DB connection string
    connection_string = 'mysql://root:ErhCthdbC_2006@localhost:3306/mynotebookdb'

    # create SQL Alchemy connection object
    engine = create_engine(connection_string)

    # read rows from DB into Pandas DataFrame
    sql_query = 'select * from notes'
    df = pd.read_sql(sql_query, engine)
    #print(df)

    # export/write DataFrame to JSON file
    df.to_json(r'C:\Users\ukrse\PROJECTS\my_notebook\flask_server\templates\notes.json', orient='table', force_ascii=False)

def update_note(new_note):
    # MySQL DB connection string
    connection_string = 'mysql://root:ErhCthdbC_2006@localhost:3306/mynotebookdb'
    # create SQL Alchemy connection object
    engine = create_engine(connection_string)
    # read rows from DB into Pandas DataFrame
    sql_query = "update notes set content='{}' where note_id={}".format(new_note.get('content'), new_note.get('note_id'))
    print(sql_query)
    conn = engine.connect()
    conn.execute(sql_query)

def add_note(new_note):
    # MySQL DB connection string
    connection_string = 'mysql://root:ErhCthdbC_2006@localhost:3306/mynotebookdb'
    # create SQL Alchemy connection object
    engine = create_engine(connection_string)
    # read rows from DB into Pandas DataFrame
    sql_query = "insert into notes (title, category, content, creation_date) values ('{}', {}, '{}', now())".format(new_note.get('title'),
                                                                              new_note.get('category'),
                                                                              new_note.get('content'))
                                                                              # new_note.get('creation_date'),
                                                                              # new_note.get('last_edit_date'))
    print(sql_query)
    conn = engine.connect()
    conn.execute(sql_query)