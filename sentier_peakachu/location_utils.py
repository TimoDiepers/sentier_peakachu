import polars as pl
import pandas as pd
import networkx as nx

class LocationUtility():

    def __init__(self) -> None:        
        self.geonameid_base = "https://sws.geonames.org/"
        self.iso_iri_table = "../../data/Location-Services/iso_iri_table.csv"
        self.hierarchy_table = "../../data/Location-Services/hierarchy.txt"
        self.lookup_separator = "\t"
        self.hierarchy_graph = nx.DiGraph()

    def IRI_Lookup(self, code: str) -> str:
        geonameid = self.geonameid_Lookup(code)
        return self.geonameid_base + str(geonameid) + "/"
    
    def geonameid_Lookup(self, code:str):
        lookup = pl.scan_csv(self.iso_iri_table, separator=self.lookup_separator)
        if len(code) == 3:
            id = lookup.sql(f"SELECT geonameid FROM self WHERE ISO3 = '{code}'").collect().item(0,0)
        elif len(code) == 2:
            id = lookup.sql(f"SELECT geonameid FROM self WHERE ISO2 = '{code}'").collect().item(0,0)
        else:
            raise ValueError('Please use a two or three digit ISO code')

        return id
    
    def build_graph(self):
        df = pd.read_csv("../../data/Location-Services/hierarchy.txt",sep="\t",header=0)
        df.columns = ['parent','child','type']
        for index, row in df.iterrows():
            self.hierarchy_graph.add_edge(row['parent'], row['child'])
        
    def get_graph_children(self, geonameid:int) -> list[tuple[str,int]]:
        
