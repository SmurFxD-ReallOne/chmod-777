#!/usr/bin/env python3
"""
File Permissions and chmod Demonstration
=======================================

This script demonstrates:
1. Understanding Linux file permissions
2. Creating a flowchart representation
3. Using chmod to set permissions to rwxrwxr-x (775)

Author: Linux Systems Course
"""

import os
import stat
import subprocess

def print_flowchart():
    """Print a text-based flowchart explaining file permissions"""
    print("=" * 60)
    print("FILE PERMISSIONS FLOWCHART")
    print("=" * 60)
    print()
    print("┌─────────────────────────────────────────────────────────┐")
    print("│                    FILE PERMISSIONS                     │")
    print("└─────────────────────────────────────────────────────────┘")
    print("                              │")
    print("                              ▼")
    print("┌─────────────────────────────────────────────────────────┐")
    print("│              THREE PERMISSION CATEGORIES               │")
    print("└─────────────────────────────────────────────────────────┘")
    print("                              │")
    print("                              ▼")
    print("┌─────────────┐    ┌─────────────┐    ┌─────────────┐")
    print("│   OWNER     │    │   GROUP     │    │   OTHERS    │")
    print("│  (User)     │    │ (Group)     │    │ (Everyone)  │")
    print("└─────────────┘    └─────────────┘    └─────────────┘")
    print("      │                   │                   │")
    print("      ▼                   ▼                   ▼")
    print("┌─────────────┐    ┌─────────────┐    ┌─────────────┐")
    print("│    rwx      │    │    rwx      │    │    r-x      │")
    print("│  Read/Write │    │  Read/Write │    │ Read/Execute│")
    print("│  Execute    │    │  Execute    │    │ (No Write)  │")
    print("└─────────────┘    └─────────────┘    └─────────────┘")
    print("      │                   │                   │")
    print("      ▼                   ▼                   ▼")
    print("┌─────────────┐    ┌─────────────┐    ┌─────────────┐")
    print("│      7      │    │      7      │    │      5      │")
    print("│   (4+2+1)   │    │   (4+2+1)   │    │   (4+0+1)   │")
    print("└─────────────┘    └─────────────┘    └─────────────┘")
    print("      │                   │                   │")
    print("      └───────────────────┼───────────────────┘")
    print("                          ▼")
    print("┌─────────────────────────────────────────────────────────┐")
    print("│              FINAL PERMISSION: 775                     │")
    print("│              chmod 775 filename                        │")
    print("└─────────────────────────────────────────────────────────┘")
    print()

def explain_permissions():
    """Explain the permission system in detail"""
    print("PERMISSION EXPLANATION:")
    print("-" * 40)
    print("r = Read permission (4)")
    print("w = Write permission (2)")
    print("x = Execute permission (1)")
    print()
    print("rwxrwxr-x breakdown:")
    print("Owner (rwx):   Read + Write + Execute = 4+2+1 = 7")
    print("Group (rwx):   Read + Write + Execute = 4+2+1 = 7")
    print("Others (r-x):  Read + Execute (no write) = 4+0+1 = 5")
    print("Final: 775")
    print()

def create_test_file():
    """Create a test file to demonstrate permissions"""
    filename = "test_file.txt"
    
    with open(filename, 'w') as f:
        f.write("This is a test file for permission demonstration.\n")
        f.write("Owner can read, write, and execute.\n")
        f.write("Group can read, write, and execute.\n")
        f.write("Others can read and execute, but not write.\n")
    
    print(f"Created test file: {filename}")
    return filename

def show_current_permissions(filename):
    """Show current permissions of the file"""
    try:
        file_stat = os.stat(filename)
        current_permissions = stat.filemode(file_stat.st_mode)
        octal_permissions = oct(file_stat.st_mode)[-3:]
        
        print(f"Current permissions of {filename}: {current_permissions}")
        print(f"Octal representation: {octal_permissions}")
        
        return current_permissions, octal_permissions
    except FileNotFoundError:
        print(f"Error: File {filename} not found!")
        return None, None

def set_permissions_chmod(filename, permissions="775"):
    """Set file permissions using chmod command"""
    try:
        result = subprocess.run(['chmod', permissions, filename], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Successfully set permissions to {permissions} using chmod")
            return True
        else:
            print(f"Error setting permissions: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("Error: chmod command not found. This script should be run on a Unix-like system.")
        return False

def set_permissions_python(filename, permissions="775"):
    """Set file permissions using Python's os.chmod"""
    try:
        mode = int(permissions, 8)
        os.chmod(filename, mode)
        print(f"Successfully set permissions to {permissions} using Python os.chmod")
        return True
    except Exception as e:
        print(f"Error setting permissions with Python: {e}")
        return False

def main():
    """Main function to demonstrate file permissions"""
    print("FILE PERMISSIONS AND CHMOD DEMONSTRATION")
    print("=" * 50)
    print()
    
    print_flowchart()
    explain_permissions()
    
    filename = create_test_file()
    print()
    
    print("STEP 1: Check initial permissions")
    print("-" * 35)
    show_current_permissions(filename)
    print()
    
    print("STEP 2: Set permissions using chmod command")
    print("-" * 40)
    if set_permissions_chmod(filename, "775"):
        show_current_permissions(filename)
    print()
    
    print("STEP 3: Set permissions using Python os.chmod")
    print("-" * 40)
    if set_permissions_python(filename, "775"):
        show_current_permissions(filename)
    print()
    
    print("STEP 4: Verify final permissions")
    print("-" * 30)
    final_perms, final_octal = show_current_permissions(filename)
    
    if final_octal == "775":
        print("SUCCESS: Permissions set correctly to 775 (rwxrwxr-x)")
    else:
        print("FAILED: Permissions not set correctly")
    
    print()
    print("=" * 50)
    print("DEMONSTRATION COMPLETE!")
    print("=" * 50)

if __name__ == "__main__":
    main() 