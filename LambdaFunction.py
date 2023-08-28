import boto3

ec2 = boto3.resource('ec2')

#Provide Security Group id in Which the Intruder Will be Moved After Performing any Malicious Activity
isolated_sg = '<instance_id_here>'

#Function to Change Group of Intruder
def lambda_handler(event, context):

  #Using "event" tag to gather info of "FINDINGS" & "AFFECTED INSTANCE"
  finding_type = event['detail']['type'] 
  instance_id = event['detail']['resource']['instanceDetails']['instanceId']

  #LOGGING 
  print(f"Finding type: {finding_type}")
  print(f"Instance ID: {instance_id}")

  #Matching Finding Type Using "FINDINGS"
  if finding_type == 'Recon:EC2/Portscan':
    victim_ec2 = ec2.Instance(instance_id)
    victim_ec2.modify_attribute(Groups=[isolated_sg])
