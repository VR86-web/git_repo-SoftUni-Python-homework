import re


def parse_barcodes(barcodes):
    pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
    for barcode in barcodes:
        matches = re.fullmatch(pattern, barcode)

        if matches:
            product_group = "".join(re.findall(r"\d", barcode))
            product_group = product_group if product_group else "00"
            print(f"Product group: {product_group}")
        else:
            print("Invalid barcode")


count_of_barcodes = int(input())
data = [input() for _ in range(count_of_barcodes)]
parse_barcodes(data)