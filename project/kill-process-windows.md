# How to Kill a Process using Command Line on Windows

## Using PID

If using Git Bash, replace all slashes in the command with
double-slashes (because Git Bash otherwise interprets them
as paths instead of flags). Otherwise, this slash replacement
is not necessary in cmd.exe and Powershell.

To kill a process by specifying its PID, execute:

```bash
taskkill /f /pid PIDNumberGoesHere
```

## Using Process Name

To kill a process by specifying the process name,
execute:

```bash
taskkill /f /im ProcessNameGoesHere
```

For example, you can start an instance of the Windows
calculator and then run:

```bash
taskkill /f /im calculator.exe
```