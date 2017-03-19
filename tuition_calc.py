
try:
    import wx
except ImportError:
    raise ImportError,"You need wxPython module to run this program - get it from http://www.wxpython.org/ "



class Frame(wx.Frame):

    
    def __init__(self, image, parent=None, id=-1,
        pos=wx.DefaultPosition):
        wx.Frame.__init__(self, parent, id, title, pos, size)
           
            
class simpleapp_wx(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.parent = parent
        self.SetBackgroundColour('white')
        self.initialize()
        
            
    def initialize(self):
        sizer = wx.GridBagSizer()


        image = wx.Image('uislogo.jpg', wx.BITMAP_TYPE_JPEG)
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)
        sizer.Add( self.bmp, (0,0),(1,20), wx.EXPAND )


        calchead= wx.StaticText(self, -1, "UIS Graduate Tuition Calculator", (75, 225))
        font = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        calchead.SetFont(font)
        sizer.Add( calchead, (2,0),(1,20), wx.ALIGN_CENTER_HORIZONTAL )



        self.plsenter = wx.StaticText(self,-1,label=u"Select Number of Hours:")
        sizer.Add(self.plsenter,(3,5),(1,1),wx.EXPAND )

       
        self.spin = wx.SpinCtrl(self, -1, "", size=(40,20))
        self.spin.SetRange(1,12)
        self.spin.SetValue(4) 
        sizer.Add(self.spin,(3,7), (1,1),  wx.EXPAND )

         
        self.ckcs = wx.CheckBox(self, -1, "Computer Science?")
        sizer.Add(self.ckcs, (3,10),(1,4), wx.EXPAND)
        

        button = wx.Button(self,-1,label="Calculate")
        sizer.Add(button, (5,0), (1,20), wx.ALIGN_CENTER_HORIZONTAL )
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick, button)

        
        self.totalcost = wx.StaticText(self,-1,label=u'')
        self.totalcost.SetForegroundColour(wx.BLUE)
        totalfont = wx.Font(14, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        self.totalcost.SetFont(totalfont)
        sizer.Add( self.totalcost, (7,0),(1,5), wx.ALIGN_CENTER_HORIZONTAL )
        

        sizer.AddGrowableCol(0)
        self.SetSizerAndFit(sizer)
        self.SetSizeHints(-1,self.GetSize().y,-1,self.GetSize().y );
        self.spin.SetFocus()
        self.Show(True)

    def OnButtonClick(self,event):  
        self.totalcost.SetLabel( "Total Tuition, Fees, and Asessments: $" + str(self.Tuition(self.spin.GetValue())) )
 
         
    def Tuition(self,hours): 
        if hours>= 9: # fulltime
            assessment = 174.00
            assperhour  = 18.20
        else:
            assessment = 108.00
            assperhour = 18.20 #in case this number is ever different from fulltime in the future

        gradrate = 352.50
        onlinefee = 25

        if self.ckcs.GetValue():
            cost = hours*gradrate + (onlinefee * hours) + assessment + (hours*assperhour) + (hours*40.75)
        else:
            cost = hours*gradrate + (onlinefee * hours)+ assessment + (hours*assperhour) 

        return format(cost, '.2f')
    
      
if __name__ == "__main__":
    app = wx.App()
    frame = simpleapp_wx(None,-1,'CSC 470 Final: Tuition Calculator')
    app.MainLoop()
