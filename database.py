class FilmsDatabase:
    def __init__(self, filename, handler_filename):
        self.filename = filename
        self.handler_filename = handler_filename
        with open(handler_filename, 'r+') as handler:
            self.field_names = handler.readline().split(';')
            self.field_names[len(self.field_names) - 1] = self.field_names[len(self.field_names) - 1].replace('\n', '')
            self.field_lengths = [int(size) for size in handler.readline().split(';')]
            self.node_size_in_bytes = 0
            for size in self.field_lengths:
                self.node_size_in_bytes += size + 1
        rows = []
        with open(filename, 'r+') as data_file:
            self.max_id = 0
            for line in data_file:
                raw_row = line.split(';')
                rows.append([raw_row[0].replace('^', ''), int(raw_row[1]), float(raw_row[2]), int(raw_row[3])])
                self.max_id = max(self.max_id, int(raw_row[3]))
        if rows:
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
        year = int(year)
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
        try:
            self.db.append([new_node[0], int(new_node[1]), float(new_node[2]), self.max_id + 1])
            self.max_id += 1
            self.id_dicts[self.max_id] = len(self.db) - 1
        except Exception:
            print('Incorrect data:')

    def delete_node(self, node_id):
        with open(self.filename, 'r+') as data_file:
            data_file.seek(self.node_size_in_bytes * (len(self.db) - 1))
            final_node = data_file.readline().split(';')
            final_node_id = int(final_node[3])
            final_node[3] = str(node_id)
            data_file.seek(self.node_size_in_bytes * self.id_dicts[node_id])
            data_file.write(';'.join(final_node))
            data_file.truncate(self.node_size_in_bytes * (len(self.db) - 1) - 1)
        del self.db[self.id_dicts[final_node_id]]
        del self.id_dicts[final_node_id]

    def change_node(self, updated_data: list):
        """

        :param updated_data: list which consist of 4 elements - updated values of fields for the node
        :return:
        """
        node_id = int(updated_data[3])
        self.db[self.id_dicts[node_id]] = [updated_data[0], int(updated_data[1]), float(updated_data[2]), int(updated_data[3])]
        if len(updated_data[0]) < self.field_lengths[0]:
            updated_data[0] += '^' * (self.field_lengths[0] - len(updated_data[0]))
        if len(updated_data[2]) != self.field_lengths[2]:
            updated_data[2] = '0' * (self.field_lengths[2] - len(updated_data[2])) + updated_data[2]
        with open(self.filename, 'r+') as data_file:
            data_file.seek(self.node_size_in_bytes * self.id_dicts[node_id])
            data_file.write(';'.join(updated_data))

