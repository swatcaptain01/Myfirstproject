#!/usr/bin/env python
# coding: utf-8

# In[ ]:


__all__ = ["ag_num","ashow"]
# 定义全局变量
ag_num = 10

# 定义函数
def ashow():
    print("我是一个函数")
    
# 定义类
class AStudent(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_msg(self):
        print(self.name, self.age) 
        
if __name__ == '__main__':
    ashow()

