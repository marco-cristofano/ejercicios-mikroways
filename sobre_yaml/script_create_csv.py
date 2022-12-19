class CreateCSV:

    @classmethod
    def run(cls):
        csv_file = cls._init_csv()
        cls._write_lines(csv_file)

    @staticmethod
    def _init_csv():
        csv_file = open('./archivo.csv', 'w')
        return csv_file

    @staticmethod
    def _write_lines(file):
        for row in range(1, 50):
            index = str(row)
            prov = 'provincia' + index
            city = 'city' + index
            school = 'school' + index
            level = 'level' + index
            line = '{};{};{};{} \n'.format(prov, city, school, level)
            file.write(line)
