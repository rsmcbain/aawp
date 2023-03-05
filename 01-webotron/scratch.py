import boto3

def get_buckets():
    session = boto3.Session(profile_name='default')
    s3 = session.resource('s3')


    for bucket in s3.buckets.all():
        print(bucket)

    #new_bucket = s3.create_bucket(Bucket='scotts-examples.com', CreateBucketConfiguration={'LocationConstraint':'us-east-2'})

if __name__ == '__main__':
    get_buckets()