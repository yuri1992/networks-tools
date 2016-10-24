import subprocess
import tldextract

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


def run_whois_lookup(url):
    try:
        out = subprocess.check_output(["whois", get_clean_url(url)])
        return out
    except Exception as e:
        return None
