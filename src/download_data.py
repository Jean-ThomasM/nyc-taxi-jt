class NYCTaxiDataDownloader:
    def __init__(self,base_url,year,data_dir):
        self.base_url=base_url
        self.year=year
        self.data_dir=data_dir

    def get_fle