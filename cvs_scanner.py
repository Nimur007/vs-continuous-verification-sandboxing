import os
import sys
import re

def scan_file_for_vulnerabilities(file_path):
    """
    CVS Reference Architecture - Static Analysis Module
    Scans source code files for injected vulnerabilities (SQLi, Hardcoded Secrets).
    """
    vulnerabilities = []
    
    # Common vulnerability patterns for the pilot study setup
    patterns = {
        "Hardcoded Credentials": r"(password|passwd|secret|api_key)\s*=\s*['\"][a-zA-Z0-9_\-\+\/]{8,}['\"]",
        "SQL Injection Surface": r"execute\(\s*['\"].*SELECT.*WHERE.*?\+.*?\)",
        "Insecure Deserialization": r"pickle\.loads\("
    }

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                for vuln_type, pattern in patterns.items():
                    if re.search(pattern, line, re.IGNORECASE):
                        vulnerabilities.append({
                            "file": file_path,
                            "line": line_num,
                            "type": vuln_type,
                            "content": line.strip()
                        })
    except Exception as e:
        print(f"[-] Error reading {file_path}: {e}")
        
    return vulnerabilities

def main():
    print("[*] Starting CVS Ephemeral Static Scan...")
    target_dir = "."
    all_vulns = []

    # Walk through the repository files
    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.endswith('.py') and file != 'cvs_scanner.py':
                file_path = os.path.join(root, file)
                vulns = scan_file_for_vulnerabilities(file_path)
                all_vulns.extend(vulns)

    # Report results for the evaluation gate
    if all_vulns:
        print(f"\n[!] CVS Gated Filtration: Found {len(all_vulns)} potential issues!")
        for v in all_vulns:
            print(f" -> [{v['type']}] in {v['file']} at line {v['line']}: {v['content']}")
        print("\n[-] Evaluation Gate: FAILED. Patch rejected from human review queue.")
        sys.exit(1) # Fail the CI/CD pipeline step
    else:
        print("\n[+] Evaluation Gate: PASSED. No machine-detectable failures found.")
        print("[+] Forwarding candidate patch to Human Contextual Review.")
        sys.exit(0)

if __name__ == "__main__":
    main()
