# This works however parameters/metrics are set to constant,
# so no interaction with metrics achievable during model training

# import platform
# print(platform.python_version())

# https://www.youtube.com/watch?v=w18a5kMV-co

import mlflow

if __name__ == "__main__":
    mlflow.set_experiment(experiment_name="experiment_video")
    with mlflow.start_run(run_name="test_run_name"):
        mlflow.log_param("b", 2)
        for a in range(10):
            mlflow.log_metric("a", a)
        
        mlflow.log_artifact("file.txt")