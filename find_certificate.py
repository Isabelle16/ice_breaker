import ssl
import certifi


def check_certificate(cert_file):
    context = ssl.create_default_context(cafile=certifi.where())
    try:
        context.load_verify_locations(cert_file)
        print(f"Certificate {cert_file} is already in the certifi bundle.")
    except ssl.SSLError as e:
        print(f"Certificate {cert_file} is NOT in the certifi bundle. Error: {e}")


# Path to the required certificate
cert_file = "statoil_proxy_server_ca.pem"
check_certificate(cert_file)
