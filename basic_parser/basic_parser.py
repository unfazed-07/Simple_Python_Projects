import os

script_dir=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(script_dir, "use_it_for_parsing.txt")

def wow_parser(file_path):
    
    with open(file_path, 'r', encoding='UTF-8') as file:
        for line in file:
            line=line.strip()
            if not line:
                continue
            part=line.split()

            if len(part)>=4:
                first_name=part[0]
                last_name=part[1]
                email=part[2]
                phone_no=part[3]

                if '@' in email:
                    local_part=email.split('@')[0]
                    domain_name=email.split('@')[1]
                    
                    print(f"First name is {first_name}")
                    print(f"Last name is {last_name}")
                    print(f"Username  is {local_part}")
                    print(f"domain name is {domain_name}")
                    print(f"phone number is {phone_no}")
                    print()
wow_parser(file_path)
