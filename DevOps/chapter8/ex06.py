import subprocess

def get_device(device):
    """
    ID_PART_ENTRY_TYPE
    """
    stdout = subprocess.check_output(['blkid', '-p', '-o', 'udev', device])
    for line in stdout.split('\n'):
        if 'ID_PART_ENTRY_TYPE=' in line:
            return line.split('=')[-1].strip()
    return ''

def test_type(monkeypatch):
    monkeypatch.setattr(
        'subprocess.check_output',
        lambda cmd: '\nID_PART_ENTRY_TYPE=aaaaa'
    )
    assert get_device('/dev/sda') == 'aaaa'