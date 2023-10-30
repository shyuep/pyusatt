# USATT

Python tools for working with the USATT website

# Simple CLI examples

To get the USATT ratings for a few USATT ids, using the top ranked USATT ids as an example:

```shell
usatt ratings -i 1165420 220283
```

gives

|   USATT# | Name      |   Tournament Rating |   Highest Tournament Rating |   Tournaments Played |   League Rating |   Highest League Rating |   Leagues Played |
|---------:|:----------|--------------------:|----------------------------:|---------------------:|----------------:|------------------------:|-----------------:|
|  1165420 | Lei Kou   |                2826 |                        2864 |                   32 |            2816 |                    2843 |                3 |
|   220283 | Jinbao Ma |                2760 |                        2809 |                   32 |            2723 |                    2723 |                5 |

To get a summary of all USATT ratings,

```shell
usatt summary --outfile usatt.csv
```

This  will dump all USATT ratings to a CSV file.
