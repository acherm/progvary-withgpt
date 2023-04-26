# generate_combinations.py
import itertools
import subprocess

def generate_feature_combinations(features):
    combinations = []
    for length in range(len(features) + 1):
        for subset in itertools.combinations(features, length):
            combinations.append(subset)
    return combinations

def main():
    features = ['--hello', '--beautiful', '--wonderful', '--world']
    combinations = generate_feature_combinations(features)

    for combo in combinations:
        # print(f"Running CLI with options: {' '.join(combo)}")
        subprocess.run(['python', 'features.py', *combo])

if __name__ == '__main__':
    main()
