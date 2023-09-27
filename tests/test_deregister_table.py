import pytest
from quackpanda.core import QuackPanda
import pandas as pd


def test_deregister_table():
    qp = QuackPanda()

    # Create a dummy DataFrame
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

    # Register the table
    table_name = "dummy_table"
    qp.register_temp_table(df, table_name)
    
    # Deregister the table
    qp.deregister_temp_table(table_name)
    
    # Ensure the table is removed from the self.tables dictionary
    assert table_name not in qp.tables
    
    # Query DuckDB's information schema to check if the table still exists in DuckDB
    result_df = qp.execute_query(f"SELECT * FROM information_schema.tables WHERE table_name = '{table_name}'")
    assert result_df.empty  # The result should be an empty DataFrame if the table does not exist.
    
    qp.close()
