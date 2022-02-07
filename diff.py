import yaml
import json
from deepdiff import DeepDiff
from pprint import pprint

def yaml_as_dict(my_file):
    my_dict = {}
    with open(my_file, 'r') as fp:
        docs = yaml.safe_load_all(fp)
        for doc in docs:
            for key, value in doc.items():
                my_dict[key] = value
    return my_dict

if __name__ == '__main__':
    b = yaml_as_dict("test.yaml")
    a = yaml_as_dict("test-cluster.yaml")
    excludePath = {"root['metadata']",
                    "root['status']",
                    "root['spec']['progressDeadlineSeconds']",
                    "root['spec']['revisionHistoryLimit']",
                    "root['spec']['strategy']",
                    "root['spec']['template']['metadata']['creationTimestamp']",
                    "root['spec']['template']['spec']['dnsPolicy']",
                    "root['spec']['template']['spec']['restartPolicy']",
                    "root['spec']['template']['spec']['schedulerName']",
                    "root['spec']['template']['spec']['securityContext']",
                    "root['spec']['template']['spec']['terminationGracePeriodSeconds']"}
    excludeRegex = {r"root\['spec'\]\['template'\]\['spec'\]\['containers'\]\[\d+\]\['imagePullPolicy'\]",
                    r"root\['spec'\]\['template'\]\['spec'\]\['containers'\]\[\d+\]\['resources'\]",
                    r"root\['spec'\]\['template'\]\['spec'\]\['containers'\]\[\d+\]\['terminationMessagePath'\]",
                    r"root\['spec'\]\['template'\]\['spec'\]\['containers'\]\[\d+\]\['terminationMessagePolicy'\]",
                    r"root\['spec'\]\['template'\]\['spec'\]\['volumes'\]\[\d+\]\['emptyDir'\]"}
    ddiff = DeepDiff(a, b, exclude_paths=excludePath, exclude_regex_paths=excludeRegex, ignore_order=True)
    # parsed = json.loads(json(ddiff))
    print(ddiff.pretty())
    # print(json.dumps(parsed, indent=4))