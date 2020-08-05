# deb_stats

For a given architecture, deb_stats retrieves a list of Debian packages from a mirror and outputs a ranked list of the package names containing the most number of files.

## Usage

```
./deb_stats.py -a [arch]
```
## Additional Information
A quick shell proof of concept is also included, which accepts a positional argument:

```
./deb_stats.sh [arch]
```
This code is the basis of what is used within the python script.

Ideally, this portion of the script would be re-written in pure python, by saving the output of the metadata into an array and counting duplicates.

## License
[MIT](https://choosealicense.com/licenses/mit/)
