from GSheetsEtl import GSheetsEtl

config = {
    "remote": "https://example.com/sheet.csv",
    "local_dir": "data/",
    "data_format": "csv",
    "destination": "output/"
}

my_etl = GSheetsEtl(config)

print(my_etl.__doc__)
help(my_etl)
