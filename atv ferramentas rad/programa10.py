import wx

class Tela(wx.Frame):
    
    def __init__(self, parent, id=wx.ID_ANY,
                 title="Programa 10",
                 pos=wx.DefaultPosition, size=(400, 300)): # Tamanho reduzido pois não há imagem
        
        style = wx.DEFAULT_FRAME_STYLE
        name = "Tela"
        
        super(Tela, self).__init__(parent, id, title, pos,
                                   size, style, name)
        
        self.CenterOnScreen()
        self.panel = wx.Panel(self)
        
        # Componentes de texto, entrada e botão
        self.texto = wx.StaticText(self.panel, wx.ID_ANY, "Insira sua frase abaixo:", pos=(40, 60))
        self.campo = wx.TextCtrl(self.panel, size=(200, 25), pos=(40, 80))
        self.botao = wx.Button(self.panel, wx.ID_OK, pos=(40, 120))
        
        self.Bind(wx.EVT_BUTTON, self.imprime_frase)

    def imprime_frase(self, event):
        if not self.campo.IsEmpty():
            wx.MessageBox(self.campo.GetValue(), "Frase")

class Programa_Imagem(wx.App):
    
    def OnInit(self):
        self.frame = Tela(parent=None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

app = Programa_Imagem(False)
app.MainLoop()