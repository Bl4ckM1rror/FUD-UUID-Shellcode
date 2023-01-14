#!/usr/bin/env python3


def bin_to_uuid(bin_data, output=None):
    from uuid import UUID
    
    uuid_str = ''

    with open(bin_data, 'rb') as fh:
        # read in 16 bytes from the file
        data_chunk = fh.read(16)
        while data_chunk:
            # if chunk is less than 16 bytes then we pad the
            # difference with a NOP(0x90)
            if len(data_chunk) < 16:
                padding = 16 - len(data_chunk)
                data_chunk += (b'\x90' * padding)

            uuid_str = "\n".join((uuid_str, f'{UUID(bytes_le=data_chunk)}'))

            # read in more 16 bytes from the file
            data_chunk = fh.read(16)

    uuid_str = uuid_str.lstrip('\n')
    if output:
        with open(output, "w") as fh:
            fh.write(uuid_str)
    else:
        print(uuid_str)

    return


def main():
    from argparse import ArgumentParser

    parser = ArgumentParser(
        "bin_to_uuid", description="Converts binary files into legit UUID")

    parser.add_argument(
        '-p',
        '--payload',
        required=True,
        help='payload (in binary format) that is to be converted to UUID')
    parser.add_argument(
        '-o',
        '--output',
        required=False,
        help='output file for the payload that was converted to UUID')

    args = vars(parser.parse_args())

    bin_to_uuid(args['payload'], args['output'])


if '__main__' == __name__:
    main()
