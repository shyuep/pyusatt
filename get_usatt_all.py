"""Script to download a summary of all USATT registered players into a usatt.csv file."""

from __future__ import annotations

import warnings

from pyusatt.data import get_usatt_summary

warnings.simplefilter("ignore")


all_data = get_usatt_summary()

all_data.to_csv("usatt.csv")
