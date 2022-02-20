#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[24]:

#Ingresan valores de 5 pokemones que tendrá el usuario
df = {'Nombre':['Zapdos', 'Togepi', 'Charizard', 'Totodile', 'Mew'], 'Numero':['145', '175', '6', '158', '151'], 'Tipo':['Eléctrico', 'Hada', 'Fuego', 'Agua', 'Psiquico'], 'altura':['1.6', '0.3', '1.7', '0.6', '0.4'], 'Peso':['52.6', '1.5', '92', '9.5', '4'], 'Sexo':['Femenino', 'Femenino', 'Masculino', 'Masculino', 'Desconocido'], 'Habilidad':['Presion', 'Entusiasmo', 'Mar llamas', 'Torrente', 'Sincronía']}


# In[25]:


df = pd.DataFrame(df)
#Se crea el json con los datos de los pokemones
df.to_json('pokemones.json')
# In[26]:


df





# %%
