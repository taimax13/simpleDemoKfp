# Kubeflow Pipelines Demo: Simple Pipeline
Author: Talex Maxim

This project demonstrates how to create, compile, and run a simple pipeline using Kubeflow Pipelines.

## Prerequisites

- Python 3.7+
- pip (Python package installer)
- Access to a Kubeflow Pipelines installation (local or remote)

## Setup

1. Clone this repository or create a new directory for the project.

2. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
   
3. Install the required packages:

    ```bash
    pip install -r requirements.txt

 ## Project Structure

- `pipeline.py`: The main script that defines and compiles the pipeline.
- `simple_pipeline.yaml`: The compiled pipeline file (will be generated when you run the script).

## Pipeline Description

This simple pipeline consists of two components:

1. `print_component`: Prints a welcome message.
2. `add_component`: Adds two numbers and prints the result.

The pipeline demonstrates how to:
- Define components using the `@dsl.component` decorator
- Create a pipeline using the `@dsl.pipeline` decorator
- Connect components in a pipeline
- Compile the pipeline to a YAML file

## Usage

1. Run the script to compile the pipeline:

    ```bash
    python pipeline.py
    ```  
   

This will create `simple_pipeline.yaml` in your current directory.

2. Upload the pipeline to your Kubeflow Pipelines installation:
- Open your Kubeflow Pipelines UI (e.g., http://localhost:8080/#/pipelines)
- Click "Upload pipeline"
- Select the `simple_pipeline.yaml` file
- Give your pipeline a name and click "Create"

3. Create a run of your pipeline:
- In the Kubeflow Pipelines UI, find your uploaded pipeline
- Click "Create run"
- Adjust parameters if desired (default is a=1.0, b=7.0)
- Click "Start" to run the pipeline

## Modifying the Pipeline

To modify the pipeline:

1. Edit the `pipeline.py` file.
2. Add new components or modify existing ones.
3. Update the `simple_pipeline` function to change the pipeline structure.
4. Re-run the script to compile the updated pipeline.
5. Upload the new `simple_pipeline.yaml` to Kubeflow Pipelines.

## Troubleshooting

- If you encounter issues uploading or running the pipeline, ensure your Kubeflow Pipelines installation is correctly set up and accessible.
- Check the Kubeflow Pipelines documentation for version-specific information or changes.

## Further Resources

- [Kubeflow Pipelines Documentation](https://www.kubeflow.org/docs/components/pipelines/)
- [KFP SDK Reference](https://kubeflow-pipelines.readthedocs.io/en/stable/)

## License

This project is open-source and available under the MIT License.