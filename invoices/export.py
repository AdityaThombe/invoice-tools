"""Exporting invoices and reading their attachments."""
import os
import subprocess


def export_label(number):
    result = subprocess.run(f"echo INVOICE-{number}", shell=True, capture_output=True, text=True, check=True)
    return result.stdout.strip()


def read_attachment(root, name):
    with open(os.path.join(root, name), encoding="utf-8") as handle:
        return handle.read()
