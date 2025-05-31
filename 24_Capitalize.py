# Question Link https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true


def print_formatted(number):

    for n in range(1, number + 1):
  
        #octal
        number_octal = oct(n)
        number_octal_w_prefix = number_octal[2:]

        #hexa
        number_hexa = hex(n).upper()
        number_hexa_w_prefix = number_hexa[2:]

        #bin
        number_bin = bin(n)
        number_bin_w_prefix = number_bin[2:]

        #n to str
        n_string = str(n)

        #width
        bin_number = bin(number)
        bin_number_w_prefix = bin_number[2:]

        #printar
        print(f'{n_string.rjust(len(bin_number_w_prefix))} {number_octal_w_prefix.rjust(len(bin_number_w_prefix))} {number_hexa_w_prefix.rjust(len(bin_number_w_prefix))} {number_bin_w_prefix.rjust(len(bin_number_w_prefix))}')

    return

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)