# Getting started with MLflow
1. Create folder for your project
2. Go to new folder and with right mouse click `Open with Code` (it opens Visual Studio Code)
3. Open terminal with `F1 -> Toggle Terminal`
4. Create Python virtual environment
    * when `virtualenvwrapper` installed, use:<br>
    `mkvirtualenv --python=C:\Python379\python.exe venv379_mlflow`
    * new virtual environment should be activated now
    * check Python version:<br>
    `python --version`
5. Install MLflow with `pip install mlflow`
6. Type `mlflow ui` for opening MLflow user interface
    * this should automatically open new terminal named `mlflow`
    * open `http://127.0.0.1:5000` where MLflow is serving on
    * this Youtube tutorial on [Getting started with mlflow for machine learning lifecycle](https://www.youtube.com/watch?v=w18a5kMV-co) is good starting point
7.  If you are now automatically moved to terminal `mlflow`, you can create new terminal to be able to install stuff in virtual environment again
8. Install Tensorflow with `pip install tensorflow`
9. Type `python tf_fashion_mnist.py` (or use `Code Runner` extension)
10. Go back to your browser `http://127.0.0.1:5000`, refresh if necessary, and see how content has been changed