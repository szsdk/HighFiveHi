# HighFiveHi

- `IPython`, good!
- HDF5, good!
- `h5py`, good!

But when you use `h5py` to view some HDF5 files in `IPython`, every time, you need to type some many
lines for just viewing keys like think
```
# ipython
In [1]: import h5py

In [2]: f = h5py.File('t.h5', 'r')

In [3]: f.keys()
Out[3]: <KeysViewHDF5 ['aa']>

In [4]: f.close()
```
So painful !!! 

`HighFiveHi` is a small tool to simplify this process. Now, all you need to do is
```
# hfh t.h5

In [1]: hf.keys()
Out[1]: <KeysViewHDF5 ['aa']>
```
No more extra lines !!!

## Installation
```
pip install .
```

## Usage

Open one hdf5 file.
```
# hfh one.h5

In [1]: hf
Out[1]: <HDF5 file "one.h5" (mode r)>
```
The variable `hf` is the handle for the input hdf5 file. The read-only mode is used as the default
for file handles.


You can set the file mode by `--mode`/`-m`. For example,
```
# hfh -m a one.h5

In [1]: hf
Out[1]: <HDF5 file "one.h5" (mode r+)>
```

When multiple files are opened, `hf` becomes a list of all file handles.
```
# hfh -m a one.h5 two.h5
In [1]: hf
Out[1]: [<HDF5 file "one.h5" (mode r+)>, <HDF5 file "two.h5" (mode r+)>]
```

Also, you could pass scripts from command line. These scripts would be run automatically, which
is similar to the `%run` magic command in `IPython`.
```
# cat t.py
def g():
    pass

# hfh -m a one.h5 t.py
In [1]: hf, g
Out[1]: (<HDF5 file "one.h5" (mode r+)>, <function g()>)
```
