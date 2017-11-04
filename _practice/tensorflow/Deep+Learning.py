
# coding: utf-8

# In[155]:


import tensorflow as tf
import numpy as np


# In[145]:


sess = tf.InteractiveSession()


# In[146]:


inputx = [[1,2,3],[2,4,5],[6,7,8]]
inputy = [[1],[0],[0]]


# In[147]:


x = tf.placeholder(shape=[None,3],dtype=tf.float32)
y = tf.placeholder(shape=[None,1],dtype=tf.float32)


# In[148]:


w1 = tf.Variable(tf.random_uniform([3,3], -1.0, 1.0),dtype=tf.float32)
b1 = tf.Variable(tf.zeros([3]),dtype=tf.float32)

L1 = tf.sigmoid(tf.matmul(x,w1)+b1)


# In[149]:


w2 = tf.Variable(tf.random_uniform([3,3], -1.0, 1.0),dtype=tf.float32)
b2 = tf.Variable(tf.zeros([3]),dtype=tf.float32)

L2 = tf.sigmoid(tf.matmul(L1,w2)+b2)


# In[150]:


w3 = tf.Variable(tf.random_uniform([3,1], -1.0, 1.0),dtype=tf.float32)
b3 = tf.Variable(tf.zeros([1]),dtype=tf.float32)

L3 = tf.matmul(L2,w3)+b3


# In[151]:


c = tf.reduce_mean(tf.square(L3 - y))


# In[152]:


train = tf.train.AdamOptimizer(learning_rate=0.1).minimize(c)


# In[153]:


sess.run(tf.global_variables_initializer())
for i in range(0,1000):
    _ , cost = sess.run([train,c],feed_dict={x:inputx, y:inputy})
    print(cost)


# In[154]:


sess.run([L3],feed_dict={x:inputx})

