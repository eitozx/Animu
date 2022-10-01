class _Base:
    def __init__(self, data):
        self._data = data

    def __getitem__(self, key):
        return self._data[key]


class Fact(_Base):
    def __init__(self, data):
        super().__init__(data)

        self.id = data.get('_id')
        self.fact = data.get('fact')
        self.tags = data.get('tags')

    def __str__(self):
        return self.fact


class Password(_Base):
    def __init__(self, data):        
        super().__init__(data)

        self.password = data.get('pass')

    def __str__(self):
        return self.password


class Quote(_Base):
    def __init__(self, data):
        super().__init__(data)

        self.id = data.get('_id')
        self.quote = data.get('quote')
        self.anime = data.get('anime')
        self.said = data.get('said')

    def __str__(self):
        return self.quote


class Roleplay(_Base):
    def __init__(self, data):
        super().__init__(data)

        self.url = data.get('url')

    def __str__(self):
        return self.url


class Waifu(_Base):
    def __init__(self, data):
        super().__init__(data)
        
        self.id = data.get('_id')
        self.images = data.get('images')
        
        self.names = data.get('names')
        self.en_name = self.names.get('en')
        self.jp_name = self.names.get('jp')
        self.alt_name = self.names.get('alt')

        self.animeinfo = data['from']
        self.anime = self.animeinfo.get('name')
        self.anime_type = self.animeinfo.get('type')

        self.statistics = data.get('statistics')
        self.fav = self.statistics.get('fav')
        self.love = self.statistics.get('love')
        self.hate = self.statistics.get('hate')
        self.upvote = self.statistics.get('upvote')
        self.downvote = self.statistics.get('downvote')
        
    def __str__(self):
        return self.en_name or self.jp_name or self.alt_name