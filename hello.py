import argparse

def main():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description='A simple script to print parameters')

    # Add command line arguments
    parser.add_argument('--username', required=True, help='Your username')
    parser.add_argument('--password', required=True, help='Your password')

    # Parse the command line arguments
    args = parser.parse_args()

    # Print the values of the parameters
    print(f"Username: {args.username}")
    print(f"Password: {args.password}")

if __name__ == '__main__':
    main()
