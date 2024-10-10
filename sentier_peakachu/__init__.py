"""sentier_peakachu."""

__all__ = (
    "__version__",
    "ElectricityModel",
    "create_local_datastorage",
    "get_geonames_iri_from_iso_code",
)

__version__ = "0.1.0"

from sentier_peakachu.data import create_local_electricity_datastorage
from sentier_peakachu.model import ElectricityModel
from sentier_peakachu.utils_location import get_geonames_iri_from_iso_code
