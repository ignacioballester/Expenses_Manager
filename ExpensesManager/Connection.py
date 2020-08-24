import openpyxl


class Connection:
    def __init__(self, nombreArchivo, nombreHoja):
        self.nombreArchivo = nombreArchivo
        self.nombreHoja = nombreHoja
        self.wb = openpyxl.load_workbook(nombreArchivo)
        self.sheet = self.wb[nombreHoja]

    def save(self):
        self.wb.save('Movements2.xlsx')
