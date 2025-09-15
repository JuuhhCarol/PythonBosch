import numpy as np

lista=[1,2,3]
# print(lista)
# print(type(lista))

listaP=["Ve",1]
array=np.array(listaP)
# print(array)
# print(type(array))

matriz=[[1,2,3],[4,5,6],[7,8,9]]
#print(matriz)

mat_numpy=np.array(matriz)
#print(mat_numpy)

#print(array.shape)
#print(mat_numpy.shape)
#print(array.ndim)
#print(mat_numpy.ndim)

my_array=np.array([1,2,3,4,5,6,7,8,])
#print(my_array)

print('\n',my_array.reshape((2,4)))
#np.reshape(my_array,(2,4))

array=np.arange(20,30,2)
# print(array)

array=np.arange(10).reshape((2,5))
# print(array)
# print(np.zeros((2,2)))
# print(np.random.randint(0,10,10))


num=[1,2,3,4,5,6,7,8]
print('num',array.argmax())
print('num',array.argmin())
print('num',array.min())
print('num',array.max())
print('num',array.mean())
print('num',array.std())
print('num',array.var())
print(np.median())