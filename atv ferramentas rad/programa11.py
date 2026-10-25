import wx

class Tela(wx.Frame):
    
    def __init__(self, parent, id=wx.ID_ANY,
                 title="Programa 11",
                 pos=wx.DefaultPosition, size=(400, 400)):
        
        style = wx.DEFAULT_FRAME_STYLE
        name = "Tela"
        
        super(Tela, self).__init__(parent, id, title, pos,
                                   size, style, name)
        
        self.CenterOnScreen()
        self.panel = wx.Panel(self)
        
        # --- Componentes da Interface (Slide 1) ---
        textoUsuario = wx.StaticText(self.panel, wx.ID_ANY, "Usuário: ")
        campoUsuario = wx.TextCtrl(self.panel, wx.ID_ANY, value="user")
        
        textoSenha = wx.StaticText(self.panel, wx.ID_ANY, "Senha: ")
        # style=wx.TE_PASSWORD mascara os caracteres digitados
        campoSenha = wx.TextCtrl(self.panel, wx.ID_ANY, value="password", style=wx.TE_PASSWORD)
        
        botaoAcessar = wx.Button(self.panel, wx.ID_ANY, "Acessar")
        botaoCancelar = wx.Button(self.panel, wx.ID_ANY, "Cancelar")
        
        # --- Inicialização dos Sizers ---
        PrincipalSizer = wx.BoxSizer(wx.VERTICAL)
        UsuarioSizer = wx.BoxSizer(wx.HORIZONTAL)
        SenhaSizer = wx.BoxSizer(wx.HORIZONTAL)
        BotaoSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # --- Adicionando elementos aos Sizers (Slide 2) ---
        UsuarioSizer.Add(window=textoUsuario, proportion=0, flag=wx.ALL, border=5)
        UsuarioSizer.Add(window=campoUsuario, proportion=0, flag=wx.ALL, border=5)
        
        SenhaSizer.Add(window=textoSenha, proportion=0, flag=wx.ALL, border=5)
        SenhaSizer.Add(window=campoSenha, proportion=0, flag=wx.ALL, border=5)
        
        BotaoSizer.Add(window=botaoAcessar, proportion=0, flag=wx.ALL, border=5)
        BotaoSizer.Add(window=botaoCancelar, proportion=0, flag=wx.ALL, border=5)
        
        # --- Organização do Sizer Principal (Slide 2) ---
        PrincipalSizer.Add(UsuarioSizer, 0, wx.ALIGN_CENTER_HORIZONTAL)
        PrincipalSizer.Add(SenhaSizer, 0, wx.ALIGN_CENTER_HORIZONTAL)
        PrincipalSizer.Add(BotaoSizer, 0, wx.ALIGN_CENTER_HORIZONTAL)
        
        # --- Configuração final do Layout ---
        self.panel.SetSizer(PrincipalSizer)
        self.panel.Fit()
        self.Fit()

class Programa_Imagem(wx.App):
    
    def OnInit(self):
        self.frame = Tela(parent=None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

app = Programa_Imagem(False)
app.MainLoop()
