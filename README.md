# GNSS data processing with Python

Welcome to the hands-on tutorials for GNSS data processing using Python and
Jupyter Notebooks/book

The tutorials are written using Jupyter books but can be executed independently
using tools such as Binder.

To do so, click on the following badge:  [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/rokubun/gnss_tutorials/HEAD)

Otherwise, keep reading 😉

## Developing notebooks

If you'd like to fork the project and modify the Notebooks, you can do so by
using a Jupyter Notebook Docker image

```bash
docker run -v `pwd`:/home/jovyan -p 9999:8888 -ti jupyter/datascience-notebook
```

Open the browser at this [url](http://127.0.0.1:9999).

You can open the notebooks and edit them from Jupyterhub. The changes will be
persistent, so they will modify your local folders.
