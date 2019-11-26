# Breaking Bad Deaths Crowler

[List of deaths on Breaking Bad](https://breakingbad.fandom.com/wiki/List_of_deaths_on_Breaking_Bad) contains all the deaths of the famous series Breaking Bad for all the seasons. Cooking meth is not an easy task, thus some blood has to be spilled.

## Running the script

Using [Beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), I crawled the page and extracted all the information. In order to run the script use:

```python crowl_breaking_bad.py <path>```

Find below the description of the arg parsers:
```
usage: crowl_breaking_bad.py [-h] path

Add the path where you want to save the data. Path example:
C:\<name>\<directory>\outcome.csv

positional arguments:
  path        dont forget to add filename in the end (output.csv)

optional arguments:
  -h, --help  show this help message and exit
  ```

Don't forget to add the filename in the end, or the program will be terminated.

## Prerequisites

* ```pip install pandas```
* ```pip install beautifulsoup4```
* ```pip install numpy```
* ```pip install requests```
* ```pip install os```
* ```pip install argparse```