import pandas as pd
import pytest
from quackpanda.core import QuackPanda

# Initialize the QuackPanda instance
@pytest.fixture
def qp():
    return QuackPanda()


# Initialize a sample DataFrame
@pytest.fixture
def generate_sample_df():
    return pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})


def test_register_temp_table(qp, generate_sample_df):
    sample_df = generate_sample_df  # get the DataFrame returned by the fixture
    print(f"The dataframe is {sample_df.head()}")
    # Register a DataFrame as a temporary table
    table_name = qp.register_temp_table(table_name="my_table", df=sample_df)

    # Assert the table_name is correct
    assert table_name == "my_table"

    # Assert the table is correctly registered
    assert "my_table" in qp.tables
    assert qp.tables["my_table"].equals(sample_df)


def test_execute_query(qp, sample_df):
    table_name = "sample_table"
    qp.register_temp_table(df=sample_df, table_name=table_name)

    # Perform a query and get the result
    result_df = qp.execute_query(f"SELECT * FROM {table_name} WHERE a > 1")

    # Expected result
    expected_df = pd.DataFrame({"a": [2, 3], "b": [5, 6]})

    # Assert the result DataFrame is correct
    pd.testing.assert_frame_equal(result_df, expected_df)


def test_close(qp):
    # Closing the connection should not raise an exception
    try:
        qp.close()
    except Exception as e:
        pytest.fail(f"Closing connection raised an exception: {e}")
