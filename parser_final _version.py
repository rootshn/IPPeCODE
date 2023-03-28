import os
import xml.etree.ElementTree as ET

def parse_instruction(instruction):
    parts = instruction.split(' ')
    opcode = parts[0]
    params = parts[1:]
    return opcode, params

def parse_file(source):
    instructions = []
    with open(source, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith('#'):
                continue
            instructions.append(line)

    program = ET.Element('program')
    program.set('language', 'IPPeCode')

    for i, instruction in enumerate(instructions):
        opcode, params = parse_instruction(instruction)
        tac = ET.SubElement(program, 'tac')
        tac.set('opcode', opcode.upper())
        tac.set('order', str(i+1))
        for j, param in enumerate(params):
            operand = ET.SubElement(tac, f'src{j+1}')
            operand.set('type', 'variable' if param.startswith('@') else 'integer')
            operand.text = param.strip('@')

    xml_string = ET.tostring(program, encoding='unicode', method='xml')
    return xml_string

def main():
    xml_path = os.path.join(os.path.dirname(__file__), 'program.xml')
    output_file = 'program_output.xml'

    xml_string = parse_file(xml_path)

    with open(output_file, 'w') as file:
        file.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
        file.write(xml_string)

if __name__ == '__main__':
    main()
