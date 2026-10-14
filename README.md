# Python Mini Projects

Small command-line projects that combine several Python concepts.
Built while studying, as part of my transition into data engineering.

## Projects

| File | Description | Libraries |
|------|-------------|-----------|
| `project_contact_book.py` | Contact book with a menu, accent-insensitive name search and multiple phones/emails per contact | `unicodedata` |
| `project_inventory_management.py` | Inventory control with product registration, input validation and total stock count | `math` |
| `project_shopping_cart.py` | Shopping cart simulation with product search and tiered discounts (10% above R$ 200, 20% above R$ 500) | `unicodedata` |
| `project_student_data_analysis.py` | Student grade analysis with list comprehensions: classification, class average, highest and lowest grades | none |
| `project_finhealth_dataset.py` | Synthetic dataset of 500 Brazilian clients' finances generated with Faker and random distributions, exported to CSV | `faker`, `pandas`, `random` |

## Concepts practiced

Loops, conditionals, lists and dictionaries, functions, input validation,
string normalization, list comprehensions, f-strings and synthetic data
generation with Faker and pandas.

## Requirements

- Python 3 (tested with Python 3.14.3)
- External libraries (only needed for `project_finhealth_dataset.py`):

```bash
pip install faker pandas
```

`unicodedata`, `math` and `random` are part of the Python standard library
and need no installation.

## How to run

From the root of the repository:

```bash
python3 project_contact_book.py
```

The dataset project generates a CSV file (`finhealth_data.csv`) in the same
folder. It uses `;` as separator and `,` as decimal mark, so read it with:

```python
import pandas as pd

df = pd.read_csv("finhealth_data.csv", sep=";", decimal=",")
```

## Notes

- All data used in these projects (contacts, products, students, clients) is
  fictional or generated with Faker. No real personal data is included.
- The contact book and inventory projects keep their data in memory only, so
  changes are lost when the program exits.