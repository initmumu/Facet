from konlpy.tag import Okt
from pprint import pprint

from classes.config import conf

class Facet:
    def __init__(self, datasets):

        '''
        name: Facet 클래스 생성자
        desc: Metadataset들을 매개변수로 하여 Facet class를 생성
        '''
        self.__original_datasets = list()
        self.set_original_datasets(datasets)

        self.__filtered_datasets = list()
        self.set_filtered_datasets(datasets)

        self.__facet_key = self.make_facet_key()
        self.__facet_value = self.make_facet_value()
        self.__facet = self.make_facet()

    ''' Belows are Logic Methods '''
    def extract_nouns(self, datalist):
        okt = Okt()

        extracted_datalist = list()
        for item in datalist:
            extracted_datalist += okt.nouns(item)

        return list(set(extracted_datalist))

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
    
    def type_filter(self, current_sifter_facet_list):
        cur_filtered_datasets = list()
        for dataset in self.__filtered_datasets:
            for current_facet in current_sifter_facet_list:


    ''' Belows are Maker Methods '''
    def make_facet_key(self):
        return conf['facet_key']

    def make_facet_value(self):
        facet_value = dict()

        for key in self.__facet_key:
            facet_value[key] = list()

        for dataset in self.__original_datasets:
            for key in self.__facet_key:
                facet_value[key].append(dataset[key])
        
        return facet_value

    def make_facet(self):
        facet = dict()
        for key, value in self.__facet_value.items():
            if key in ["title", "desc"]:
                facet[key] = self.extract_nouns(value)
            elif key == "filetype":
                

        return facet

    ''' Belows are Setter Methods '''
    def set_original_datasets(self, datasets):
        self.__original_datasets = datasets

    def set_filtered_datasets(self, datasets):
        self.__filtered_datasets = datasets

    ''' Belows are Getter Methods '''
    def get_original_datasets(self):
        return self.__original_datasets

    def get_facet_key(self):
        return self.__facet_key

    def get_facet_value(self):
        return self.__facet_value

    def get_facet(self):
        return self.__facet

    def get_filtered_datasets(self):
        return self.__filtered_datasets

    ''' Belows are Print Methods '''
    def print_original_datasets(self):
        pprint(self.__original_datasets)

    def print_facet_key(self):
        pprint(self.__facet_key)

    def print_facet_value(self):
        pprint(self.__facet_value)

    def print_facet(self):
        pprint(self.__facet)

    def print_filtered_datasets(self):
        pprint(self.__filtered_datasets)
