# https://docs.microsoft.com/en-us/azure/databricks/applications/mlflow/quick-start-python
# This is well described doc how to use automatic logging with `mlflow.<ml_framework>.autolog()`
# Using this approach you get for example `saved_model.pb` in example location:
# your_project_location\mlruns\10\3ef10256f1d14af38820373292059026\artifacts\model\data 

# https://databricks.com/blog/2019/08/19/mlflow-tensorflow-open-source-show.html
# Here there are two options for logging:
# 1. using `callback` with log statements (requires more code efforts) AND
# 2. using automatic logging and you only need to add function call `mlflow.<ml_framework>.autolog()`

# TensorFlow and tf.keras
import tensorflow as tf

# MLflow is an open source platform for managing the end-to-end machine learning lifecycle
import mlflow

# Helper libraries
# import numpy as np
# import matplotlib.pyplot as plt

print(tf.__version__)

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

train_images = train_images / 255.0
test_images = test_images / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# https://docs.microsoft.com/en-us/azure/databricks/applications/mlflow/quick-start-python
# MLflow provides mlflow.<framework>.autolog() APIs to automatically log training code written in many ML frameworks.
# You can call this API before running training code to log model-specific metrics, parameters, and model artifacts.
# Use `import mlflow.tensorflow` and `mlflow.tensorflow.autolog()`` if using tf.keras
mlflow.tensorflow.autolog()
mlflow.set_experiment(experiment_name="tf_fashion_mnist_5")

model.fit(train_images, train_labels, epochs=3)