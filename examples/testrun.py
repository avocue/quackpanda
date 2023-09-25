import pandas as pd
from quackpanda.core import QuackPanda

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)

# Initialize QuackPanda
qp = QuackPanda()

# Register DataFrame as a temporary table
qp.register_temp_table(df, 'people')

# Execute SQL query
result_df = qp.execute_query('SELECT * FROM people WHERE Age > 25')

# Display the result
print(result_df)