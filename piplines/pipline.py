import kfp
from kfp import dsl
import yaml


@dsl.component(base_image='python:3.9')
def print_component(text: str):
    print(text)


@dsl.component(base_image='python:3.9')
def add_component(a: float, b: float) -> float:
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


@dsl.pipeline(
    name='Simple Pipeline',
    description='A simple pipeline that prints a message and adds two numbers'
)
def simple_pipeline(a: float = 1.0, b: float = 7.0):
    print_task = print_component(text='Welcome to Kubeflow Pipelines!')
    add_task = add_component(a=a, b=b)
    print_task.after(add_task)


# if __name__ == '__main__':
#     compiler = kfp.compiler.Compiler()
#
#     # Compile the pipeline to YAML
#     compiler.compile(simple_pipeline, 'simple_pipeline.yaml')
#     print("Pipeline compiled successfully. Check 'simple_pipeline.yaml' in the current directory.")
#
#     # Read and print the contents of the YAML file
#     with open('simple_pipeline.yaml', 'r') as file:
#         yaml_content = yaml.safe_load(file)
#         print("\nPipeline structure:")
#         print(yaml.dump(yaml_content, default_flow_style=False))


if __name__ == '__main__':
    compiler = kfp.compiler.Compiler()
    compiler.compile(simple_pipeline, 'simple_pipeline.yaml')
    print("Pipeline compiled successfully. Check 'simple_pipeline.yaml' in the current directory.")

    # Upload the pipeline
    client = kfp.Client(host='http://localhost:8080')
    pipeline_filename = 'simple_pipeline.yaml'
    pipeline_name = 'Simple Pipeline Example'

    try:
        pipeline = client.upload_pipeline(
            pipeline_filename,
            pipeline_name=pipeline_name,
            description='A simple pipeline that prints a message and adds two numbers'
        )
        print(f"Pipeline uploaded successfully. ID: {pipeline.id}")
    except Exception as e:
        print(f"Failed to upload pipeline: {e}")