class CommitCache:
    _data = {}
    @classmethod
    def get(cls, h): return cls._data.get(h)
    @classmethod
    def set(cls, h, v): cls._data[h] = v
