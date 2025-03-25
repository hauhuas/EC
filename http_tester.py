import argparse
import requests
import json
from urllib.parse import urlparse

def main():
    parser = argparse.ArgumentParser(description='HTTP Request Tester')
    parser.add_argument('--url', required=True, help='Target URL')
    parser.add_argument('--method', default='GET', choices=['GET', 'POST'], help='HTTP method')
    parser.add_argument('--headers', action='append', help='Request headers (format: "Key:Value")')
    parser.add_argument('--params', action='append', help='Query parameters (format: "key=value")')
    parser.add_argument('--data', help='Request body data')
    parser.add_argument('--json', help='JSON request body')
    parser.add_argument('--timeout', type=int, default=10, help='Request timeout in seconds')

    args = parser.parse_args()

    # Prepare request components
    headers = {}
    if args.headers:
        for h in args.headers:
            k, v = h.split(':', 1)
            headers[k.strip()] = v.strip()

    params = {}
    if args.params:
        for p in args.params:
            k, v = p.split('=', 1)
            params[k.strip()] = v.strip()

    try:
        response = requests.request(
            method=args.method,
            url=args.url,
            headers=headers,
            params=params,
            data=args.data,
            json=json.loads(args.json) if args.json else None,
            timeout=args.timeout
        )

        # Format output
        result = {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'content': response.text,
            'elapsed': f"{response.elapsed.total_seconds():.3f}s",
            'history': [{
                'url': r.url,
                'status_code': r.status_code
            } for r in response.history]
        }

        print(json.dumps(result, indent=2))

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {str(e)}")
    except json.JSONDecodeError:
        print("Invalid JSON format in --json parameter")

if __name__ == '__main__':
    main()