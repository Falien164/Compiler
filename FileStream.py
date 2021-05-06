import codecs
from antlr4.InputStream import InputStream


class FileStream(InputStream):
    __slots__ = "fileName"

    def __init__(self, fileName: str, encoding: str = "ascii", errors: str = "strict"):
        super().__init__(self.readDataFrom(fileName, encoding, errors))
        self.fileName = fileName

    def readDataFrom(self, fileName: str, encoding: str, errors: str = "strict"):
        # read binary to avoid line ending conversion
        with open(fileName, "rb") as file:
            bytes = file.read()
            return codecs.decode(bytes, encoding, errors)
