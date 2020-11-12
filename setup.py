from setuptools import setup

setup(
    name             = "hfh",
    version          = "0.2",
    author           = "szsdk",
    scripts=["hfh"],
    install_requires = ["click", "IPython", "h5py"]
)
