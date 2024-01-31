def create_table(db, table, schema):
    conn = db()
    cur = conn.cursor()

    keys = schema.keys()
    
    desc = ''
    for i in range(len(keys)):
        desc += '{} {}, '.format(list(keys)[i], schema[list(keys)[i]])
    desc = desc[:-2]

    sql = '''
        CREATE TABLE {} ({});
    '''.format(table, desc)

    print('LOG: EXECUTING \n {}'.format(sql))

    cur.execute(sql)

    cur.close()
    conn.close()

def rename_table(db, table, new_name):
    conn = db()
    cur = conn.cursor()

    sql = '''
        ALTER TABLE {}
        RENAME TO {};
    '''.format(table, new_name)

    print('LOG: EXECUTING \n {}'.format(sql))

    cur.execute(sql)

    cur.close()
    conn.close()

def drop_table(db, table):
    conn = db()
    cur = conn.cursor()

    sql = '''
        DROP TABLE {};
    '''.format(table)

    print('LOG: EXECUTING \n {}'.format(sql))

    cur.execute(sql)

    cur.close()
    conn.close()


OPERATIONS = {
    'CREATE_TABLE': create_table,
    'DROP_TABLE': drop_table
}