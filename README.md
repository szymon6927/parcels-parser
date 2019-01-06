# ParcelsParser

Recruitment task for company: ADGROUP (05.01.2019)

Application prints out extracted data about province code, county code,commune code, commune type, district number, parcel number based on columns with cadastral parcel identifiers

### Prerequisites

Application does not require any prerequisites because all libraries which i use here are in python standard library 

### Running

An program use argparse so you could define start parameters like filename and column name with data

Default arguments are:
```
--filename test_cadastral_parcels.tsv
--column cadastral_parcel_identifier
```

After gitclone to start, go to application directroy:
```
$ cd parcels-parser
```
And then
```
$ python run.py
```

If you want specify different start arguments

```
$ python run.py --filename YOUR_FILE --column YOUR_COLUMN_NAME
```

## Running the tests

To run test go to application directory
```
$ cd parcels-parser
```
And then
```
$ python -m unittest discover -v
```

## Authors

* **Szymon Miks** - [personal website](https://szymonmiks.pl/)


## License

This project is licensed under the MIT License
