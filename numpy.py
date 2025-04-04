import streamlit as st
import numpy as np

st.title("Numpy Blog")

st.write('NumPy is the fundamental package for scientific computing in Python. '
'It is a Python library that provides a multidimensional array object, various derived '
'objects and an assortment of routines for fast operations on arrays, including mathematical, '
'logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, '
'basic linear algebra, basic statistical operations, random simulation and much more.')

st.markdown("""
### Numpy Arrays Vs Python Sequences
- NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically). Changing the size of an ndarray will create a new array and delete the original.
- The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory
- NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data. Typically, such operations are executed more efficiently and with less code than is possible using Python’s built-in sequences
- A growing plethora of scientific and mathematical Python-based packages are using NumPy arrays; though these typically support Python-sequence input, they convert such input to NumPy arrays prior to processing, and they often output NumPy arrays.
""")
st.subheader("Import numpy")
st.code("""
import numpy as np
""")

st.subheader("Creating Numpy Arrays")
st.text("This is simple numpy array")
st.code("""
# 1D array
array = np.array([1,2,3,4])
print(array)
#output
[1 2 3 4]
        """)

st.code("""
# 2D array
array = np.array([[1,2,3,4],[5,6,7,8]])
print(array)
#output
[[1 2 3 4]
 [5 6 7 8]]
        """)


st.code("""
# 3D array
array = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(array)
        """)
#output

st.subheader("dtype")
st.text("Describes how the bytes in the fixed-size block of memory corresponding to an array item should be interpreted")
st.code("""
#dtype
array = np.array([1,2,3,4],dtype = float)
""")
st.text("for more info..")
st.text("https://numpy.org/doc/stable/reference/arrays.dtypes.html")

st.subheader("arange function")
st.text("The numpy.arange() function in NumPy is used to create arrays with evenly spaced values within a specified interval")
st.code("""
# arange
array = np.arange(8)
print(array)
""")
st.text("for more info..")
st.text("https://numpy.org/doc/stable/reference/arrays.dtypes.html")

st.subheader("reshape function")
st.text("The numpy.reshape() function allows you to change the shape of an array without altering its data. This is useful for organizing data in different configurations.")
st.code("""
#reshape
np.arange(4).reshape((2,2))
""")
st.text("for more info..")
st.text("https://numpy.org/doc/stable/reference/generated/numpy.reshape.html")

st.subheader("ones function")
st.text("The np.ones function in NumPy is used to create a new array of given shape and type, filled with ones")
st.code("""
# ones
np.ones((3,4))
#output
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
""")

st.subheader("random function")
st.text("Create an array of the given shape and populate it with random samples from a uniform distribution over (0,1).")
st.code("""
# random
# both are same
np.random.rand(2,3)
np.random.ramdom((2,3))
#output
array([[ 0.14022471,  0.96360618],  #random
       [ 0.37601032,  0.25528411],  #random
       [ 0.49313049,  0.94909878]]) #random
""")

