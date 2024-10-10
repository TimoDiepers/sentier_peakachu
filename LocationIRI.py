import polars as pl

geonameid_base = "https://sws.geonames.org/"
lookup_file = "docs/iso_iri_table.csv"
lookup_separator = "\t"

def ISO_Lookup(code: str) -> str:
    lookup = pl.scan_csv(lookup_file, separator=lookup_separator)
    if len(code) == 3:
        id = lookup.sql(f"SELECT geonameid FROM self WHERE ISO3 = '{code}'").collect().item(0,0)
    elif len(code) == 2:
        id = lookup.sql(f"SELECT geonameid FROM self WHERE ISO2 = '{code}'").collect().item(0,0)
    else:
        raise ValueError('Please use a two or three digit ISO code')

    return geonameid_base + str(id) + "/"