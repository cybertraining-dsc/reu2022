import resource
import time

RESOURCES = [
    ('ru_utime', 'User time'),
    ('ru_stime', 'System time'),
    ('ru_maxrss', 'Max. Resident Set Size'),
    ('ru_ixrss', 'Shared Memory Size'),
    ('ru_idrss', 'Unshared Memory Size'),
    ('ru_isrss', 'Stack Size'),
    ('ru_inblock', 'Block inputs'),
    ('ru_oublock', 'Block outputs'),
]

"""
Gregor suggests:
RESOURCES = [
("ru_utime", "time in user mode (float seconds)"),
("ru_stime", "time in system mode (float seconds)"),
("ru_maxrss", "maximum resident set size"),
("ru_ixrss", "shared memory size"),
("ru_idrss", "unshared memory size"),
("ru_isrss", "unshared stack size"),
("ru_minflt", "page faults not requiring I/O"),
("ru_majflt", "page faults requiring I/O"),
("ru_nswap", "number of swap outs"),
("ru_inblock", "block input operations"),
("ru_oublock", "block output operations"),
("ru_msgsnd", "messages sent"),
("ru_msgrcv", "messages received"),
("ru_nsignals", "signals received"),
("ru_nvcsw", "voluntary context switches"),
("ru_nivcsw", "involuntary context switches"),
"""

usage = resource.getrusage(resource.RUSAGE_SELF)

for name, desc in RESOURCES:
    try:
        print('{:<25} ({:<10}) = {}'.format(
            desc, name, getattr(usage, name)))
    except:
        print('{:<25} ({:<10}) = {}'.format(
            desc, name, "not found"))
