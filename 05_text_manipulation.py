### Changed this slightly to get total restarts
### Split the columns and get the information

def process_pod_status(file_path):
    running_pods = 0
    failed_pods = 0
    total_restarts = 0

    with open(file_path, 'r') as file:
        next(file)

        for line in file:
            parts = line.split()
            if len(parts) < 4:
                continue

            status = parts[2]
            restarts = int(parts[3])

            if status == "Running":
                running_pods += 1
            else:
                failed_pods += 1

            total_restarts += restarts

    print(f"Running Pods: {running_pods}")
    print(f"Failed Pods: {failed_pods}")
    print(f"Total Restarts: {total_restarts}")


if __name__ == "__main__":
    process_pod_status("pod_status.txt")