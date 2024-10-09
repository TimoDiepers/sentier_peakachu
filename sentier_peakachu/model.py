from sentier_data_tools import Dataset, Demand, Flow, ProductIRI, SentierModel


class ElectricityModel(SentierModel):
    provides = {
        ProductIRI(
            "http://openenergy-platform.org/ontology/oeo/OEO_00000139"
        ): "electricity"
    }
    aliases = {}

    def run(self, abbreviate_iris: bool = True) -> tuple[list[Demand], list[Flow]]:
        self.prepare()

    def prepare(self) -> None:
        self.get_model_data()
        self.data_validity_checks()
        self.resample()

    def get_generation_mix(self) -> list[Dataset]:
        datasets = list(
            Dataset.select().where(
                (Dataset.product == self.demand.product_iri)
                & (Dataset.location == self.demand.spatial_context)
            )
        )
        return self.merge_datasets_to_dataframes(datasets)
