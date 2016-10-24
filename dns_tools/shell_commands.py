import subprocess
import tldextract
from django.core.validators import URLValidator, validate_ipv46_address

url_validator = URLValidator()


def get_clean_url(url):
    parsed = tldextract.extract(url)
    return parsed.registered_domain


def run_dns_lookup(url):
    try:
        out = subprocess.check_output(["dig", get_clean_url(url)])
        return out
    except Exception as e:
        return None


def run_reverse_dns(ip):
    try:
        out = subprocess.check_output(["host", ip])
        reversed_host = out.split()[-1]
        return reversed_host
    except Exception:
        return None


def run_ping_query(host):
    try:
        url_validator(host)
        host = get_clean_url(host)
    except:
        try:
            validate_ipv46_address(host)
        except:
            return None

    try:
        out = subprocess.check_output(["ping", "-c 2", "-W 5", host])
        return out
    except Exception:
        return None


def run_traceroute_query(host):
    try:
        out = subprocess.check_output(["traceroute", host])
        return out
    except Exception as e:
        return None


def run_whois_lookup(url):
    try:
        out = subprocess.check_output(["whois", get_clean_url(url)])
        return out
    except Exception as e:
        return None
