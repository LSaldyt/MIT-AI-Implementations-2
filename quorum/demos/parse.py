from ..parse import parse_file, parse_pattern

def parse(args):
    pattern = '''
    if  @x isa @y, @y @rel @z
    then @x @rel @z because @x isa @y
    '''
    #print(parse_pattern(pattern))
    print(parse_file('data/test.txt'))
