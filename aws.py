import boto3
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: python aws.py {key,secret key}\n")
        sys.exit(0)
    else:
        code = sys.argv[1] 
        secret = sys.argv[2]
    role_arn = "arn:aws:iam::411815166437:role/chen_s3_role"
    serialnumber = "arn:aws:iam::411815166437:mfa/chen.xu"
    mfa = 'arn:aws:iam::411815166437:mfa/chen.xu  '+str(code)
    client = boto3.client('s3')
    response = client.list_buckets()
    blist = response['Buckets']
    objlist = client.list_objects(Bucket='testbucketchen')
    for bucket in blist:
        if (bucket['Name']=='testbucketchen'):
            response = client.put_bucket_versioning(Bucket='testbucketchen',VersioningConfiguration={'MFADelete':'Disabled','Status':'Suspended'})
            temp = objlist['Contents']
            for each in temp:
                key = each['Key']
                response1 = client.delete_object(Bucket='testbucketchen',Key=key)
                print(response1)


if __name__ == '__main__':
    main()