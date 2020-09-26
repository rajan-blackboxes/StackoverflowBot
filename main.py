import os
import argparse


def get_args():
    """
    Gets arguments from command line
    """
    parser = argparse.ArgumentParser("Run stackoverflow bot")
    lang_desc = "str: name of language to be scraped"
    max_len_desc = """int: maximum pagination of that language"""
    output_desc = """output filename (.csv or .json)"""
    parser._action_groups.pop()
    required = parser.add_argument_group("Required")

    required.add_argument('-lang', type=str, help=lang_desc, required=True)
    required.add_argument('-max_page', type=int, help=max_len_desc, required=True)
    required.add_argument('-o', type=str, help=output_desc, required=True)

    args = parser.parse_args()

    return args


def run_scrapy(dicts):
    if dicts['o'] in os.listdir('.'):
        os.remove(dicts['o'])
    os.system(f"scrapy crawl stackoverflow -a language='{dicts['lang']}'"
              f" -a max_page={dicts['max_page']} -o {dicts['o']}")


def main():
    args = get_args()
    run_scrapy(vars(args))
    print("Successfully completed...............")


if __name__ == '__main__':
    main()
