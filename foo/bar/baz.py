from prefect import flow


@flow
def baz():
    return 42
