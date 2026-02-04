from enum import Enum

class S3ListKeys(str, Enum):
    CONTENTS = "Contents"
    NEXT_TOKEN = "NextContinuationToken"
    CONTINUATION = "ContinuationToken"