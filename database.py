class FilmsDatabase:
    def __init__(self, rows: list = None):
        if rows is not None:
            self.db = rows
            self.id_dicts = dict([[rows[i][3], i] for i in range(0, len(rows))])
        else:
            self.db = []
            self.id_dicts = {}
        pass

    def search_by_name(self, name) -> list:
        result = []
        for row in self.db:
            if row[0] == name:
                result.append(row)
        return result

    def search_by_year(self, year) -> list:
        result = []
        for row in self.db:
            if row[1] == year:
                result.append(row)
        return result

    def search_by_rate(self, rate) -> list:
        rate = float(rate)
        result = []
        for row in self.db:
            if row[2] == rate:
                result.append(row)
        return result

    def search_by_id(self, node_id) -> list:
        node_id = int(node_id)
        result = []
        for row in self.db:
            if row[3] == node_id:
                result.append(row)
        return result

    def add(self, new_node: list):
        self.db.append(new_node)

