# features.py
import argparse

def main():
    parser = argparse.ArgumentParser(description='Select features to print.')

    parser.add_argument('--hello', action='store_true', help='Print "Hello"')
    parser.add_argument('--beautiful', action='store_true', help='Print "Beautiful"')
    parser.add_argument('--wonderful', action='store_true', help='Print "Wonderful"')
    parser.add_argument('--world', action='store_true', help='Print "World"')

    args = parser.parse_args()

    output = []

    if args.hello:
        output.append('Hello')
    if args.beautiful:
        output.append('Beautiful')
    if args.wonderful:
        output.append('Wonderful')
    if args.world:
        output.append('World')

    print(' '.join(output))

if __name__ == '__main__':
    main()
