import mimetypes
from botocore.exceptions import ClientError

from .boto_client import s3_client
from ..core.config import config


def create_bucket(bucket_name: str):
    s3_client.create_bucket(Bucket=bucket_name)


def create_presigned_url_post_operation(bucket_name: str, object_name: str, expiration: int = 600) -> dict:
    response = s3_client.generate_presigned_post(
        Bucket=bucket_name,
        Key=object_name,
        Conditions=[
            ["content-length-range", 0, config.max_file_size], # Define range of allowed file sizes
            # {"Content-Type": content_type},
        ],
        ExpiresIn=expiration,
    )

    return response


def create_presigned_url_get_operation(bucket_name, object_name, expiration=600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.


    code taken from: https://docs.aws.amazon.com/boto3/latest/guide/s3-examples.html
    """

    # Generate a presigned URL for the S3 object
    try:
        response = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=expiration,
        )
    except ClientError as e:
        print(f"\n\nError: {e}\n\n") # TODO
        return None

    # The response contains the presigned URL
    return response


def create_presigned_url_put_operation(bucket_name: str, object_name: str, expiration: int = 600):
    """Generate a presigned URL for PUT with content-type and content-length conditions.

    :param bucket_name: S3 bucket name
    :param object_name: S3 object key
    :param content_type: Required MIME type for the upload
    :param content_length: Required file size in bytes
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """
    try:
        response = s3_client.generate_presigned_url(
            'put_object',
            Params={
                'Bucket': bucket_name,
                'Key': object_name,
            },
            ExpiresIn=expiration,
        )
    except ClientError as e:
        print(f"\n\nError: {e}\n\n") # TODO
        return None

    return response

