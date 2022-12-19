import csv


class ToJSONAndYAML:

    @classmethod
    def run(cls):
        yaml_file = cls._init_yaml()
        json_file = cls._init_json()
        with open("./archivo.csv", 'r') as csv_file:
            csvreader = csv.reader(csv_file)
            for row in csvreader:
                cls._write_line_yaml(yaml_file, row)
                cls._write_line_json(json_file, row)
        cls._end_json(json_file)

    @staticmethod
    def _init_yaml():
        yaml_file = open('./archivo.yaml', 'w')
        yaml_file.write('---\n')
        yaml_file.write('cities:\n')
        return yaml_file

    @staticmethod
    def _write_line_yaml(file, row):
        prov, city, school, level = row[0].split(';')
        file.write(' province: ' + prov + '\n')
        file.write(' city: ' + city + '\n')
        file.write(' school: ' + school + '\n')
        file.write(' level: ' + level + '\n')

    @staticmethod
    def _init_json():
        json_file = open('./archivo.json', 'w')
        json_file.write('{\n')
        json_file.write('"cities":\n')
        json_file.write('[\n')
        return json_file

    @staticmethod
    def _write_line_json(file, row):
        prov, city, school, level = row[0].split(';')
        file.write('    { \n')
        file.write('        "province": " ' + prov + '", \n')
        file.write('        "city": " ' + city + '", \n')
        file.write('        "school": " ' + school + '", \n')
        file.write('        "level": " ' + level + '", \n')
        file.write('    }, \n')

    @staticmethod
    def _end_json(file):
        file.write(']\n')
        file.write('}\n')
