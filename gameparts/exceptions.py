class FieldIndexError(IndexError):

    def __str__(self):
        return "Vvedeno znachenie za granicami igrovogo polya"


class CellOccupiedError(Exception):

    def __str__(self):
        return "Popitka izmenit zanyatuu yacheiku"
