# QuackPanda: SQL Capability for Pandas using DuckDB 🦆🐼
quackpanda is a Python library designed to bring Spark-like SQL capabilities to Pandas DataFrames using DuckDB, allowing users to execute SQL queries and perform advanced database operations directly on DataFrames.

## Features
Seamless integration with DuckDB for executing SQL queries on Pandas DataFrames.
Efficient registration of DataFrames as temporary tables.
Supports a variety of SQL functionalities, offering flexibility in DataFrame manipulation.
Installation
To install quackpanda, use pip:
```
pip install quackpanda
```
Quick Start
Here's a basic example of how to use quackpanda to register a DataFrame as a table and execute a SQL query:

```python
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
```
## Documentation
For detailed information on quackpanda's features and usage, please refer to the official documentation (add the link to your documentation).

## Contributing
We welcome contributions to quackpanda! Please see our Contributing Guide for more details.

## Support & Feedback
For support, questions, or feedback, please submit an issue on GitHub.

## License
quackpanda is licensed under the MIT License.

## Acknowledgments
Special thanks to the creators and contributors of Pandas and DuckDB for their incredible work, which made quackpanda possible.

Make sure to adapt the file paths, URLs, and other specific information to match your project's actual details. Also, consistently update the README as your project evolves, adding new sections or modifying existing ones as needed.