import boto3
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['POST'])
def generate_presigned_url(request):
    # Get the file_name and content_type from the request body
    file_name = request.data.get('file_name')
    content_type = request.data.get('content_type')
    
    # Configure your AWS credentials and bucket name
    s3_client = boto3.client('s3')
    
    presigned_url = s3_client.generate_presigned_url(
        'put_object',
        Params={
            'Bucket': 'practice-repo-bucket',
            'Key': file_name,
            'ContentType': content_type
        },
        ExpiresIn=3600
    )
    
    return JsonResponse({'presigned_url': presigned_url})

@api_view(['GET'])
def get_buckets():
    # Configure your AWS credentials and bucket name
    s3_client = boto3.client('s3')
    return JsonResponse(s3_client.list_buckets())
    