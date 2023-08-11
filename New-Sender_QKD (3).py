#!/usr/bin/env python
# coding: utf-8

# In[3]:


import qiskit


# In[4]:


from qiskit import*


# In[5]:


from qiskit.tools.visualization import plot_bloch_multivector


# In[6]:


qr=QuantumRegister(6)


# In[7]:


cr=ClassicalRegister(6)


# In[8]:


circuit=QuantumCircuit(qr,cr)


# In[9]:


circuit.h(0)


# In[10]:


simulator=Aer.get_backend('statevector_simulator')


# In[11]:


result=execute(circuit,backend=simulator).result()


# In[12]:


statevector=result.get_statevector()


# In[13]:


print(statevector)


# In[14]:


circuit.h(1)


# In[15]:


simulator=Aer.get_backend('statevector_simulator')


# In[16]:


result=execute(circuit,backend=simulator).result()


# In[17]:


statevector=result.get_statevector()


# In[18]:


print(statevector)


# In[19]:


matplotlib inline


# In[ ]:





# In[20]:


circuit.h(2)


# In[21]:


circuit.draw(output='mpl')


# In[22]:


circuit.draw(output='mpl')


# In[23]:


circuit.h(3)


# In[24]:


circuit.h(4)


# In[25]:


circuit.h(5)
circuit.measure([0,1,2,3,4,5],[0,1,2,3,4,5])


# In[26]:


circuit.draw(output='mpl')


# In[ ]:




