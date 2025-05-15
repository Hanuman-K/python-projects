d={1:'hanu',2:'sonu',3:'monu'}
print(d)
print(d[3])
print(d.get(1))
print(d.get(4))
print(d.get(1,'not found'))
print(d.get(4,'not found'))
print(d.keys())
print(d.values())

a=['hanu','monu','sonu']
b=['kana','mana','pana']

c=dict(zip(a,b))
print(c)

print(c['hanu'])

c['kira']='mira' #to add
print(c)

del c['monu']
print(c)

c.pop('kira')
print(c)

pro={'js':'atom','cs':'vs','python':['pycharm','sublime'],'java':{'jse':'netbeans','jee':'eclipse'}}
print(pro)
print(pro['js'])
print(pro['python'])
print(pro['python'][1])
print(pro['java'])
print(pro['java']['jee'])

print(type(pro))
