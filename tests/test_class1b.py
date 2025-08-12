import os
import re
import pytest
from pathlib import Path

from utilities import subprocess_runner, remove_ansible_warnings


TEST_CASES = [
    "../class1/collateral/host_vars/test1/simple_pb1.yml",
    "../class1/collateral/host_vars/test1/simple_pb2.yml",
    "../class1/collateral/host_vars/test2/simple_pb2.yml",
    "../class1/collateral/modules/my_modules_1.yml",
    "../class1/collateral/collections/coll_pb1.yml",
    "../class1/collateral/collections/coll_pb2.yml",
    "../class1/collateral/set_fact/simple_pb.yml",
    # "../class1/collateral/set_fact/test_prompt.yml",
    "../class1/collateral/variables/simple_pb.yml",
    "../class1/collateral/variables/simple_pb_1.yml",
]


@pytest.mark.parametrize("test_case", TEST_CASES)
def test_runner_collateral(test_case):
    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]
    cmd_list = ["ansible-playbook", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, script_dir)
    std_err = remove_ansible_warnings(std_err)
    assert return_code == 0
    assert std_err == ""


def test_class1_ex4a():
    base_path = "../class1/exercises/exercise4"
    cmd_list = ["ansible-playbook", "exercise4a.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_out.count("10.220.88.32") == 4
    assert (
        "arista5                    : ok=3    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )

    std_err = remove_ansible_warnings(std_err)
    assert std_err == ""
    assert return_code == 0


def test_class1_ex4b():
    base_path = "../class1/exercises/exercise4"
    cmd_list = ["ansible-playbook", "exercise4b.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_out.count("10.220.88.32") == 4
    assert '"ansible_host": "arista5.lasthop.io"' in std_out
    assert (
        "arista5                    : ok=5    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    std_err = remove_ansible_warnings(std_err)
    assert std_err.strip() == ""
    assert return_code == 0


def test_class1_ex4c():
    base_path = "../class1/exercises/exercise4/exercise4c"
    cmd_list = ["ansible-playbook", "exercise4c.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_out.count("10.220.88.32") == 4
    assert '"ansible_host": "arista5.lasthop.io"' in std_out
    assert '"ansible_network_os": "eos"' in std_out
    assert '"ansible_host": "arista5.lasthop.io"' in std_out
    assert '"desired_eos_version": "4.34.1F"' in std_out
    assert (
        "arista5                    : ok=6    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )

    std_err = remove_ansible_warnings(std_err)
    assert std_err.strip() == ""
    assert return_code == 0


def test_class1_ex4d():
    base_path = "../class1/exercises/exercise4/exercise4d"
    cmd_list = ["ansible-playbook", "exercise4d.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_out.count("10.220.88.32") == 4
    assert '"ansible_host": "arista5.lasthop.io"' in std_out
    assert '"ansible_network_os": "eos"' in std_out
    assert '"ansible_host": "arista5.lasthop.io"' in std_out
    assert '"desired_eos_version": "4.33.2F"' in std_out
    assert (
        "arista5                    : ok=6    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )

    std_err = remove_ansible_warnings(std_err)
    assert std_err.strip() == ""
    assert return_code == 0


def test_class1_ex4e():
    base_path = "../class1/exercises/exercise4/exercise4e"
    cmd_list = ["ansible-playbook", "exercise4e.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert std_out.count("10.220.88.32") == 4
    assert '"ansible_host": "arista5.lasthop.io"' in std_out
    assert '"ansible_network_os": "eos"' in std_out
    assert '"ansible_host": "arista5.lasthop.io"' in std_out
    assert '"desired_eos_version": "4.33.2F"' in std_out
    assert '"device_hostname": "arista5.lab.io"' in std_out
    assert (
        "arista5                    : ok=8    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )

    std_err = remove_ansible_warnings(std_err)
    assert std_err.strip() == ""
    assert return_code == 0


def test_class1_ex5a():
    base_path = "../class1/exercises/exercise5/exercise5a"
    cmd_list = ["ansible-playbook", "exercise5a.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "The ASN for host cisco1 is 65001" in std_out
    assert "The ASN for host cisco2 is 65001" in std_out
    assert "The ASN for host cisco5 is 65001" in std_out
    assert "The ASN for host cisco6 is 65001" in std_out
    assert (
        "cisco1                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "cisco2                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "cisco5                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "cisco6                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class1_ex5b():
    base_path = "../class1/exercises/exercise5/exercise5b"
    cmd_list = ["ansible-playbook", "exercise5b.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "The ASN for host cisco1 is 65001" in std_out
    assert "The ASN for host cisco2 is 65001" in std_out
    assert "The ASN for host cisco5 is 65535" in std_out
    assert "The ASN for host cisco6 is 65001" in std_out
    assert (
        "cisco1                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "cisco2                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "cisco5                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "cisco6                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0


def test_class1_ex5c():
    base_path = "../class1/exercises/exercise5/exercise5c"
    cmd_list = ["ansible-playbook", "exercise5c.yml"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert "The ASN for host cisco1 is 65001, the router-id is 1.1.1.1" in std_out
    assert "The ASN for host cisco2 is 65001, the router-id is 2.2.2.2" in std_out
    assert "The ASN for host cisco5 is 65535, the router-id is 5.5.5.5" in std_out
    assert "The ASN for host cisco6 is 65001, the router-id is 6.6.6.6" in std_out
    assert (
        "cisco1                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "cisco2                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "cisco5                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert (
        "cisco6                     : ok=1    changed=0    unreachable=0    failed=0    "
        "skipped=0    rescued=0    ignored=0" in std_out
    )
    assert std_err == ""
    assert return_code == 0

