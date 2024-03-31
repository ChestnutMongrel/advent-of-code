from common import read_file, sum_tuple
from difflib import context_diff


def create_config(data: list) -> dict:
    config = dict()

    for line in data:
        module, destination = line.split(' -> ')
        if module[0] in '%&':
            type_ = module[0]
            name = module[1:]
        else:
            name = module
            type_ = ''
        instruction = {'type': type_, 'to': tuple(destination.split(', '))}
        if type_ == '&':
            instruction['from'] = dict()  # Would it lead problems?
        if type_ == '%':
            instruction['switch'] = False
        config[name] = instruction

    for module, data in config.items():
        for name in data['to']:
            if name not in config:
                continue
            if config[name]['type'] == '&':
                config[name]['from'][module] = False

    return config


def push_the_button(config: dict, rx: bool = False) -> tuple:
    signals_to = (('broadcaster', False, 'button'),)
    total = [1, 0]

    while signals_to:
        new_signals = list()
        for name, level, from_ in signals_to:
            if rx and name == 'rx':
                print(level)
                if level == 0:
                    return None
                continue

            if name not in config:
                continue  # ?

            if config[name]['type'] == '':
                new_level = level

            if config[name]['type'] == '%':
                if level:
                    continue

                config[name]['switch'] = not config[name]['switch']
                new_level = config[name]['switch']

            if config[name]['type'] == '&':
                config[name]['from'][from_] = level
                if all(config[name]['from'].values()):
                    new_level = 0
                else:
                    new_level = 1

            new_signals += [(item, new_level, name) for item in config[name]['to']]
            total[new_level] += len(config[name]['to'])

        signals_to = new_signals

    return tuple(total)


def main() -> None:
    for name in ('data/12_example.txt', 'data/example_20.txt', 'data/20_input.txt',):  #
        initial_config = create_config(read_file(name))

        new_config = initial_config.copy()
        total_signals = (0, 0)
        pushes = 1_000
        for i in range(pushes):
            signals = push_the_button(new_config)
            if signals is None:
                print(f'{i = }')
                break
            total_signals = sum_tuple(total_signals, signals)
            if new_config.values() == initial_config.values():
                break

        print(f'{i = }')

        print(f'{total_signals = }')
        print('low * high', total_signals[0] * total_signals[1])
        # From reddit: 'My answer was about 230 trillion.'


if __name__ == '__main__':
    main()
