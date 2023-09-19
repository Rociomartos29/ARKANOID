import os
import pygame as pg
MAX_RECORDS = 10


class Records:
    filename = 'records.csv'
    base_dir = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(base_dir, 'data', filename)
    def __init__(self) :
        self.game_records = []
        self.data_path = os.path.join(os.path.dirname(self.path), 'data',  )
        self.file_path = os.path.join(self.data_path, self.filename)
        self.check_records_file()

    def check_records_file(self):
        if not os.path.isdir(self.data_path):
            os.makedirs(self.data_path)
        if not os.path.exists(self.file_path):
            self.reset()

        

    def insertar_records(self,nombre, puntuacion):
        pass

    def es_puntuacion_menor(self):
        pass

    def guardar(self):
        pass


    def cargar(self):
        pass


    def reset(self):
        self.game_records = []
        for cont in range(MAX_RECORDS):
            self.game_records.append(['-----', 0])
        self.guardar()
