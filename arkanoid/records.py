import os
import csv
MAX_RECORDS = 10


class Records:
    filename = 'records.csv'
    base_dir = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(base_dir, 'data', filename)
    def __init__(self) :
        self.game_records = []
        self.data_path = os.path.join(os.path.dirname(self.path), 'data')
        self.file_path = os.path.join(self.data_path, self.filename)
        self.check_records_file()
        self.cargar()

    def check_records_file(self):
        if not os.path.isdir(self.data_path):
            os.makedirs(self.data_path)
            print('No existe pero lo he creado')
        if not os.path.exists(self.file_path):
            self.reset()

        

    def insertar_records(self,nombre, puntuacion):
        self.game_records.append([nombre, puntuacion])
        self.game_records.sort(key = lambda item: item[1], reverse= True)
        self.game_records = self.game_records[:MAX_RECORDS]
        
        
        
        
        self.guardar()

    def es_puntuacion_menor(self):
        return self.game_record[-1]

    def guardar(self):
        '''LECTOR = open(self.file_path, mode = 'w')
        LECTOR.close()'''
        with open(self.file_path, mode = 'w') as records_file:
            writer = csv.writer(records_file)
            writer.writerow(('Nombre', 'Puntos'))
            writer.writerows(self.game_records)
            


    def cargar(self):
        with open(self.file_path, mode = 'r') as records_file:
            reader = csv.reader(records_file)
            contador = 0
            self.game_record = []
            for linea in reader:
                contador += 1
                if contador == 1:
                    continue
                self.game_records.append([linea[0], int(linea[1])])


    def reset(self):
        self.game_records = []
        for cont in range(MAX_RECORDS):
            self.game_records.append(['-----', 0])
        self.guardar()
