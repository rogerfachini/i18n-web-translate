import json
import goslate
import argparse
from collections import OrderedDict
import io


class jsonTranslate:
    def __init__(self, cmdArgs = True):
        self.original_data = {}
        self.gs = goslate.Goslate()            

    def translate(self, inFile, inLang, outLang, outFile = None):
        with open(inFile, 'r') as f:
            original_data = json.load(f, object_pairs_hook=OrderedDict)

            print "The input data is:"
            print original_data

            print "The translated data is:"
            translated_data = self.translate_recursive(
                original_data, outLang, inLang, self.gs)
            print translated_data

            unicode_data = self.byteify(translated_data)
            return unicode_data

    def writeFile(self, unicode_data, fileName):
        with io.open(fileName, 'w') as f:
            # json.dump(translated_data, f, indent=args.indent, ensure_ascii=False)
            data = json.dumps(
                unicode_data, indent=2, ensure_ascii=False).decode('utf8')
            f.write(data)
            # try:
            #     f.write(data)
            # except TypeError:
            # Decode data to Unicode first
            #     f.write(data.decode('utf8'))

    def translate_recursive(self, data_to_translate, translate_lang, input_lang, goslate_instance):
        translated_data = data_to_translate
        for i in data_to_translate:
            if i == "_meta":
                continue
            if isinstance(data_to_translate[i], dict):
                translated_data[i] = self.translate_recursive(
                    data_to_translate[i], translate_lang, input_lang, goslate_instance)
            else:
                translated_data[i] = goslate_instance.translate(
                    data_to_translate[i], translate_lang, input_lang)
        return translated_data

    def byteify(self, input):
        if isinstance(input, dict):
            return {self.byteify(key): self.byteify(value) for key, value in input.iteritems()}
        elif isinstance(input, list):
            return [self.byteify(element) for element in input]
        elif isinstance(input, unicode):
            return input.encode('utf-8')
        else:
            return input

if __name__ == '__main__':
    t = jsonTranslate(True)
    parser = argparse.ArgumentParser()

    parser.add_argument("infile",  help="This is the input translation file.")
    parser.add_argument("targetlang", help="The language to translate to.")
    parser.add_argument("-o", "--outfile", help="The file to save the translation in.")
    parser.add_argument("-s", "--sourcelang", default="en",
                        help="The language the input file is in (default: en).")
    parser.add_argument("-i", "--indent", type=int, nargs='?', const=1,
                        help="Specify the indent level of the outputted JSON file "
                        "(default: 2). If not specified the output file "
                        "will not extra whitespace.")
    parser.add_argument("-a", "--ascii", action="store_true",
                        help="Make the output file ascii only (default: False). "
                        "When not specified the output file will be encoded"
                        "with unicode (UTF-8).")

    args = parser.parse_args()

    print args
    t.translate(args.infile,args.sourcelang ,args.targetlang)