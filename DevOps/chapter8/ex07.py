def test_release(host):
    release_file = host.file("/etc/os-release")
    assert release_file.contains("Ubuntu")
    assert release_file.contains("22.04")

def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed
    assert nginx.version.startswith("1.2")