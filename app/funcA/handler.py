def lambda_handler(event, context):
    n = 3
    grid_lines = []

    for _ in range(n):
        grid_lines.append("+---" * n + "+")
        grid_lines.append("|   " * n + "|")
    grid_lines.append("+---" * n + "+")

    grid = "\n".join(grid_lines)

    print(grid)

    return {
        "statusCode": 200,
        "body": grid 
    }