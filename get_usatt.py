"""Script to get the USATT ratings based on USATT#s."""
from __future__ import annotations

import sys
import warnings

import pandas as pd

from pyusatt.data import get_ratings

warnings.simplefilter("ignore")


data = []

for usattid in sys.argv[1:]:
    data.append(get_ratings(usattid))

df = pd.DataFrame(data)
df = df.set_index("USATT#")
print(df.to_markdown())
