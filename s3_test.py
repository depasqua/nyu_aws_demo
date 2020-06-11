import boto3


def list_all_buckets():
	s3=boto3.resource("s3")
	for bucket in s3.buckets.all():
		print(bucket.name)


def create_new_file(bucketname, filename):
	s3=boto3.client('s3')
	with open(filename, 'rb') as f:
		s3.upload_fileobj(f, bucketname, filename)


def main():
	input("Enter to start...")
	list_all_buckets()

	input("Enter to continue...")
	create_new_file('nyu-cloud', 's3_test.py')

main()