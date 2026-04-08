### Mac ###
# Virtual Environment:
source /Users/jerry/Desktop/hey_cindy/.venv/bin/activate

# Dashboard：
python local_dashboard.py
http://127.0.0.1:6060/

# Run Program:
python voice_to_light_wakeword.py


### AWS EC2 (Ubuntu) ###
https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#Instances:instanceState=running
ssh -i hey-cindy-key.pem ubuntu@3.85.92.201