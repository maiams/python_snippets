from pessoa_fisica import PessoaFisica
from decorator import stars


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


@stars
def hi_with_decorator():
    print("hi there")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    pf = PessoaFisica('ricardo maia', 40, None)
    pf.set_cpf('123456')

    hi_with_decorator()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
