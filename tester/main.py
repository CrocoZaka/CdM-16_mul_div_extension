import importlib
import importlib.util
import os.path
import subprocess
import sys
from os import listdir
from os.path import isfile
from pathlib import Path
from tempfile import NamedTemporaryFile

from colorama import init as color_init, Fore, Style

from runners import LogisimRunner, EmulatorRunner, Runner, RunnerStatus

required_keys = {"code"}
optional_keys = {"r0", "r1", "r2", "r3", "sp", "ps", "pc", "mem"}

# def print_error(name, )

assembler_path = Path(__file__).parent.parent.joinpath('main.py')

runners: list[Runner] = [LogisimRunner(), EmulatorRunner()]


def run_test(filename: str):
    test_name = filename.split('/')[-1]

    def log(msg):
        print(f"[{test_name}] {msg}")

    def ok(msg):
        return f"{Fore.GREEN}{msg}{Fore.RESET}"

    def warn(msg):
        return f"{Fore.YELLOW}{msg}{Fore.RESET}"

    def error(msg):
        return f"{Fore.RED}{msg}{Fore.RESET}"

    try:
        spec = importlib.util.spec_from_file_location(f"test_module_{filename.split('.')[0]}", filename)
        test_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(test_module)
        test = {item: test_module.__dict__[item] for item in dir(test_module) if not item.startswith("_")}
    except SyntaxError:
        log(error("syntax error"))
        return
    log("loaded")

    for key in test.keys():
        if key not in required_keys | optional_keys:
            return log(error(f"Key not allowed: {key}"))
    if len(missing_keys := required_keys - test.keys()) != 0:
        return log(error(f"Missing required keys: {missing_keys}"))

    # TODO: always remove .img file
    with NamedTemporaryFile(suffix=".asm", delete=True, mode='w') as asm_file:
        success = True
        asm_file.write(test["code"])
        asm_file.flush()
        img_file_name = os.path.splitext(asm_file.name)[0] + ".img"
        asm_process = subprocess.run([sys.executable, str(assembler_path), asm_file.name], stderr=subprocess.STDOUT,
                                     stdout=subprocess.PIPE, cwd=Path(__file__).parent.parent)
        if asm_process.returncode != 0 or not os.path.exists(img_file_name):
            log(error("Error assembling test, assembler output here:"))
            print(asm_process.stdout.decode())
            return
        results = []

        # run assembled code
        for runner in runners:
            status, result = runner.run(img_file_name, 10000)
            if status != RunnerStatus.SUCCESS:
                log(error(f"[{runner.name}] failed: {status.value}"))
                success = False
                continue
            results.append(result)

        # compare results with each other - they should match
        for i in range(len(results)):
            for j in range(i + 1, len(results)):
                if results[i] != results[j]:
                    r1 = results[i]
                    r2 = results[j]
                    log(warn(f"WARNING: results of {runners[i].name} and {runners[j].name} are different"))
                    for reg_name in r1.regs.keys():
                        if r1.regs[reg_name] != r2.regs[reg_name]:
                            log(warn(f"{r1.runner_name}.{reg_name} = {r1.regs[reg_name]}; {r2.runner_name}.{reg_name} = {r2.regs[reg_name]}"))


        # verify results
        for result in results:
            for reg_name, reg_value in result.regs.items():
                if reg_name in test.keys():
                    if test[reg_name] != reg_value:
                        success = False
                        log(error(f"ERROR: [{result.runner_name}]: registers do not match: {reg_name} = {reg_value}, expected {test[reg_name]}"))
            if "mem" in test.keys():
                mem_test: dict[int, list[int]] = test["mem"]
                for offset, data in mem_test.items():
                    if (result_data := result.mem[offset:offset + len(data)]) != data:
                        success = False
                        log(error(
                            f"ERROR: [{result.runner_name}]: memory does not match at {hex(offset)}: got {result_data}, expected {data}"))
        if success:
            log(ok(f"Ok"))
        else:
            log(error(f"Failed"))


if __name__ == "__main__":
    color_init()
    test_dir = Path(__file__).parent.parent.joinpath('tests')
    test_files = [file for file in listdir(test_dir) if isfile(test_dir.joinpath(file))]
    for file in test_files:
        run_test(str(test_dir.joinpath(file)))
