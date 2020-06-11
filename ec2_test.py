import boto3

ec2 = boto3.resource('ec2')

def list_instances():
	instances = ec2.instances.filter(
	    Filters=[ {'Name': 'instance-state-name', 'Values': ['running']}] )

	for instance in instances:
	    print(instance.id, instance.instance_type)


def main():
	list_instances()

main()