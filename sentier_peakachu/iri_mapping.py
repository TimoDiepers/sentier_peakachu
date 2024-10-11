ENTSOE_PRODUCT_IRIS_MAPPING = {
    "Fossil Oil": "https://vocab.sentier.dev/products/electricity/crude-oil",
    "Fossil Oil shale": "https://vocab.sentier.dev/products/electricity/oil-shale",
    "Fossil Gas": "https://vocab.sentier.dev/products/electricity/natural-gas",
    "Fossil Coal-derived gas": "https://vocab.sentier.dev/products/electricity/coalbed-gas",
    "Fossil Hard coal": "https://vocab.sentier.dev/products/electricity/hard-coal",
    "Fossil Brown coal/Lignite": "https://vocab.sentier.dev/products/electricity/lignite",
    "Fossil Peat": "https://vocab.sentier.dev/products/electricity/peat",
    "Wind Offshore": "https://vocab.sentier.dev/products/electricity/offshore",
    "Wind Onshore": "https://vocab.sentier.dev/products/electricity/onshore",
    "Hydro Water Reservoir": "https://vocab.sentier.dev/products/electricity/hydro-reservoirs",
    "Hydro Pumped Storage": "https://vocab.sentier.dev/products/electricity/pumped-storage",
    "Hydro Run-of-river and poundage": "https://vocab.sentier.dev/products/electricity/run-of-river",
    "Marine": "https://vocab.sentier.dev/products/electricity/marine",
    "Solar": "http://openenergyplatform.org/ontology/oeo/OEO_00010419/",
    "Geothermal": "https://vocab.sentier.dev/products/electricity/geothermal",
    "Biomass": "https://vocab.sentier.dev/products/electricity/biomass",
    "Other renewable": "https://vocab.sentier.dev/products/electricity/other-renewable-sources",
    "Nuclear": "http://openenergyplatform.org/ontology/oeo/OEO_00010417/",
    "Waste": "https://vocab.sentier.dev/products/electricity/waste",
    "Other": "https://vocab.sentier.dev/products/electricity/other",
}

DIRTY_TRACE_AGGREGATION = {
    "https://vocab.sentier.dev/products/electricity/crude-oil": "https://vocab.sentier.dev/products/electricity/fossil-oil",
    "https://vocab.sentier.dev/products/electricity/oil-shale": "https://vocab.sentier.dev/products/electricity/fossil-oil",
    "https://vocab.sentier.dev/products/electricity/natural-gas": "https://vocab.sentier.dev/products/electricity/fossil-gas",
    "https://vocab.sentier.dev/products/electricity/coalbed-gas": "https://vocab.sentier.dev/products/electricity/fossil-gas",
    "https://vocab.sentier.dev/products/electricity/hard-coal": "https://vocab.sentier.dev/products/electricity/fossil-coal",
    "https://vocab.sentier.dev/products/electricity/lignite": "https://vocab.sentier.dev/products/electricity/fossil-coal",
    "https://vocab.sentier.dev/products/electricity/peat": "https://vocab.sentier.dev/products/electricity/peat",
    # "https://vocab.sentier.dev/products/electricity/offshore": None,
    # "https://vocab.sentier.dev/products/electricity/onshore": None,
    # "https://vocab.sentier.dev/products/electricity/hydro-reservoirs": None,
    # "https://vocab.sentier.dev/products/electricity/pumped-storage": None,
    # "https://vocab.sentier.dev/products/electricity/run-of-river": None,
    # "https://vocab.sentier.dev/products/electricity/marine": None,
    # "http://openenergyplatform.org/ontology/oeo/OEO_00010419/": None,
    # "https://vocab.sentier.dev/products/electricity/geothermal": None,
    # "https://vocab.sentier.dev/products/electricity/biomass": None,
    # "https://vocab.sentier.dev/products/electricity/other-renewable-sources": None,
    # "http://openenergyplatform.org/ontology/oeo/OEO_00010417/": None,
    # "https://vocab.sentier.dev/products/electricity/waste": "https://vocab.sentier.dev/products/electricity/waste",
    # "https://vocab.sentier.dev/products/electricity/other": None,
}

TRACE_PRODUCT_IRIS_MAPPING = {
    "oil": "https://vocab.sentier.dev/products/electricity/fossil-oil",
    "gas": "https://vocab.sentier.dev/products/electricity/fossil-gas",
    "other_fossil": "https://vocab.sentier.dev/products/electricity/peat",
    "coal": "https://vocab.sentier.dev/products/electricity/fossil-coal",
    "biomass": "https://vocab.sentier.dev/products/electricity/biomass",
    "waste": "https://vocab.sentier.dev/products/electricity/waste",
}

DIRTY_BONSAI_PRODUCT_IRIS_MAPPING = {  # RENEWABLES ONLY
    # "Production of electricity by biomass and waste": "https://vocab.sentier.dev/products/electricity/biomass",
    "Production of electricity by geothermal": "https://vocab.sentier.dev/products/electricity/geothermal",
    "Production of electricity by hydro": "https://vocab.sentier.dev/products/electricity/run-of-river",  # WRONG
    "Production of electricity by nuclear": "http://openenergyplatform.org/ontology/oeo/OEO_00010417/",
    "Production of electricity by solar photovoltaic": "http://openenergyplatform.org/ontology/oeo/OEO_00010419/",
    "Production of electricity by tide, wave, ocean": "https://vocab.sentier.dev/products/electricity/marine",
    "Production of electricity by wind": "https://vocab.sentier.dev/products/electricity/offshore",  # WRONG
}

# DIRTY_BONSAI_AGGREGATION = {
