# Create a multi-tab matrix

It is possible to use the writeRow() method to create a
matrix based on an rowBuffer. The writeRow(row index, rowBuffer, dataType)
method takes the following attributes:

â¢ row index = the index of the row to be written

â¢ rowBuffer = the buffer row array from which to write the
row, this needs to be a CubeAPI array object

â¢ dataType = the CubeMatrixDataType of rowBuffer

The below example shows how to undertake this for a
multi-tab matrix, by using two Python dictionaries, with matrix names and
buffer arrays, and defining a matrix file with multiple matrices with random
values between 0 and 10.

```
import random
import contextlib
from pathlib import Path
import cubepy as cp

new_mt = "output/random_matrix_1000_multi.cube-matrix"
zones = 1000
n_matrices = 3


random.seed(1234)

with contextlib.suppress(FileNotFoundError):
     Path(new_mt).unlink()  # pathlib to remove

mt = cp.CubeMatrixFile(new_mt)
mt.openWithCreate(zones)

matrix_dict = {}  # empty dictionary to store the matrix names
buffer_dict = {}  # empty dictionary to store the buffer arrays
for mat in range(n_matrices):
    mat_name = f"mat_{mat + 1}"
    matrix_dict[f"mat_{mat + 1}"] = mt.addMatrix(mat_name)
    buffer_dict[f"mat_{mat + 1}"] = cp.DoubleArray(zones)

for i in range(zones):
    for mat in range(n_matrices):
        for j in range(zones):
            buffer_dict[f"mat_{mat + 1}"][j] = random.random() * 10  
	    # array for the entire row
       	    # random float uniformly in the semi-open range [0.0, 1.0),
      	    # times 10 to have a number between 0 (excl) and 10
        matrix_dict[f"mat_{mat + 1}"].writeRow(i, buffer_dict[f"mat_{mat + 1}"])
mt.close()
```

Alternatively, the writeNumpyArrayToMatrix() method can be
used to directly access a NumPy array. The argument of this method is the NumPy
array with zones x zones dimension. The below example shows how to undertake
this for a multi-tab matrix, by using a Python dictionary, with matrix names,
and defining a matrix file with multiple matrices with random values between 0
and 10.

```
import contextlib
from pathlib import Path
import numpy as np
import cubepy as cp

new_mt = "output/random_matrix_1000_multi_np.cube-matrix"
zones = 1000
n_matrices = 3

np.random.seed(1234)

with contextlib.suppress(FileNotFoundError):
     Path(new_mt).unlink()  # pathlib to remove

mt = cp.CubeMatrixFile(new_mt)
mt.openWithCreate(zones)

matrix_dict = {}  # empty dictionary to store the matrix names
for mat in range(n_matrices):
    mat_name = f"mat_{mat + 1}"
    matrix_dict[f"mat_{mat + 1}"] = mt.addMatrix(mat_name)

    mt_npArray = 10 * np.random.random((zones, zones))  
    # generating a numpy array with random numbers
    matrix_dict[f"mat_{mat + 1}"].writeNumpyArrayToMatrix(mt_npArray)

mt.close()
```

**Parent topic:** [Application of the
Matrix API with CubePy](GUID-AFCFCBB1-51C9-4D88-8C62-C2DB08CD7F15.html)

|
|  |
|
|  |
