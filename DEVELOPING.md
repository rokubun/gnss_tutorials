# Developing notes

This section includes some hints and tips to develop the notebooks present in this
repository

If you'd like to fork the project and modify the Notebooks, you can do so by
using a Jupyter Notebook Docker image

```bash
docker run -v `pwd`:/home/jovyan -p 9999:8888 -ti jupyter/datascience-notebook
```

Open the browser at this [url](http://127.0.0.1:9999).

You can open the notebooks and edit them from Jupyterhub. The changes will be
persistent, so they will modify your local folders.
