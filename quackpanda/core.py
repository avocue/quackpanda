import duckdb
import pandas as pd
import logging


class QuackPanda:
    def __init__(self, db_path=":memory:", read_only=False):
        self.conn = duckdb.connect(db_path)
        self.tables = {}

    def register_temp_table(self, df: pd.DataFrame, table_name: str) -> str:
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
            logging.error(
                f"Error registering DataFrame as table: {table_name}, Error: {str(e)}"
            )
            raise

    def execute_query(self, query: str) -> pd.DataFrame:
        try:
            result = self.conn.execute(query)
            return result.fetchdf()
        except Exception as e:
            logging.error(f"Error executing query: {query}, Error: {str(e)}")
            raise

    def close(self):
        self.conn.close()
