def apply_facet_filter(self, selected_facets):
    for cur_sifter, cur_facets in selected_facets.items():
        self.facet_filter(cur_sifter, cur_facets)


def facet_filter(self, sifter, current_sifter_facet_list):
    if sifter in ["title", "desc", "filetype"]:
        self.text_filter(sifter, current_sifter_facet_list)


def text_filter(self, sifter, current_sifter_facet_list):
    cur_filtered_datasets = list()
    for dataset in self.__filtered_datasets:
        for current_facet in current_sifter_facet_list:
            if current_facet in dataset[sifter]:
                cur_filtered_datasets.append(dataset)
                break
    self.__filtered_datasets = cur_filtered_datasets


'''def type_filter(self, current_sifter_facet_list):
    cur_filtered_datasets = list()
    for dataset in self.__filtered_datasets:
        for current_facet in current_sifter_facet_list:'''