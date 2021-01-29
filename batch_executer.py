"""Execute command from [--app-dir]/[--app-name] with arguments [--app-args] on [--input-dir] directory, and put the result into the [--output-dir] directory maintaining its structure."""
import argparse
import glob
from pathlib import Path


class BatchExecuter:
    make_backup = False

    def __init__(self, app_name, app_args='', app_base_dir='app', app_input_parameter='', input_dir='input',
                 app_output_parameter='-o', output_dir='output', relative=True, include_subdirs=True, file_mask='*',
                 dir_mask='*', replace_files=True):
        self.app_name = app_name
        self.app_args = app_args

        self.relative = relative
        self.app_base_dir = Path(app_base_dir)
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        if self.relative:
            self.app_base_dir = Path('.') / self.app_base_dir
            self.input_dir = Path('.') / self.input_dir
            self.output_dir = Path('.') / self.output_dir
        self.app_input_parameter = app_input_parameter
        self.app_output_parameter = app_output_parameter
        self.include_subdirs = include_subdirs
        self.file_mask = file_mask
        self.dir_mask = dir_mask
        self.replace_files = replace_files

    def run(self, additional_args=''):
        subdirs = '**/' if self.include_subdirs else ''
        files = [f for f in self.input_dir.glob(subdirs + '*.[jp][pn]g')]
        for f in files:
            print('cwebp ' + additional_args + ' ' + str(f) + ' ' + self.app_output_parameter + ' ' + str(self.output_dir))


if __name__ == '__main__':
    # todo: add arg parse
    parser = argparse.ArgumentParser(
        description='Execute command from [--app-base-dir]/[--app-folder]/[--app-name] '
                    'with arguments [--app-args] on [--input] directory, '
                    'and put the result into the [--output] directory, maintaining its structure.')
    parser.add_argument('-id', '--input-dir', type=str, default='input')
    parser.add_argument('-od', '--output-dir', type=str, default='output')
    parser.add_argument('-ad', '--app-dir', type=str, default='app')
    parser.add_argument('-an', '--app-name', type=str, default='app.exe')
    parser.add_argument('-aa', '--app-args', type=str, default='????')
    args = parser.parse_args()
    # todo: add json options handling

    batch_executer = BatchExecuter(app_name='bin/cwebp.exe', include_subdirs=True)
    input_path = Path('.')
    input_path = input_path / Path('input')
    # print(list(input_path.glob('**/*.[jp][pn]g')))
    batch_executer.run()
