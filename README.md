# Linux File Permissions Task

## Task Description
**Understand the file permissions and create a flowchart for it. Then, apply the chmod command in a Python file to make the permissions `rwxrwxr-x`**

## What This Task Covers

Based on the course slides provided, this task covers:

### 1. File Permissions Understanding
- **Owner permissions**: Read, Write, Execute
- **Group permissions**: Read, Write, Execute  
- **Others permissions**: Read, Execute (no write)

### 2. Permission Notation
- **Symbolic**: `rwxrwxr-x`
- **Octal**: `775`
- **Breakdown**:
  - Owner: `rwx` = 4+2+1 = 7
  - Group: `rwx` = 4+2+1 = 7
  - Others: `r-x` = 4+0+1 = 5

### 3. chmod Command
- **Purpose**: Change file permissions
- **Usage**: `chmod 775 filename`
- **Python equivalent**: `os.chmod(filename, 0o775)`

## Files Included

### 1. `file_permissions_flowchart.py`
This Python script demonstrates:
- **Text-based flowchart** explaining file permissions
- **Permission breakdown** and explanation
- **chmod command usage** via subprocess
- **Python os.chmod** implementation
- **Permission verification**

### 2. `README.md` (this file)
Documentation and explanation

## How to Run

### Prerequisites
- Python 3.x
- Unix-like system (Linux, macOS, WSL) for chmod command

### Execution
```bash
python3 file_permissions_flowchart.py
```

### Expected Output
The script will:
1. Display a flowchart explaining file permissions
2. Create a test file
3. Show initial permissions
4. Set permissions using chmod command
5. Set permissions using Python os.chmod
6. Verify the final permissions are `775` (rwxrwxr-x)

## Course Context

This task relates to the Linux systems course slides covering:
- **File permissions and security**
- **Command line interface (CLI)**
- **Filesystem operations**
- **System administration commands**

## Learning Objectives

1. **Understand Linux file permission system**
2. **Create visual representations (flowcharts)**
3. **Use chmod command effectively**
4. **Implement file operations in Python**
5. **Verify permission changes**

## Security Note

The permission `775` (rwxrwxr-x) is commonly used for:
- **Scripts** that need to be executed by group members
- **Directories** that need group write access
- **Shared files** in collaborative environments

**Remember**: Never use `chmod 777` (rwxrwxrwx) as it's a security risk!

## Reference
- YouTube Video: https://youtu.be/LnKoncbQBsM?si=IfV4m31fDSf5Ctw 