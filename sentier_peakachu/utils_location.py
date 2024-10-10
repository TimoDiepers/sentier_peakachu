import warnings

import polars as pl
from sentier_data_tools import GeonamesIRI

BASE_URL = "https://sws.geonames.org/"
LOOKUP_FILE = "../data/iso_iri_table.csv"
LOOKUP_SEPARATOR = "\t"


def get_geonames_iri_from_iso_code(iso_code: str) -> GeonamesIRI:
    """
    Lookup the geoname identifier for a given ISO code using a CSV lookup table.

    Parameters
    ----------
    iso_code : str
        The ISO country code. It can be either a two-digit ISO 3166-1 alpha-2 code
        or a three-digit ISO 3166-1 alpha-3 code.

    Returns
    -------
    GeonamesIRI
        The IRI of the location identifier.

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
    res = lookup.sql(query).collect()

    if res.is_empty():
        warnings.warn(f"ISO code {iso_code} not found")
        return None

    geoname_id = res.item(0, 0)
    iri = BASE_URL + str(geoname_id) + "/"
    return GeonamesIRI(iri)
