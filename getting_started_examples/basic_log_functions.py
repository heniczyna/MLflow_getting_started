# It does not work as `trainings_steps` or `accuracy` are not defined
# however it might be useful to see basic MLflow APIs
# `export_path` seems to not working as well
# just leaves as it is for reference

# 2 https://medium.com/analytics-vidhya/mlflow-basic-logging-functions-e16cdea047b
# 3 https://medium.com/analytics-vidhya/mlflow-logging-for-tensorflow-37b6a6a53e3c

import mlflow

export_path = "artifacts"

if __name__ == "__main__":
    mlflow.start_run()
    # the model code
    mlflow.log_param('training_steps', training_steps)
    mlflow.log_metric('accuracy', accuracy)
    mlflow.log_artifacts(export_path, "model")
    mlflow.end_run()