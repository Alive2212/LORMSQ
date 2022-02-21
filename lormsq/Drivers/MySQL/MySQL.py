import re
import sys

import mysql.connector

from ...DatabaseSQLAbstract import DatabaseSQLAbstract
from ...Drivers.MySQL.Model import Model
from .Options import Options
from ...Model.SQLModelColumnAbstract import SQLModelColumnAbstract
from ...Model.SQLModelColumnTypeAbstract import SQLModelColumnTypeAbstract


class MySQL(DatabaseSQLAbstract):

    def __init__(
            self,
            options: Options
    ) -> None:
        self.__options = options
        super().__init__()

    def init_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.__options.host,
                user=self.__options.user,
                passwd=self.__options.password,
                db=self.__options.database,
                ssl_disabled=True,
            )
        except mysql.connector.Error as e:
            print("""Error: {} {}""".format(e.args[0], e.args[1]))
            sys.exit(1)

    def init_cursor(self):
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()

    def get_skeleton(self):
        self.cursor.execute("SHOW TABLES")
        db_response_tables = self.cursor.fetchall()

        models = []
        for (table_name,) in db_response_tables:
            model = Model(
                table_name=table_name
            )
            self.cursor.execute("""DESCRIBE {};""".format(table_name))
            table_columns = self.cursor.fetchall()
            for table_id, table_column_object in enumerate(table_columns):
                (
                    table_column_title,
                    table_column_type,
                    nullable_str,
                    primary_str,
                    default_value,
                    extra_value
                ) = table_column_object
                table_column_type_params = re.search(
                    """([a-zA-Z0-9]+)(\()?([0-9,]+)?([\) ]+)?([a-zA-Z0-9]+)?""",
                    table_column_type
                )
                (
                    table_column_type_title,
                    tmp1,
                    table_column_type_len_value,
                    tmp2,
                    table_column_type_attributes,
                ) = table_column_type_params.groups()
                if "," in str(table_column_type_len_value):
                    table_column_type_len_value = eval("""({})""".format(table_column_type_len_value))
                model.columns.append(SQLModelColumnAbstract(
                    table_id=table_id,
                    title=table_column_title,
                    data_type=SQLModelColumnTypeAbstract(
                        title=table_column_type_title,
                        len_values=table_column_type_len_value,
                        attributes=table_column_type_attributes
                    ),
                    primary=False,
                ))
            models.append(model)
