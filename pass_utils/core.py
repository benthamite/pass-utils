import subprocess

def get_pass_value(entry_name, field=None):
    """Get a value from a pass entry.
    
    Args:
        entry_name: The name of the pass entry
        field: The field to extract (e.g., "key", "user")
               If None, returns the password (first line)
        
    Returns:
        The value of the specified field without trailing newline
    """
    if field is None:
        # Get just the first line (the password)
        cmd = f"pass show {entry_name} | head -n 1"
    else:
        # Get a specific field
        cmd = f"pass show {entry_name} | grep '{field}:' | cut -d ' ' -f 2-"
    
    result = subprocess.check_output(cmd, shell=True, text=True).strip()
    return result
