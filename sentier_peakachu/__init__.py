"""sentier_peakachu."""

__all__ = (
    "__version__",
    "ElectricityModel",
    "create_local_datastorage",
)

__version__ = "0.1.0"

from sentier_peakachu.data import create_local_datastorage
from sentier_peakachu.model import ElectricityModel
