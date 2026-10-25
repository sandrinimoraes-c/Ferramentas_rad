import wx

class Primeiro_Exemplo(wx.App):

    def OnInit(self):
        tela = wx.Frame(parent=None, title="Minha primeira tela")
        tela.Show()
        return True
    
programa = Primeiro_Exemplo()
programa.MainLoop()