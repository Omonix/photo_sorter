import os, time
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo, showwarning

screen = Tk()
screen.geometry('300x500')
screen.title('Ranger')
screen['bg'] = '#191919'
screen.resizable(height=False, width=False)

month = {'jan': '01janvier', 'feb': '02fevrier', 'mar': '03mars', 'apr': '04avril', 'may': '05mai', 'jun': '06juin', 'jul': '07juillet', 'aug': '08aout', 'sep': '09septembre', 'oct': '10octobre', 'nov': '11novembre', 'dec': '12decembre'}
def lb_sort(fromer, to):
    if fromer != '' and to != '':
        for i in os.listdir(fromer):
            before = time.time()
            element = time.ctime(os.path.getmtime(f'{fromer}\\{i}')).split(' ')
            if os.path.exists(f'{to}\\{element[-1]}'):
                if os.path.exists(f'{to}\\{element[-1]}\\{month[element[1].lower()]}'):
                    os.rename(f'{fromer}\\{i}', f'{to}\\{element[-1]}\\{month[element[1].lower()]}\\{i}')
                else:
                    os.mkdir(f'{to}\\{element[-1]}\\{month[element[1].lower()]}')
                    return
            else:
                os.mkdir(f'{to}\\{element[-1]}')
                return
    else:
        showwarning(message='Invalid URL')
        return
    second = time.time() - before
    milliseconds = second * 1000
    showinfo(message=f'Sorting finished in {round(second)} seconds - {round(milliseconds, 4)} milliseconds')
    from_url.set('')
    to_url.set('')
    return
def lb_open_folder(opener):
    if opener:
        from_url.set(fd.askdirectory())
    else:
        to_url.set(fd.askdirectory())

from_url = StringVar()
to_url = StringVar()
Label(screen, text='Mixed photo directory', font=("Helvetica", 20),  fg='#F62FB0', bg='#191919').pack(pady=20)
Entry(screen, textvariable=from_url, font=("Helvetica", 10), fg='#F62FB0', bg='#191919', width=25).place(x=15, y=70)
Button(screen, text='Open folder', font=("Helvetica", 10), fg='#F62FB0', bg='#191919', command=lambda: lb_open_folder(True)).place(x=210, y=66)
Label(screen, text='Sorted photo directory', font=("Helvetica", 20),  fg='#F62FB0', bg='#191919').pack(pady=20)
Entry(screen, textvariable=to_url, font=("Helvetica", 10), fg='#F62FB0', bg='#191919', width=25).place(x=15, y=147)
Button(screen, text='Open folder', font=("Helvetica", 10), fg='#F62FB0', bg='#191919', command=lambda: lb_open_folder(False)).place(x=210, y=144)
Button(screen, text='Sort', font=("Helvetica", 25), fg='#f62fb0', bg='#191919', command=lambda: lb_sort(from_url.get(), to_url.get())).place(x=120, y=400)

screen.mainloop()