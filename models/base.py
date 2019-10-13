import sqlite3

from datetime import date

from errors import ValidationError

class SQLiteModel:
    _DATABASE = None
    _TABLE = None
    _MAPPING = {}
    __TYPE_MAPPING = {
        int : 'int',
        str : 'varchar(2000)',
        date : 'varchar(30)'
    }

    @classmethod
    def _connect(cls):
        return sqlite3.connect(cls._DATABASE)


    @classmethod
    def get_by_pk(cls, pk):
        conn = cls._connect()
        cur = conn.cursor()

        cur.execute(
            """
                SELECT *
                FROM :table
                WHERE id = :pk
            """,
            {'table': cls._TABLE, 'pk': pk}
        )

        result = {}
        record = cur.fetchone()
        for idx, col in enumerate(cur.description):
            result[col] = record[idx]
        conn.close()
        return result

    
    @classmethod
    def create_mapping(cls):
        conn = cls._connect()
        cur = conn.cursor()
        mapfortable = [str(k) + " " + str(cls.__TYPE_MAPPING.get(v)) for k, v in cls._MAPPING.items()]
        
        cur.execute("""CREATE TABLE IF NOT EXISTS ? (""" + ("?," * len(mapfortable))[:-1]  + """)""", (cls._TABLE,) + mapfortable)

        conn.commit()
        conn.close()

    @classmethod
    def update_mapping(cls):
        """Сделать обновления полей таблицы"""
        pass

    @classmethod
    def insert(cls):
        """Сделать вставку"""
        pass
        


class BaseModel(SQLiteModel):
    _DATABASE = 'def.db'

    def __getattr__(self, attr):
        if attr in self._MAPPING.keys():
            return None
        raise AttributeError()

    def __setattr__(self, attr, val):
        if attr in self._MAPPING.keys():
            if self._validate(attr, val):
                self.__dict__[attr] = val
                return
        raise AttributeError()


    def fill(self, data):
        for key, val in data.items():
            if self._validate(key, val):
                self.__dict__[key] = val
    

    def _validate(self, key, val):
        key_type = self._MAPPING.get(key)

        if not key_type:
            raise ValidationError

        if key_type != type(val):
            raise ValidationError

        return True

    @classmethod
    def get_by_pk(cls, pk):
        record = cls.get_by_pk(pk)
        obj = cls()
        obj.fill_data(record)
        return obj
    

    def get_data(self):
        data = {}

        for key in self._MAPPING:
            data[key] = getattr(self, key)

        return data

class UserModel(BaseModel):
    _TABLE='Users'
    _MAPPING={
        'realname' : str,
        'username' : str,
        'password' : str,
        'email' : str,
        'birthday' : date,
        'registration_date' : date,
        'info' : str,
        'phone_number' : str,
        'city' : str
    }

"""Дописать остальные модели"""
