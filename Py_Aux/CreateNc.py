import os
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.styles import Alignment

class CreateNc:
    def __init__(self, perguntas, respostas, justificativas, gravidade, nome_proj, responsavel_proj, rqa_proj):
        self.perguntas = perguntas
        self.respostas = respostas
        self.justificativas = justificativas
        self.gravidade = gravidade
        self.nome_proj = nome_proj
        self.responsavel_proj = responsavel_proj
        self.rqa_proj = rqa_proj
        self.len_nc = 0
        self.dir = None

    def start(self):

        if 0 not in self.respostas:
            return None, None

        if self.createFolder() == False:
            return False, False

        self.CreateExcel()

        return self.dir, self.len_nc
        
    def createFolder(self):
        self.dir = f"./ExcelNc/{self.nome_proj}"

        try:
            if os.path.exists(self.dir):
                for file in os.listdir(self.dir):
                    os.remove(f"{self.dir}/{file}")
            else:
                os.makedirs(self.dir)
        except:
            print("Error")
            return False
    
    def CreateExcel(self):
        #Selecionar Perguntas de Foram respondidas com Não

        perguntas_nc = []
        respostas_nc = []
        justificativas_nc = []
        gravidade_nc = []

        for i in range(len(self.respostas)):
            if(self.respostas[i] == 0):
                self.NcCreate(self.perguntas[i], self.justificativas[i], self.gravidade[i])
                self.len_nc += 1
                
    def NcCreate(self, pergunta, justificativa, gravidade):
        wb = Workbook()
        ws = wb.active

        ws.append(["Nome do Projeto", "Responsável do Projeto", "RQA do Projeto", "Pergunta", "Resposta", "Gravidade", "Justificativa"])
        ws.append([self.nome_proj, self.responsavel_proj, self.rqa_proj, pergunta, 'Não', gravidade, justificativa])

        tab = Table(displayName="Table1", ref=f"A1:G2")

        style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
                                showLastColumn=False, showRowStripes=True, showColumnStripes=False)
        
        tab.tableStyleInfo = style

        ws.add_table(tab)

        for i in range(1, 3):
            ws[f'A{i}'].alignment = Alignment(wrap_text=True)
            ws[f'B{i}'].alignment = Alignment(wrap_text=True)
            ws[f'C{i}'].alignment = Alignment(wrap_text=True)
            ws[f'D{i}'].alignment = Alignment(wrap_text=True)
            ws[f'E{i}'].alignment = Alignment(wrap_text=True)
            ws[f'F{i}'].alignment = Alignment(wrap_text=True)
            ws[f'G{i}'].alignment = Alignment(wrap_text=True)

        ws.column_dimensions['A'].width = 40
        ws.column_dimensions['B'].width = 12
        ws.column_dimensions['C'].width = 40
        ws.column_dimensions['D'].width = 40
        ws.column_dimensions['E'].width = 12
        ws.column_dimensions['F'].width = 12
        ws.column_dimensions['G'].width = 40

        wb.save(f"{self.dir}/Nc{self.len_nc + 1}.xlsx")

