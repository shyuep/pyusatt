"""Script to download a summary of all USATT registered players into a usatt.csv file."""

from __future__ import annotations

import sys
import warnings

from pyusatt.data import get_usatt_summary

warnings.simplefilter("ignore")

query = None if len(sys.argv) == 1 else sys.argv[1]

all_data = get_usatt_summary(query=query)

print(all_data.to_markdown())

all_data.to_csv("usatt.csv")
