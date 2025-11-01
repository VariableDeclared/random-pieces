#/bin/env python3

from string import Template
import argparse
TEMPLATE="""
interface $vlan
 no shutdown
!\n"""
T_TEMPLATE = Template(TEMPLATE)
def generate_vlans(tags=[]):
    configuration = ""
    for tag in tags:
        configuration += T_TEMPLATE.substitute({"vlan": tag})

    return configuration


parser = argparse.ArgumentParser("VLAN Dell OS templater")
parser.add_argument("--tags", "-t", type=str)
parser.add_argument("--file", "-f", type=str, required=False)
def main():
    args = parser.parse_args()
    vlan_config = generate_vlans(args.tags.split(" "))
    print(vlan_config)
    if args.file is not None:
        with open(args.file, 'w') as output:
            output.write(vlan_config)

if __name__ == "__main__":
    main()
