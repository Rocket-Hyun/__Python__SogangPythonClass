
# coding: utf-8

# In[46]:


import tensorflow as tf
import numpy as np


# In[47]:


sess = tf.InteractiveSession()


# In[48]:


x = tf.constant([1,2,3],dtype='float32')
y = tf.constant([1,2,3],dtype='float32')


# In[49]:


w = tf.Variable(tf.random_uniform([1], -1.0, 1.0), dtype='float32')
b = tf.Variable(tf.random_uniform([1], -1.0, 1.0), dtype='float32')


# In[50]:


h = (w*x) + b


# In[51]:


c = tf.reduce_mean(tf.square(h-y))


# In[60]:


train = tf.train.AdamOptimizer(learning_rate=1).minimize(c)


# In[59]:


init = tf.global_variables_initializer()
sess.run(init)

for i in range(1,1000):
    sess.run(train)
    print('w:', sess.run(w))
    print('b:', sess.run(b))


# In[ ]:




