from storages.backends.s3boto3 import S3Boto3Storage

class OverwriteStorage(S3Boto3Storage):
    def get_available_name(self, name, max_length=None):
        # Always use the same name, overwrite if it exists
        return name
