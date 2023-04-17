class Paper:
    def __init__(self, dict):
        # check if a flag exists before storing it
        if dict.get('flag', None):
            self.flag = dict["flag"]

        self.title = dict['title']
        self.doi = dict['doi']
        self.language = dict['language']
        self.countries = dict['countries']
        self.database = dict['database']
        self.type = dict['type']
        self.meta = dict['meta']
        self.variants = dict['variants']
        self.keywords = dict['keywords']
        
        # normalize the data
        self.normalizeKeywords()

    def normalizeKeywords(self):
        self.keywords = [Paper.normalize(kw) for kw in self.keywords]


    # static methods
    @staticmethod
    def normalize(word):
        return Paper.depluralize(Paper.decapitalize(word))

    @staticmethod
    def decapitalize(word):
        return word.lower()
        
    @staticmethod
    def depluralize(word):
        return word[:-1] if word[-1:][0] == 's' else word

