import polars as pl

BASE_URL = "https://sws.geonames.org/"
LOOKUP_FILE = "data/iso_iri_table.csv"
LOOKUP_SEPARATOR = "\t"


def get_geonames_iri_from_iso_code(iso_code: str) -> str:
    """
    Lookup the geoname identifier for a given ISO code using a CSV lookup table.

    Parameters
    ----------
    iso_code : str
        The ISO country code. It can be either a two-digit ISO 3166-1 alpha-2 code
        or a three-digit ISO 3166-1 alpha-3 code.

    Returns
    -------
    str
        The full URL that appends the geoname identifier to a base URL.

    Raises
    ------
    ValueError
        If the `iso_code` is not two or three characters long or if no matching geoname identifier is found.
    """
    if len(iso_code) not in [2, 3]:
        raise ValueError("Please provide a two-digit or three-digit ISO code")

    lookup = pl.scan_csv(LOOKUP_FILE, separator=LOOKUP_SEPARATOR)
    column = "ISO3" if len(iso_code) == 3 else "ISO2"
    query = f"SELECT geonameid FROM self WHERE {column} = '{iso_code}'"
    geoname_id = lookup.sql(query).collect().item(0, 0)

    if geoname_id is None:
        raise ValueError("ISO code not found")

    return BASE_URL + str(geoname_id) + "/"
