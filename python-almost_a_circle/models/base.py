#!/usr/bin/python3
""" task 0 """
import json as j


class Base:
    ''' class '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, lst_obj):
        with open(cls.__name__+'.json', 'w') as f:
            if lst_obj is None:
                f.write("[]")
            else:
                new = [i.to_dictionary() for i in lst_obj]
                f.write(Base.to_json_string(new))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            n = cls(1, 1)
        else:
            n = cls(1)
        n.update(**dictionary)
        return n

    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name__+'.json', "r") as f:
                lst_d = Base.from_json_string(f.read())
                return [cls.create(**i) for i in lst_d]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, lst_obj):
        with open(cls.__name__+'.csv', 'w', newline='') as f:
            if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
            else:
                field_names = ["id", "size", "x", "y"]
            data = csv.DictWriter(f, fieldnames=field_names)
            for i in lst_obj:
                data.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        try:
            with open(cls.__name__+'.csv', "r") as f:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                data = csv.DictReader(f, fieldnames=field_names)
                lst_dic = [dict([k, int(v)] for k, v in d.items())
                              for d in data]
                return [cls.create(**d) for d in lst_dic]
        except IOError:
            return []

    @staticmethod
    def to_json_string(l_d):
        if l_d is None or len(l_d) == 0:
            return j.dumps([])
        else:
            return j.dumps(l_d)

    @staticmethod
    def from_json_string(js_str):
        if js_str is None or len(js_str) == 0:
            return []
        else:
            return j.loads(js_str)
