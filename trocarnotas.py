

from tkinter import *
class Trocar:
    valor=0.00
    nota50, nota20, nota10, nota05, nota02, nota01=0,0,0,0,0,0
    def __init__(self, root):
        self.root=root
        self.root.title('Trocar de Notas')

        self.entrada=StringVar()

        Label(self.root, text='Valor: ', fg='red').grid(row=1, column=1, sticky=E+W, pady=3)
        
        self.ent=Entry(self.root, textvariable=self.entrada, width=15)
        self.ent.focus_force()
        self.ent.grid(row=1, column=2, sticky=E+W, pady=3)
        self.ent.bind('<Return>', self.calcula)

        Label(self.root, text='Notas de R$ 50,00: ').grid(row=3, column=1, sticky=W, pady=2)
        Label(self.root, text='Notas de R$ 20,00: ').grid(row=4, column=1, sticky=W, pady=2)
        Label(self.root, text='Notas de R$ 10,00: ').grid(row=5, column=1, sticky=W, pady=2)
        Label(self.root, text='Notas de R$  5,00: ').grid(row=6, column=1, sticky=W, pady=2)
        Label(self.root, text='Notas de R$  2,00: ').grid(row=7, column=1, sticky=W, pady=2)
        Label(self.root, text='Notas de R$  1,00: ').grid(row=8, column=1, sticky=W, pady=2)
        Label(self.root, text='Valor Total').grid(row=10, column=1, sticky=E+W, pady=3)

        self.msg50=Label(self.root, text='0', fg='blue')
        self.msg50.grid(row=3, column=2, sticky=W, pady=2)
        self.msg20=Label(self.root, text='0', fg='blue')
        self.msg20.grid(row=4, column=2, sticky=W, pady=2)
        self.msg10=Label(self.root, text='0', fg='blue')
        self.msg10.grid(row=5, column=2, sticky=W, pady=2)
        self.msg05=Label(self.root, text='0', fg='blue')
        self.msg05.grid(row=6, column=2, sticky=W, pady=2)
        self.msg02=Label(self.root, text='0', fg='blue')
        self.msg02.grid(row=7, column=2, sticky=W, pady=2)
        self.msg01=Label(self.root, text='0', fg='blue')
        self.msg01.grid(row=8, column=2, sticky=W, pady=2)

        self.total=Label(self.root, text='0')
        self.total.grid(row=10, column=2, sticky=W, pady=3)

    def calcula(self, evento):
        x=int(self.entrada.get())
        self.valor+=float(x)
        while x>=50:
            self.nota50+=1
            x-=50
        while x>=20:
            self.nota20+=1
            x-=20
        while x>=10:
            self.nota10+=1
            x-=10
        while x>=5:
            self.nota05+=1
            x-=5
        while x>=2:
            self.nota02+=1
            x-=2
        while x==1:
            self.nota01+=1
            x-=1
        self.msg50['text']=self.nota50
        self.msg20['text']=self.nota20
        self.msg10['text']=self.nota10
        self.msg05['text']=self.nota05
        self.msg02['text']=self.nota02
        self.msg01['text']=self.nota01
        
        self.total['text']=self.valor

        self.limpa()

    def limpa(self):
        self.entrada.set('')

loop=Tk()
Trocar(loop)
loop.mainloop()
