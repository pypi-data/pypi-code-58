# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/04_html.ipynb (unless otherwise specified).

__all__ = ['DOM', 'list_group', 'col_sm', 'list_group_kv', 'JS', 'JS_file']

# Cell
from IPython.display import HTML

class DOM:
    def __init__(self,txt,tag,kwargs = dict()):
        self.txt = txt
        self.tag = str(tag).lower()
        self.attrs = kwargs
        self.refresh_attr()

    @staticmethod
    def extend(text,tag,**kwargs):
        attributes =(" ".join(f'{k}="{v}"' for k,v in kwargs.items()))
        attributes=" "+attributes if attributes else attributes
        start = f"<{tag}{attributes}>"
        inner = f"{text}"
        end = f"</{tag}>"
        text = f"{start}{inner}{end}"
        return start,inner,end

    def refresh_attr(self):
        self.start,self.inner,self.end = self.extend(self.txt,self.tag,**self.attrs)

    def __mul__(self,new_tag):
        assert type(new_tag)==str
        return DOM(self.text,new_tag)

    def __add__(self,dom):
        return self.text+dom.text

    def __repr__(self):
        return f"{self.start}{self.inner}{self.end}"

    def __getitem__(self,k):
        return self.attrs[k]

    def __setitem__(self,k,v):
        self.update({k,v})

    def __call__(self):
        self.display()

    @property
    def text(self):
        return str(self)

    def append(self,subdom):
        self.inner = self.inner+str(subdom)
        return self

    def update(self,dict_):
        self.attrs.update(dict_)
        self.refresh_attr()
        return self

    def display(self):
        display(HTML(self.text))

# Cell
def list_group(iterable):
    ul = DOM("","ul",{"class":"list-group"})
    for i in iterable:
        li = DOM(i,"li",{"class":"list-group-item"})
        ul.append(li)
    return ul

# Cell
import math
def col_sm(iterable,portions = None,):
    if portions == None:
        portions = [math.floor(12/len(iterable)),]* len(iterable)
    row = DOM("","div",{"class":"row"})
    for i,p in zip(iterable,portions):
        row.append(DOM(i,"div",{"class":f"col-sm-{p}"}))
    return row


# Cell
def list_group_kv(data):
    result = []
    for k,v in data.items():
        row = DOM("","div",{"class":"row"})
        row.append(DOM(f"{k}","strong",{"class":"col-sm-5"}))\
            .append(DOM(f"{v}","span",{"class":"col-sm-7"}))
        result.append(row)
    return list_group(result)

# Cell
def JS(code):
    DOM(code,"script",)()

def JS_file(path):
    """
    load javascript file
    """
    with open(path,"r") as f:
        DOM(f.read(),"script")()