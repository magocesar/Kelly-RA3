import os
import pythoncom
import win32com.client as win32

class EmailNc:
    def __init__(self, nome_proj, responsavel, rqa, dir_nc, len_nc, email_envio):
        self.nome_proj = nome_proj
        self.responsavel = responsavel
        self.rqa = rqa
        self.dir_nc = dir_nc
        self.len_nc = len_nc
        self.email_envio = email_envio
        pythoncom.CoInitialize()

    def mandarEmail(self):
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = self.email_envio
        mail.Subject = f"Não Conformidades - {self.nome_proj}"
        mail.Body = f"""
        Olá {self.responsavel},
        Segue em anexo o(s) arquivo(s) de Não Conformidades do projeto {self.nome_proj}.
        Responsável do Projeto: {self.responsavel}
        RQA do Projeto: {self.rqa}
        Atenciosamente,
        Equipe de Qualidade.
        """

        for file in os.listdir(self.dir_nc):
            #Notebook César
            #mail.Attachments.Add(f"C:\projetos\Kelly-RA3\\ExcelNc\\{self.nome_proj}\\{file}")

            #Computador César
           mail.Attachments.Add(f"C:\\Users\\cesin\\Desktop\\Kelly-RA3\\ExcelNc\\{self.nome_proj}\\{file}")
        
    def mandarNcEscalonada(self, nome_supervisor, email_supervisor):
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = email_supervisor
        mail.Subject = f"Não Conformidades - {self.nome_proj}"
        mail.Body = f"""
        Olá {nome_supervisor},
        Segue em anexo o(s) arquivo(s) de Não Conformidades do projeto {self.nome_proj}.
        Responsável do Projeto: {self.responsavel}
        RQA do Projeto: {self.rqa}
        Atenciosamente,
        Equipe de Qualidade.
        """

        for file in os.listdir(self.dir_nc):
            #Notebook César
            #mail.Attachments.Add(f"C:\projetos\Kelly-RA3\\ExcelNc\\{self.nome_proj}\\{file}")

            #Computador César
           mail.Attachments.Add(f"C:\\Users\\cesin\\Desktop\\Kelly-RA3\\ExcelNc\\{self.nome_proj}\\{file}")

        mail.Send()
        print("Email enviado com sucesso!")





    