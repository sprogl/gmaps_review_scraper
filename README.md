# Google maps review scraper(gmaps_review_scraper)
This script manipulates the internal google maps API to scrape the reviews of places/businesses.
# revscr:
usage: usage: revscr [-h] [-l LUDOCID] [-s SEARCH] [-o OUTPUT]

where `ludocid` is cid of the business whose reviews are to be scraped, e.g.
```
revscr --ludocid 3435981545910666830
```
or
```
revscr --l 3435981545910666830
```
.

Alternatively a `search term` can be supplied, instead of `ludocid`. In this case, the script will find the ludocid of the palce by a google search.

e.g.
```
revscr --search "Aspria Berlin Ku'damm"
```
or
```
revscr --s "Aspria Berlin Ku'damm"
```
.

Note that one the two arguments `--search` and `--ludocid` must be supplied!

To get the help page, run
```
revscr -h
```
or
```
revscr --help
```
.