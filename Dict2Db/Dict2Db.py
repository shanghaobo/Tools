import pymysql

class Dict2Db:
    """字典导入数据库"""
    def __init__(self,db_ip,db_user,db_password,db_name):
        self.conn = pymysql.connect(
            host=db_ip,
            user=db_user,
            password=db_password,
            database=db_name,
            port=3306,
            charset='utf8'
        )

    def row_dict2db(self,table_name,row_dict):
        """
        行字典插入数据库行
        :param table_name: 表名
        :param row_dict: 行字典 {key1:value1,key2:value2,...}
        :return: 
        """
        keys=list(row_dict.keys())
        values=list(row_dict.values())
        length=len(keys)
        keys_str=','.join(keys)
        temps=['%s' for i in range(length)]
        temps_str=','.join(temps)
        cursor=self.conn.cursor()
        sql="insert into %s(%s) value(%s)"%(table_name,keys_str,temps_str)
        print('sql=',sql%(tuple(values)))
        cursor.execute(sql,tuple(values))
        cursor.close()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()