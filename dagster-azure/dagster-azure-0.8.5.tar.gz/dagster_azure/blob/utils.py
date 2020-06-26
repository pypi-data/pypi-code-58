import warnings

try:
    # Centralise Azure imports here so we only need to warn in one place
    from azure.core.exceptions import ResourceNotFoundError
    from azure.storage.blob import (
        generate_blob_sas,
        BlobServiceClient,
    )
except ImportError:
    msg = (
        "Could not import required Azure objects. This probably means you have an old version "
        "of azure-storage-blob installed. dagster-azure requires azure-storage-blob~=12.0.0; "
        "this conflicts with dagster-snowflake which requires azure-storage-blob<12.0.0 and is "
        "incompatible. Please uninstall dagster-snowflake and reinstall dagster-azure to fix "
        "this error."
    )
    warnings.warn(msg)
    raise


def _create_url(storage_account, subdomain):
    return "https://{}.{}.core.windows.net/".format(storage_account, subdomain)


def create_blob_client(storage_account, credential):
    """
    Create a Blob Storage client.
    """
    account_url = _create_url(storage_account, "blob")
    if hasattr(credential, "account_key"):
        credential = credential.account_key
    return BlobServiceClient(account_url, credential)


__all__ = ['create_blob_client', 'generate_blob_sas', 'BlobServiceClient', 'ResourceNotFoundError']
