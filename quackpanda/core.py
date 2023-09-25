import duckdb
import pandas as pd
import logging


class QuackPanda:
    """
    QuackPanda Class: Provides an interface to register Pandas DataFrames as tables and 
    execute SQL queries on them using DuckDB.
    
    :param db_path: The path to the DuckDB database, defaults to ":memory:" for in-memory database.
    :type db_path: str, optional
    :param read_only: The read_only attribute is not used in the current implementation.
    """
    def __init__(self, db_path=":memory:", read_only=False):
        """
        Initializes a new instance of QuackPanda, establishing a connection to DuckDB.
        """
        self.conn = duckdb.connect(db_path)
        self.tables = {}

    def register_temp_table(self, df: pd.DataFrame, table_name: str) -> str:
        """
        Registers a Pandas DataFrame as a temporary table in DuckDB.
        
        :param df: The Pandas DataFrame to be registered.
        :type df: pd.DataFrame
        :param table_name: The name under which the DataFrame will be registered.
        :type table_name: str
        :return: The name under which the DataFrame has been registered.
        :rtype: str
        :raises ValueError: Raises if df is not a Pandas DataFrame or table_name is not a string.
        """
        logging.debug(f"Dataframe content is {df.head()}")
        
        if not isinstance(df, pd.DataFrame):
            raise ValueError("df must be a Pandas DataFrame")
        if not isinstance(table_name, str):
            raise ValueError("table_name must be a string")
        
        try:
            self.conn.register(table_name, df)
            self.tables[table_name] = df
            return table_name
        except Exception as e:
            logging.error(f"Error registering DataFrame as table: {table_name}, Error: {str(e)}")
            raise

    def execute_query(self, query: str) -> pd.DataFrame:
        """
        Executes a SQL query on the registered DataFrames and returns the result as a Pandas DataFrame.
        
        :param query: The SQL query to be executed.
        :type query: str
        :return: The result of the SQL query as a Pandas DataFrame.
        :rtype: pd.DataFrame
        :raises Exception: Raises an exception if there is an error executing the query.
        """
        try:
            result = self.conn.execute(query)
            return result.fetchdf()
        except Exception as e:
            logging.error(f"Error executing query: {query}, Error: {str(e)}")
            raise

    def close(self):
        """
        Closes the connection to DuckDB.
        """
        self.conn.close()
