import pytest
class Todo:
    def __init__(self,code_id:int, description:str , title:str):
        self.code_id=code_id
        self.description:str=description
        self.title:str=title
        self.completed:bool=False
        self.tags:list[str]=[]
    def mark_completed(self,completed:bool):
        self.completed:bool=True
    def add_tag(self,tag:str):
        if tag not in self.tags:
            self.tags.append(tag)
    def __str__(self):
        return f"{self.code_id} - {self.title}"
class TodoBook:
    todos={int:Todo}
    def __init__(self):
        self.todos={}
    def add_todo(self,title:str, description:str)->int:
        code_id = len(self.todos)+1
        self.todos[code_id]=Todo(code_id,description,title)
        return code_id    
