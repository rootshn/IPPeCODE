# Generating an XML File by Parsing an IPPeCode Source File

This program analyzes an IPPeCode source file and produces an output as an XML file. The program uses an XML tree structure to add each command in the source file to the output. The tree is then saved as an XML file.

### Installation
The program is written in Python 3 and does not require any external packages. To use it, simply call the `parse_file()` function with the source parameter. For example:

xml_string = parse_file('program.txt')

This will analyze the `program.txt` source file and output it as an XML string.

### Usage
The program assumes the source file to be `program.txt` by default. If you run the code with your source file named `program.txt`, an XML file named `program.xml` will be generated.


if __name__ == '__main__':
    main()


The program skips blank lines and comments while reading the source file and collects each command in a list. It then creates a separate XML element for each command and adds the command's order and type (opcode) to the element.

for i, instruction in enumerate(instructions):
    opcode, params = parse_instruction(instruction)
    tac = ET.SubElement(program, 'tac')
    tac.set('opcode', opcode.upper())
    tac.set('order', str(i+1))
    for j, param in enumerate(params):
        operand = ET.SubElement(tac, f'src{j+1}')
        operand.set('type', 'variable' if param.startswith('@') else 'integer')
        operand.text = param.strip('@')


### Development
This program is a useful tool for converting IPPeCode source files to XML files. However, its features may be insufficient for a larger project, particularly when developing a compiler. In that case, the program should be further developed.

### Resources
This program is a tool specific to the IPPeCode language. For more information on the features of IPPeCode, refer to https://github.com/rootshn/IPPeCODE
