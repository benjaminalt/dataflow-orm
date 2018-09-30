from antlr4.InputStream import InputStream


class CaseChangingInputStream(InputStream):
    def __init__(self, data, stream: InputStream, upper: bool):
        super(CaseChangingInputStream, self).__init__(data)
        self.stream = stream
        self.upper = upper

    def getText(self, start :int, stop: int):
        return self.stream.getText(start, stop)

    def consume(self):
        self.stream.consume()

    def LA(self, offset: int):
        c = self.stream.LA(offset)
        if c <= 0:
            return c
        if self.upper:
            return ord(chr(c).upper())
        return ord(chr(c).lower())

    def LT(self, offset: int):
        return self.stream.LT(offset)

    def mark(self):
        return self.stream.mark()

    def release(self, marker: int):
        return self.stream.release(marker)

    def seek(self, _index: int):
        self.stream.seek(_index)

    @property
    def index(self):
        return self.stream.index

    @property
    def size(self):
        return self.stream.size