from rdflib.namespace import SKOS, RDF
from rdflib import URIRef, Namespace, Literal
import skosify

PRODUCTS = Namespace("https://vocab.sentier.dev/products/")

EL_ENERGY_PRODUCTS_DATA = [
    # Fossil fuel-based electrical energy
    (
        URIRef(PRODUCTS + "Fossil fuel-based electrical energy"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Fossil fuel-based electrical energy"),
        SKOS.broader,
        URIRef("http://data.europa.eu/xsp/cn2024/271600000080")
    ),
    (
        URIRef(PRODUCTS + "Fossil fuel-based electrical energy"),
        SKOS.prefLabel,
        Literal("Fossil fuel-based electrical energy", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Fossil fuel-based electrical energy"),
        SKOS.definition,
        Literal("Fossil fuel-based electrical energy is electrical energy produced by incineration of fossil fuels.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Fossil fuel-based electrical energy"),
        SKOS.related,
        URIRef("https://de.wikipedia.org/wiki/Fossile_Energie")
    ),
    # Fossil oil-based electrical energy
    (
        URIRef(PRODUCTS + "Fossil oil-based electrical energy"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Fossil oil-based electrical energy"),
        SKOS.broader,
        URIRef(PRODUCTS + "Fossil fuel-based electrical energy")
    ),
    (
        URIRef(PRODUCTS + "Fossil oil-based electrical energy"),
        SKOS.prefLabel,
        Literal("Fossil oil-based electrical energy", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Fossil oil-based electrical energy"),
        SKOS.definition,
        Literal("Fossil oil-based electrical energy is electrical energy produced by the combustion of fossil oils.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Fossil oil-based electrical energy"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Petroleum")
    ),
    # Electrical energy from (crude) oil
    (
        URIRef(PRODUCTS + "Electrical energy from crude oil"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from crude oil"),
        SKOS.broader,
        URIRef(PRODUCTS + "Fossil oil-based electrical energy")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from crude oil"),
        SKOS.prefLabel,
        Literal("Electrical energy from crude oil", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from crude oil"),
        SKOS.definition,
        Literal("Electrical energy from crude oil refers to electricity generated from the combustion of crude oil.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from crude oil"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Petroleum")
    ),
    # Electrical energy from oil shale
    (
        URIRef(PRODUCTS + "Electrical energy from oil shale"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from oil shale"),
        SKOS.broader,
        URIRef(PRODUCTS + "Fossil oil-based electrical energy")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from oil shale"),
        SKOS.prefLabel,
        Literal("Electrical energy from oil shale", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from oil shale"),
        SKOS.definition,
        Literal("Electrical energy from oil shale is generated from the processing and combustion of oil shale.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from oil shale"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Oil_shale")
    ),
    # Natural gas-based electrical energy
    (
        URIRef(PRODUCTS + "Natural gas-based electrical energy"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Natural gas-based electrical energy"),
        SKOS.broader,
        URIRef(PRODUCTS + "Fossil fuel-based electrical energy")
    ),
    (
        URIRef(PRODUCTS + "Natural gas-based electrical energy"),
        SKOS.prefLabel,
        Literal("Natural gas-based electrical energy", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Natural gas-based electrical energy"),
        SKOS.definition,
        Literal("Natural gas-based electrical energy is electrical energy produced through the combustion of natural gas.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Natural gas-based electrical energy"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Natural_gas")
    ),
    # Electrical energy from natural gas
    (
        URIRef(PRODUCTS + "Electrical energy from natural gas"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from natural gas"),
        SKOS.broader,
        URIRef(PRODUCTS + "Natural gas-based electrical energy")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from natural gas"),
        SKOS.prefLabel,
        Literal("Electrical energy from natural gas", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from natural gas"),
        SKOS.definition,
        Literal("Electrical energy from natural gas refers to electricity generated from the combustion of natural gas.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from natural gas"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Natural_gas")
    ),
    # Electrical energy from coal seam gas
    (
        URIRef(PRODUCTS + "Electrical energy from coal seam gas"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from coal seam gas"),
        SKOS.broader,
        URIRef(PRODUCTS + "Natural gas-based electrical energy")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from coal seam gas"),
        SKOS.prefLabel,
        Literal("Electrical energy from coal seam gas", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from coal seam gas"),
        SKOS.definition,
        Literal("Electrical energy from coal seam gas is generated through the combustion of coal seam gas.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from coal seam gas"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Coalbed_methane")
    ),
    # Coal-based electrical energy
    (
        URIRef(PRODUCTS + "Coal-based electrical energy"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Coal-based electrical energy"),
        SKOS.broader,
        URIRef(PRODUCTS + "Fossil fuel-based electrical energy")
    ),
    (
        URIRef(PRODUCTS + "Coal-based electrical energy"),
        SKOS.prefLabel,
        Literal("Coal-based electrical energy", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Coal-based electrical energy"),
        SKOS.definition,
        Literal("Coal-based electrical energy is electrical energy produced by the combustion of coal.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Coal-based electrical energy"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Coal-fired_power_station")
    ),
    # Electrical energy from hard coal
    (
        URIRef(PRODUCTS + "Electrical energy from hard coal"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from hard coal"),
        SKOS.broader,
        URIRef(PRODUCTS + "Coal-based electrical energy")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from hard coal"),
        SKOS.prefLabel,
        Literal("Electrical energy from hard coal", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from hard coal"),
        SKOS.definition,
        Literal("Electrical energy from hard coal is generated from the combustion of hard coal.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from hard coal"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Coal-fired_power_station")
    ),
    # Electrical energy from brown coal/lignite
    (
        URIRef(PRODUCTS + "Electrical energy from brown coal/lignite"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from brown coal/lignite"),
        SKOS.broader,
        URIRef(PRODUCTS + "Coal-based electrical energy")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from brown coal/lignite"),
        SKOS.prefLabel,
        Literal("Electrical energy from brown coal/lignite", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from brown coal/lignite"),
        SKOS.definition,
        Literal("Electrical energy from brown coal/lignite is generated from the combustion of brown coal or lignite.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from brown coal/lignite"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Lignite")
    ),
    # Electrical energy from other fossil fuels
    (
        URIRef(PRODUCTS + "Electrical energy from other fossil fuels"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from other fossil fuels"),
        SKOS.broader,
        URIRef(PRODUCTS + "Fossil fuel-based electrical energy")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from other fossil fuels"),
        SKOS.prefLabel,
        Literal("Electrical energy from other fossil fuels", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from other fossil fuels"),
        SKOS.definition,
        Literal("Electrical energy from other fossil fuels includes electricity generated from various other fossil fuels such as peat.", lang="en")
    ),
    # Electrical energy from peat
    (
        URIRef(PRODUCTS + "Electrical energy from peat"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from peat"),
        SKOS.broader,
        URIRef(PRODUCTS + "Electrical energy from other fossil fuels")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from peat"),
        SKOS.prefLabel,
        Literal("Electrical energy from peat", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from peat"),
        SKOS.definition,
        Literal("Electrical energy from peat is generated through the combustion of peat.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from other fossil fuels"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Peat")
    ),

    # Renewable electrical energy - already existing
    # Wind-based electrical energy
    (
        URIRef(PRODUCTS + "Electricity from wind energy"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Electricity from wind energy"),
        SKOS.broader,
        URIRef("http://openenergy-platform.org/ontology/oeo/OEO_00010384")
    ),
    (
        URIRef(PRODUCTS + "Electricity from wind energy"),
        SKOS.prefLabel,
        Literal("Electricity from wind energy", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electricity from wind energy"),
        SKOS.definition,
        Literal("Electricity from wind energy is electrical energy produced by converting wind energy into electricity through wind turbines.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electricity from wind energy"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Wind_power")
    ),
    # Electrical energy from offshore wind
    (
        URIRef(PRODUCTS + "Electricity from offshore wind energy"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Electricity from offshore wind energy"),
        SKOS.broader,
        URIRef(PRODUCTS + "Electricity from wind energy")
    ),
    (
        URIRef(PRODUCTS + "Electricity from offshore wind energy"),
        SKOS.prefLabel,
        Literal("Electrical energy from offshore wind", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electricity from offshore wind energy"),
        SKOS.definition,
        Literal("Electrical energy from offshore wind is generated by wind turbines located in bodies of water.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electricity from offshore wind energy"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Offshore_wind_power")
    ),
    # Electrical energy from onshore wind
    (
        URIRef(PRODUCTS + "Electricity from onshore wind energy"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Electricity from onshore wind energy"),
        SKOS.broader,
        URIRef(PRODUCTS + "Electricity from wind energy")
    ),
    (
        URIRef(PRODUCTS + "Electricity from onshore wind energy"),
        SKOS.prefLabel,
        Literal("Electricity from onshore wind energy", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electricity from onshore wind energy"),
        SKOS.definition,
        Literal("Electricity from onshore wind energy is generated by wind turbines located on land.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electricity from onshore wind energy"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Wind_power")
    ),
    # Water-based electrical energy
    (
        URIRef(PRODUCTS + "Electricity from hydropower"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Electricity from hydropower"),
        SKOS.broader,
        URIRef("http://openenergy-platform.org/ontology/oeo/OEO_00010384")
    ),
    (
        URIRef(PRODUCTS + "Electricity from hydropower"),
        SKOS.prefLabel,
        Literal("Water-based electrical energy", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electricity from hydropower"),
        SKOS.definition,
        Literal("Electricity from hydropower is electrical energy generated through the use of water resources.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electricity from hydropower"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Hydroelectricity")
    ),
    # Electrical energy from hydro water reservoirs
    (
        URIRef(PRODUCTS + "Electrical energy from hydro water reservoirs"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from hydro water reservoirs"),
        SKOS.broader,
        URIRef(PRODUCTS + "Electricity from hydropower")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from hydro water reservoirs"),
        SKOS.prefLabel,
        Literal("Electrical energy from hydro water reservoirs", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from hydro water reservoirs"),
        SKOS.definition,
        Literal("Electrical energy from hydro water reservoirs is generated using stored water in reservoirs to drive hydro turbines.", lang="en")
    ),
    # Electrical energy from pumped storage hydro
    (
        URIRef(PRODUCTS + "Electrical energy from pumped storage hydro"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from pumped storage hydro"),
        SKOS.broader,
        URIRef(PRODUCTS + "Electricity from hydropower")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from pumped storage hydro"),
        SKOS.prefLabel,
        Literal("Electrical energy from pumped storage hydro", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from pumped storage hydro"),
        SKOS.definition,
        Literal("Electrical energy from pumped storage hydro is generated through a two-reservoir system where water is pumped to a higher elevation for storage and released to generate electricity.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from pumped storage hydro"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Pumped-storage_hydroelectricity")
    ),
    # Electrical energy from run-of-river and poundage hydro
    (
        URIRef(PRODUCTS + "Electrical energy from run-of-river and poundage hydro"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from run-of-river and poundage hydro"),
        SKOS.broader,
        URIRef(PRODUCTS + "Electricity from hydropower")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from run-of-river and poundage hydro"),
        SKOS.prefLabel,
        Literal("Electrical energy from run-of-river and poundage hydro", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from run-of-river and poundage hydro"),
        SKOS.definition,
        Literal("Electrical energy from run-of-river and poundage hydro is generated without large reservoirs, utilizing the natural flow of rivers.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from run-of-river and poundage hydro"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Run-of-the-river_hydroelectricity")
    ),
    # Electrical energy from marine sources
    (
        URIRef(PRODUCTS + "Electrical energy from marine sources"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from marine sources"),
        SKOS.broader,
        URIRef(PRODUCTS + "Electricity from hydropower")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from marine sources"),
        SKOS.prefLabel,
        Literal("Electrical energy from marine sources", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from marine sources"),
        SKOS.definition,
        Literal("Electrical energy from marine sources is generated from ocean and tidal forces, exploiting kinetic energy.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from marine sources"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Marine_energy")
    ),
    # Solar-based electrical energy - already existing
    # Other renewable electrical energy
    (
        URIRef(PRODUCTS + "Other renewable electrical energy"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Other renewable electrical energy"),
        SKOS.broader,
        URIRef("http://openenergy-platform.org/ontology/oeo/OEO_00010384")
    ),
    (
        URIRef(PRODUCTS + "Other renewable electrical energy"),
        SKOS.prefLabel,
        Literal("Other renewable electrical energy", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Other renewable electrical energy"),
        SKOS.definition,
        Literal("Other renewable electrical energy includes electricity generated from sources such as geothermal and biomass.", lang="en")
    ),
    # Electrical energy from geothermal sources
    (
        URIRef(PRODUCTS + "Electrical energy from geothermal sources"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from geothermal sources"),
        SKOS.broader,
        URIRef(PRODUCTS + "Other renewable electrical energy")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from geothermal sources"),
        SKOS.prefLabel,
        Literal("Electrical energy from geothermal sources", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from geothermal sources"),
        SKOS.definition,
        Literal("Electrical energy from geothermal sources is generated by harnessing heat from the earth's interior.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from geothermal sources"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Geothermal_energy")
    ),
    # Electrical energy from biomass
    (
        URIRef(PRODUCTS + "Electrical energy from biomass"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from biomass"),
        SKOS.broader,
        URIRef(PRODUCTS + "Other renewable electrical energy")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from biomass"),
        SKOS.prefLabel,
        Literal("Electrical energy from biomass", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from biomass"),
        SKOS.definition,
        Literal("Electrical energy from biomass is generated by burning organic materials such as plant and animal waste to produce electricity.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from biomass"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Bioenergy")
    ),
    # Electrical energy from other renewable sources
    (
        URIRef(PRODUCTS + "Electrical energy from other renewable sources"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from other renewable sources"),
        SKOS.broader,
        URIRef(PRODUCTS + "Other renewable electrical energy")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from other renewable sources"),
        SKOS.prefLabel,
        Literal("Electrical energy from other renewable sources", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Electrical energy from other renewable sources"),
        SKOS.definition,
        Literal("Electrical energy from other renewable sources includes electricity generated from various innovative renewable technologies.", lang="en")
    ),
    # Other electrical energy
    (
        URIRef(PRODUCTS + "Other electrical energy"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Other electrical energy"),
        SKOS.broader,
        URIRef("http://data.europa.eu/xsp/cn2024/271600000080")  # Electrical energy
    ),
    (
        URIRef(PRODUCTS + "Other electrical energy"),
        SKOS.prefLabel,
        Literal("Other electrical energy", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Other electrical energy"),
        SKOS.definition,
        Literal("Other electrical energy includes various forms of electrical energy generation not classified as renewable or fossil fuel-based.", lang="en")
    ),
    # Nuclear-based electrical energy - already existing
    # Waste-based electrical energy
    (
        URIRef(PRODUCTS + "Waste-based electrical energy"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Waste-based electrical energy"),
        SKOS.broader,
        URIRef(PRODUCTS + "Other electrical energy")
    ),
    (
        URIRef(PRODUCTS + "Waste-based electrical energy"),
        SKOS.prefLabel,
        Literal("Waste-based electrical energy", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Waste-based electrical energy"),
        SKOS.definition,
        Literal("Waste-based electrical energy is generated by converting waste materials into electricity, typically through incineration or anaerobic digestion.", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Waste-based electrical energy"),
        SKOS.related,
        URIRef("https://en.wikipedia.org/wiki/Waste-to-energy")
    ),
    # Other electrical energy sources
    (
        URIRef(PRODUCTS + "Other electrical energy sources"),
        RDF.type,
        SKOS.Concept
    ),
    (
        URIRef(PRODUCTS + "Other electrical energy sources"),
        SKOS.broader,
        URIRef(PRODUCTS + "Other electrical energy")
    ),
    (
        URIRef(PRODUCTS + "Other electrical energy sources"),
        SKOS.prefLabel,
        Literal("Other electrical energy sources", lang="en")
    ),
    (
        URIRef(PRODUCTS + "Other electrical energy sources"),
        SKOS.definition,
        Literal("Other electrical energy sources encompass diverse methods and technologies for generating electricity that do not fall into traditional categories.", lang="en")
    ),
]
skosify.infer.skos_hierarchical(EL_ENERGY_PRODUCTS_DATA)