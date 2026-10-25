import wx
import os

class Tela(wx.Frame):
    
    def __init__(self, parent, id=wx.ID_ANY,
                 title="Programa com imagem",
                 pos=wx.DefaultPosition, size=(800,800)):
        
        style = wx.DEFAULT_FRAME_STYLE
        name = "Tela"
        
        super(Tela, self).__init__(parent, id, title, pos,
                                   size, style, name)
        
        self.CenterOnScreen()
        self.panel = wx.Panel(self)
        caminho_usuario = os.path.expanduser('~')
        caminho_imagem = os.path.join(caminho_usuario, "Downloads", "nova pasta", "IMG-20260818-WA0055.jpg")
        bitmap = wx.Bitmap(caminho_imagem, wx.BITMAP_TYPE_JPEG)
        self.bitmap = wx.StaticBitmap(self.panel, bitmap=bitmap)

class Programa_Imagem(wx.App):
    
    def OnInit(self):
        self.frame = Tela(parent=None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

app = Programa_Imagem(False)
app.MainLoop()

