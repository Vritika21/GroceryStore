from sql_connection import get_sql_connection

def get_all_products(connection):
    
    cursor = connection.cursor()
    query = ("SELECT PRODUCT.PRODUCT_ID, PRODUCT.NAME, PRODUCT.UM_ID, PRODUCT.PRICE_PER_UNIT, UM.UM_NAME "
             "FROM PRODUCT inner join UM on PRODUCT.UM_ID=UM.UM_ID")

    cursor.execute(query)

    response = []

    for (PRODUCT_ID, NAME, UM_ID, PRICE_PER_UNIT, UM_NAME) in cursor:
        response.append(
        {    
         'PRODUCT_ID' : PRODUCT_ID,
         'NAME' : NAME, 
         'UM_ID' : UM_ID,
         'PRICE_PER_UNIT' : PRICE_PER_UNIT,
         'UM_NAME' : UM_NAME
        }
    )
    return response

def insert_new_product(connection, PRODUCT):
    cursor = connection.cursor()
    query = ("insert into PRODUCT"
             "(NAME, UM_ID, PRICE_PER_UNIT)"
             "VALUE(%s, %s, %s)")
    data = (PRODUCT['NAME'], PRODUCT['UM_ID'], PRODUCT['PRICE_PER_UNIT'])

    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid

def delete_PRODUCT(connection,PRODUCT_ID):
    cursor = connection.cursor()
    query = ("DELETE FROM PRODUCTS where PRODUCT_ID=" + str(PRODUCT_ID))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__=='main':
    connection = get_sql_connection()
    print(get_all_products(connection))
    # print(get_all_products(connection))
    print(insert_new_product(connection,
     {
        #'NAME': 'potatoes',
        #'UM_ID': '1',
        #'PRICE_PER_UNIT': '10',
     }
    ))
    