# AWS-IntelliSec
AWS Threat detection automated real-time prevention management.

GuardDuty, an AWS-managed threat detection service, is highly regarded by customers for fortifying their AWS infrastructure and its automated response capabilities.
By leveraging a blend of AWS CloudTrail, Amazon VPC Flow Logs, and DNS Logs, GuardDuty identifies potential security breaches and issues alerts when suspicious activities are detected within the AWS environment.
Each discovery made by GuardDuty denotes a plausible security concern identified in the network. 
Whenever unexpected or potentially harmful actions are observed in your AWS setup, GuardDuty generates these findings.
Through the use of GuardDuty, deliberate findings can be fabricated, allowing for the observation of these incidents in the GuardDuty console. 
Subsequent rectification can be carried out through the utilization of AWS CloudWatch events and Lambda functions.
