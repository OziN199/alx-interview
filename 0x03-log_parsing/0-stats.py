import sys

def parse_line(line):
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-3])
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except (ValueError, IndexError):
        return None, None, None

def print_statistics(stats):
    total_size = sum(stats.values())
    print(f"Total file size: {total_size}")
    for code in sorted(stats.keys()):
        print(f"{code}: {stats[code]}")

def main():
    stats = {}
    line_count = 0

    try:
        for line in sys.stdin:
            ip_address, status_code, file_size = parse_line(line.strip())
            if ip_address is not None and status_code is not None and file_size is not None:
                stats[status_code] = stats.get(status_code, 0) + file_size
                line_count += 1

            if line_count == 10:
                print_statistics(stats)
                line_count = 0

    except KeyboardInterrupt:
        print_statistics(stats)

if __name__ == "__main__":
    main()
