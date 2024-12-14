
class DictUtil:
    @staticmethod
    def sort_dict_by_value(d, reverse=True):
        return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=reverse)}

    @staticmethod
    def sort_dict_by_key(d, reverse=False):
        return {k: v for k, v in sorted(d.items(), key=lambda item: item[0], reverse=reverse)}

    @staticmethod
    def sort_dict_by_value_property(d, property_name, reverse=False):
        return {k: v for k, v in sorted(d.items(), key=lambda item: item[1][property_name], reverse=reverse)}
