import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(
        re.sub(r"_", r"-", r"coral_perm_demo"),
        "coral_perm_demo.urls",
        name="coral_perm_demo",
    ),
)
