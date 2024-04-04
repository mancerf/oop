class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.massage = "Файл item.csv поврежден"